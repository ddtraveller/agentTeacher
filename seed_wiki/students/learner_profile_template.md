---
title: Learner Profile Template
type: template
status: live
topic: student record schema
updated: 2026-05-11
---

# Learner Profile Template

Copy this file to `students/<nickname>.md` for each real learner. The nickname is the filename stem and the bot's primary identifier — make it short, lowercase, no spaces (e.g. `lek.md`, `noi.md`, `aey.md`).

Set `status: live` after the first real session. Until then, leave it as DRAFT so the bot doesn't surface it to other learners.

---

```markdown
---
title: <Nickname> — Learner Profile
type: learner
status: DRAFT
topic: <nickname>'s profile
updated: YYYY-MM-DD
---

# <Nickname> (<ชื่อเล่นไทย>)

## Basics

- **Real name:** <given name + surname; optional>
- **Preferred name in class:** <nickname>
- **Age:** <number>
- **L1:** Thai (Northern Thai / Standard / both)
- **Other languages:** <e.g., some English from school, a few words of Lisu>
- **Started:** YYYY-MM-DD
- **Schedule:** <e.g., Tuesdays + Fridays, 7pm, 60 min>
- **Format:** <in-person, voice-only via the orchestrator, async chat, mixed>

## Baseline (initial assessment)

- **CEFR estimate at start:** <A0 / A1 / A2 / B1>
- **Receptive (can understand):** <one paragraph; what they get when listening or reading>
- **Productive (can produce):** <one paragraph; what they say or write unprompted>
- **Tech baseline:** <e.g., uses Facebook, Line, TikTok; never opened a terminal; no GitHub account; tried ChatGPT once>
- **AI experience:** <none / casual user / curious about how it works / suspicious of it>

## Goals (in the learner's own words, then in English)

- "<Thai or broken-English statement of why they're here>"
- (translation) "<smooth English rendering for the bot>"

Examples:
- "อยากใช้ ChatGPT เป็น" → *I want to be able to use ChatGPT.*
- "อยากคุยกับฝรั่งที่ตลาด" → *I want to talk to foreigners at the market.*
- "อยากทำงาน remote" → *I want to be able to do remote work.*

## Interests (use these as lesson contexts)

- <e.g., motorbike repair, K-pop, coffee, gaming, family business>
- <pick 3–5; lessons should pull example contexts from this list>

## Pronunciation watchlist

Initial findings (update as you teach):

- [ ] Final consonants (*work*, *like*, *want* dropping the final sound)
- [ ] /v/ vs /w/ (*very* / *wery*)
- [ ] /r/ vs /l/ (*right* / *light*)
- [ ] /θ/ and /ð/ (*think*, *this*)
- [ ] Vowel length (*ship* / *sheep*)
- [ ] Tone-stress mismatch (using Thai tone where English uses stress)
- [ ] Schwa avoidance (*com-pu-ter* instead of *com-pyoo-tə*)

See `pronunciation/thai_l1_interference.md` for the full pattern reference.

## Lexical chunks acquired

Bot maintains this section. Don't edit by hand. Format:

```
- YYYY-MM-DD  open the terminal       (intro w1)         [reuses: 0]
- YYYY-MM-DD  could you say that again (w1 fix)         [reuses: 3]
- YYYY-MM-DD  run the script           (w3)              [reuses: 1]
```

## Current goals (rolling, 2–3 at a time)

What this learner is working on right now. Bot updates after each session.

- 🎯 <e.g., produce past-simple narratives of 3+ sentences>
- 🎯 <e.g., describe what an AI chatbot is in English>
- 🎯 <e.g., write an `about me` HTML page>

## Notes log

Free-form notes, newest first. Bot appends after each session under `## Auto-log`. Teacher / owner appends to `## Manual notes`. Don't interleave.

### Auto-log

YYYY-MM-DD — <one-paragraph session summary>
- new chunks: <list>
- errors noticed: <list>
- planned reuse: <next session>

### Manual notes

YYYY-MM-DD — <human teacher's observations>

## Privacy

This file contains personally identifying information. It stays in the local wiki volume. It is **not** shared with other learners' sessions, not synced to any cloud, and not used as a NotebookLM input (NotebookLM only sees curriculum/, lessons/, and references/).

If the learner leaves the program, set `status: archived`, move to `students/archive/`, and the bot will stop using it.
```
