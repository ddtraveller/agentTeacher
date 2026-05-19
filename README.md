# Kru Eng — Local AI English Tutor for Thai Schools

**ครูอิงค์ — ผู้ช่วยสอนภาษาอังกฤษด้วย AI ที่ทำงานในเครื่องของโรงเรียน**

A voice-in / voice-out English tutor that runs entirely on your school's
own PC. No student audio ever leaves the building. No subscription. No
account. No data shared with any cloud AI provider.

Built for Thai schools, Thai PDPA, and a Thai network connection that
isn't always cooperative.

```
[mic] -> Whisper (speech-to-text) -> Qwen 2.5 (language model)
                                          |
[speakers] <- Edge TTS / XTTS v2 <- reply text
```

## Why this exists

Schools using ChatGPT or other cloud AI for student English practice send
every student utterance to a US-based provider. Under Thailand's PDPA, that
exposes the school to a real compliance question — especially for minors.

This stack runs **entirely on your school's PC**. Whisper does speech
recognition locally. Qwen 2.5 generates replies locally. Edge TTS handles
voice output (free, online, voices only — no user audio sent).

Your students' voices never leave your network.

## What you get

- **Voice conversation practice** — students hold a button, speak, get a reply spoken back. Web UI works on any modern browser.
- **A 12-week A1→B1 curriculum** — English combined with Tech and AI literacy. Lives in `seed_wiki/` as plain markdown. Edit it to match your syllabus, your students' names, your teaching style.
- **A scaffolded PPP lesson engine** — Presentation → Practice → Production. Sample lesson included (Past Continuous).
- **Voice cloning, optional** — drop a 6-second WAV of any teacher's voice into `voices/`; XTTS v2 will clone it.
- **All open source.** MIT licensed.

## Quick start

You need [Docker Desktop](https://docs.docker.com/desktop/) with Compose v2.

```bash
git clone https://github.com/YOUR-USERNAME/kru-eng-classroom.git
cd kru-eng-classroom
cp .env.example .env                     # edit if you want; defaults work
docker compose up -d --build             # first build pulls ~2 GB
python scripts/pull_models.py            # pulls Qwen 2.5 (~2 GB for 3b, ~4.4 GB for 7b)
```

Then open **http://localhost:8000**. You should see a green health row at the
bottom. Hold the **🎙 Hold to talk** button, speak, release. The reply plays
back through your speakers.

## Hardware honestly

This is the section every other "local AI" project glosses over. The model
that makes this useful runs slowly on CPU. Plan accordingly.

| Setup | Reply latency | Verdict |
|---|---|---|
| 8th-gen i5 / 16 GB RAM / no GPU, qwen2.5:3b | 8–20s per reply | Usable for homework practice; not for live classroom |
| Ryzen 7 / 32 GB RAM / no GPU, qwen2.5:7b | 15–40s per reply | Painful. Don't. |
| Any decent NVIDIA GPU (RTX 3060+) / qwen2.5:7b | 1–3s per reply | This is the real experience |
| Mac M2/M3 with 16+ GB / qwen2.5:7b (host Ollama) | 2–4s per reply | Comparable to a GPU |

**Recommended setup for a school:** one mid-range gaming PC (~฿30,000 used)
with a used RTX 3060 or 4060, running this stack 24/7 in a corner of the
computer lab. Students take turns using it.

You need ~12 GB disk for the models, plus another ~5 GB for Whisper and XTTS.

## Customizing Kru Eng for your school

The `seed_wiki/` directory is the bot's brain. It's all plain markdown.
Edit it however you want — the bot picks up your changes the next time it
indexes (or set `RAG_ENABLED=true` in `.env` and restart).

Quick wins:

- `seed_wiki/school/about_kru_eng.md` — change the school name, your
  pedagogical philosophy, what you want the bot to know about your
  institution.
- `seed_wiki/staff/kru_eng_persona.md` — the bot's voice and tone. Make her
  formal, casual, more Thai-leaning, whatever fits your school.
- `seed_wiki/students/` — one markdown file per student. The bot adapts to
  individual learners' levels and interests. Template included.
- `seed_wiki/lessons/` — twelve weekly lessons covering English + tech +
  AI. Each follows a common template (Presentation, Practice, Production).
  Add, edit, remove freely.

The wiki is in English because English is the language Qwen reasons best in.
Thai gloss goes inline in parentheses: `market (ตลาด)`. Don't translate
whole sentences — the bot does that on output.

## Endpoints

The orchestrator exposes these on port 8000:

| Endpoint | Purpose |
|---|---|
| `GET  /` | Web UI (mic + speaker) |
| `GET  /health` | Per-backend status (used by UI footer) |
| `POST /chat` | `{message, history}` → streaming text reply |
| `POST /converse` | Multipart audio in → `{user, bot, audio, visemes}` |
| `POST /speak` | `{text}` → audio (TTS only — handy for testing) |
| `GET  /lesson` | Scaffolded PPP lesson UI |
| `GET  /lesson/list` | List available lesson plans |

## Day-2 operations

```bash
docker compose ps                # check all services are up
docker compose logs -f orchestrator
docker compose logs -f tts       # watch on first request — XTTS download is slow
docker compose down              # stop
docker compose down -v           # stop + delete model volumes (frees ~15 GB)
```

## Configuration reference

All knobs live in `.env`. See `.env.example` for the full annotated list.
The headline ones:

| Variable | Default | What it does |
|---|---|---|
| `MODEL` | `qwen2.5:3b` | Any tag from https://ollama.com/library |
| `WHISPER_MODEL` | `small` | `tiny` / `base` / `small` / `medium` / `large-v3` |
| `TTS_DEVICE` | `cpu` | Set to `cuda` once you wire GPU into the tts image |
| `RAG_ENABLED` | `false` | Set to `true` to ground replies in `seed_wiki/` |

## Known limitations

- **First `/synthesize` for ja/ko is slow** — XTTS v2 weights (~2 GB)
  download lazily on first non-en/th/zh call. English, Thai, and Chinese
  go through Edge TTS so they have no warmup penalty.
- **CPU XTTS is slow.** ~0.3× realtime for ja/ko. Switch the tts Dockerfile
  to a CUDA torch wheel + uncomment the GPU stanza in compose for usable
  latency on those languages.
- **No persistent chat history.** `/converse` is single-turn server-side.
  The UI keeps history in JS and passes it to `/chat`. Add a session store
  (Redis/SQLite) when you want multi-device continuity.
- **GPU on Windows** needs Docker Desktop WSL2 + NVIDIA Container Toolkit.
  The compose file has the GPU block commented out — uncomment when set up.
- **Edge TTS needs internet.** It's a free Microsoft service. If your
  school's connection is offline, English/Thai TTS falls back to nothing.
  For fully-offline TTS, swap Edge TTS for Piper in `tts/server.py`.

## File layout

```
kru-eng-classroom/
├── docker-compose.yml
├── .env.example
├── README.md (this file)
├── LICENSE (MIT)
├── orchestrator/                 # FastAPI app: STT → LLM → TTS glue
│   ├── Dockerfile
│   ├── main.py                   # /chat, /converse, /speak, /lesson, /health
│   ├── requirements.txt
│   ├── static/                   # Web UI (mic + speaker, lesson page)
│   └── lessons/                  # Lesson plan JSONs (PPP scaffolds)
├── tts/                          # TTS service: Edge TTS + XTTS v2 + Rhubarb
│   ├── Dockerfile
│   ├── server.py
│   └── requirements.txt
├── voices/                       # Drop WAV reference clips here for XTTS cloning
│   └── README.md
├── seed_wiki/                    # The bot's brain — edit this for your school
│   ├── INDEX.md
│   ├── README.md
│   ├── school/                   # Identity, mission, methodology
│   ├── staff/                    # Bot persona (the system prompt)
│   ├── students/                 # Per-learner profiles
│   ├── curriculum/               # 12-week scope
│   ├── lessons/                  # Weekly lesson markdown
│   ├── vocabulary/               # Lexical chunks
│   ├── pronunciation/            # Thai L1 interference patterns
│   ├── grammar/                  # Form-meaning-use
│   ├── assessment/               # Formative techniques
│   └── references/               # Methodology + bibliography
└── scripts/
    └── pull_models.py            # Bootstrap Ollama after first compose up
```

## What this is not

- **Not a SaaS.** There is no cloud version. There is no account. You run it.
- **Not a finished commercial product.** It's a working tool, polished
  where it needed to be, rough where it didn't. PRs and forks welcome.
- **Not a replacement for a teacher.** It's a practice partner. Use it for
  the speaking drills your teachers don't have time for.
- **Not legal advice.** If your school's PDPA officer wants a data-flow
  diagram, the architecture section above is your starting point. Talk to
  them.

## Contributing

PRs welcome. The code is intentionally small — ~700 lines of Python for
the orchestrator, ~300 for the TTS service. Read both files before
proposing structural changes.

Issues from teachers who've tried to deploy this are particularly valuable
— if you got stuck somewhere, that's a documentation bug.

## License

Code: MIT (see [LICENSE](./LICENSE)).

AI models you'll download are governed by their own licenses (Qwen, Whisper,
XTTS v2, Edge TTS) — also documented in [LICENSE](./LICENSE). The default
configuration routes English, Thai, and Chinese through Edge TTS, leaving
XTTS v2 only for Japanese/Korean — keep that in mind for commercial use,
since XTTS is non-commercial.

## Credits

Built in Chiang Mai by the [krueng.ai](https://krueng.ai) project — a free
bilingual TEFL site for Thai learners of English. If this stack helps your
school, the best thank-you is a note saying so.

Made with care for Thai students. ขอบคุณค่ะ.
