# Hybrid TTS service:
#   - Coqui XTTS v2 for en/es/fr/de/it/pt/pl/tr/ru/nl/cs/ar/zh-cn/hu/ko/ja/hi
#     (with optional voice cloning from a 6+ second reference WAV)
#   - Piper for Thai (th_TH-anchali-medium) — XTTS doesn't support Thai upstream
#
# License notes:
#   - XTTS v2 is CPML — non-commercial only. Fine for personal/teaching use.
#   - Piper voices are MIT/community licenses; check per voice if shipping.

FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    COQUI_TOS_AGREED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential ffmpeg libsndfile1 espeak-ng curl unzip \
    && rm -rf /var/lib/apt/lists/*

# Rhubarb Lip Sync — generates Preston-Blair mouth-shape timings from a WAV.
# Used downstream by the orchestrator UI to drive an animated face.
RUN curl -fL -o /tmp/rhubarb.zip \
        https://github.com/DanielSWolf/rhubarb-lip-sync/releases/download/v1.13.0/Rhubarb-Lip-Sync-1.13.0-Linux.zip && \
    unzip -q /tmp/rhubarb.zip -d /opt && \
    mv /opt/Rhubarb-Lip-Sync-1.13.0-Linux /opt/rhubarb && \
    ln -s /opt/rhubarb/rhubarb /usr/local/bin/rhubarb && \
    rm /tmp/rhubarb.zip

WORKDIR /app

# CPU torch. Swap for a CUDA wheel + nvidia base image for GPU.
RUN pip install --index-url https://download.pytorch.org/whl/cpu \
        torch==2.2.2 torchaudio==2.2.2

# Coqui XTTS — `coqui-tts` is the maintained fork (idiap) of the archived coqui-ai/TTS.
RUN pip install "coqui-tts>=0.24,<0.27"

# Piper TTS — provides the `piper` CLI and the Python `piper` package.
RUN pip install piper-tts

COPY requirements.txt .
RUN pip install -r requirements.txt

# Thai Piper voice is NOT baked in — rhasspy/piper-voices has no Thai voice.
# Mount one at /models/piper/<voice>.onnx (+ .json) and set PIPER_VOICE to point
# at it, or Thai requests will fail at runtime. XTTS v2 weights (~2 GB) are still
# pulled lazily on first /synthesize and cached in ~/.local/share/tts.
RUN mkdir -p /models/piper

COPY server.py .

EXPOSE 8001

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]
