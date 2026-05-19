---
title: Week 10 — Prompt Engineering Basics
type: lesson
status: live
topic: writing effective prompts + imperatives + first conditional
updated: 2026-05-11
week: 10
cefr: A2-B1
duration_min: 60
can_do: I can write a clear prompt for an AI, with a role, a context, a format, and an example.
english_focus: imperatives, first conditional, sequencing markers (first/then/finally)
tech_focus: prompt patterns; iterating on a prompt; few-shot prompting
ai_thread: prompts are instructions written for a non-human reader — clarity and example-driven
---

# Week 10 — Prompt Engineering Basics

## Can-do

> I can write a clear prompt for an AI tool, with a role, a context, a format, and one example. I can read its output, decide what's wrong, and improve the prompt.

This is the lesson where the learner stops being a *user* of AI and starts being a **director** of it. Imperatives in English ("Write a summary", "Translate this", "Don't include …") are the grammar of giving instructions, which is what prompts are. Form serves function exactly.

## Pre-task (10 min) — Two prompts, one task

Show the learner two prompts that ask for the same thing. They've seen the AI by now (week 8), so they have intuition.

**Prompt A:**
> summarize this

**Prompt B:**
> You are an English teacher helping a Thai student at CEFR A2. Summarize the following text in 3 sentences using simple vocabulary. Keep the summary under 60 words. If a Thai cultural term appears, keep it in Thai and add a short English gloss in parentheses.
>
> Text: [...short Thai-news article...]

Without running them, ask:

1. Which one will give a more useful answer? Why?
2. What is in prompt B that isn't in prompt A?
3. Has the learner ever written a prompt like B?

This activates the intuition that *more specification → more useful output*. The lesson is going to formalize that intuition into a pattern.

## Input (10 min) — A short reading

A 120-word reading the learner reads silently, then aloud once.

> A prompt is a set of instructions you give to an AI. It is written in normal English, but for a reader that is not human. So the rules are a little different.
>
> A good prompt usually has four parts. **First**, a role — *"You are an English teacher."* **Then**, a context — *"You are helping a Thai student at CEFR A2."* **Next**, a format — *"Give me three sentences, under 60 words."* **Finally**, an example or two — *"For instance, instead of 'utilize,' use 'use.'"*
>
> If you give the AI a role, it will speak from that role. If you give it a format, it will try to match the format. If you give it an example, it will copy the shape of the example. If you don't, the AI will guess — and its guesses are often boring.

Comprehension:

1. What are the four parts of a good prompt?
2. What happens if you don't give a format?
3. *Noticing:* The text uses *first, then, next, finally*. What are these for?

## Noticing (5 min) — Imperatives, first conditional, sequencers

Three things showed up in the reading. Pull them out.

**Imperatives.** *Summarize this. Keep the summary under 60 words. Use simple vocabulary. Don't include cultural terms.*

> Shape: **verb (base form) + the rest**. No subject.
> Function: giving instructions. Polite enough for AI (no *please* needed, but it doesn't hurt humans).

**First conditional.** *If you give the AI a role, it will speak from that role.*

> Shape: **if + present simple, ... + will + verb**.
> Function: cause and effect, prediction. Exactly what we need to talk about prompts: *if I do this, the AI will do that*.

**Sequencing markers.** *First, then, next, finally.*

> Function: connecting steps in a procedure. Useful for both English production and prompt-writing (sometimes prompts are themselves sequenced).

Concept check: which is better in a prompt — *"Could you possibly summarize this text for me, if it's not too much trouble?"* or *"Summarize this text in three sentences."*? Why?

(Answer: the second. Politeness fillers add tokens without adding information. AIs respond well to direct imperatives.)

## Controlled practice (10 min)

**Form-focused, imperatives.** Rewrite each polite request as a clean imperative for an AI:

1. Could you maybe write a short summary?
2. I was wondering if you could translate this.
3. Would it be possible to give three examples?
4. If you don't mind, please don't use complicated words.

(Suggested rewrites: *Write a short summary. Translate this. Give three examples. Use simple words only.*)

**Form-focused, first conditional.** Complete:

1. If I add an example, the AI ___ (copy) the shape.
2. If you don't specify a length, the AI ___ (give) you something too long.
3. If the prompt is in Thai, the AI usually ___ (reply) in Thai.

**Meaning-focused.** For each of these prompts, predict (in one sentence) what the AI will do. Use the first conditional.

- "Translate." → *If the prompt is just "translate", the AI will ask what to translate.*
- "Write a poem about Doi Suthep in 4 lines, with rhyme." → *...*
- "Be more concise." (in the middle of a long chat) → *...*

## The Task (15 min) — Iterate a real prompt

The learner picks one of three real jobs:

**Job A — Tourist explainer.** Write a prompt that gets the AI to explain *Loy Krathong* to a foreign visitor in 4 sentences, in English, using simple words.

**Job B — Vocabulary helper.** Write a prompt that gets the AI to give 10 useful English chunks for buying coffee at a café, with Thai translations, in a table.

**Job C — Code helper.** Write a prompt that gets the AI to write a Python script that prints the days of the week in English and Thai.

Then **iterate**. The bot guides:

1. **Version 1.** The learner writes their first prompt. Run it. Read the output together.
2. **Diagnose.** What's wrong? Too long? Wrong format? Misses Thai? Uses words too hard?
3. **Version 2.** Add one of the four parts (role, context, format, example). Run again.
4. **Version 3.** Add a second part. Run again.
5. **Compare.** Which version is most useful? Why?

The learner produces (in writing, in English) at least three sentences using imperatives and first conditional, comparing the versions:

> "If I add a role, the AI sounds more like a teacher. The third version is the most useful because it has an example. Without an example, the AI used hard words like 'culinary'."

## Post-task language focus (5 min) — Reformulation

Likely errors and recasts:

| Learner says | Bot's recast |
|---|---|
| "If you will give an example, the AI copy it." | "*If you give an example, the AI will copy it.* — only one *will*, on the main verb." |
| "Please you to translate this." | "*Translate this, please.* — imperative is just the verb, no *you*." |
| "First, the next, finally..." | "*First, ..., next, ..., finally, ...* — drop the *the*." |

## Wrap (5 min) — Reflection

1. What's one thing you'll do differently the next time you write a prompt?
2. What's one thing in English that was hard today?
3. The lesson said *"the AI will guess, and its guesses are often boring."* Do you agree? Why?

## Vocabulary / chunk bank

```
- write a prompt              (เขียน prompt)                   [tech, neutral]
- give a clear instruction    (ให้คำสั่งที่ชัดเจน)              [neutral]
- specify the format          (ระบุรูปแบบ)                     [neutral]
- give an example             (ยกตัวอย่าง)                     [neutral]
- a role                      (บทบาท)                          [neutral]
- a context                   (บริบท)                          [neutral]
- iterate on a prompt         (ปรับปรุง prompt)                [tech]
- copy the shape              (ลอกแบบ / ตามรูปแบบ)             [neutral]
- a one-shot example          (ตัวอย่างเดียว / one-shot)        [tech, jargon]
- a few-shot example          (ตัวอย่างหลายชิ้น / few-shot)     [tech, jargon]
```

## Pronunciation focus — Stress on imperative verbs

In an imperative, the verb is the most important word in the sentence. English speakers **stress it**. Thai speakers often flatten the stress, which can make the instruction sound like a question.

Drill — say each twice. First emphasize the verb; then the wrong way (flat):

- **Write** a summary. / Write a summary. *(flat — sounds uncertain)*
- **Translate** this. / Translate this.
- **Don't** include cultural terms. / Don't include cultural terms.

*Don't* in imperatives is especially important. The /n't/ is the contradiction; stress carries the meaning. Learners who say "don't include" all flat may have the AI ignore the negation in voice mode.

## Homework

1. **Production (5 min):** pick a job you do — at your work, at home, or just for fun. Write a prompt (4 parts) that asks the AI to help you with one step of that job. Send the prompt and the AI's response to Kru Eng.
2. **Comparison (3 min):** take one of your existing prompts and write a "before" and "after" version. Show one improvement using the first conditional: *"If I add ___, the AI will ___."*
3. **Reuse:** bring back week 8's *can / can't* — in one sentence of your homework, hedge an AI capability claim. *"The AI can translate, but it can't always catch tone."*

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation of prior knowledge | Pre-task (two prompts) |
| Modeled language | Input (reading + sample prompt B) |
| Concept-checking | Noticing |
| Controlled practice with feedback | Controlled practice |
| Communicative production | The Task |
| Error correction | Post-task language focus |
| Learner reflection | Wrap |
| Cross-curricular link (tech) | The Task |

## References

- *[ref:Reynolds & McDonell 2021]* — early work on prompt patterns and few-shot framing.
- *[ref:Lewis 1993]* — *write a prompt*, *iterate on the prompt*, *copy the shape* as lexical chunks.
- `lessons/w08_what_is_ai_and_what_can_it_do.md` — *can/can't* foundation reused here.
- `vocabulary/tech_lexical_chunks.md` — prompt-engineering chunks.
