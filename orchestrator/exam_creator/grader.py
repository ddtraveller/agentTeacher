"""Deterministic grader for exam submissions.

INTENTIONAL DUPLICATION of _normalize_answer and the per-exercise grading
logic from main.py:429-457. Keeping a local copy here avoids a circular
import (main.py imports exam_creator.api; importing back from main would
hit a half-initialized module at startup). The duplicated code is small,
stable, and the LLM-as-grader anti-pattern (rubber-stamping wrong
answers) is exactly why this stays string-normalized rather than
delegated to anything smarter.
"""
from __future__ import annotations

import re


def _normalize_answer(s: str) -> str:
    """Lowercase, strip, collapse whitespace, expand common contractions."""
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("wasn't", "was not").replace("weren't", "were not")
    s = s.replace("didn't", "did not").replace("don't", "do not")
    return s


def grade_exercise(exercise: dict, answers: list[str]) -> dict:
    """Grade one exercise's answers.

    `answers` is a list of strings interpreted by question type:
      - Multi-choice exercise (has `options`): the strings are option
        texts the student checked. Correct iff the set equals the set
        of options marked correct.
      - Fill-blank exercise (has `blanks`, prompt has `_____`): one
        string per blank, the typed text. Each is compared against the
        blank's `accept` list after normalization.

    Response shape is identical for both modes so the UI handles them
    uniformly:
      {correct, per_blank, expected, correct_options}
    where for multi-choice, per_blank has exactly one entry.
    """
    options = exercise.get("options") or []
    if options:
        correct_set = {o["text"] for o in options if o["correct"]}
        chosen_set = set(answers or [])
        ok = chosen_set == correct_set
        sorted_correct = sorted(correct_set)
        return {
            "correct": ok,
            "per_blank": [ok],
            "expected": [", ".join(sorted_correct)],
            "correct_options": [sorted_correct],
        }

    blanks = exercise.get("blanks", [])
    if len(answers) != len(blanks):
        return {
            "correct": False,
            "per_blank": [False] * len(blanks),
            "expected": [
                (b.get("accept") or [""])[0] for b in blanks
            ],
            "correct_options": [None] * len(blanks),
        }
    per_blank: list[bool] = []
    expected: list[str] = []
    for typed, blank in zip(answers, blanks):
        norm = _normalize_answer(typed)
        accept_norm = {_normalize_answer(a) for a in blank.get("accept", [])}
        per_blank.append(norm in accept_norm)
        accept = blank.get("accept") or []
        expected.append(accept[0] if accept else "")
    return {
        "correct": all(per_blank),
        "per_blank": per_blank,
        "expected": expected,
        "correct_options": [None] * len(blanks),
    }
