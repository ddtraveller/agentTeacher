"""Pull the configured Ollama model.

Run after `docker compose up -d` so Ollama is reachable on localhost:11434.
The first pull of qwen2.5:7b is ~4.4 GB — go make tea.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request

OLLAMA = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "qwen2.5:7b")


def wait_for_ollama(timeout: int = 120) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"{OLLAMA}/api/tags", timeout=2)
            return True
        except urllib.error.URLError:
            time.sleep(2)
    return False


def pull(model: str) -> None:
    print(f"Pulling {model} from Ollama...")
    body = json.dumps({"name": model}).encode()
    req = urllib.request.Request(
        f"{OLLAMA}/api/pull",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    last_status = ""
    with urllib.request.urlopen(req) as resp:
        for raw in resp:
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            status = event.get("status", "")
            if status and status != last_status:
                completed = event.get("completed")
                total = event.get("total")
                if completed and total:
                    pct = 100 * completed / total
                    print(f"  {status}  {pct:5.1f}%", end="\r", flush=True)
                else:
                    print(f"  {status}", flush=True)
                last_status = status
    print("\nDone.")


def main() -> int:
    print(f"Waiting for Ollama at {OLLAMA} ...")
    if not wait_for_ollama():
        print("Ollama is not responding. Is the container up?")
        print("  docker compose ps")
        return 1
    try:
        pull(MODEL)
    except urllib.error.HTTPError as e:
        print(f"Pull failed: HTTP {e.code} — {e.read().decode(errors='replace')}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
