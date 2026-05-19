"""Orchestrator: glues the user's mic/speaker to Ollama, Whisper, and TTS.

Day-side request flow:
    audio -> Whisper STT -> [LlamaIndex retrieval over wiki] -> Ollama -> TTS

Wiki retrieval is opt-in via RAG_ENABLED=true. When on, LlamaIndex builds
a persistent vector index over /data/wiki/**/*.md (using Ollama's
nomic-embed-text for embeddings) at first startup, then loads from disk on
subsequent boots. Per-query: embed the user message, pull top-K chunks,
inject them as a system note. Adds ~50-150ms latency per turn and ~600
tokens of context — manageable with qwen2.5:3b.
"""

from __future__ import annotations

import json
import logging
import os
import re
import secrets
import threading
from dataclasses import dataclass
from pathlib import Path

import httpx
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

log = logging.getLogger("orchestrator")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
WHISPER_URL = os.getenv("WHISPER_URL", "http://localhost:9000")
TTS_URL = os.getenv("TTS_URL", "http://localhost:8001")
MODEL = os.getenv("MODEL", "qwen2.5:3b")

RAG_ENABLED = os.getenv("RAG_ENABLED", "false").lower() in ("1", "true", "yes")
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
WIKI_PATH = Path(os.getenv("WIKI_PATH", "/data/wiki"))
INDEX_PATH = Path(os.getenv("INDEX_PATH", "/data/wiki_index"))
RAG_TOP_K = int(os.getenv("RAG_TOP_K", "3"))

# Cap generation so a short chat reply doesn't run on for 90s on CPU.
# Override per-request if a long answer is genuinely needed.
OLLAMA_OPTIONS: dict = {
    "num_predict": int(os.getenv("OLLAMA_NUM_PREDICT", "180")),
    "temperature": float(os.getenv("OLLAMA_TEMPERATURE", "0.7")),
    "num_ctx": int(os.getenv("OLLAMA_NUM_CTX", "1536" if not RAG_ENABLED else "2560")),
}

SYSTEM_PROMPT = (
    "You are Kru Eng, a friendly English tutor based in Chiang Mai, Thailand. "
    "Always reply in English, even if the student writes to you in Thai (ไทย) "
    "or Mandarin Chinese (中文). This is intentional — students are here to "
    "practise reading and understanding English. "
    "You may quote a Thai or Chinese word inside an English sentence when you "
    "need to teach what it means (for example: \"'ตลาด' means 'market'.\"). "
    "But your sentences are always in English. "
    "Only switch to a full Thai or Chinese reply when the student explicitly "
    "asks you to — for example: 'please answer in Thai', 'อธิบายเป็นภาษาไทย', "
    "or '请用中文回答'. When that happens, give the requested-language reply, "
    "then briefly offer the English equivalent so the student still gets "
    "exposure to English. "
    "Keep replies short (1-3 sentences). Use vocabulary suitable for a learner. "
    "Be warm and encouraging."
)

STATIC = Path(__file__).parent / "static"

app = FastAPI(title="Kru Eng Local Bot — Orchestrator")

# CORS — allow the public krueng.ai lesson page to call this local bot.
# Localhost is allowed for dev. Add other origins (school LAN, tunnel) as needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://krueng.ai",
        "https://www.krueng.ai",
        "https://d3iqzt3jh2n6qq.cloudfront.net",
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
    ],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=STATIC), name="static")


class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []
    student: str | None = None


class TTSRequest(BaseModel):
    text: str


@dataclass
class Grounding:
    text: str
    citations: list[str]


# ── LlamaIndex-backed wiki retrieval ────────────────────────────────────────
# Module state. _INDEX is built lazily on the first call (and persisted to
# disk so subsequent container restarts skip embedding). A lock makes the
# build single-threaded — concurrent first calls won't all start embedding.

_INDEX = None
_INDEX_LOCK = threading.Lock()
_INDEX_STATE = "off"  # off | empty | building | ready | error


def _build_or_load_index():
    """Idempotent: returns the LlamaIndex VectorStoreIndex over the wiki,
    loading from INDEX_PATH if persisted, otherwise building from scratch."""
    global _INDEX, _INDEX_STATE

    from llama_index.core import (
        Settings,
        SimpleDirectoryReader,
        StorageContext,
        VectorStoreIndex,
        load_index_from_storage,
    )
    from llama_index.embeddings.ollama import OllamaEmbedding

    Settings.embed_model = OllamaEmbedding(
        model_name=EMBED_MODEL,
        base_url=OLLAMA_URL,
    )
    # We don't use LlamaIndex's LLM layer — Ollama is called directly from
    # /chat. Setting llm=None prevents LlamaIndex from trying to load an
    # OpenAI client.
    Settings.llm = None

    persisted = INDEX_PATH.exists() and any(INDEX_PATH.iterdir())
    if persisted:
        log.info("loading wiki index from %s", INDEX_PATH)
        ctx = StorageContext.from_defaults(persist_dir=str(INDEX_PATH))
        _INDEX = load_index_from_storage(ctx)
        _INDEX_STATE = "ready"
        return _INDEX

    if not WIKI_PATH.exists():
        log.warning("WIKI_PATH %s missing; RAG will be empty", WIKI_PATH)
        _INDEX_STATE = "empty"
        return None

    log.info("building wiki index from %s (this happens once)", WIKI_PATH)
    docs = SimpleDirectoryReader(
        input_dir=str(WIKI_PATH),
        recursive=True,
        required_exts=[".md"],
    ).load_data()
    if not docs:
        log.warning("no .md files under %s; RAG will be empty", WIKI_PATH)
        _INDEX_STATE = "empty"
        return None

    _INDEX = VectorStoreIndex.from_documents(docs)
    INDEX_PATH.mkdir(parents=True, exist_ok=True)
    _INDEX.storage_context.persist(str(INDEX_PATH))
    _INDEX_STATE = "ready"
    log.info("wiki index built: %d documents indexed under %s", len(docs), INDEX_PATH)
    return _INDEX


def _get_index():
    """Thread-safe lazy build. First call may block ~30s on first run while
    embedding 25 files; subsequent calls return instantly from cache."""
    global _INDEX, _INDEX_STATE
    if not RAG_ENABLED:
        _INDEX_STATE = "off"
        return None
    if _INDEX is not None:
        return _INDEX
    with _INDEX_LOCK:
        if _INDEX is not None:
            return _INDEX
        _INDEX_STATE = "building"
        try:
            return _build_or_load_index()
        except Exception as exc:  # noqa: BLE001
            log.exception("index build failed: %s", exc)
            _INDEX_STATE = f"error: {type(exc).__name__}"
            return None


def ground(question: str) -> Grounding | None:
    """Retrieve top-K wiki chunks relevant to the question. Returns None if
    RAG is off, the index is empty, or no chunk clears the relevance bar."""
    idx = _get_index()
    if idx is None or not question.strip():
        return None
    try:
        retriever = idx.as_retriever(similarity_top_k=RAG_TOP_K)
        nodes = retriever.retrieve(question)
    except Exception as exc:  # noqa: BLE001
        log.warning("retrieval failed: %s", exc)
        return None
    if not nodes:
        return None

    passages: list[str] = []
    citations: list[str] = []
    for n in nodes:
        text = (n.text or "").strip()
        if not text:
            continue
        # File path lives in metadata; surface a short citation name.
        fp = (n.metadata or {}).get("file_path") or (n.metadata or {}).get("file_name") or ""
        cite = Path(fp).stem if fp else ""
        if cite and cite not in citations:
            citations.append(cite)
        passages.append(text[:900])  # cap per-chunk so the prompt stays small

    if not passages:
        return None
    return Grounding(text="\n\n---\n\n".join(passages), citations=citations)


# Build the index at import time so the first /chat call doesn't pay the
# ~30s cost. If RAG is off this is a fast no-op.
if RAG_ENABLED:
    try:
        _build_or_load_index()
    except Exception as exc:  # noqa: BLE001
        log.exception("startup index build failed: %s", exc)


def build_messages(req: ChatRequest, grounding: Grounding | None) -> list[dict]:
    """Insert the grounded draft as a system note so Ollama can re-render it
    in the Kru Eng voice. Cite the wiki pages explicitly."""
    messages: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]
    if grounding and grounding.text:
        cite_line = ""
        if grounding.citations:
            cite_line = f"\n\nSources (cite these by name if relevant): {', '.join(grounding.citations)}"
        messages.append({
            "role": "system",
            "content": (
                "The school's wiki provides this grounded draft answer. "
                "Use it as the source of truth; do not invent facts outside it. "
                "Rewrite it warmly in 1-3 sentences for a learner:"
                f"\n\n{grounding.text}{cite_line}"
            ),
        })
    messages.extend(req.history)
    messages.append({"role": "user", "content": req.message})
    return messages


@app.get("/")
async def root():
    return FileResponse(STATIC / "index.html")


@app.get("/health")
async def health():
    """Per-backend readiness check used by the UI footer."""
    out: dict[str, str] = {"rag": _INDEX_STATE}
    async with httpx.AsyncClient(timeout=3) as c:
        for name, url in [
            ("ollama", f"{OLLAMA_URL}/api/tags"),
            ("whisper", f"{WHISPER_URL}/docs"),
            ("tts", f"{TTS_URL}/health"),
        ]:
            try:
                r = await c.get(url)
                out[name] = "ok" if r.status_code < 500 else f"http_{r.status_code}"
            except httpx.HTTPError as e:
                out[name] = f"down ({type(e).__name__})"
    return out


@app.post("/chat")
async def chat(req: ChatRequest):
    """Wiki-grounded streaming chat. Returns SSE chunks for the UI to render
    progressively. Always emits a final {done:true} sentinel."""
    grounding = ground(req.message)
    messages = build_messages(req, grounding)

    async def gen():
        try:
            async with httpx.AsyncClient(timeout=300) as c:
                async with c.stream(
                    "POST",
                    f"{OLLAMA_URL}/api/chat",
                    json={
                        "model": MODEL,
                        "messages": messages,
                        "stream": True,
                        "options": OLLAMA_OPTIONS,
                    },
                ) as r:
                    r.raise_for_status()
                    async for line in r.aiter_lines():
                        if not line.strip():
                            continue
                        obj = json.loads(line)
                        chunk = obj.get("message", {}).get("content", "")
                        done = obj.get("done", False)
                        payload = {"chunk": chunk, "done": done}
                        if done and grounding:
                            payload["citations"] = grounding.citations
                        yield f"data: {json.dumps(payload)}\n\n"
                        if done:
                            return
        except (httpx.HTTPError, json.JSONDecodeError) as e:
            yield f"data: {json.dumps({'error': str(e), 'done': True})}\n\n"

    return StreamingResponse(gen(), media_type="text/event-stream")


@app.post("/converse")
async def converse(audio: UploadFile = File(...), student: str | None = None):
    """Full voice loop: audio -> Whisper -> Khoj -> Ollama -> TTS -> audio + visemes."""
    audio_bytes = await audio.read()
    if not audio_bytes:
        raise HTTPException(400, "Empty audio")

    async with httpx.AsyncClient(timeout=180) as c:
        # 1. Transcribe
        files = {"audio_file": (audio.filename or "rec.webm", audio_bytes,
                                audio.content_type or "audio/webm")}
        wr = await c.post(
            f"{WHISPER_URL}/asr",
            params={"output": "json", "task": "transcribe"},
            files=files,
        )
        wr.raise_for_status()
        user_text = (wr.json().get("text") or "").strip()

        if not user_text:
            return {"user": "", "bot": "(no speech detected — try again)",
                    "audio": None, "citations": []}

        # 2. Wiki grounding (best-effort)
        grounding = ground(user_text)

        # 3. Ollama re-renders the grounded draft in Kru Eng voice
        messages = build_messages(
            ChatRequest(message=user_text, student=student), grounding
        )
        cr = await c.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": MODEL,
                "messages": messages,
                "stream": False,
                "options": OLLAMA_OPTIONS,
            },
        )
        cr.raise_for_status()
        reply = cr.json()["message"]["content"].strip()

        # 4. TTS — best-effort; UI falls back to browser speechSynthesis if missing
        audio_b64: str | None = None
        visemes = None
        try:
            tr = await c.post(f"{TTS_URL}/synthesize",
                              json={"text": reply}, timeout=120)
            if tr.status_code == 200:
                tts = tr.json()
                audio_b64 = tts.get("audio")
                visemes = tts.get("visemes")
        except httpx.HTTPError:
            pass

    return {
        "user": user_text,
        "bot": reply,
        "audio": audio_b64,
        "visemes": visemes,
        "citations": grounding.citations if grounding else [],
    }


@app.post("/speak")
async def speak(req: TTSRequest):
    """Text -> audio + visemes. Forwards the TTS service's JSON unchanged."""
    async with httpx.AsyncClient(timeout=120) as c:
        r = await c.post(f"{TTS_URL}/synthesize", json={"text": req.text})
        r.raise_for_status()
    return r.json()


# ── Scaffolded PPP lesson cycle ─────────────────────────────────────────────
# Lesson plans live in ./lessons/*.json. Each is a Presentation → Controlled
# Practice → Freer Production scaffold. Crucially, P2 is graded by string
# normalization against an answer key — the LLM never decides correctness
# (qwen2.5:3b will rubber-stamp wrong answers as fine, breaking the gate).
# A rolling-window accuracy threshold opens P3.

LESSONS_DIR = Path(__file__).parent / "lessons"
_LESSONS: dict[str, dict] = {}
_SESSIONS: dict[str, dict] = {}
_SESSIONS_LOCK = threading.Lock()


def _load_lessons() -> None:
    if not LESSONS_DIR.exists():
        log.warning("LESSONS_DIR %s missing — no lessons loaded", LESSONS_DIR)
        return
    for path in sorted(LESSONS_DIR.glob("*.json")):
        # Sibling files like *_image_prompts.json live in the same dir but
        # aren't lessons; skip them.
        if path.stem.endswith("_image_prompts"):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            _LESSONS[data["id"]] = data
            log.info("loaded lesson %s (%s)", data["id"], path.name)
        except (OSError, json.JSONDecodeError, KeyError) as e:
            log.warning("failed to load lesson %s: %s", path, e)


_load_lessons()


def _normalize_answer(s: str) -> str:
    """Lowercase, strip, collapse whitespace, expand common contractions.
    Contraction expansion makes 'wasn't' and 'was not' equivalent without
    forcing the lesson author to list every form."""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("wasn't", "was not").replace("weren't", "were not")
    s = s.replace("didn't", "did not").replace("don't", "do not")
    return s


def _grade_p2(exercise: dict, answers: list[str]) -> dict:
    blanks = exercise["blanks"]
    if len(answers) != len(blanks):
        return {
            "correct": False,
            "per_blank": [False] * len(blanks),
            "expected": [b["accept"][0] for b in blanks],
        }
    per_blank = []
    for ans, blank in zip(answers, blanks):
        norm = _normalize_answer(ans)
        accept_norm = {_normalize_answer(a) for a in blank["accept"]}
        per_blank.append(norm in accept_norm)
    return {
        "correct": all(per_blank),
        "per_blank": per_blank,
        "expected": [b["accept"][0] for b in blanks],
    }


def _p2_window_accuracy(s: dict, lesson: dict) -> float:
    window = s["p2_results"][-lesson["config"]["p2_window_size"]:]
    return sum(window) / len(window) if window else 0.0


def _p2_pass(s: dict, lesson: dict) -> bool:
    cfg = lesson["config"]
    window = s["p2_results"][-cfg["p2_window_size"]:]
    if len(window) < cfg["p2_min_attempts"]:
        return False
    return sum(window) / len(window) >= cfg["p2_pass_threshold"]


def _session_snapshot(s: dict, lesson: dict) -> dict:
    return {
        "session_id": s["id"],
        "lesson_id": s["lesson_id"],
        "phase": s["phase"],
        "p1_idx": s["p1_idx"],
        "p1_total": len(lesson["p1_examples"]),
        "p2_attempts": len(s["p2_results"]),
        "p2_accuracy": round(_p2_window_accuracy(s, lesson), 2),
        "p2_threshold": lesson["config"]["p2_pass_threshold"],
        "p3_turns": s["p3_turns"],
        "p3_target_turns": lesson["config"]["p3_target_turns"],
    }


def _current_item(s: dict, lesson: dict) -> dict:
    phase = s["phase"]
    if phase == "p1":
        idx = s["p1_idx"]
        return {
            "kind": "p1_example",
            "data": lesson["p1_examples"][idx],
            "intro": lesson["p1_intro"] if idx == 0 else None,
            "is_last": idx == len(lesson["p1_examples"]) - 1,
        }
    if phase == "p2":
        ex = lesson["p2_exercises"][s["p2_idx"] % len(lesson["p2_exercises"])]
        public = {k: v for k, v in ex.items() if k != "blanks"}
        public["n_blanks"] = len(ex["blanks"])
        return {"kind": "p2_exercise", "data": public}
    if phase == "p3":
        scen = lesson["p3_scenarios"][s["p3_scenario_idx"] % len(lesson["p3_scenarios"])]
        return {
            "kind": "p3_scenario",
            "data": scen,
            "history": s["p3_history"],
            "is_first_turn": not s["p3_history"],
        }
    if phase == "done":
        return {"kind": "done"}
    return {}


class LessonStartReq(BaseModel):
    lesson_id: str


class LessonTurnReq(BaseModel):
    session_id: str
    action: str  # "next" | "submit" | "skip"
    payload: dict | None = None


@app.get("/lesson/list")
async def lesson_list():
    return [
        {"id": l["id"], "title": l["title"], "title_th": l["title_th"],
         "cefr": l["cefr"], "can_do": l.get("can_do", "")}
        for l in _LESSONS.values()
    ]


@app.post("/lesson/start")
async def lesson_start(req: LessonStartReq):
    lesson = _LESSONS.get(req.lesson_id)
    if not lesson:
        raise HTTPException(404, f"Unknown lesson: {req.lesson_id}")
    sid = secrets.token_urlsafe(12)
    s = {
        "id": sid,
        "lesson_id": req.lesson_id,
        "phase": "p1",
        "p1_idx": 0,
        "p2_idx": 0,
        "p2_results": [],
        "p3_scenario_idx": 0,
        "p3_turns": 0,
        "p3_history": [],
    }
    with _SESSIONS_LOCK:
        _SESSIONS[sid] = s
    return {
        "state": _session_snapshot(s, lesson),
        "item": _current_item(s, lesson),
        "feedback": None,
    }


@app.post("/lesson/turn")
async def lesson_turn(req: LessonTurnReq):
    with _SESSIONS_LOCK:
        s = _SESSIONS.get(req.session_id)
    if not s:
        raise HTTPException(404, "Unknown session")
    lesson = _LESSONS.get(s["lesson_id"])
    if not lesson:
        raise HTTPException(404, "Lesson missing")

    feedback: dict | None = None
    payload = req.payload or {}

    if s["phase"] == "p1":
        if req.action == "next":
            if s["p1_idx"] < len(lesson["p1_examples"]) - 1:
                s["p1_idx"] += 1
            else:
                s["phase"] = "p2"
                feedback = {
                    "phase_change": "p1->p2",
                    "msg": "Now let's practise. Fill in the blanks. "
                           "Type the past continuous (was/were + V-ing) or "
                           "past simple where it fits.",
                    "msg_th": "ตอนนี้มาฝึกกัน เติมคำในช่องว่าง — ใช้ "
                              "past continuous (was/were + V-ing) หรือ "
                              "past simple ตามความเหมาะสม",
                }

    elif s["phase"] == "p2":
        if req.action == "submit":
            answers = payload.get("answers", [])
            ex = lesson["p2_exercises"][s["p2_idx"] % len(lesson["p2_exercises"])]
            grade = _grade_p2(ex, answers)
            s["p2_results"].append(1 if grade["correct"] else 0)
            feedback = {
                "correct": grade["correct"],
                "per_blank": grade["per_blank"],
                "expected": grade["expected"],
                "explanation_th": ex.get("explanation_th", ""),
                "explanation_zh": ex.get("explanation_zh", ""),
            }
            s["p2_idx"] += 1
            if _p2_pass(s, lesson):
                s["phase"] = "p3"
                feedback["phase_change"] = "p2->p3"
                feedback["msg"] = (
                    "Excellent — you've got the pattern. "
                    "Now let's use it in conversation."
                )
                feedback["msg_th"] = (
                    "เยี่ยม — คุณเข้าใจรูปประโยคแล้ว "
                    "ทีนี้มาใช้ในการสนทนากัน"
                )
        elif req.action == "skip":
            s["p2_idx"] += 1

    elif s["phase"] == "p3":
        if req.action == "submit":
            user_msg = payload.get("message", "").strip()
            if not user_msg:
                raise HTTPException(400, "Empty message")
            messages: list[dict] = [
                {"role": "system", "content": lesson["p3_system_prompt"]},
            ]
            if not s["p3_history"]:
                scen = lesson["p3_scenarios"][s["p3_scenario_idx"]]
                messages.append({"role": "assistant", "content": scen["opener"]})
            messages.extend(s["p3_history"])
            messages.append({"role": "user", "content": user_msg})

            try:
                async with httpx.AsyncClient(timeout=120) as c:
                    r = await c.post(
                        f"{OLLAMA_URL}/api/chat",
                        json={
                            "model": MODEL,
                            "messages": messages,
                            "stream": False,
                            "options": OLLAMA_OPTIONS,
                        },
                    )
                    r.raise_for_status()
                    reply = r.json()["message"]["content"].strip()
            except httpx.HTTPError as e:
                raise HTTPException(502, f"Ollama error: {e}")

            s["p3_history"].append({"role": "user", "content": user_msg})
            s["p3_history"].append({"role": "assistant", "content": reply})
            s["p3_turns"] += 1
            feedback = {"reply": reply}
            if s["p3_turns"] >= lesson["config"]["p3_target_turns"]:
                s["phase"] = "done"
                feedback["phase_change"] = "p3->done"
                feedback["msg"] = (
                    "Well done! You used past continuous in a real "
                    "conversation. Lesson complete."
                )
                feedback["msg_th"] = (
                    "เก่งมาก! คุณใช้ past continuous ในบทสนทนาจริงได้แล้ว "
                    "บทเรียนนี้จบแล้ว"
                )

    with _SESSIONS_LOCK:
        _SESSIONS[s["id"]] = s

    return {
        "state": _session_snapshot(s, lesson),
        "item": _current_item(s, lesson),
        "feedback": feedback,
    }


@app.get("/lesson")
async def lesson_ui():
    return FileResponse(STATIC / "lesson.html")
