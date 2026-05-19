---
title: Kru Eng Wiki — Index
type: index
audience: [khoj, hermes-night, owner-bridge, humans]
updated: 2026-05-11
---

# Kru Eng Wiki Index

This is the schema map of Kru Eng's knowledge base. Khoj reads it to decide which pages are relevant. `hermes-night` reads it to know what's prune-eligible. Humans read it to find anything fast.

Every page in this wiki has YAML frontmatter with `type`, `status` (`live` | `DRAFT`), `topic`, and `updated`. Khoj indexes the body; the agents key off the frontmatter.

## Schema rules

1. **One topic per file.** If a page covers two unrelated topics, split it.
2. **Filenames are slugs.** `lower_snake_case.md`. No spaces.
3. **Frontmatter is required.** Pages without it are treated as DRAFT.
4. **Status: live | DRAFT.** Owner promotes DRAFT → live via the LINE/Slack bridge.
5. **Cite sources inline** as `[ref:short_name]` and resolve the link in `references/sources.md`.
6. **Bilingual is the default,** but English is the operating language inside the wiki. Thai appears next to English (in parentheses or a `tt:` field) so the bot can produce code-switched output without translating on the fly.

## Directory map

```
seed_wiki/
├── INDEX.md                         — this file
├── README.md                        — how to use the wiki (humans)
├── school/
│   └── about_kru_eng.md             — identity, mission, methodology
├── staff/
│   └── kru_eng_persona.md           — the bot's voice and operating rules
├── students/
│   └── learner_profile_template.md  — copy-and-fill per real learner
├── curriculum/
│   └── syllabus_12week.md           — week-by-week scope
├── lessons/
│   ├── LESSON_TEMPLATE.md           — canonical lesson shape (modern PPP+Task)
│   ├── w01_greetings_and_the_terminal.md
│   ├── w02_daily_life_and_files.md
│   ├── w03_describing_and_editing.md
│   ├── w04_wh_questions_and_the_internet.md
│   ├── w05_past_events_and_git.md
│   ├── w06_describing_spaces_html.md
│   ├── w07_likes_and_css.md
│   ├── w08_what_is_ai_and_what_can_it_do.md
│   ├── w09_future_plans_and_python.md
│   ├── w10_prompt_engineering_basics.md
│   ├── w11_comparing_and_evaluating_ai.md
│   └── w12_ai_ethics_and_bias.md
├── vocabulary/
│   └── tech_lexical_chunks.md       — verbs+nouns that travel together
├── pronunciation/
│   └── thai_l1_interference.md      — predictable Thai-speaker errors
├── grammar/
│   └── grammar_through_chunks.md    — form-meaning-use treatment
├── assessment/
│   └── formative_techniques.md      — low-stakes checks for understanding
└── references/
    ├── teaching_methods.md          — TBLT, ESA, lexical, CALL, AI-mediated
    ├── sources.md                   — full bibliography for [ref:...] citations
    └── notebooklm_bootstrap.md      — day-zero asset generation recipe
```

## Page registry

| Path | Topic | Status |
|---|---|---|
| school/about_kru_eng.md | Identity and mission of Kru Eng | live |
| staff/kru_eng_persona.md | Bot voice, tone, code-switching rules | live |
| students/learner_profile_template.md | Template for a single learner record | live |
| curriculum/syllabus_12week.md | Twelve-week scope, A1→B1, English+Tech+AI | live |
| lessons/LESSON_TEMPLATE.md | Lesson scaffold every weekly page follows | live |
| lessons/w01_greetings_and_the_terminal.md | Greetings + first terminal session | live |
| lessons/w02_daily_life_and_files.md | Present simple + filesystem operations | live |
| lessons/w03_describing_and_editing.md | Adjectives + have got + text editor | live |
| lessons/w04_wh_questions_and_the_internet.md | Wh-questions + URL/server/browser | live |
| lessons/w05_past_events_and_git.md | Simple past + git basics | live |
| lessons/w06_describing_spaces_html.md | Prepositions + there is/are + HTML | live |
| lessons/w07_likes_and_css.md | like/love + frequency adverbs + CSS | live |
| lessons/w08_what_is_ai_and_what_can_it_do.md | AI literacy + can/can't modal | live |
| lessons/w09_future_plans_and_python.md | going to vs will + first Python script | live |
| lessons/w10_prompt_engineering_basics.md | Writing effective prompts + imperatives | live |
| lessons/w11_comparing_and_evaluating_ai.md | Comparatives + hedging + AI evaluation | live |
| lessons/w12_ai_ethics_and_bias.md | AI ethics + opinion/hedging language | live |
| vocabulary/tech_lexical_chunks.md | Multi-word tech phrases for A2–B1 | live |
| pronunciation/thai_l1_interference.md | Thai-speaker error patterns | live |
| grammar/grammar_through_chunks.md | Grammar treated via formulaic chunks | live |
| assessment/formative_techniques.md | Daily formative-assessment recipes | live |
| references/teaching_methods.md | Modern TEFL methodology reference | live |
| references/sources.md | Bibliography — full citations for every [ref:...] key | live |
| references/notebooklm_bootstrap.md | NotebookLM one-shot install recipe | live |

## What the agents do with this

- **Khoj** reads every `status: live` file as a retrieval source.
- **owner-bridge** uses `lessons/` and `curriculum/` to answer "what should week N cover" type questions, and writes DRAFT pages.
- **hermes-night** uses INDEX.md to find prune candidates (no frontmatter, stale `updated:`, broken `[ref:...]`).
- **NotebookLM** (one-shot) consumes `curriculum/` + selected `lessons/` to generate audio overviews and flashcards.

Anything not listed here is unindexed. Add it here when you add it to the wiki.
