---
title: NotebookLM Bootstrap Recipe (one-shot install)
type: operational
status: live
topic: how to use NotebookLM once, day zero, to generate derivative learning assets
updated: 2026-05-11
audience: owner
---

# NotebookLM Bootstrap Recipe

This is the day-zero asset-generation pass. You use NotebookLM **once**, on a connected workstation, to convert this wiki into the derivative learning assets the bot can't reasonably synthesize at runtime: audio overviews, study guides, flashcard decks, and slide outlines.

After this pass, you can firewall the host and the bot stack runs entirely offline. NotebookLM is **not** in the docker stack and is not called by any service.

## What you need before starting

- A machine with a browser and internet access. Does **not** need to be the docker host.
- A Google account.
- The repo cloned, including `docker/seed_wiki/`.
- ~2 hours of focused time. Not 2 hours of "while doing other things" — NotebookLM's UI requires repeated short manual clicks.
- The two helper scripts at the repo root: `notebooklm_login.py` and `notebooklm_autologin.py`.

## Step 0 — Decide what gets uploaded

NotebookLM should see **curriculum**, **lessons**, and **references** — the pedagogy and content. It should **not** see student profiles or transcripts.

Set this in your head before clicking anything:

| Folder | Upload? | Why |
|---|---|---|
| `seed_wiki/INDEX.md` | ✅ | Helps NotebookLM scope topics |
| `seed_wiki/school/` | ✅ | Identity context |
| `seed_wiki/staff/` | ⚠️ optional | Helps tone of audio; not required |
| `seed_wiki/students/` | ❌ | PII — never upload |
| `seed_wiki/curriculum/` | ✅ | Scope |
| `seed_wiki/lessons/` | ✅ | Primary content |
| `seed_wiki/vocabulary/` | ✅ | Source of flashcards |
| `seed_wiki/pronunciation/` | ✅ | Source of audio drills |
| `seed_wiki/grammar/` | ✅ if present | Source |
| `seed_wiki/assessment/` | ⚠️ optional | Useful for owner-facing decks; not for student-facing |
| `seed_wiki/references/teaching_methods.md` | ❌ | Internal — not for learners |
| `seed_wiki/references/notebooklm_bootstrap.md` | ❌ | This file is for you, not for NotebookLM |

## Step 1 — Authenticate

```
pip install playwright
python -m playwright install chromium
python notebooklm_login.py
```

This opens a Chromium window. Sign in with your Google account. When you see the NotebookLM home page, the script saves auth to `~/.notebooklm/storage_state.json` and exits. Don't close the browser before it's saved.

If `python -m notebooklm login` works for you directly, use that instead — `notebooklm_login.py` is the fallback for Windows machines where the official command fails to open a visible browser.

## Step 2 — Create one notebook per asset family

NotebookLM works best when each notebook has a focused source set. Don't put everything in one notebook. Plan:

| Notebook | Sources to upload | Output type |
|---|---|---|
| **Kru Eng — Curriculum overview** | INDEX.md, syllabus_12week.md, about_kru_eng.md | 1 audio overview (~10 min), 1 study guide |
| **Kru Eng — Lessons W1–W4** | LESSON_TEMPLATE.md + w01–w04 lessons | 1 audio overview per week, 1 flashcard deck per week, 1 study guide per week |
| **Kru Eng — Lessons W5–W8** | w05–w08 lessons | same as above |
| **Kru Eng — Lessons W9–W12** | w09–w12 lessons | same as above |
| **Kru Eng — Pronunciation** | thai_l1_interference.md | 1 audio drill set (~10 min), 1 study guide |
| **Kru Eng — Vocabulary** | tech_lexical_chunks.md | 1 flashcard deck per group (A–G) |

Twelve notebooks is a lot of clicking. That's why this is a one-shot pass. After it's done, the assets live in the wiki and the bot serves them; you don't redo this every week.

## Step 3 — For each notebook, generate the assets

In each notebook:

1. **Upload the sources.** Drag-and-drop the markdown files. NotebookLM accepts text, markdown, PDF, audio, and YouTube URLs. Markdown works fine.

2. **Generate an Audio Overview.**
   - Click "Audio Overview" in the right panel.
   - Set the focus: "An English teacher and her colleague discuss this lesson. They explain it in simple English at CEFR A2–B1 level. Keep it under 8 minutes."
   - Generate. Wait ~5 minutes.
   - When ready, click the download arrow. Save the MP3 as `wiki/audio/<notebook-slug>.mp3`.

3. **Generate a Study Guide.**
   - Click "Study Guide" in the Notes/Outputs panel.
   - When ready, click the three-dot menu → "Convert to markdown" or copy the text.
   - Save as `wiki/derived/<notebook-slug>_studyguide.md`.

4. **Generate FAQ / Briefing.** Same flow. Save as `<notebook-slug>_faq.md` and `<notebook-slug>_briefing.md`.

5. **Generate flashcards via chat.** NotebookLM doesn't have a flashcard button. Use the chat:
   > Generate 20 flashcards covering the key chunks from these sources. Format as JSON: a list of objects with `front`, `back`, and `chunk_type` keys. Front in English, back in Thai. No prose around the JSON.

   Copy the JSON. Save as `wiki/derived/<notebook-slug>_flashcards.json`.

6. **Generate a slide outline.** NotebookLM doesn't export slides either. Use the chat:
   > Outline a 15-slide deck covering these sources, for a CEFR A2–B1 learner. Each slide should have a title and 3 bullet points. Return as JSON.

   Copy. Save as `wiki/derived/<notebook-slug>_slides.json`. Later, `hermes-night` can run pandoc or python-pptx to produce an actual .pptx from this JSON.

## Step 4 — Where the outputs go

After step 3, your local `wiki/` directory should look like:

```
wiki/
├── INDEX.md
├── audio/
│   ├── curriculum-overview.mp3
│   ├── lesson-w01.mp3
│   ├── lesson-w02.mp3
│   ...
│   └── pronunciation-drill.mp3
├── derived/
│   ├── curriculum-overview_studyguide.md
│   ├── curriculum-overview_faq.md
│   ├── lesson-w01_studyguide.md
│   ├── lesson-w01_flashcards.json
│   ├── lesson-w01_slides.json
│   ...
└── (the original seed_wiki/ tree unchanged)
```

Copy this entire tree into the docker `wiki` named volume:

```bash
docker compose -f docker/docker-compose.yml cp \
  ./wiki/. orchestrator:/data/wiki/
```

Or, if you prefer a host bind-mount, set it up in `docker/docker-compose.override.yml` and the changes are reflected live.

## Step 5 — Trigger a Khoj reindex

The wiki is now richer than what Khoj indexed at first boot. Trigger a reindex:

```bash
curl -X POST http://localhost:42110/api/index/update -d '{"force": true}'
```

Or, via the LINE/Slack bridge: DM the bot `reindex_khoj`.

After reindex, the bot can cite the new content. Test by asking a Khoj-grounded question:

> What does the curriculum say about how we teach AI ethics?

The expected response should reference `lessons/w12_ai_ethics_and_bias.md` and possibly the audio overview's content.

## Step 6 — Cut the cord (optional but recommended)

If your deployment posture is offline-first, this is where you firewall the docker host's outbound. The remaining outbound the stack needs:

- **Ollama model pulls** (for new models): block outside of maintenance windows.
- **LINE / Slack** webhook responses (via Cloudflare Tunnel): keep open.
- **Everything else**: block.

NotebookLM is never called again from the host. If you need to regenerate assets — say, after writing five new lessons in `lessons/w13_*` to `lessons/w17_*` — you do it on the same workstation that did the day-zero pass, then `docker cp` the new outputs into the volume.

## Step 7 — Document what you generated

Append to `INDEX.md` under a new section:

```markdown
## Generated assets (NotebookLM, YYYY-MM-DD)

- audio/curriculum-overview.mp3 — 9 min, generated YYYY-MM-DD
- audio/lesson-w01.mp3 through audio/lesson-w12.mp3 — ~8 min each
- derived/*_studyguide.md, *_faq.md, *_flashcards.json, *_slides.json
- audio/pronunciation-drill.mp3 — 11 min
```

This way the bot can locate the assets without you having to type the paths into prompts.

## Cost and time estimate

- **Time on Bigthe workstation**: 90–120 minutes for the full 12-notebook pass.
- **NotebookLM cost**: free tier as of 2026-05; check current limits. Audio overviews count against monthly generation quota.
- **Storage**: ~120 MB of audio + ~5 MB of markdown + ~1 MB of JSON.

## Things that go wrong

- **Audio overview is too long.** Re-generate with a tighter prompt: "Keep it under 6 minutes." NotebookLM mostly obeys.
- **Audio overview drifts into US-centric examples.** Re-generate with "Northern Thai context, examples from Chiang Mai." It improves but isn't perfect.
- **Flashcard JSON has invalid escaping.** NotebookLM sometimes uses smart quotes. Pipe through a quick fixup: `python -c 'import json,sys; json.dump(json.load(sys.stdin), sys.stdout)' < raw.json > clean.json` to catch errors.
- **Storage state expires.** Re-run `python notebooklm_login.py`.

## What this recipe does NOT do

- It doesn't generate the lessons themselves. Those are written in the wiki — the lessons are the source, NotebookLM produces derivative assets *from* them.
- It doesn't sync to S3. If you want the audio served from `s3://krueng.ai/audio/`, that's a separate step. (CLAUDE.md describes the S3 path conventions.)
- It doesn't update the syllabus when you add new lessons. That's `hermes-night`'s job.
- It doesn't fact-check. NotebookLM's outputs need a human pass before they're considered live. Diff each `*_studyguide.md` against the source lesson on the first pass; after you trust the process, spot-check.

## References

- `notebooklm_login.py` — Playwright-based login helper (repo root).
- `notebooklm_autologin.py` — headless re-use of saved auth (repo root).
- `INDEX.md` — wiki schema. Update after generation.
- *[ref:NotebookLM docs]* — https://notebooklm.google.com (current as of 2026-05).
