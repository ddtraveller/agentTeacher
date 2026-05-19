"""TTS service.

Routing:
    Thai text  -> Edge TTS (Microsoft neural voices, online, free)
    Everything -> Coqui XTTS v2 (local — supports en, zh-cn, ja, ko, es, fr, de, …)

XTTS supports voice cloning from a reference WAV. Mount your reference
clips into the container (e.g. via a volume) and pass `speaker_wav` as a
container path. Without it, XTTS uses a built-in speaker.

POST /synthesize {"text": "..."}                                    -> WAV bytes
POST /synthesize {"text": "...", "speaker_wav": "/voices/me.wav"}   -> cloned voice (XTTS langs only)
GET  /health
"""

from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

import edge_tts
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DEVICE = os.getenv("DEVICE", "cpu")
XTTS_MODEL = os.getenv("XTTS_MODEL", "tts_models/multilingual/multi-dataset/xtts_v2")
XTTS_DEFAULT_SPEAKER = os.getenv("XTTS_SPEAKER", "Ana Florence")
# pocketSphinx is best for English; phonetic works on any language but lower quality.
RHUBARB_RECOGNIZER = os.getenv("RHUBARB_RECOGNIZER", "pocketSphinx")
EDGE_VOICE_EN = os.getenv("EDGE_VOICE_EN", "en-US-JennyNeural")
EDGE_VOICE_TH = os.getenv("EDGE_VOICE_TH", "th-TH-PremwadeeNeural")
EDGE_VOICE_ZH = os.getenv("EDGE_VOICE_ZH", "zh-CN-XiaoxiaoNeural")
# Set EDGE_FOR_ZH=1 to also route Chinese through Edge TTS (better quality
# than XTTS at the cost of needing internet at request time).
EDGE_FOR_ZH = os.getenv("EDGE_FOR_ZH", "0") == "1"

app = FastAPI(title="Kru Eng TTS — XTTS v2 + Edge TTS")

_xtts = None  # lazy-loaded; the model file is ~2 GB

_THAI_RE = re.compile(r"[฀-๿]")
_CHINESE_RE = re.compile(r"[一-鿿]")
_JAPANESE_RE = re.compile(r"[぀-ヿ]")
_KOREAN_RE = re.compile(r"[가-힯]")


def detect_language(text: str) -> str:
    if _THAI_RE.search(text):
        return "th"
    if _CHINESE_RE.search(text):
        return "zh-cn"
    if _JAPANESE_RE.search(text):
        return "ja"
    if _KOREAN_RE.search(text):
        return "ko"
    return "en"


def _char_lang(ch: str) -> str | None:
    """Script of a single character. Letters are 'en'; everything else (digits,
    punctuation, whitespace) is None and gets attached to whichever segment is
    currently building."""
    if "฀" <= ch <= "๿":
        return "th"
    if "一" <= ch <= "鿿":
        return "zh-cn"
    if "぀" <= ch <= "ヿ":
        return "ja"
    if "가" <= ch <= "힯":
        return "ko"
    if ch.isalpha():
        return "en"
    return None


def segment_by_script(text: str) -> list[tuple[str, str]]:
    """Group consecutive runs by script so each can use the right TTS engine.

    Returns [(lang, segment_text), ...] in input order. Punctuation and whitespace
    cling to whichever language run is currently open, so "Hello! สวัสดี" yields
    [("en", "Hello! "), ("th", "สวัสดี")] — never a Thai voice reading "Hello!".
    """
    segs: list[tuple[str, str]] = []
    cur_lang: str | None = None
    buf: list[str] = []
    for ch in text:
        l = _char_lang(ch)
        if l is None:
            buf.append(ch)
        elif cur_lang is None or cur_lang == l:
            cur_lang = l
            buf.append(ch)
        else:
            segs.append((cur_lang, "".join(buf)))
            cur_lang = l
            buf = [ch]
    if buf:
        segs.append((cur_lang or "en", "".join(buf)))
    return segs


def get_xtts():
    global _xtts
    if _xtts is None:
        from TTS.api import TTS  # heavy import; deferred until first use
        _xtts = TTS(model_name=XTTS_MODEL, progress_bar=False).to(DEVICE)
    return _xtts


class TTSRequest(BaseModel):
    text: str
    language: str | None = None        # override autodetection (e.g. "en", "zh-cn", "th")
    speaker: str | None = None         # XTTS built-in speaker name
    speaker_wav: str | None = None     # path inside container to reference WAV (XTTS cloning)
    speed: float = 1.0


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "device": DEVICE,
        "xtts_loaded": _xtts is not None,
        "edge_voice_en": EDGE_VOICE_EN,
        "edge_voice_th": EDGE_VOICE_TH,
        "edge_voice_zh": EDGE_VOICE_ZH,
        "edge_for_zh": EDGE_FOR_ZH,
    }


def _synth_xtts(req: TTSRequest, language: str) -> bytes:
    tts = get_xtts()
    fd, out_path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    try:
        kwargs = {
            "text": req.text,
            "language": language,
            "file_path": out_path,
            "speed": req.speed,
        }
        if req.speaker_wav:
            ref = Path(req.speaker_wav)
            if not ref.exists():
                raise HTTPException(400, f"speaker_wav not found: {ref}")
            kwargs["speaker_wav"] = str(ref)
        else:
            kwargs["speaker"] = req.speaker or XTTS_DEFAULT_SPEAKER
        tts.tts_to_file(**kwargs)
        return Path(out_path).read_bytes()
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass


async def _edge_mp3(text: str, voice: str) -> bytes:
    communicate = edge_tts.Communicate(text=text, voice=voice)
    chunks: list[bytes] = []
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            chunks.append(chunk["data"])
    if not chunks:
        raise HTTPException(500, "Edge TTS returned no audio")
    return b"".join(chunks)


def _mp3_to_wav(mp3_bytes: bytes) -> bytes:
    # ffmpeg can't write a seekable WAV header to stdout, so the chunk-size
    # fields end up zeroed and strict parsers (e.g. rhubarb) report duration 0.
    # Use a temp file so ffmpeg can rewrite the header on close.
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
        out_path = tf.name
    try:
        proc = subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", "pipe:0", out_path],
            input=mp3_bytes,
            capture_output=True,
            timeout=30,
        )
        if proc.returncode != 0:
            err = proc.stderr.decode(errors="replace")[:300]
            raise HTTPException(500, f"ffmpeg failed: {err}")
        with open(out_path, "rb") as f:
            return f.read()
    finally:
        try:
            os.unlink(out_path)
        except OSError:
            pass


async def _synth_edge(text: str, voice: str) -> bytes:
    mp3 = await _edge_mp3(text, voice)
    return _mp3_to_wav(mp3)


def _concat_wavs(wavs: list[bytes]) -> bytes:
    if not wavs:
        raise HTTPException(500, "no audio to return")
    if len(wavs) == 1:
        return wavs[0]
    with tempfile.TemporaryDirectory() as td:
        in_paths = []
        for i, w in enumerate(wavs):
            p = os.path.join(td, f"in{i}.wav")
            with open(p, "wb") as f:
                f.write(w)
            in_paths.append(p)
        out_path = os.path.join(td, "out.wav")
        cmd = ["ffmpeg", "-loglevel", "error"]
        for p in in_paths:
            cmd += ["-i", p]
        cmd += ["-filter_complex",
                f"concat=n={len(in_paths)}:v=0:a=1[a]",
                "-map", "[a]", out_path]
        proc = subprocess.run(cmd, capture_output=True, timeout=120)
        if proc.returncode != 0:
            err = proc.stderr.decode(errors="replace")[:300]
            raise HTTPException(500, f"ffmpeg concat failed: {err}")
        with open(out_path, "rb") as f:
            return f.read()


async def _synth_one(req: TTSRequest, text: str, language: str) -> bytes:
    # Voice cloning request -> XTTS (Edge TTS has fixed voices only).
    if req.speaker_wav:
        sub_req = req.model_copy(update={"text": text})
        return _synth_xtts(sub_req, language)
    if language == "th":
        return await _synth_edge(text, EDGE_VOICE_TH)
    if language == "en":
        return await _synth_edge(text, EDGE_VOICE_EN)
    if language == "zh-cn" and EDGE_FOR_ZH:
        return await _synth_edge(text, EDGE_VOICE_ZH)
    # ja, ko, or zh-cn (without EDGE_FOR_ZH) still go to XTTS.
    sub_req = req.model_copy(update={"text": text})
    return _synth_xtts(sub_req, language)


def _generate_visemes(wav_bytes: bytes) -> list[dict] | None:
    """Run rhubarb on a WAV and return Preston-Blair mouth cues.

    Each cue is {"start": float_secs, "end": float_secs, "shape": "A".."H"|"X"}.
    Returns None if rhubarb fails so the UI can fall back to amplitude.
    """
    with tempfile.TemporaryDirectory() as td:
        wav_path = os.path.join(td, "in.wav")
        with open(wav_path, "wb") as f:
            f.write(wav_bytes)
        try:
            proc = subprocess.run(
                ["rhubarb", "-f", "json", "-r", RHUBARB_RECOGNIZER, wav_path],
                capture_output=True,
                timeout=120,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return None
        if proc.returncode != 0:
            return None
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError:
            return None
        return [
            {"start": c["start"], "end": c["end"], "shape": c["value"]}
            for c in data.get("mouthCues", [])
        ]


@app.post("/synthesize")
async def synthesize(req: TTSRequest):
    text = (req.text or "").strip()
    if not text:
        raise HTTPException(400, "text is empty")

    try:
        # If the caller forced a language, honor it as a single-engine call.
        if req.language:
            audio = await _synth_one(req, text, req.language)
        else:
            segments = segment_by_script(text)
            distinct = {l for l, s in segments if s.strip()}
            if len(distinct) <= 1:
                lang = next(iter(distinct), "en")
                audio = await _synth_one(req, text, lang)
            else:
                wavs = []
                for lang, seg in segments:
                    if not seg.strip():
                        continue
                    wavs.append(await _synth_one(req, seg, lang))
                audio = _concat_wavs(wavs)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"TTS failed: {type(e).__name__}: {e}")

    return {
        "audio": base64.b64encode(audio).decode(),
        "visemes": _generate_visemes(audio),
    }
