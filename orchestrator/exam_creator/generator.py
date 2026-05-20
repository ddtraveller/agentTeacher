"""LLM-driven exam generator.

Calls the orchestrator's configured Ollama with `format="json"`, validates
the response against the Exam schema, and retries up to 3 times on
malformed or schema-mismatched output. Generation is sync (CLI use case).

For the prompt design: we feed 3 P2 examples from the source lesson as
few-shot, the lesson's `target_structure` as the grammar to drill, and
an explicit instruction to use Chiang Mai / Lanna local context. The
output is wrapped in `{"exercises": [...]}` rather than a bare array
because qwen2.5:3b's JSON mode is more consistent with object-rooted
responses.
"""
from __future__ import annotations

import json
import logging
import os
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
from pydantic import ValidationError

from .schema import Exam, ExamExercise

log = logging.getLogger("orchestrator.exam_creator.generator")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "qwen2.5:3b")
GENERATION_TIMEOUT = int(os.getenv("EXAM_GEN_TIMEOUT", "300"))

LESSONS_DIR = Path(__file__).parent.parent / "lessons"

_TZ_BKK = timezone(timedelta(hours=7))


def load_lesson(lesson_id: str) -> dict | None:
    """Load lesson JSON from /app/lessons/{lesson_id}.json.

    The CLI runs in a separate process from the FastAPI app, so this
    can't reuse main.py's _LESSONS dict. Reading from disk is the
    one-line cost of process isolation.
    """
    path = LESSONS_DIR / f"{lesson_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _build_prompt(lesson: dict, count: int, prior_error: str | None) -> str:
    """Few-shot prompt for the Ollama JSON-mode call."""
    p2 = lesson.get("p2_exercises", [])
    examples = random.sample(p2, min(3, len(p2)))
    few_shot = json.dumps({"exercises": examples}, ensure_ascii=False, indent=2)

    retry_note = ""
    if prior_error:
        retry_note = (
            "\n\nIMPORTANT: Your previous response was invalid:\n"
            f"  {prior_error}\n"
            "Output ONLY valid JSON matching the exact schema above. "
            "Do not include any text outside the JSON object.\n"
        )

    return (
        f"You are an English language teacher creating exam exercises "
        f"for Thai students at CEFR level {lesson.get('cefr', 'A1-A2')}.\n"
        f"\n"
        f"Lesson topic: {lesson.get('title', 'English grammar')}\n"
        f"Grammar target: {lesson.get('target_structure', 'unspecified')}\n"
        f"\n"
        f"Generate exactly {count} fresh fill-in-the-blank exercises matching "
        f"the style of these example exercises:\n"
        f"\n"
        f"{few_shot}\n"
        f"\n"
        f"Schema for each exercise:\n"
        f"- id: short string identifier (e.g. 'ex_01', 'ex_02')\n"
        f"- prompt: English sentence with one or more '_____' blanks "
        f"(five underscores) marking what the student fills in\n"
        f"- prompt_th: Thai translation keeping the '_____' blanks in the "
        f"same positions\n"
        f"- prompt_zh: Simplified Chinese translation, same blank positions\n"
        f"- blanks: array (one entry per '_____') of objects shaped "
        f"{{'accept': [...]}} listing acceptable answers; for negatives or "
        f"contractions, list both forms (e.g. ['did not like', \"didn't like\"])\n"
        f"- explanation_th: one or two sentences in Thai explaining the grammar\n"
        f"- explanation_zh: same explanation in Simplified Chinese\n"
        f"\n"
        f"Style requirements:\n"
        f"- Use Chiang Mai / northern Thailand local context where possible: "
        f"Warorot market, Doi Suthep, Wat Phra Singh, khao soi, sai oua, "
        f"Nimman, Mae Sa, Songkran, the Walking Street\n"
        f"- Mix regular and irregular verbs\n"
        f"- Include at least 1 negative form (did not / didn't) and at least "
        f"1 question form (Did + S + V1, or Wh + did + S + V1)\n"
        f"- DO NOT reuse the example prompts verbatim — they are only style guides\n"
        f"- The number of '_____' blanks in 'prompt' must equal the number of "
        f"entries in 'blanks'\n"
        f"{retry_note}"
        f"\n"
        f"Respond with a JSON object of the exact form "
        f"{{\"exercises\": [<{count} exercise objects>]}}. "
        f"Output ONLY the JSON object — no prose, no markdown fences."
    )


def _call_ollama(prompt: str) -> str:
    """Make a single Ollama JSON-mode chat call; return the message content."""
    with httpx.Client(timeout=GENERATION_TIMEOUT) as c:
        r = c.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0.7,
                    # Bigger output budget than the chat default of 180 —
                    # 10 exercises × ~150 tokens each + structure overhead.
                    "num_predict": 4000,
                    # Bigger context than the chat default of 1536 — few-shot
                    # examples alone are ~600 tokens.
                    "num_ctx": 4096,
                },
            },
        )
        r.raise_for_status()
        return r.json()["message"]["content"]


def _parse_response(content: str) -> list[ExamExercise]:
    """Parse Ollama's content into validated ExamExercise objects.

    Accepts both bare arrays and {"exercises": [...]} wrappers, since
    qwen2.5:3b's JSON mode occasionally returns either shape regardless
    of what we ask for.
    """
    raw = json.loads(content)
    if isinstance(raw, dict) and "exercises" in raw:
        raw = raw["exercises"]
    if not isinstance(raw, list):
        raise TypeError(f"expected list, got {type(raw).__name__}")
    exercises = [ExamExercise(**ex) for ex in raw]

    # Schema validation passed, but we still cross-check that the number
    # of '_____' blanks in prompt matches the number of blanks entries.
    for ex in exercises:
        n_underscores = ex.prompt.count("_____")
        if n_underscores != len(ex.blanks):
            raise ValueError(
                f"exercise {ex.id!r}: {n_underscores} '_____' blanks in prompt "
                f"but {len(ex.blanks)} entries in blanks"
            )

    return exercises


def _make_exam_id(lesson_id: str) -> tuple[str, str]:
    """Return (exam_id, generated_at_iso)."""
    now = datetime.now(_TZ_BKK)
    ts = now.strftime("%Y%m%d-%H%M%S")
    return f"{lesson_id}_{ts}", now.isoformat()


def generate_exam(lesson: dict, count: int = 10, max_retries: int = 3) -> Exam:
    """Generate a fresh exam from a lesson via Ollama.

    Validates the response against the Exam schema; on JSON / schema /
    blank-count failures, retries with the error message included in the
    next prompt. Raises RuntimeError if all retries fail.
    """
    last_error: str | None = None
    for attempt in range(max_retries):
        prompt = _build_prompt(lesson, count, last_error)
        log.info("exam_creator: attempt %d/%d (lesson=%s, count=%d)",
                 attempt + 1, max_retries, lesson["id"], count)
        try:
            content = _call_ollama(prompt)
        except httpx.HTTPError as e:
            last_error = f"Ollama call failed: {type(e).__name__}: {e}"
            log.warning("exam_creator: %s", last_error)
            continue
        try:
            exercises = _parse_response(content)
        except (json.JSONDecodeError, ValidationError, TypeError, ValueError) as e:
            last_error = f"{type(e).__name__}: {e}"
            log.warning("exam_creator: attempt %d invalid: %s",
                        attempt + 1, last_error)
            continue
        if len(exercises) < count:
            last_error = f"only {len(exercises)} exercises generated, wanted {count}"
            log.warning("exam_creator: %s", last_error)
            continue

        exam_id, generated_at = _make_exam_id(lesson["id"])
        return Exam(
            id=exam_id,
            lesson_id=lesson["id"],
            lesson_title=lesson.get("title", ""),
            cefr=lesson.get("cefr", ""),
            generated_at=generated_at,
            count=len(exercises),
            exercises=exercises,
        )

    raise RuntimeError(
        f"exam generation failed after {max_retries} attempts. "
        f"Last error: {last_error}"
    )
