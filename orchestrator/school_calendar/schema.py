"""Calendar Event schema.

All event times are ISO 8601 strings WITH explicit offset
(e.g. "2026-06-02T08:30:00+07:00"). The all_day flag is a UI hint; for
all-day events the convention is start = 00:00 of day 1, end = 00:00 of
the day AFTER the last included day, so a single-day all-day event spans
exactly 24 hours.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class Event(BaseModel):
    id: str
    title: str
    start: str
    end: str
    all_day: bool = False
    source: Literal["docs", "shared", "personal"]
    description: str = ""
