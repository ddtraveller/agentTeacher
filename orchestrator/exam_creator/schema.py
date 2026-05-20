"""Exam schema.

Mirrors the P2 exercise shape from lessons/*.json so the existing
_grade_p2 / _normalize_answer logic in main.py applies unchanged.
"""
from __future__ import annotations

from pydantic import BaseModel


class AnswerOption(BaseModel):
    """A multiple-choice option authored by the teacher.

    `correct` is server-only: the GET /exam/{id} endpoint strips it from
    the response so DevTools can't reveal the answer key.
    """
    text: str
    correct: bool


class ExamBlank(BaseModel):
    """A blank in a fill-blank prompt (legacy / LLM-generated).

    `accept` is the list of strings the student's typed answer is matched
    against after normalization. Multi-choice questions live at the
    exercise level (see ExamExercise.options) and do not use this type.
    """
    accept: list[str]


class ExamExercise(BaseModel):
    """A single exam question.

    Two mutually exclusive question modes:
      - **Multiple-choice** (manual UI): `options` is populated with the
        choices, each flagged correct/incorrect. The prompt has no
        `_____` markers. `blanks` is empty.
      - **Fill-blank** (legacy / LLM-generated): `blanks` is populated;
        the prompt has `_____` markers, one per entry in `blanks`.
        `options` is empty.

    The grader and UI detect type by checking which field is populated.
    """
    id: str
    prompt: str
    prompt_th: str = ""
    prompt_zh: str = ""
    blanks: list[ExamBlank] = []
    options: list[AnswerOption] = []
    explanation_th: str = ""
    explanation_zh: str = ""


class Exam(BaseModel):
    id: str                          # e.g. past_simple_20260520-143022
    lesson_id: str
    lesson_title: str
    cefr: str = ""
    generated_at: str                # ISO 8601 with offset
    count: int
    exercises: list[ExamExercise]


class ExamInputExercise(BaseModel):
    """An exercise as the teacher writes it — id is optional (server fills).

    Provide exactly one of:
      - `options`: list of {text, correct} for multi-choice. No `_____`
        markers in the prompt.
      - `blanks`: list of {accept: [...]} for fill-blank. One `_____` in
        the prompt per blank entry.
    """
    id: str = ""
    prompt: str
    prompt_th: str = ""
    prompt_zh: str = ""
    blanks: list[ExamBlank] = []
    options: list[AnswerOption] = []
    explanation_th: str = ""
    explanation_zh: str = ""


class ExamInput(BaseModel):
    """Teacher-authored payload for POST /exam.

    The server fills in `id`, `lesson_id` (default "custom"),
    `generated_at`, `count`, and exercise ids when missing.
    """
    title: str
    lesson_id: str = "custom"
    cefr: str = ""
    exercises: list[ExamInputExercise]
