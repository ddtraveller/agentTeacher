#!/usr/bin/env python3
"""Generate lesson illustrations via Gemini Nano Banana 2.

Reads <lesson_id>_image_prompts.json (style + per-image prompts), calls
gemini-3.1-flash-image-preview, and saves each result as a .jpg into the
orchestrator's static dir so the lesson UI picks it up immediately.

Usage:
    python gen_lesson_images.py past_continuous
    python gen_lesson_images.py past_continuous --only sunday_market
    python gen_lesson_images.py past_continuous --force   # regenerate even if file exists
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
import time
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
STATIC_DIR = HERE.parent / "static" / "lesson_images"
KEY_FILE = Path("C:/Users/Admin/claude/env.txt.txt")
MODEL = "gemini-3.1-flash-image-preview"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def load_api_key() -> str:
    if not KEY_FILE.exists():
        sys.exit(f"API key file not found: {KEY_FILE}")
    for line in KEY_FILE.read_text(encoding="utf-8").splitlines():
        if line.startswith("google-api:"):
            return line.split(":", 1)[1].strip()
    sys.exit("No google-api: line in env.txt.txt")


def generate_one(prompt: str, api_key: str, out_path: Path) -> None:
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    req = urllib.request.Request(
        f"{ENDPOINT}?key={api_key}",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        resp = json.loads(r.read().decode("utf-8"))

    parts = (resp.get("candidates", [{}])[0]
                 .get("content", {}).get("parts", []))
    for p in parts:
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(base64.b64decode(inline["data"]))
            return
    raise RuntimeError(f"No image in response: {json.dumps(resp)[:500]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("lesson_id")
    ap.add_argument("--only", help="Generate only this image key")
    ap.add_argument("--force", action="store_true",
                    help="Regenerate even if file exists")
    args = ap.parse_args()

    prompts_file = HERE / f"{args.lesson_id}_image_prompts.json"
    if not prompts_file.exists():
        sys.exit(f"Prompts file not found: {prompts_file}")
    cfg = json.loads(prompts_file.read_text(encoding="utf-8"))
    prefix = cfg.get("style_prefix", "")
    suffix = cfg.get("style_suffix", "")
    out_dir = STATIC_DIR / args.lesson_id

    api_key = load_api_key()
    images = cfg["images"]
    keys = [args.only] if args.only else list(images.keys())

    for i, key in enumerate(keys, 1):
        spec = images[key]
        out = out_dir / f"{key}.jpg"
        if out.exists() and not args.force:
            print(f"[{i}/{len(keys)}] skip {key} (exists)")
            continue
        prompt = prefix + spec["prompt"] + suffix
        print(f"[{i}/{len(keys)}] generating {key}…")
        try:
            generate_one(prompt, api_key, out)
            print(f"        -> {out}")
        except Exception as e:  # noqa: BLE001
            print(f"        FAILED: {e}", file=sys.stderr)
            continue
        # Be polite to the API.
        if i < len(keys):
            time.sleep(2)

    return 0


if __name__ == "__main__":
    sys.exit(main())
