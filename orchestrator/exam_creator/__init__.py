"""Exam creator: LLM-generated fill-blank exams from existing lessons.

Generated exams live in /data/exams/{exam_id}.json (bind-mounted writable).
Grading uses the same deterministic logic as the P2 phase of lessons
(reuses _grade_p2 / _normalize_answer from main.py).
"""
from __future__ import annotations

from .generator import generate_exam, load_lesson
from .schema import (
    AnswerOption,
    Exam,
    ExamBlank,
    ExamExercise,
    ExamInput,
    ExamInputExercise,
)
from .store import exam_from_input, list_exams, load_exam, save_exam

__all__ = [
    "AnswerOption",
    "Exam",
    "ExamBlank",
    "ExamExercise",
    "ExamInput",
    "ExamInputExercise",
    "generate_exam",
    "load_lesson",
    "exam_from_input",
    "list_exams",
    "load_exam",
    "save_exam",
]
