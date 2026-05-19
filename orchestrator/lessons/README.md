# Scaffolded PPP Lessons

Lessons live here as JSON. Each is a Presentation → Controlled Practice →
Freer Production scaffold for the Kru Eng local bot.

## Available lessons

| File | Target | CEFR |
|---|---|---|
| `past_continuous.json` | was/were + V-ing for interrupted past actions | A2 |

## How a lesson is structured

```
p1_examples       — Presentation. 5 image+sentence cards with continuous/simple highlights.
p2_exercises      — Controlled practice. ~12 fill-blanks with deterministic answer keys.
p3_scenarios      — Freer production. Conversation openers + locked system prompt.
config            — p2_window_size, p2_pass_threshold, p2_min_attempts, p3_target_turns
```

## Why P2 is graded by string match, not by the LLM

`qwen2.5:3b` will rubber-stamp wrong learner answers as fine. The 70%
production-unlock gate only means something if grading is deterministic.
The server normalizes (lowercase, whitespace-collapse, contraction-expand)
and compares against each blank's `accept` list. No LLM in the loop.

## Adding a lesson

1. Drop a new `<id>.json` in this directory matching the shape of
   `past_continuous.json`. Required keys:
   - `id`, `title`, `title_th`, `cefr`
   - `p1_intro`, `p1_examples[]` (each with `sentence`, `th`, `highlight_continuous`, `highlight_simple`, `image`)
   - `p2_exercises[]` (each with `prompt` containing `_____` blanks and `blanks[].accept[]`)
   - `p3_scenarios[]`, `p3_system_prompt`, `config`
2. Restart the orchestrator. Lessons load at startup.
3. Generate images (see below) and drop them in
   `../static/lesson_images/<lesson_id>/`.

## Generating images

The prompts file `<lesson_id>_image_prompts.json` is the input for the
existing Replicate FLUX Dev pipeline at `python/img_gen/generate_images.py`.
From the repo root:

```bash
python python/img_gen/generate_images.py \
  docker/orchestrator/lessons/past_continuous_image_prompts.json
```

Output lands in `docker/orchestrator/static/lesson_images/past_continuous/`
because that path is set in the JSON's `output_dir` field. The UI degrades
gracefully if images are missing — it shows the filename in the alt slot.

Cost: ~$0.03 per image × 5 = ~$0.15 for the Past Continuous lesson.

## Running the lesson

After rebuilding the orchestrator image (`docker compose up -d --build orchestrator`):

- **Lesson UI**: http://localhost:8000/lesson
- **API**:
  - `GET  /lesson/list` → available lessons
  - `POST /lesson/start` `{lesson_id}` → opens a session
  - `POST /lesson/turn`  `{session_id, action, payload}` → advances state

The lesson UI is separate from the main `/` chat. Sessions are in-memory
only — restarting the container drops them. That's fine for the local-only
deployment; add SQLite if you want resume-across-restart.
