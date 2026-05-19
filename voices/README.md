# Reference voice clips for XTTS cloning

Drop a 6+ second WAV (mono, 16-22 kHz, clean speech, no background music)
into this directory, then call /synthesize with `speaker_wav` set to the
container path:

```
curl -X POST http://localhost:8001/synthesize \
  -H 'Content-Type: application/json' \
  -d '{"text": "Hello, I am your tutor.", "speaker_wav": "/voices/me.wav"}' \
  --output cloned.wav
```

Files here are mounted read-only at /voices inside the tts container.
