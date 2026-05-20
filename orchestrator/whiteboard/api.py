"""Whiteboard HTTP API — FastAPI router mounted by main.py.

Routes (under /whiteboard prefix):

    POST /whiteboard/analyze    body {image: "data:image/png;base64,..."}
                                → {description, vocab, encouragement}

The endpoint strips the data URL prefix, validates that the rest is
real base64, posts the bare bytes to Ollama's /api/chat with the
configured vision model (qwen2.5vl:3b by default), and parses the
returned JSON into the response shape.

No image bytes are stored. No image bytes are logged. The vision
model's response is returned to the caller and forgotten.
"""
from __future__ import annotations

import base64
import binascii
import json
import logging
import os

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

log = logging.getLogger("orchestrator.whiteboard")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
VISION_MODEL = os.getenv("VISION_MODEL", "qwen2.5vl:3b")
ANALYZE_TIMEOUT = int(os.getenv("WHITEBOARD_TIMEOUT", "180"))

# 2 MB cap on the incoming data URL. An 800×500 antialiased PNG is
# typically 50-300 KB; 2 MB is generous headroom and bounds DoS exposure.
MAX_IMAGE_BYTES = 2 * 1024 * 1024

# Strict tutor prompt — short, encouraging, English-only, vocab-focused.
# Asks for JSON so the client can render structured output cleanly.
_SYSTEM_PROMPT = (
    "You are Kru Eng, a warm English tutor in Chiang Mai. A student has "
    "drawn a picture on a digital whiteboard. Look at the picture and "
    "respond in JSON with three fields:\n"
    "  - description: 1-2 sentences describing what you see (in English)\n"
    "  - vocab: an array of 2-4 useful English words related to the picture\n"
    "  - encouragement: one warm sentence encouraging the student to "
    "keep practicing English\n"
    "Reply ONLY with the JSON object. No markdown, no prose around it."
)

router = APIRouter(prefix="/whiteboard", tags=["whiteboard"])


class AnalyzeRequest(BaseModel):
    image: str  # data URL: "data:image/png;base64,<...>"


class AnalyzeResponse(BaseModel):
    description: str
    vocab: list[str]
    encouragement: str


def _extract_b64(image_url: str) -> str:
    """Strip the data:image/...;base64, prefix and validate the remainder."""
    if not image_url:
        raise HTTPException(status_code=400, detail="image is empty")
    if len(image_url) > MAX_IMAGE_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"image is too large (>{MAX_IMAGE_BYTES // (1024*1024)} MB)",
        )
    prefix_end = image_url.find(",")
    if image_url.startswith("data:") and prefix_end > 0:
        b64 = image_url[prefix_end + 1:]
    else:
        # Allow a bare base64 string too (no data URL wrapper)
        b64 = image_url
    try:
        # Decode to verify, then discard the bytes — we send the base64
        # string to Ollama, not the raw bytes.
        base64.b64decode(b64, validate=True)
    except (binascii.Error, ValueError) as e:
        raise HTTPException(
            status_code=400, detail=f"image is not valid base64: {e}"
        ) from e
    return b64


@router.post("/analyze")
async def analyze_endpoint(req: AnalyzeRequest) -> AnalyzeResponse:
    """Send the canvas PNG to the local vision model and return a
    structured tutor reaction.

    Returns a graceful fallback if the model's JSON output is malformed
    (rare with format=json but qwen2.5vl can wander) so the UI still
    gets *something* useful to show.
    """
    b64 = _extract_b64(req.image)

    payload = {
        "model": VISION_MODEL,
        "messages": [
            {"role": "system", "content": _SYSTEM_PROMPT},
            {
                "role": "user",
                "content": "Describe the student's drawing.",
                "images": [b64],
            },
        ],
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.7,
            "num_predict": 400,
            "num_ctx": 4096,
        },
    }

    try:
        async with httpx.AsyncClient(timeout=ANALYZE_TIMEOUT) as c:
            r = await c.post(f"{OLLAMA_URL}/api/chat", json=payload)
            r.raise_for_status()
            content = r.json()["message"]["content"]
    except httpx.HTTPError as e:
        log.warning("whiteboard: Ollama call failed: %s", e)
        raise HTTPException(
            status_code=502,
            detail=f"vision model unavailable: {type(e).__name__}",
        ) from e

    log.info("whiteboard: vision response %d chars", len(content))

    try:
        data = json.loads(content)
        return AnalyzeResponse(
            description=str(data.get("description", "")).strip(),
            vocab=[str(v).strip() for v in data.get("vocab", []) if str(v).strip()],
            encouragement=str(data.get("encouragement", "")).strip(),
        )
    except (json.JSONDecodeError, TypeError, ValueError):
        # The model returned non-JSON; surface the raw text as description
        # so the UI shows *something*, and leave vocab + encouragement
        # blank rather than 500ing.
        log.warning("whiteboard: model output wasn't JSON; falling back")
        return AnalyzeResponse(
            description=content.strip()[:500],
            vocab=[],
            encouragement="",
        )
