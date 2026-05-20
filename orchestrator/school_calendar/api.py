"""Calendar HTTP API — FastAPI router mounted by main.py.

Routes (all under /calendar prefix):

    GET    /calendar/events                 list docs + shared events
                                            optional ?from=YYYY-MM-DD&to=YYYY-MM-DD
                                            filters in Asia/Bangkok (+07:00)
    POST   /calendar/events                 add a shared event (server-side store)
    DELETE /calendar/events/{event_id}      remove a shared event
                                            (returns 400 for docs events;
                                            they're immutable per release)

Personal events live in browser localStorage and never touch this API.

Auth: when CLASSROOM_CALENDAR_TEACHER_PASS is set in the environment,
POST and DELETE require a matching X-Teacher-Pass header. When the env
var is empty (the default), all routes are unauthenticated.
"""
from __future__ import annotations

import os
from datetime import datetime, time, timedelta, timezone

from fastapi import APIRouter, Header, HTTPException, Query, Response
from pydantic import ValidationError

from . import load_docs_events
from .schema import Event
from .store import add_shared_event, delete_shared_event, list_shared_events

router = APIRouter(prefix="/calendar", tags=["calendar"])

# All filters are interpreted in Asia/Bangkok. Storing the offset as a
# constant keeps the rest of the codebase honest — if the deployment ever
# moves school, this is the one place to change.
_TZ_BKK = timezone(timedelta(hours=7))

# Empty string = no gating. When set, POST and DELETE require the matching
# X-Teacher-Pass header. Read once at import; restart to change.
_TEACHER_PASS = os.getenv("CLASSROOM_CALENDAR_TEACHER_PASS", "")


def _check_teacher_pass(supplied: str | None) -> None:
    """Raise 403 when a pass is configured and the supplied header is
    missing or wrong. No-op when the env var is empty (default)."""
    if _TEACHER_PASS and supplied != _TEACHER_PASS:
        raise HTTPException(
            status_code=403, detail="Missing or invalid X-Teacher-Pass"
        )


def _parse_filter_date(value: str, field: str) -> datetime:
    """Parse a YYYY-MM-DD filter into a tz-aware datetime in Asia/Bangkok."""
    try:
        d = datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"{field} must be YYYY-MM-DD; got {value!r}",
        ) from e
    return datetime.combine(d, time.min, tzinfo=_TZ_BKK)


def _events_in_range(
    events: list[Event],
    date_from: str | None,
    date_to: str | None,
) -> list[Event]:
    """Return events that overlap [date_from 00:00, date_to 23:59:59.999999]
    in Asia/Bangkok. If both filters are None, returns events unchanged.
    """
    if date_from is None and date_to is None:
        return events
    from_dt = (
        _parse_filter_date(date_from, "from")
        if date_from is not None
        else datetime.min.replace(tzinfo=_TZ_BKK)
    )
    to_dt = (
        _parse_filter_date(date_to, "to").replace(
            hour=23, minute=59, second=59, microsecond=999999
        )
        if date_to is not None
        else datetime.max.replace(tzinfo=_TZ_BKK)
    )
    result: list[Event] = []
    for e in events:
        try:
            ev_start = datetime.fromisoformat(e.start)
            ev_end = datetime.fromisoformat(e.end)
        except ValueError:
            # Skip malformed events rather than 500ing the whole request.
            continue
        if ev_start <= to_dt and ev_end >= from_dt:
            result.append(e)
    return result


@router.get("/events")
async def list_events(
    from_: str | None = Query(None, alias="from"),
    to: str | None = Query(None),
) -> dict:
    """List calendar events.

    Returns docs events (from seed_wiki/calendar/school_events.json) and
    shared events (from /data/calendar/shared_events.json), optionally
    filtered by date range. Re-reads both files on every request so edits
    to either are reflected without a container restart.

    Personal events are client-side only and never come from this endpoint.
    """
    events = load_docs_events() + list_shared_events()
    filtered = _events_in_range(events, from_, to)
    return {"events": [e.model_dump() for e in filtered]}


@router.post("/events", status_code=201)
async def create_event(
    payload: dict,
    x_teacher_pass: str | None = Header(None, alias="X-Teacher-Pass"),
) -> dict:
    """Add a shared event.

    The server forces source='shared' regardless of the request body and
    assigns a UUID4 id when one isn't supplied. Returns the persisted
    event so the client can use the assigned id.
    """
    _check_teacher_pass(x_teacher_pass)
    try:
        event = add_shared_event(payload)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors()) from e
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    return {"event": event.model_dump()}


@router.delete("/events/{event_id}")
async def delete_event(
    event_id: str,
    x_teacher_pass: str | None = Header(None, alias="X-Teacher-Pass"),
) -> Response:
    """Remove a shared event by id. Returns 204 No Content on success.

    Docs events (term dates etc. from seed_wiki/calendar/school_events.json)
    are immutable per release — attempting to delete one returns 400 with
    a pointer to the source file.
    """
    _check_teacher_pass(x_teacher_pass)
    if any(e.id == event_id for e in load_docs_events()):
        raise HTTPException(
            status_code=400,
            detail=(
                "Docs events are immutable; "
                "edit seed_wiki/calendar/school_events.json to change them."
            ),
        )
    if not delete_shared_event(event_id):
        raise HTTPException(status_code=404, detail=f"Event {event_id!r} not found")
    return Response(status_code=204)
