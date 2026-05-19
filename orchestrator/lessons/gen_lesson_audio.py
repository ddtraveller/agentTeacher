#!/usr/bin/env python3
"""Pre-generate intro audio via edge-tts.

Reads <lesson_id>.json's p1_intro {en, th, zh} and writes
intro_en.mp3 / intro_th.mp3 / intro_zh.mp3 into the orchestrator's
static dir so the lesson UI can play them with plain <audio> tags.

Voices match the docker TTS service defaults (docker/tts/server.py):
    EN  en-US-JennyNeural
    TH  th-TH-PremwadeeNeural
    ZH  zh-CN-XiaoxiaoNeural

Usage:
    python gen_lesson_audio.py past_continuous
    python gen_lesson_audio.py past_continuous --force
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

import edge_tts

HERE = Path(__file__).resolve().parent
STATIC_DIR = HERE.parent / "static" / "lesson_images"

VOICES = {
    "en": "en-US-JennyNeural",
    "th": "th-TH-PremwadeeNeural",
    "zh": "zh-CN-XiaoxiaoNeural",
}


def _sanitize(text: str) -> str:
    # Edge TTS sometimes returns NoAudioReceived for unusual punctuation.
    # Em/en dashes, ellipses, and certain quote marks are the usual culprits.
    return (text
            .replace("—", " - ")
            .replace("–", " - ")
            .replace("…", "...")
            .replace("​", "")
            .replace(" ", " "))


async def synth(text: str, voice: str, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    clean = _sanitize(text)
    last_err = None
    for attempt in range(3):
        try:
            communicate = edge_tts.Communicate(clean, voice)
            await communicate.save(str(out))
            return
        except edge_tts.exceptions.NoAudioReceived as e:
            last_err = e
            await asyncio.sleep(1.5)
    raise last_err


def _gather_items(lesson: dict) -> list[tuple[str, dict]]:
    """Walk the lesson and emit (filename_stem, {lang: text, ...}) for
    every speakable group. Each group becomes 1-3 MP3 files."""
    items: list[tuple[str, dict]] = []
    intro = lesson.get("p1_intro")
    if intro:
        items.append(("intro", {l: intro.get(l) for l in VOICES}))
    for ex in lesson.get("p1_examples", []):
        items.append((f"p1_{ex['id']}", {
            "en": ex.get("sentence"),
            "th": ex.get("th"),
            "zh": ex.get("zh"),
        }))
    for scen in lesson.get("p3_scenarios", []):
        items.append((f"p3_{scen['id']}", {
            "en": scen.get("opener"),
            "th": scen.get("opener_th"),
            "zh": scen.get("opener_zh"),
        }))
    return items


async def run(lesson_id: str, force: bool) -> int:
    lesson_path = HERE / f"{lesson_id}.json"
    if not lesson_path.exists():
        print(f"lesson not found: {lesson_path}", file=sys.stderr)
        return 1
    lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
    out_dir = STATIC_DIR / lesson_id / "audio"

    total = 0
    for stem, by_lang in _gather_items(lesson):
        for lang, voice in VOICES.items():
            text = by_lang.get(lang)
            if not text:
                continue
            out = out_dir / f"{stem}_{lang}.mp3"
            total += 1
            if out.exists() and not force:
                print(f"[skip] {out.name}")
                continue
            print(f"[gen]  {out.name} via {voice}")
            await synth(text, voice, out)
            print(f"        -> {out.stat().st_size:,} bytes")
    print(f"\ndone. {total} files considered.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lesson_id")
    ap.add_argument("--force", action="store_true",
                    help="Regenerate even if file exists")
    args = ap.parse_args()
    return asyncio.run(run(args.lesson_id, args.force))


if __name__ == "__main__":
    sys.exit(main())
