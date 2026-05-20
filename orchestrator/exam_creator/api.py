"""Exam HTTP API — FastAPI router mounted by main.py.

Routes (all under /exam prefix):

    GET    /exam/list                 metadata for every exam on disk
    GET    /exam/{exam_id}            exam content WITHOUT accept lists
                                      (so DevTools can't reveal answers)
    POST   /exam/{exam_id}/submit     accept answers + return graded results
                                      (Phase 3 — added separately)
"""
from __future__ import annotations

import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .grader import grade_exercise
from .schema import ExamInput
from .store import exam_from_input, list_exams, load_exam, save_exam

router = APIRouter(prefix="/exam", tags=["exam"])

# Path-component validation. Exam ids look like "past_simple_20260520-143022";
# we accept letters, digits, underscore, and hyphen. Prevents path traversal
# via `..` and similar tricks.
_EXAM_ID_RE = re.compile(r"^[A-Za-z0-9_\-]+$")


@router.post("", status_code=201)
async def create_endpoint(payload: ExamInput) -> dict:
    """Create a teacher-authored exam from a JSON body.

    No LLM is involved — this is the manual / file-import path. The
    server generates the id and timestamps, validates that each prompt's
    "_____" blank count matches the declared blanks, and saves to disk.
    Returns the persisted Exam (including its assigned id).
    """
    try:
        exam = exam_from_input(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    save_exam(exam)
    return {"exam": exam.model_dump()}


@router.get("/list")
async def list_endpoint() -> dict:
    """List every exam on disk, newest first.

    Returns metadata only — id, lesson_id, lesson_title, cefr,
    generated_at, count — not the questions themselves.
    """
    return {"exams": list_exams()}


@router.get("/{exam_id}")
async def get_endpoint(exam_id: str) -> dict:
    """Fetch the exam by id, with answers stripped.

    The `accept` list on every blank is removed before returning so a
    student inspecting DevTools (or curl) cannot see the answer key.
    The grader (POST /exam/{id}/submit) still has access server-side.
    """
    if not _EXAM_ID_RE.match(exam_id):
        raise HTTPException(status_code=400, detail="bad exam id format")
    exam = load_exam(exam_id)
    if exam is None:
        raise HTTPException(status_code=404, detail=f"exam {exam_id!r} not found")

    # Strip answer keys before returning:
    #  - Multi-choice (`options` at exercise level): keep option text so
    #    the client can render checkboxes; drop `correct` so DevTools
    #    can't see which is right.
    #  - Fill-blank (`blanks` at exercise level): drop `accept` lists;
    #    the client only needs to know each blank exists (for counting).
    payload = exam.model_dump()
    for ex in payload["exercises"]:
        if ex.get("options"):
            ex["options"] = [{"text": o["text"]} for o in ex["options"]]
            ex["blanks"] = []
        else:
            ex["blanks"] = [{} for _ in ex.get("blanks", [])]
            ex["options"] = []
    return payload


class SubmitRequest(BaseModel):
    # answers[exercise_idx] is a list of strings, interpreted by type:
    #   Multi-choice: list of option texts the student checked (0 or more)
    #   Fill-blank:   one typed-text string per blank in the prompt
    answers: list[list[str]]


@router.post("/{exam_id}/submit")
async def submit_endpoint(exam_id: str, req: SubmitRequest) -> dict:
    """Grade submitted answers and return per-question results.

    Grading is deterministic — string normalization against the exam's
    `accept` lists. No LLM in the grading path; qwen2.5:3b would
    rubber-stamp wrong answers, per the same logic protecting lesson P2.

    Response shape:
      {
        "exam_id": "...",
        "score": {"correct": 7, "total": 10, "pct": 0.7},
        "per_question": [{id, correct, per_blank, expected,
                          explanation_th, explanation_zh}, ...]
      }
    """
    if not _EXAM_ID_RE.match(exam_id):
        raise HTTPException(status_code=400, detail="bad exam id format")
    exam = load_exam(exam_id)
    if exam is None:
        raise HTTPException(status_code=404, detail=f"exam {exam_id!r} not found")

    if len(req.answers) != len(exam.exercises):
        raise HTTPException(
            status_code=400,
            detail=(
                f"answer count mismatch: got {len(req.answers)} exercises, "
                f"exam has {len(exam.exercises)}"
            ),
        )

    per_question: list[dict] = []
    correct_count = 0
    for ex, ans in zip(exam.exercises, req.answers):
        ex_dict = ex.model_dump()
        grade = grade_exercise(ex_dict, ans)
        per_question.append({
            "id":               ex.id,
            "correct":          grade["correct"],
            "per_blank":        grade["per_blank"],
            "expected":         grade["expected"],
            "correct_options":  grade["correct_options"],
            "explanation_th":   ex.explanation_th,
            "explanation_zh":   ex.explanation_zh,
        })
        if grade["correct"]:
            correct_count += 1

    total = len(exam.exercises)
    return {
        "exam_id": exam.id,
        "score": {
            "correct": correct_count,
            "total":   total,
            "pct":     round(correct_count / total, 3) if total else 0.0,
        },
        "per_question": per_question,
    }
