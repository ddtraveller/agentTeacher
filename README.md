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
every student utterance to a US-based provider. Under Thailand's PDPA,
that exposes the school to a real compliance question — especially for
minors.

Two things make this worse going forward:

1. **ChatGPT's free tier is moving to ad-supported.** OpenAI has signaled
   plans to monetize free-tier users with advertising and partnerships,
   which means student conversations become training and targeting
   signal. Schools sending student queries to a free-tier US AI service
   are not the customer — they're the product.
2. **Mass data transfer to American AI providers is an emerging legal
   risk.** Thailand's PDPA, the EU's GDPR-influenced rules, and recent
   education-sector data rulings all point the same direction: bulk
   transfer of student utterances — especially minors' — to overseas
   processors is exposure waiting to happen. Schools that haven't been
   audited yet probably will be.

This stack runs **entirely on your school's PC**. Whisper does speech
recognition locally. Qwen 2.5 generates replies locally. Edge TTS
handles voice output (free Microsoft service, voices only — no user
audio sent). Your students' voices never leave your network. Your
school's curriculum, your students' progress data, your teachers'
custom materials — none of it gets uploaded anywhere.

## What you get

- **Voice conversation practice** — students hold a button, speak, get a reply spoken back. Web UI works on any modern browser.
- **A 12-week A1→B1 curriculum** — English combined with Tech and AI literacy. Lives in `seed_wiki/` as plain markdown. Edit it to match your syllabus, your students' names, your teaching style.
- **A scaffolded PPP lesson engine** — Presentation → Practice → Production. Sample lesson included (Past Continuous).
- **Voice cloning, optional** — drop a 6-second WAV of any teacher's voice into `voices/`; XTTS v2 will clone it.
- **All open source.** MIT licensed.

## What schools can do with it

The same local-AI stack underneath Kru Eng can power a lot more than
English speaking practice. Below: what's possible today with what ships
in this repo, what's a small extension away, and what you could grow
into. All of it stays on your PC.

### Today, with what ships in this repo

- **A 24/7 English speaking partner.** Students who never speak in
  class because they're embarrassed will talk to a bot. The bot doesn't
  judge, doesn't get tired, doesn't run out of patience.
- **A tireless homework grader.** Plug your rubric into
  `seed_wiki/assessment/`, drop student work into a chat, get
  consistent feedback in seconds. Teachers spot-check; the bot drafts.
- **A lesson planner and quiz generator.** Ask for a 45-minute lesson
  on a topic; the bot drafts presentation slides, practice exercises,
  and an exit ticket — grounded in your school's curriculum, not a
  generic textbook.
- **A teaching assistant that knows your students.** Per-learner
  markdown profiles in `seed_wiki/students/` let the bot adapt
  difficulty, remember a student's interests, and follow up on
  previous conversations. Add or remove students by editing files.
- **An institutional Q&A bot.** Drop your school handbook, dress code,
  schedule, holiday calendar, and SOPs into the wiki. Students, parents,
  and staff can ask in natural language and get cited answers — never
  invented.
- **A safe alternative to ChatGPT for student exploration.** The same
  curiosity-driven "let me ask the AI" instinct, redirected to a system
  the school controls. Schools can decide what topics the bot will and
  won't discuss by editing the persona file.
- **A multilingual tutor.** English, Thai, Chinese, Japanese, Korean —
  all handled. Useful for international students, EP programs, and
  Chinese-Thai dual-language schools.

### A small extension away (a few hours of work each)

- **A LINE chatbot for parents and students.** Same agent, accessed via
  Thailand's dominant chat app. Push daily vocab cards, homework
  reminders, exam-prep prompts. Kids practice English while waiting for
  the bus.
- **Scheduled tasks.** "Push 5 vocabulary cards to M4/2 at 7 AM every
  weekday." "Email the principal a summary of student questions every
  Friday afternoon." Cron + the local agent = zero monthly cost.
- **A local website on the school LAN.** The orchestrator already
  serves a web UI. Open the port to the LAN and any phone, tablet, or
  PC on the school network can use it — no app install, no internet,
  no per-seat license. Students get one URL; staff get another with
  different permissions.
- **Local image generation for classroom materials.** SDXL Turbo runs on
  any decent GPU. Worksheets, slide illustrations, vocab flashcards —
  generated on demand from a teacher's prompt, sized correctly,
  printable. No Canva subscription.
- **Voice cloning for specific teachers.** Already in the box. Record a
  teacher's voice once, and the bot can deliver lessons in their voice
  — useful for absent-teacher cover, accent modeling, or recordings
  that sound like the actual classroom teacher.
- **Multi-agent role-play.** Two instances of the bot with different
  personas talking to each other (Customer + Shopkeeper, Doctor +
  Patient, Teacher + Student). Students join the dialogue or watch and
  transcribe — a TEFL technique that's expensive with humans, free
  with two local agents.

### A bigger project (worth doing if it matches your school's needs)

- **A digital security guard.** Local vision models (Qwen-VL, LLaVA,
  Llama Vision) can watch a camera feed and flag anomalies — a student
  in a restricted area, an open gate after hours, a fall in a stairwell.
  Runs on the same GPU. Nothing leaves the building. Privacy-preserving
  by design — the model sees frames; only flagged events get logged.
- **Whole-school staff agent.** HR FAQs, leave-request walkthroughs,
  finance-form lookups. Most internal admin questions are repetitive —
  let staff ask the bot and free your office for the hard cases.
- **Curriculum-specific tutoring beyond English.** Math, science,
  Thai-language exam prep — change the seed wiki, change the persona,
  same infrastructure. One local AI, many subjects.
- **Knowledge preservation.** Every veteran teacher who retires takes
  hard-won expertise with them. Capture it in markdown over a year of
  conversations, and the institution keeps the knowledge — without
  ever uploading it to a third party who would train on it.

### Using your school's existing digital media as the AI's knowledge

A school doesn't start with an empty bot. Most schools already have
years of materials gathering dust on shared drives — and all of it can
become the AI's corpus:

- **PDFs and Word documents** — lesson plans, worksheets, parent
  handbooks, policy documents, course outlines. The shipped index
  pipeline reads markdown only (by design — keeps the corpus clean),
  so convert these to `.md` first. `pandoc input.docx -o output.md`
  handles Word in one line; PDFs are stickier — try `pandoc`,
  `pdftotext`, or `marker` (best for layout-heavy PDFs) and review the
  output. See the "Adding your own knowledge files" section below for
  the full recipe.
- **Slide decks** — PowerPoint files convert to markdown easily. The
  bot then references "Slide 12 of the Photosynthesis deck" when a
  student asks about chloroplasts.
- **Recorded lectures and audio** — feed them through Whisper (already
  in this stack) to produce text transcripts. The bot can then answer
  "what did Ajarn Som say about the Sukhothai period last term?"
- **Scanned books and handwritten notes** — OCR them (Tesseract works
  well for Thai + English) and the text joins the corpus. A school's
  out-of-print textbooks become searchable.
- **Past exam papers** — become practice material. The bot generates
  variations grounded in your school's actual exam style, not generic
  textbook patterns.
- **Photos of classroom whiteboards** — vision models can extract the
  text. A semester of whiteboard work becomes a study reference.
- **Old teacher emails, parent newsletters, school magazines** — your
  institutional voice and history. The bot learns to *sound like your
  school*, not like a generic tutor.

The pattern is always the same: text-bearing artifact → wiki markdown
→ indexed → the bot uses it. Once a school commits to feeding its
existing materials in, the AI rapidly becomes more useful than any
cloud tutor could be — because it knows things only your school knows.

### What stays safe

Local AI is the only deployment model where **your school's special
knowledge** can be used by AI *and* stay yours. Everything that lives
in `seed_wiki/` — past exam patterns, your school's pedagogical method,
the rubrics you've refined over a decade, your students' progress
notes, parent communication templates, internal SOPs — feeds the bot
without leaking to anyone. The model uses it; nobody trains on it.

Compare to a cloud AI: every question your teachers type, every
student utterance, every uploaded document becomes training data,
targeting signal, or both. Your school's hard-won expertise becomes
free fuel for someone else's product.

### What it can produce

- **Text** — lesson plans, rubrics, parent communications, worksheets,
  exam questions, vocab lists, story prompts.
- **Audio** — narrated lessons, pronunciation models, audiobooks in
  Thai or English, voice-cloned teacher recordings.
- **Images** — classroom illustrations, vocab flashcards, worksheet
  graphics (with a GPU and SDXL Turbo).
- **Structured data** — student progress reports, class summaries,
  attendance digests, exam analytics — all in formats your existing
  systems can ingest.

## System requirements

### Minimum (works, but slow on CPU)

- **OS:** Windows 10/11, macOS 12+, or Linux (any modern distro)
- **CPU:** Any 64-bit x86 or Apple Silicon, 4 cores
- **RAM:** 8 GB (16 GB strongly recommended)
- **Disk:** 20 GB free (~15 GB for AI models + 5 GB for Docker images and indices)
- **Docker:** Docker Desktop with Compose v2 (Linux: Docker Engine 24+ with the compose plugin)
- **Network:** Internet for first install (Docker images + Ollama model downloads). After that, only Edge TTS needs internet — Whisper, Ollama, and the wiki all work fully offline
- **Browser:** Chrome, Edge, Firefox, or Safari — recent versions, with microphone permission
- **Microphone + speakers** (or headset) on the host machine

### Recommended (responsive for live classroom use)

- **GPU:** NVIDIA card with **6 GB+ VRAM** and a recent CUDA driver (RTX 3060, 4060, or better). Or a Mac with Apple Silicon M2/M3 and 16+ GB unified memory running Ollama natively on the host
- **RAM:** 32 GB if running qwen2.5:7b or larger
- **Disk:** 50 GB free if you plan to add custom models, more lessons, image generation, or video
- **A dedicated PC** the school can leave on 24/7 in a quiet corner — laptops thermally throttle under sustained AI load

### Ports the stack uses

The Docker stack publishes these ports on the host. Make sure nothing
else is listening on them, or remap in `docker-compose.yml`:

| Port | Service | What it serves |
|---|---|---|
| **8000** | orchestrator | Web UI + REST API (the thing students/teachers open in a browser) |
| **11434** | ollama | Language model inference (internal — only the orchestrator calls it) |
| **9000** | whisper | Speech-to-text (internal) |
| **8001** | tts | Text-to-speech (internal — useful to hit directly for testing) |

For a school LAN deployment, only port 8000 needs to be reachable from
student devices — the rest stay private to the host.

### Windows-specific notes

- Docker Desktop requires **WSL2 backend**. Enable WSL2 before installing
  Docker Desktop.
- For GPU on Windows, you also need **NVIDIA Container Toolkit**
  inside WSL2. The compose file has the GPU stanza commented out —
  uncomment it once the toolkit is set up.
- Path lengths: keep the install directory short (e.g.,
  `C:\krueng\`) — deep paths can trip Docker volume mounts on Windows.

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

### What to open in a browser

| URL | What you'll see |
|---|---|
| **http://localhost:8000/** | Web UI — mic + speaker chat with Kru Eng. Click "🎙 Hold to talk", speak, release. |
| **http://localhost:8000/lesson** | Scaffolded PPP lesson UI — runs the Past Continuous lesson (presentation → practice → production). |

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
Edit it however you want, then restart the orchestrator and the bot
uses your changes.

### Quick wins (files you can edit today)

- `seed_wiki/school/about_kru_eng.md` — change the school name, your
  pedagogical philosophy, what you want the bot to know about your
  institution.
- `seed_wiki/staff/kru_eng_persona.md` — the bot's voice and tone. Make
  her formal, casual, more authoritative, whatever fits your school.
- `seed_wiki/students/` — one markdown file per student. The bot adapts
  to individual learners' levels and interests. Template included.
- `seed_wiki/lessons/` — twelve weekly lessons covering English + tech +
  AI. Each follows a common template (Presentation, Practice,
  Production). Add, edit, remove freely.

The wiki is in English because English is the language Qwen reasons best
in. Native-script terms can be quoted inline (`market (ตลาด)`), but
don't translate whole sentences — that's the bot's job at output time.

### Adding your own knowledge files (step by step)

Use this when you have school-specific content the default wiki doesn't
cover: your handbook, your past exams, your syllabus, your teachers'
notes, your subject curriculum. The bot then cites your file when a
student asks something covered there.

**1. Turn on retrieval.** Edit `.env` and set:

```
RAG_ENABLED=true
```

This is `false` by default because the empty wiki doesn't need RAG and
turning it on costs ~30s at first startup (one-time index build). Once
you have your own content, you want it on.

**2. Put your file in the right place.** Filename in
`lower_snake_case.md`, dropped into the directory that matches its
topic:

```
seed_wiki/
├── school/        ← school identity, mission, philosophy
├── staff/         ← the bot's persona (only one file expected)
├── students/      ← one file per real learner
├── curriculum/    ← week-by-week scope, term plans
├── lessons/       ← lesson plans
├── vocabulary/    ← lexical chunks, term lists
├── pronunciation/ ← phonics, common-error patterns
├── grammar/       ← grammar references
├── assessment/    ← rubrics, exam patterns, formative techniques
└── references/    ← methodology, bibliography, recipes
```

If none of those fit, create a new top-level directory — e.g.,
`seed_wiki/handbook/` for your school handbook chapters, or
`seed_wiki/policies/` for SOPs. The indexer recurses automatically.

**3. Add frontmatter at the top of every file** (strongly recommended,
not strictly required):

```yaml
---
title: Year 10 Marking Rubric
type: assessment
status: live
topic: rubrics, exam marking, year 10
updated: 2026-05-19
---

# Year 10 Marking Rubric

(your content starts here)
```

The frontmatter helps you and the bot navigate. `status: live` is the
convention for "this is real, please use it"; pages without it are
treated as drafts. `topic:` is a free-text tag — list whatever a student
might ask about that should land them here.

**4. Force a reindex.** The orchestrator persists the index to disk, so
new files aren't picked up automatically — restart the orchestrator and
delete the index cache:

```bash
docker compose down
docker volume rm kru-eng-classroom_wiki_index
docker compose up -d
```

Watch the logs to confirm the rebuild ran:

```bash
docker compose logs orchestrator | grep -i index
```

You should see `building wiki index from /data/wiki (this happens once)`
followed by `wiki index built: N documents indexed`. If `N` is what you
expect (existing docs + your new ones), you're good.

**5. Verify it landed.** Ask the bot something only your new file
answers:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What is the Year 10 marking rubric for essays?","history":[]}' \
  | tail -c 200
```

The reply should include the content, and the orchestrator's response
metadata will include a `citations` array naming the file (e.g.,
`["assessment_year10_rubric"]`). If you get a generic reply with no
citation, the file either didn't index or RAG isn't enabled.

### What file formats actually work

The shipped indexer reads **`.md` files only** — that's by design
(corpus stays clean and reviewable; the bot reads the same files a
teacher can read). For other formats, convert to markdown first:

| You have | Tool | One-liner |
|---|---|---|
| `.docx` (Word) | pandoc | `pandoc handbook.docx -o handbook.md` |
| `.pdf` (text PDFs) | pandoc / pdftotext | `pdftotext -layout doc.pdf - > doc.md` |
| `.pdf` (scanned / layout-heavy) | marker | `marker_single scan.pdf out_dir` (best results) |
| `.pptx` (PowerPoint) | pandoc | `pandoc slides.pptx -o slides.md` |
| `.xlsx` (Excel) | pandoc / python | `pandoc data.xlsx -o data.md` (small tables); script for big sheets |
| Audio (lectures) | Whisper (already in this stack) | `curl -F "audio_file=@lecture.m4a" http://localhost:9000/asr?output=txt > lecture.md` |
| Images (whiteboards, handwriting) | A vision model — Ollama can run `qwen2.5vl` locally | Ask the model to transcribe; save output as `.md` |
| Scanned books (OCR) | Tesseract (`tesseract` CLI; supports Thai + English) | `tesseract page.png page -l tha+eng` |

**One topic per file.** A 200-page handbook is better split into
`handbook_chapter_1_admissions.md`, `handbook_chapter_2_dress_code.md`,
etc. The indexer chunks content automatically, but retrieval works
better when each file is internally coherent.

**Skip media files.** Don't put `.mp3`, `.png`, `.mp4` directly in the
wiki — they're ignored by the indexer. Transcribe or describe them in
markdown instead.

### Pointing the bot at a directory outside the repo

If your school's content lives somewhere else (a SharePoint mount, a
shared drive), you don't have to copy it into `seed_wiki/`. Point the
`WIKI_PATH` env var at the external directory instead, and bind-mount
that path into the orchestrator container. Edit `docker-compose.yml`:

```yaml
orchestrator:
  environment:
    WIKI_PATH: /data/wiki
  volumes:
    - /mnt/school-shared/kru-eng-content:/data/wiki:ro  # was ./seed_wiki
    - wiki_index:/data/wiki_index
```

Then a teacher dropping a new `.md` file into the shared drive is
indexed on the next reindex — no docker compose copy step.

### When to reindex

- **Adding new files** → reindex.
- **Substantively editing existing files** → reindex.
- **Fixing a typo** → don't bother; the chunks already in the index are
  fine for most retrieval.
- **Deleting files** → reindex (orphan chunks otherwise hang around).

## Customizing through Docker — three different ways

There are three places a school's customizations live, and each has its
own update path. Knowing which is which saves a lot of time.

| What you're changing | Where it lives | How it's wired |
|---|---|---|
| School info, persona, students, curriculum, lessons (wiki), grammar references, vocab lists | `seed_wiki/**/*.md` | **Bind-mounted** read-only into the orchestrator container — host edits land instantly inside the container |
| Lesson plans for the PPP engine (`/lesson` UI) | `orchestrator/lessons/*.json` | **Baked into the orchestrator image** at build time |
| The hard-coded `SYSTEM_PROMPT`, lesson grading code, endpoints | `orchestrator/main.py` | **Baked into the orchestrator image** at build time |
| Model choice, generation params, RAG settings, Edge voice names | `.env` | **Read at compose-up time** as environment variables |
| Voice clone reference WAVs | `voices/*.wav` | **Bind-mounted** read-only into the tts container |

### Way 1 — Hot reload (for wiki content)

Use this when you're editing **anything under `seed_wiki/`**: the
persona, the school identity, student profiles, curriculum, lessons
(the markdown ones, not the JSON), grammar, vocab, references.

```bash
# 1. Edit the file on the host (any editor)
notepad++ "C:\Users\Admin\claude\kru-eng-classroom\seed_wiki\school\about_kru_eng.md"

# 2. Restart just the orchestrator (~5 seconds)
docker compose restart orchestrator

# 3. If RAG is enabled and you added/edited substantive content, force a reindex
docker compose down
docker volume rm kru-eng-classroom_wiki_index
docker compose up -d
```

Why this is fast: `./seed_wiki` is bind-mounted into the container at
`/data/wiki`, so your host edit is the container's view. No image
rebuild, no Docker layer caching to fight.

### Way 2 — Rebuild (for code, system prompt, and lesson JSONs)

Use this when you're changing **`orchestrator/main.py`** (system prompt,
endpoints, grading logic) or **`orchestrator/lessons/*.json`** (the PPP
lesson plans). These are baked into the image at build time, so the
running container has a frozen copy — you have to rebuild.

```bash
# 1. Edit the file on the host
notepad++ "C:\Users\Admin\claude\kru-eng-classroom\orchestrator\lessons\past_simple.json"

# 2. Rebuild and restart (~30 seconds — Docker reuses cached layers)
docker compose up -d --build orchestrator
```

For lesson JSONs specifically, the loader picks them up automatically
on orchestrator startup — `_load_lessons()` scans `/app/lessons/*.json`
at import time. Add a file, rebuild, and it appears in
`GET /lesson/list` next time you call it.

### Way 3 — Hot reload for lessons too (optional setup)

If you're iterating fast on lesson JSONs and don't want to rebuild
every time, add a bind mount in your `docker-compose.override.yml`:

```yaml
services:
  orchestrator:
    volumes:
      - ./orchestrator/lessons:/app/lessons:ro
```

Then host edits to `orchestrator/lessons/*.json` show up after
`docker compose restart orchestrator` — no rebuild needed. Useful for
lesson authors; not needed for school admins who only edit lessons
once in a while.

### Way 4 — Live exec (for quick experiments only)

For a five-second tweak before you decide whether to commit, you can
edit inside a running container. Lost on the next restart, so this is
only for "let me try something":

```bash
# Get a shell inside the orchestrator
docker exec -it krueng-orchestrator sh

# Inside the container:
vi /data/wiki/staff/kru_eng_persona.md   # if you have vi installed
# or:
apk add nano 2>/dev/null || apt-get install -y nano   # depending on base image
nano /data/wiki/staff/kru_eng_persona.md
```

Edits to `/data/wiki/...` ARE persisted to the host (because it's
bind-mounted), so this is actually the same as Way 1 with extra steps.
Edits to `/app/...` (orchestrator code or lessons) are container-only
and disappear on restart.

### Recipes

**To add a new lesson** (e.g., "present perfect"):

```bash
cp orchestrator/lessons/past_simple.json orchestrator/lessons/present_perfect.json
# Edit present_perfect.json — change id, title, p1_examples, p2_exercises, p3_scenarios, p3_system_prompt
docker compose up -d --build orchestrator
curl http://localhost:8000/lesson/list   # verify it appears
```

**To modify the teacher's personality** (the bot's voice and style):

```bash
# Edit the persona file
notepad++ seed_wiki/staff/kru_eng_persona.md
# Restart — no rebuild needed
docker compose restart orchestrator
```

Note that the **runtime system prompt is hardcoded** in
`orchestrator/main.py`, separate from the persona doc. The persona doc
shapes the bot's behavior only through RAG retrieval. If you want a
fundamental change to how the bot opens every conversation, edit the
`SYSTEM_PROMPT` constant in `orchestrator/main.py` (Way 2).

**To add information about the school** (handbook, history, mission,
phone numbers, holiday calendar, anything the bot should answer about
your institution):

```bash
# Pick a topic, write a markdown file with frontmatter
notepad++ seed_wiki/school/holiday_calendar_2026.md
# Restart + reindex
docker compose down
docker volume rm kru-eng-classroom_wiki_index
docker compose up -d
```

The `school/` subdirectory is the conventional home for institution-
identity content. For volume (whole handbook chapters, SOP libraries),
make a new top-level directory like `seed_wiki/handbook/` or
`seed_wiki/policies/`.

**To change the model** (e.g., switch from `qwen2.5:3b` to `qwen2.5:7b`
or `llama3.2:3b`):

```bash
# 1. Make sure the model is pulled into Ollama
python scripts/pull_models.py   # uses MODEL from .env

# 2. Edit .env
notepad++ .env   # change MODEL=qwen2.5:7b

# 3. Restart — .env is read fresh on container start
docker compose up -d
```

No rebuild needed because the model name is an env var, not baked into
the image.

**To tune voice settings** (e.g., switch the English Edge TTS voice
from Jenny to Aria):

```bash
# Edit .env
notepad++ .env   # change EDGE_VOICE_EN=en-US-AriaNeural

# Restart the tts service
docker compose up -d tts
```

[List of available Edge TTS voices](https://github.com/rany2/edge-tts#changing-the-default-voice)
— common ones: `en-US-AriaNeural`, `en-US-GuyNeural`, `en-GB-SoniaNeural`,
`th-TH-PremwadeeNeural`, `th-TH-NiwatNeural`.

### Putting it together — a typical school customization session

```bash
# Stop everything cleanly
docker compose down

# Update your school identity
notepad++ seed_wiki/school/about_kru_eng.md

# Add a new student profile
cp seed_wiki/students/learner_profile_template.md seed_wiki/students/somchai.md
notepad++ seed_wiki/students/somchai.md   # fill in name, level, interests

# Add a new lesson based on past_simple
cp orchestrator/lessons/past_simple.json orchestrator/lessons/present_continuous.json
notepad++ orchestrator/lessons/present_continuous.json   # rewrite content

# Adjust the model and turn on RAG
notepad++ .env   # MODEL=qwen2.5:7b, RAG_ENABLED=true

# Bring it back up — single command, rebuilds the orchestrator (for the
# new lesson), restarts everything else, picks up .env, rebuilds the
# index (because we just blew away the volume below)
docker volume rm kru-eng-classroom_wiki_index 2>/dev/null
docker compose up -d --build

# Verify
curl http://localhost:8000/health
curl http://localhost:8000/lesson/list
```

That's the full customization loop.

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
