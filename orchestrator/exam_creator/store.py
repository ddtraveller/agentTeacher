"""File-backed store for generated exams.

Exams persist to /data/exams/{exam_id}.json — bind-mounted to
./data/exams/ on the host, gitignored so each deployment keeps its own.
"""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from datetime import datetime, timedelta, timezone

from pydantic import ValidationError

from .schema import Exam, ExamBlank, ExamExercise, ExamInput

log = logging.getLogger("orchestrator.exam_creator.store")

EXAMS_DIR = Path(os.getenv("EXAMS_DIR", "/data/exams"))


def save_exam(exam: Exam) -> Path:
    """Write the exam to /data/exams/{exam_id}.json and return the path."""
    EXAMS_DIR.mkdir(parents=True, exist_ok=True)
    path = EXAMS_DIR / f"{exam.id}.json"
    # ensure_ascii=False keeps Thai / Chinese characters readable in git
    # diffs and `cat`. The directory is gitignored anyway, but readability
    # while debugging matters.
    path.write_text(
        json.dumps(exam.model_dump(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return path


def list_exams() -> list[dict]:
    """Return summary metadata for every exam on disk.

    Each entry: {id, lesson_id, lesson_title, cefr, generated_at, count}.
    Sorted by generated_at descending (newest first). Bad files are
    skipped with a warning rather than crashing the listing.
    """
    if not EXAMS_DIR.exists():
        return []
    results: list[dict] = []
    for p in sorted(EXAMS_DIR.glob("*.json"), reverse=True):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            results.append({
                "id":            data["id"],
                "lesson_id":     data["lesson_id"],
                "lesson_title":  data.get("lesson_title", ""),
                "cefr":          data.get("cefr", ""),
                "generated_at":  data.get("generated_at", ""),
                "count":         data.get("count", 0),
            })
        except (OSError, json.JSONDecodeError, KeyError) as e:
            log.warning("exam store: skipping unparseable %s: %s", p, e)
    return results


_TZ_BKK = timezone(timedelta(hours=7))


def exam_from_input(payload: ExamInput) -> Exam:
    """Convert a teacher-authored ExamInput into a full Exam ready to save.

    Generates id, generated_at, count, and per-exercise ids when absent.
    Each input exercise is either multi-choice (has `options`) or
    fill-blank (has `blanks`); the two are mutually exclusive.
    """
    now = datetime.now(_TZ_BKK)
    # Microsecond suffix so back-to-back POSTs don't collide on the same
    # wall-clock second and overwrite each other.
    ts = now.strftime("%Y%m%d-%H%M%S-") + f"{now.microsecond:06d}"
    safe_lesson = "".join(c if c.isalnum() or c in "_-" else "_"
                          for c in payload.lesson_id) or "custom"
    exam_id = f"{safe_lesson}_{ts}"

    exercises: list[ExamExercise] = []
    for i, inp in enumerate(payload.exercises):
        if inp.options and inp.blanks:
            raise ValueError(
                f"exercise {i + 1}: provide either `options` (multi-choice) "
                f"or `blanks` (fill-blank), not both"
            )
        if inp.options:
            # Multi-choice exercise
            if not all(o.text.strip() for o in inp.options):
                raise ValueError(
                    f"exercise {i + 1}: option text cannot be empty"
                )
            if not any(o.correct for o in inp.options):
                raise ValueError(
                    f"exercise {i + 1}: mark at least one option as correct"
                )
            exercises.append(ExamExercise(
                id=inp.id or f"ex_{i + 1:02d}",
                prompt=inp.prompt,
                prompt_th=inp.prompt_th,
                prompt_zh=inp.prompt_zh,
                blanks=[],
                options=inp.options,
                explanation_th=inp.explanation_th,
                explanation_zh=inp.explanation_zh,
            ))
        elif inp.blanks:
            # Fill-blank exercise (legacy / LLM path)
            n_underscores = inp.prompt.count("_____")
            if n_underscores == 0:
                raise ValueError(
                    f"exercise {i + 1}: fill-blank prompt has no '_____' marks"
                )
            if n_underscores != len(inp.blanks):
                raise ValueError(
                    f"exercise {i + 1}: {n_underscores} '_____' marks but "
                    f"{len(inp.blanks)} entries in blanks"
                )
            for j, b in enumerate(inp.blanks):
                if not b.accept:
                    raise ValueError(
                        f"exercise {i + 1} blank {j + 1}: at least one "
                        f"acceptable answer is required"
                    )
            exercises.append(ExamExercise(
                id=inp.id or f"ex_{i + 1:02d}",
                prompt=inp.prompt,
                prompt_th=inp.prompt_th,
                prompt_zh=inp.prompt_zh,
                blanks=inp.blanks,
                options=[],
                explanation_th=inp.explanation_th,
                explanation_zh=inp.explanation_zh,
            ))
        else:
            raise ValueError(
                f"exercise {i + 1}: provide either `options` "
                f"(multi-choice) or `blanks` (fill-blank)"
            )

    return Exam(
        id=exam_id,
        lesson_id=payload.lesson_id,
        lesson_title=payload.title,
        cefr=payload.cefr,
        generated_at=now.isoformat(),
        count=len(exercises),
        exercises=exercises,
    )


def load_exam(exam_id: str) -> Exam | None:
    """Load and validate the exam at /data/exams/{exam_id}.json."""
    path = EXAMS_DIR / f"{exam_id}.json"
    if not path.exists():
        return None
    try:
        return Exam(**json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValidationError) as e:
        log.warning("exam store: failed to load %s: %s", path, e)
        return None
