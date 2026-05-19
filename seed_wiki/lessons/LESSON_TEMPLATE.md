---
title: Lesson Template
type: template
status: live
topic: canonical lesson shape (modern TBLT + lexical + scaffolded production)
updated: 2026-05-11
---

# Lesson Template

This is the canonical shape every weekly lesson follows. Copy this file to `wNN_<slug>.md`, fill in the bracketed fields, and either leave `status: DRAFT` (for the owner to approve) or set `status: live` if you're the owner committing directly.

The template is not pure PPP. It is a **task cycle** with PPP-style scaffolding embedded inside it, plus an explicit lexical-chunk focus and a metacognitive close. The DSS-rubric mapping is in the appendix so the same lesson file is usable as Observed Teaching Practice material without rewrites.

---

```markdown
---
title: <Week N — Lesson title>
type: lesson
status: DRAFT
topic: <one-line topic>
updated: YYYY-MM-DD
week: NN
cefr: A1 | A2 | B1
duration_min: 60
can_do: <I can [verb] [object] [condition].>
english_focus: <grammar/lexis target — keep this small, one item>
tech_focus: <tool, command, or concept>
ai_thread: <the AI literacy thread for this week>
---

# Week N — <Title>

## Can-do (the destination)

By the end of this lesson, the learner can:

> <can-do statement, learner's voice, present tense>

This is the only thing that matters. The grammar, vocabulary, and tech below all serve this can-do.

## Pre-task (10 min) — Activation

A short, low-stakes warm-up that:

1. Activates schema for the topic (so the learner is already thinking about the meaning before any new form arrives).
2. Surfaces what the learner already knows / can already do in this area.
3. Lets the bot diagnose where this learner is starting today.

Examples by lesson type:
- **Conversation lesson:** show an image, ask one question.
- **Tech lesson:** ask "have you ever opened a terminal? what's a terminal?".
- **Grammar-heavy lesson:** play a 30-second audio clip and ask one comprehension question.

Avoid: presenting new vocabulary or grammar in the pre-task. The pre-task is about *meaning first*.

## Input (10 min) — Comprehensible exposure

A piece of language input slightly above the learner's current level (i+1), with the meaning recoverable from context. Types:

- A short text (60–120 words).
- A short dialogue (8–12 turns).
- A short audio clip.
- A short demo (you running the terminal command while narrating).

The learner does **not** have to produce yet. They listen / read / watch. After the input:

- 3 meaning-focused questions (what happened? who? why?).
- 1 form-focused noticing question (*how did Kru Eng say "I don't know"? Listen again.*).

The form-focused question is the bridge to the next section.

## Noticing (5 min) — Focus on form within meaning

Highlight the target form **after** the learner has met it in input. Don't pre-teach. The pattern:

1. "Did you notice this?" — pull out the target chunk or structure from the input.
2. "What does it mean?" — meaning before form.
3. "What's the shape?" — minimal explicit rule, under 25 words.
4. "Why might you say this?" — when/where would you use it?

Avoid: teaching the rule first and then giving an example. The brain takes the rule more readily when it already has examples to attach the rule to. *[ref:DeKeyser 2007]*

## Controlled practice (10 min) — Drill, but not boring

Two short exercises:

- **Form-focused:** transformation, gap-fill, or pattern drill. 6–8 items max. Get the form into the muscles.
- **Meaning-focused:** the same form, but the learner has to pick which one fits a context. Force the choice on meaning, not on form.

Avoid: doing 20 of the same drill. Doing the same drill 20 times mostly trains tolerance for drills.

## The Task (15 min) — Real-world output

The week's task. This is the destination from the can-do. Examples by week:

- **W1:** record a one-minute self-introduction with three terminal commands.
- **W6:** write `about_me.html` with one heading, three paragraphs, one list.
- **W10:** write three versions of a prompt; compare outputs.

The task must be:

- **Communicative.** It exists for someone to read / watch / use.
- **Open-ended.** There's no single "right answer".
- **Within reach.** A learner at the bottom of the lesson's CEFR band can do a basic version.
- **Stretchable.** A learner at the top of the band can produce something rich.

The bot's role during the task: **scaffold sparingly**. Offer help when asked, recast errors *after* the learner finishes a turn, don't interrupt the meaning-making.

## Post-task language focus (5 min) — Reformulation

After the task, look at one or two errors the learner made *that have the same shape as today's target form*. Recast them, write the corrected version next to the learner's version, and ask the learner to say the corrected version aloud once.

Avoid: reformulating every error. One or two. Quality over quantity.

## Wrap (5 min) — Metacognitive close

The learner reflects, in English if they can, in Thai if they need to:

- "What's one thing you can do now that you couldn't do before?"
- "What's one thing that's still hard?"
- "What do you want to come back to next week?"

The bot writes the answers into the learner's profile. They drive next week's pre-task.

## Vocabulary / chunk bank (reference, not memorize)

Chunks the lesson uses. Aim for 6–10 chunks, not 20+ single words. Format:

```
- <chunk>                       (gloss in Thai)              [register: neutral / formal / informal]
- could you say that again      (พูดอีกครั้งได้ไหม)           [register: neutral]
- I'm not sure but I think...   (ไม่แน่ใจ แต่คิดว่า…)         [register: neutral / hedge]
```

## Pronunciation focus (1–2 items)

Pick **one** L1-interference pattern that this lesson's chunks expose. Don't try to cover the whole sound system. Examples:

- W1: final consonants — *want*, *like*, *work*.
- W6: schwa in unstressed syllables — *com-pu-ter* → /kəmˈpjuːtə/.
- W10: stress on imperative verbs — *Write* a summary, not *write* a summary.

See `pronunciation/thai_l1_interference.md` for the full pattern reference.

## Homework — Spaced retrieval, not review

Three short items (10 min total). At least one must reuse a chunk from a previous week. The bot tracks reuse and times reappearances.

1. <item — production, 3–5 min>
2. <item — listening or reading, 3–5 min>
3. <item — chunk reuse from week M, 1–2 min>

## DSS-OTP mapping (appendix; optional)

For trainee teachers using this lesson as OTP material. Map each DSS observable to one or more lesson sections above.

| DSS observable | Section(s) |
|---|---|
| Clear lesson aim communicated | Can-do |
| Activation of prior knowledge | Pre-task |
| Modeled language | Input + Noticing |
| Concept-checking | Noticing (Q3, Q4) |
| Controlled practice with feedback | Controlled practice |
| Communicative production | The Task |
| Error correction sequence | Post-task language focus |
| Learner reflection | Wrap |

## References for this lesson

- *[ref:...]* — list the wiki pages and external sources used.
```

---

## Style notes for lesson writers

1. **Write in second-person plural ("we").** The lesson is a co-construction with the learner.
2. **Keep prose tight.** A lesson file should fit on two laptop screens.
3. **No emojis in the body** (the frontmatter is fine if you really want them). The bot reads this; emojis add tokens.
4. **Show real examples.** "She run to the market" is more useful than "[student error]".
5. **Cite when you cite.** If you're claiming the lexical approach says X, link to `references/teaching_methods.md` so the bot can hand the learner a follow-up.

## References

- *[ref:DeKeyser 2007]* DeKeyser, R. (2007). *Practice in a Second Language.* CUP.
- *[ref:Ellis 2003]* Ellis, R. (2003). *Task-based Language Learning and Teaching.* OUP.
- *[ref:Lewis 1993]* Lewis, M. (1993). *The Lexical Approach.* LTP.
- *[ref:Willis & Willis 2007]* Willis, D. & Willis, J. (2007). *Doing Task-Based Teaching.* OUP.
