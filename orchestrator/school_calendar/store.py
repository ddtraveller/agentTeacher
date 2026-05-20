"""File-backed store for shared calendar events.

Single-worker FastAPI deployment: a threading.Lock guards concurrent
read/modify/write so simultaneous POSTs don't lose updates. If the
orchestrator is ever run with --workers > 1, swap to filelock or sqlite
for cross-process safety.

Shared events persist to /data/calendar/shared_events.json — bind-mounted
to ./data/calendar on the host so they survive `docker compose down`.
"""
from __future__ import annotations

import json
import logging
import os
import threading
import uuid
from pathlib import Path

from pydantic import ValidationError

from .schema import Event

log = logging.getLogger("orchestrator.calendar.store")

SHARED_EVENTS_PATH = Path(
    os.getenv("CALENDAR_SHARED_PATH", "/data/calendar/shared_events.json")
)

_LOCK = threading.Lock()


def _load_unlocked() -> list[Event]:
    if not SHARED_EVENTS_PATH.exists():
        return []
    try:
        raw = json.loads(SHARED_EVENTS_PATH.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            log.warning(
                "calendar store: %s is not a JSON array; ignoring",
                SHARED_EVENTS_PATH,
            )
            return []
        return [Event(**item) for item in raw]
    except (OSError, json.JSONDecodeError, ValidationError, TypeError) as e:
        log.warning("calendar store: failed to load %s: %s", SHARED_EVENTS_PATH, e)
        return []


def _save_unlocked(events: list[Event]) -> None:
    SHARED_EVENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    # ensure_ascii=False keeps Thai/Chinese titles readable in git diffs.
    SHARED_EVENTS_PATH.write_text(
        json.dumps(
            [e.model_dump() for e in events], indent=2, ensure_ascii=False
        ),
        encoding="utf-8",
    )


def list_shared_events() -> list[Event]:
    """Return all shared events from disk."""
    with _LOCK:
        return _load_unlocked()


def add_shared_event(payload: dict) -> Event:
    """Append a new shared event. Server forces source='shared' and
    assigns a UUID4 id when absent. Raises ValidationError on bad payload.
    """
    payload = dict(payload)
    payload["source"] = "shared"
    if not payload.get("id"):
        payload["id"] = str(uuid.uuid4())
    event = Event(**payload)
    with _LOCK:
        events = _load_unlocked()
        events.append(event)
        _save_unlocked(events)
    return event


def delete_shared_event(event_id: str) -> bool:
    """Remove a shared event by id. Returns True if removed, False if
    nothing matched.
    """
    with _LOCK:
        events = _load_unlocked()
        new_events = [e for e in events if e.id != event_id]
        if len(new_events) == len(events):
            return False
        _save_unlocked(new_events)
        return True
