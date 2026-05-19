---
title: 12-Week Syllabus — English + Tech + AI
type: syllabus
status: live
topic: course scope and weekly progression
updated: 2026-05-11
cefr_start: A1
cefr_end: B1
---

# 12-Week Syllabus

A1 → B1 over twelve weeks, with English, technology, and AI literacy woven into every week. Each row is one week, ~3 hours of contact time (one 60-minute live session plus async self-study with Kru Eng).

Each weekly lesson lives at `lessons/wNN_<slug>.md` and follows `lessons/LESSON_TEMPLATE.md`.

## Design principles

- **Spiraling, not linear.** Grammar items come back two and three times across the twelve weeks, each time in a slightly different communicative frame. By week 12, *can/can't* (introduced week 2) is being used for hedging AI output evaluations.
- **The task drives the form.** Every week's grammar is whatever the week's task needs. We do not pick *present perfect* because it's the fifth thing in the textbook; we pick it because the week's task is "describe what you've learned with Kru Eng so far."
- **Tech is on-ramped, not assumed.** Week 1 opens a terminal. Week 6 writes HTML. Week 10 writes prompts. No prior tech is required.
- **AI is the through-line.** From week 8, the learner is talking to AI directly. From week 10, they are writing the prompts. From week 12, they are evaluating its outputs.

## Week-by-week

### Week 1 — Greetings and the Terminal
- **Can-do:** *I can greet someone, introduce myself, and run a simple command on a computer.*
- **English focus:** verb *to be* (am/is/are), simple intros, basic question forms.
- **Tech focus:** opening a terminal, `pwd`, `ls`, `cd`, `echo`.
- **AI thread:** what is a "command"? Computers and AIs both follow instructions, but differently.
- **Task:** record a one-minute self-introduction video; run three terminal commands while recording.

### Week 2 — Daily Life and Files
- **Can-do:** *I can describe my daily routine and create / move / delete a file.*
- **English focus:** present simple, 3rd person -s, time expressions (*every morning*, *at 7*).
- **Tech focus:** `mkdir`, `touch`, `mv`, `rm`, understanding paths.
- **AI thread:** files are how computers remember. We'll come back to memory vs no-memory in week 8.
- **Task:** make a folder structure for the course on your own device; describe your morning routine in a daily-log file you write yourself.

### Week 3 — Describing People and Things, Editing Text
- **Can-do:** *I can describe a person or a thing, and edit a text file.*
- **English focus:** adjectives, *have got* / *have*, word order in description.
- **Tech focus:** text editors (nano, VS Code), copy-paste vs typing, save vs save-as.
- **AI thread:** AIs "have" weights but not bodies; they "have" training but not memory.
- **Task:** write a 5-sentence description of your village or neighborhood; save as a `.md` file; share screen and walk through it.

### Week 4 — Asking and Answering, The Internet
- **Can-do:** *I can ask and answer Wh-questions, and explain what the internet is at a basic level.*
- **English focus:** Wh-questions (what / where / when / who / why / how), short answers.
- **Tech focus:** what is a URL, what is a server, what is a browser. DNS in one sentence.
- **AI thread:** the AI you'll talk to lives on a computer somewhere. Mine lives on this one.
- **Task:** interview a classmate (or Kru Eng) with 8 Wh-questions; present three facts from the interview.

### Week 5 — Past Events, Git Basics
- **Can-do:** *I can talk about what I did yesterday, and I can commit my work to git.*
- **English focus:** past simple — regular and high-frequency irregular (*went, had, did, made, saw*).
- **Tech focus:** `git init`, `git add`, `git commit -m`, `git log`. No remote yet.
- **AI thread:** AI doesn't *remember* between conversations the way git remembers between commits. Why?
- **Task:** make 5 commits to a personal markdown journal over the week, each describing one event from your day.

### Week 6 — Describing Spaces, HTML Structure
- **Can-do:** *I can describe a place using prepositions, and I can write a basic HTML page.*
- **English focus:** prepositions of place, *there is / there are*, locative phrases.
- **Tech focus:** HTML — `<html>`, `<head>`, `<body>`, `<h1>`, `<p>`. What "markup" means.
- **AI thread:** HTML tells the browser *what things are*. Prompts tell the AI *what to do*. Both are instructions for non-humans.
- **Task:** write an `about_me.html` page with a heading, three paragraphs, and a list. Open it in a browser.

### Week 7 — Habits, Preferences, Style with CSS
- **Can-do:** *I can talk about what I like and don't like, and style a page.*
- **English focus:** *like / love / hate* + -ing or noun, frequency adverbs (*usually*, *sometimes*).
- **Tech focus:** CSS basics — color, font-size, padding. Selectors as a way of saying *which things*.
- **AI thread:** "selectors" in CSS, "filters" in your prompts. We're learning to be precise.
- **Task:** style your `about_me.html` with three colors and two fonts; explain (in English) why you chose them.

### Week 8 — What Is AI? Modals of Ability
- **Can-do:** *I can use 'can' and 'can't' to describe what AI can and can't do.*
- **English focus:** modal *can / can't* / *be able to* — for ability and for permission.
- **Tech focus:** trying ChatGPT, Claude, and the local Ollama side by side in the browser. Noticing differences.
- **AI thread:** **the lesson is the AI.** What is a language model? Why does it sometimes get things wrong? Why does it sound confident even when wrong?
- **Task:** make a table comparing three AI tools — one row per capability (*translate Thai → English*, *write code*, *do math*, *remember last week*). Use *can* / *can't* throughout.

### Week 9 — Future and Plans, Python Hello-World
- **Can-do:** *I can talk about my plans for next week, and run a Python script.*
- **English focus:** *going to* (plans) vs *will* (predictions/decisions).
- **Tech focus:** install Python, run `python -c "print('hello')"`, then run a one-file script.
- **AI thread:** AI predicts the *next word*. You're making *future plans*. Compare.
- **Task:** write a 5-line Python script that prints your weekly plan; commit and push to GitHub.

### Week 10 — Imperatives, Prompt Engineering Basics
- **Can-do:** *I can give clear instructions in English, and write effective prompts for an AI.*
- **English focus:** imperatives, conditional *if* (zero and first conditional), sequencing (*first, then, finally*).
- **Tech focus:** prompt patterns — role, context, format, examples (few-shot), constraints.
- **AI thread:** **the lesson is the prompt.** Bad prompts → bad outputs. Why? What changes when you add an example?
- **Task:** write three versions of a prompt to summarize a 200-word Thai news article into 50 English words. Compare outputs.

### Week 11 — Comparison, Evaluating AI Output
- **Can-do:** *I can compare two things in English, and judge AI output for accuracy and bias.*
- **English focus:** comparatives and superlatives, *more / less*, hedging verbs (*seems*, *might*, *probably*).
- **Tech focus:** ground truth vs generated text. Spot-checking. Asking an AI to cite sources, then verifying the citations.
- **AI thread:** what is a hallucination? Why do they happen? When are they cheap to spot, and when are they expensive?
- **Task:** ask an AI 10 factual questions about Thailand; verify each answer against the wiki or a known source; report findings.

### Week 12 — AI Ethics, Opinion Language, Capstone Pitch
- **Can-do:** *I can give an opinion on an AI ethics question, with reasons, in 90 seconds of clear English.*
- **English focus:** opinion structures (*in my opinion*, *I think that*, *the thing is*), discourse markers, polite disagreement.
- **Tech focus:** privacy, consent, environmental cost, jobs. Concrete cases.
- **AI thread:** Kru Eng critiques her own design choices with the learner. What does the bot keep? Who owns the data? Who pays the electricity?
- **Task:** present a 90-second pitch: "One thing I want to build with AI, and one rule I want it to follow."

## After week 12

The course is designed as A1→B1. Learners who hit B1 are ready for either:

- **Track A — Build:** a project-based intermediate course where they build a small AI-assisted tool of their own. Kru Eng's role shifts from teacher to pair programmer.
- **Track B — Communicate:** a CEFR B2-oriented course focused on extended discourse, presentations, and academic/professional writing. Less tech, more language.

Both tracks reuse this same wiki infrastructure. The owner adds new lessons in `lessons/` with the appropriate frontmatter and lets `hermes-night` re-link the syllabus.

## How to deviate from this syllabus

This syllabus is a strong default, not a prescription. For a specific cohort, the owner can:

- Reorder weeks (some classes need git earlier; some need AI later).
- Drop a week and substitute (e.g., replace week 6 HTML with week 6 LINE bot scripting for older learners).
- Add a "week 0" pure-tech onboarding if learners arrive with zero device fluency.

The bot reads this file to scope retrieval; if you reorder, update the week numbers in the frontmatter of each lesson file too.

## References

- *[ref:Ellis 2003]* Ellis, R. (2003). *Task-based Language Learning and Teaching.* OUP.
- *[ref:Willis & Willis 2007]* Willis, D. & Willis, J. (2007). *Doing Task-Based Teaching.* OUP.
- *[ref:CEFR 2020]* Council of Europe. *Common European Framework of Reference for Languages: Companion Volume.*
