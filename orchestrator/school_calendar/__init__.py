"""Calendar feature: docs-loaded, shared (file-backed), and personal (browser-local) events.

Docs events live in seed_wiki/calendar/school_events.json — bind-mounted
read-only at /data/wiki/calendar/school_events.json inside the container.
They are the school maintainer's source of truth (term dates, holidays,
exam weeks) and are loaded once at orchestrator startup.

Shared and personal events are added in later phases; this module starts
with the docs loader only.
"""
from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from pydantic import ValidationError

from .schema import Event

log = logging.getLogger("orchestrator.calendar")

# Default to <WIKI_PATH>/calendar/school_events.json. WIKI_PATH is set by
# the orchestrator's docker-compose env (defaults to /data/wiki). The
# CALENDAR_DOCS_PATH override is for running outside docker (tests / dev).
_WIKI_PATH = Path(os.getenv("WIKI_PATH", "/data/wiki"))
DOCS_EVENTS_PATH = Path(
    os.getenv(
        "CALENDAR_DOCS_PATH",
        str(_WIKI_PATH / "calendar" / "school_events.json"),
    )
)


def load_docs_events() -> list[Event]:
    """Load and validate the bind-mounted school_events.json.

    Returns an empty list (with a warning logged) if the file is missing
    or malformed, so the container still boots when the seed is bad —
    other features (chat, lessons) are unaffected by a broken calendar.
    """
    if not DOCS_EVENTS_PATH.exists():
        log.warning(
            "calendar: %s not found; no docs events loaded", DOCS_EVENTS_PATH
        )
        return []
    try:
        raw = json.loads(DOCS_EVENTS_PATH.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            raise TypeError(f"expected a JSON array, got {type(raw).__name__}")
        events = [Event(**item) for item in raw]
    except (OSError, json.JSONDecodeError, TypeError, ValidationError) as e:
        log.warning("calendar: failed to load %s: %s", DOCS_EVENTS_PATH, e)
        return []
    log.info(
        "calendar: loaded %d docs events from %s", len(events), DOCS_EVENTS_PATH
    )
    return events
