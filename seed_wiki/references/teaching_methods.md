---
title: Teaching Methods Reference
type: reference
status: live
topic: modern TEFL methodology, CALL, AI-mediated language learning
updated: 2026-05-11
---

# Teaching Methods Reference

This page is Kru Eng's pedagogical operating manual. The bot reads it when the owner or a trainee teacher asks methodological questions ("why don't we just do PPP?", "what is TBLT?", "how do I scaffold this?"). It's deliberately concise — depth comes from the cited sources.

## The blend

Kru Eng does not follow a single named method. The pedagogy is a blend of:

- **Task-Based Language Teaching (TBLT)** — for the lesson shape *[ref:Ellis 2003, Long 2015, Willis & Willis 2007]*
- **Lexical Approach** — for what to teach as the core unit *[ref:Lewis 1993, Wray 2002]*
- **Sociocultural / Scaffolding** — for the gradient of support *[ref:Vygotsky 1978, Walqui 2006]*
- **Communicative Language Teaching** — for the broader orientation toward meaning *[ref:Hymes 1972, Savignon 1991]*
- **Comprehensible Input + Output** — for the input and the output ratios *[ref:Krashen 1985, Swain 1985]*
- **Cognitive Science of Learning** — for spacing, interleaving, retrieval *[ref:Cepeda 2008, Roediger & Karpicke 2006]*
- **Translanguaging** — for the Thai/English balance *[ref:García & Wei 2014, Cenoz & Gorter 2021]*
- **Computer-Assisted Language Learning (CALL) and AI-mediated language learning** — for the role of the bot itself *[ref:Chapelle 2001, Kohnke et al. 2023]*

The rest of this page describes what each contributes and how they fit together.

## Why not just PPP?

**PPP** (Presentation → Practice → Production) is the workhorse of British TEFL training and Thai DSS-OTP rubrics. It is not *wrong*; it is *partial*. Its limits:

1. **Linear synthetic syllabus.** PPP assumes the curriculum is a sequence of discrete language items to be presented one at a time. Real language doesn't divide that cleanly, and learners often acquire later items before earlier ones (the natural order hypothesis). *[ref:Krashen 1985]*
2. **Form before meaning.** PPP front-loads the form, which can make the learner attend to *correctness* before *communication*. Modern SLA research suggests meaning-first sequences produce more durable acquisition. *[ref:Ellis 2003]*
3. **Production as the final step.** Restricting "real" production to the last 10 minutes of a lesson wastes the bulk of the contact time on rehearsal that may not transfer.
4. **Underweights interaction.** PPP imagines a one-way flow (teacher → learner). Real language acquisition is interactional. *[ref:Long 1996 — interaction hypothesis]*

Kru Eng keeps PPP's strengths — explicit modeling, focused practice with feedback — but **embeds them inside a task cycle**. The lesson template's order is:

> Pre-task → Input → Noticing → Controlled practice → Task → Post-task language focus → Wrap

This is closer to **ESA cyclical** (Engage → Study → Activate, Harmer) or **TBLT** (Pre-task → Task → Language focus, Willis) than to pure PPP. *[ref:Harmer 2007, Willis & Willis 2007]*

## How TBLT works here

A **task** is a goal-oriented activity with a real-world outcome and meaningful language use. The classic test: *would anyone outside the classroom care about the result?*

In Kru Eng's syllabus, the tasks are:

- W1: record a self-introduction.
- W6: write an `about_me.html` page.
- W8: build a capability comparison of three AI tools.
- W10: iterate on a real prompt and compare outputs.
- W12: pitch a project idea with reasoning.

Each task drives the language teaching. We don't choose grammar items off a list and then invent contexts for them; we choose tasks and let the grammar emerge.

## How the Lexical Approach works here

Words mostly don't travel alone. They travel in chunks: *make a commit*, *open a tab*, *ask the model*, *if you …, the AI will …*. The lexical approach treats these as the **primary unit** of learning, with grammar emerging as the regularities across chunks rather than as a pre-existing system the chunks fill out.

In Kru Eng's wiki, this lives in `vocabulary/tech_lexical_chunks.md`. Every lesson's chunk bank is a chunk list, not a word list. The bot is configured to **recognize chunks the learner is reaching for**, complete them when the learner stalls, and **catch chunk-level errors** (*do a commit* → *make a commit*) ahead of single-word errors.

## How scaffolding works here

Vygotsky's **zone of proximal development (ZPD)** is the bandwidth between what a learner can do alone and what they can do with support. Effective teaching targets this bandwidth and gradually removes the support.

Kru Eng implements this as a **modeled → guided → independent** gradient inside every lesson:

- **Modeled** (Input phase): the bot does the thing while the learner watches.
- **Guided** (Controlled practice + early task): the learner does it with explicit prompts and recasts.
- **Independent** (Late task + post-task): the learner does it without scaffolds.

The night-time hermes-night job updates each learner's ZPD profile based on what they did with and without support in the last session. *[ref:Walqui 2006]*

## How comprehensible input + output works here

**Krashen's i+1** — input slightly above current level, with meaning recoverable from context — produces acquisition (not just learning). **Swain's output hypothesis** — that pushing learners to produce slightly harder language with feedback consolidates acquisition — adds the missing half.

In Kru Eng's lessons, the **Input** phase delivers i+1: a short text or dialogue at a level the learner can mostly follow, with one or two structures that are new. The **Task** phase pushes output: it demands language the learner can almost but not quite produce alone.

The ratio matters. Krashen estimated input should dominate; modern SLA suggests the ratio is more even at higher levels and skewed input-heavy at lower levels. Kru Eng's lessons run roughly **40% input, 60% output** at A2; **30% input, 70% output** at B1.

## How spaced retrieval works here

Vocabulary and chunks decay if not retrieved. The cognitive-science consensus: retrieval **spaced** across days produces durable learning; massed retrieval (cramming) produces fast but fragile gains.

Kru Eng implements this in two layers:

1. **Within the syllabus** (`curriculum/syllabus_12week.md`): each week's task explicitly reuses chunks from earlier weeks (week 10's homework brings back week 8's *can/can't*).
2. **Within the learner profile** (`students/<nickname>.md`): the bot tracks every chunk used and reintroduces it on a schedule (day 1, 2, 7, 21, 60).

This is automated. The owner doesn't have to do it by hand. *[ref:Cepeda 2008, Karpicke & Roediger 2008]*

## How translanguaging works here

Older orthodoxy: speak only the target language in class. Newer evidence and pedagogy: strategic use of the L1 (Thai) **accelerates** acquisition by giving the learner a foothold for abstract concepts and reducing cognitive load on meaning.

Kru Eng's policy is in `staff/kru_eng_persona.md` ("Language policy — when to use Thai"). Summary:

- **Default to English** for production.
- **Use Thai for meta-concepts** that would take 5 minutes in English and 5 seconds in Thai.
- **Use Thai for cultural terms** (เมตตา, กรรม) — don't translate culture.
- **Don't use Thai for translation of English content** — that disincentivizes attending to the English.

This is closer to **translanguaging** *[ref:García & Wei 2014]* than to traditional code-switching: the two languages are not separate "tools" but parts of one bilingual repertoire.

## How AI-mediated language learning works here

This is the newest area, and the field is still figuring it out. *[ref:Kohnke et al. 2023, Godwin-Jones 2024]* What seems to be working:

- **AI as conversational partner** for low-anxiety speaking practice (the learner can pause, retry, and not feel judged).
- **AI as feedback engine** for written production (instant, specific feedback that a human teacher couldn't provide at scale).
- **AI as content generator** for personalized examples and practice (an example about the learner's hobby, on demand).
- **AI as object of study** for critical AI literacy (week 8, 11, 12 in our syllabus).

What's risky:

- **Over-reliance.** A learner who outsources every English task to AI doesn't acquire English.
- **Untargeted feedback.** AI can correct everything, including features the learner isn't ready to attend to. Hence Kru Eng's "one error per turn" rule.
- **Confabulation.** Where the AI is the *source* of factual content (cultural facts, grammar rules), it can be wrong. Hence Khoj grounding.

## Assessment philosophy

See `assessment/formative_techniques.md` for the techniques. The philosophy:

- **Formative > summative.** Daily low-stakes checks tell us what to teach next. Big tests tell us what was taught, after it's too late to change it.
- **Can-do statements > scores.** The CEFR can-do framework is the assessment scale, not points out of 100. *[ref:CEFR Companion Volume 2020]*
- **Learner self-assessment matters.** Every lesson ends with the learner saying what they can now do and what's still hard. That data drives the next lesson.

## DSS-OTP compatibility

For trainee teachers preparing Observed Teaching Practice in the Thai DSS rubric format, every lesson file in this wiki includes a `## DSS-OTP mapping` appendix at the end. It maps lesson sections to DSS observable items. The pedagogical content is unchanged; only the labeling is adapted.

If the trainee's specific DSS rubric differs from the default, edit the appendix; the lesson body is independent of it.

## What this page is not

- Not a methods textbook. Read the references. *Doing Task-Based Teaching* (Willis & Willis), *The Lexical Approach* (Lewis), and *Task-based Language Learning and Teaching* (Ellis) are the three I'd start with.
- Not a research review. The citations are pointers, not summaries.
- Not the last word. Methods evolve. When the field's view shifts, update this file and update the lessons it informs.

## References (short)

- *Ellis, R.* (2003). *Task-based Language Learning and Teaching.* OUP.
- *Harmer, J.* (2007). *The Practice of English Language Teaching.* Pearson.
- *Krashen, S.* (1985). *The Input Hypothesis.* Longman.
- *Lewis, M.* (1993). *The Lexical Approach.* LTP.
- *Long, M.* (1996). The role of the linguistic environment in second language acquisition. *Handbook of Second Language Acquisition.*
- *Swain, M.* (1985). Communicative competence: some roles of comprehensible input and comprehensible output. *Input in Second Language Acquisition.*
- *Vygotsky, L.* (1978). *Mind in Society.* Harvard UP.
- *Willis, D. & Willis, J.* (2007). *Doing Task-Based Teaching.* OUP.
- *Walqui, A.* (2006). Scaffolding instruction for English language learners. *International Journal of Bilingual Education and Bilingualism.*
- *García, O. & Wei, L.* (2014). *Translanguaging.* Palgrave.
- *Cepeda, N.J. et al.* (2008). Spacing effects in learning. *Psychological Science.*
- *Karpicke, J. & Roediger, H.* (2008). The critical importance of retrieval for learning. *Science.*
- *Council of Europe.* (2020). *CEFR Companion Volume.*
- *Kohnke, L., Moorhouse, B.L., & Zou, D.* (2023). ChatGPT for language teaching and learning. *RELC Journal.*
- *Godwin-Jones, R.* (2024). Distributed agency in second language learning and teaching through generative AI. *Language Learning & Technology.*
