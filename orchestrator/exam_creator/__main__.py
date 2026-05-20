"""CLI entry point: generate an exam from a lesson.

Usage (inside the orchestrator container):

    docker compose exec orchestrator python -m exam_creator past_simple
    docker compose exec orchestrator python -m exam_creator past_continuous --count 15

Reads lessons/{lesson_id}.json, calls Ollama, writes
data/exams/{lesson_id}_{ts}.json. Generation can take 30-90s on CPU —
prints a progress note to stderr.
"""
from __future__ import annotations

import argparse
import logging
import sys

from . import generate_exam, load_lesson, save_exam


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )

    parser = argparse.ArgumentParser(
        prog="python -m exam_creator",
        description="Generate a fresh fill-blank exam from a lesson via Ollama.",
    )
    parser.add_argument("lesson_id",
                        help="lesson id (matches lessons/{id}.json filename stem)")
    parser.add_argument("--count", type=int, default=10,
                        help="number of exercises to generate (default 10)")
    args = parser.parse_args()

    lesson = load_lesson(args.lesson_id)
    if lesson is None:
        print(f"error: lesson {args.lesson_id!r} not found in lessons/",
              file=sys.stderr)
        return 2

    print(f"generating {args.count} exercises from {args.lesson_id!r} "
          f"(this may take 30-90s on CPU)...", file=sys.stderr)

    try:
        exam = generate_exam(lesson, args.count)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    path = save_exam(exam)
    print(f"OK: wrote {path}")
    print(f"exam_id: {exam.id}")
    print(f"exercises: {len(exam.exercises)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
