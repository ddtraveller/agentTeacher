---
title: Formative Assessment Techniques
type: reference
status: live
topic: low-stakes daily checks for understanding
updated: 2026-05-11
---

# Formative Assessment Techniques

How Kru Eng knows whether learning is happening — without resorting to graded tests. The bot runs these as part of every lesson; the owner can add or override them.

The principle: **assess to teach, not to grade.** A formative check that doesn't change what we do next is wasted effort. Every check below has a clear consequence in the next lesson.

## 1. Can-do self-rating

At the wrap of every lesson, the bot asks the learner to rate the can-do for that lesson on a four-point scale, in either English or Thai:

- 🟢 *I can do this without help.*  (มั่นใจ ทำเองได้)
- 🟡 *I can do this with a little help.*  (พอทำได้ ต้องมีคนช่วยบ้าง)
- 🟠 *I can do part of this.*  (ทำได้บางส่วน)
- 🔴 *I can't do this yet.*  (ยังทำไม่ได้)

The rating goes into `students/<nickname>.md` → Current goals.

**Consequence:**
- 🟢 → the chunk/task graduates; appears only in spaced retrieval after this.
- 🟡 → bot schedules one reinforcement turn in the next lesson's warm-up.
- 🟠 → the lesson's task gets re-run, easier version, in the next lesson.
- 🔴 → the *prerequisite* lesson gets re-run before continuing.

## 2. Exit ticket

A two-question check before the session ends:

1. *Tell me one thing you can say now that you couldn't say at the start.*  (Production check.)
2. *Tell me one thing you're still not sure about.*  (Gap check.)

The bot logs the answers verbatim. The first is evidence of gain; the second drives next lesson's input. **Never** skip the second — a learner who says "everything's fine" probably means "I don't want to admit anything's hard," and the bot follows up gently in Thai.

## 3. Concept-checking question (CCQ)

After teaching any new structure or chunk, the bot asks 2–3 short questions that test **meaning**, not form. For *can / can't* (week 8):

- "Is *can* about ability or permission?" — *both, depending on context*
- "If I say *I can't swim*, is swimming hard for me or impossible?" — *impossible, or close to it*
- "*Can* the AI search the internet right now?" — meaning check + retrieval

CCQs surface the gap between *they can repeat the form* and *they can use the meaning*.

## 4. Listen-and-do (TPR-flavored)

For tech vocabulary especially, the bot says a chunk and asks the learner to **do the action**:

- "Open the terminal." → bot watches the screen share.
- "List the files in this folder." → bot watches the output.
- "Make a commit with a short message." → bot watches the git command.

This bypasses production entirely and just tests receptive understanding through action. Useful when the learner is shy about speaking but their comprehension might be ahead.

## 5. Recast monitoring

The bot logs every recast it issues during a lesson. After three sessions, patterns emerge:

- A learner who keeps producing *"she go"* despite three weeks of recasts → escalate to focused mini-explanation.
- A learner who self-corrects after a single recast → graduate the pattern from active monitoring.

This data lives in the auto-log section of the learner profile and feeds the night-time hermes-night summary.

## 6. Chunk-reuse tracking

The bot records every chunk the learner uses unprompted. If a chunk from week 1 (*I'm from …*) appears in week 5 without being prompted, that's evidence the chunk has consolidated. If it never reappears, the bot schedules a spaced-retrieval return.

Format in profile:

```
- open the terminal      intro w1   reused w3 (prompted), w9 (unprompted)
- make a commit          intro w5   reused w9 (unprompted), w12 (unprompted)   ← consolidated
- ask the model          intro w8   no reuses                                  ← needs return
```

## 7. The "explain it to me" check

At the end of any tech or AI concept lesson, the bot asks:

> Pretend I'm a friend who has never used this. Explain it to me in 30 seconds, in English.

The learner produces an extended turn from memory. The bot listens for:
- accurate content
- chunk reuse
- pronunciation patterns
- hedging (*I think*, *probably*) where uncertainty is real

This is the single highest-bandwidth assessment Kru Eng runs. It tests production, comprehension, and metacognition simultaneously. Save the audio.

## 8. AI-mediated written feedback

For asynchronous written work the learner submits between sessions:

1. The learner submits the text in the chat or as a markdown file in their folder.
2. The bot runs a **layered feedback** pass:
   - **Layer 1 — meaning.** Did I understand it? Are there places I couldn't follow?
   - **Layer 2 — chunks.** Did the learner use any chunks from the recent lessons? Are there obvious places to suggest one?
   - **Layer 3 — form.** Are there 1–2 errors that are worth addressing this round?

   Layer 3 stops at 1–2. Marking up every error is comprehensible-input poisoning. *[ref:Truscott 1996, Ferris 2004]*

3. The bot sends the feedback back as a comment-style reply, **not** as a rewrite. Rewrites take the agency away from the learner.

## 9. Diagnostic micro-tests (start of course only)

On day 1, the bot runs three short diagnostics:

- **Pronunciation:** the 10-phrase listen-and-repeat from `pronunciation/thai_l1_interference.md`.
- **CEFR placement:** a 10-question receptive test (4 listening, 3 reading, 3 short writing prompts) drawn from CEFR descriptors. Gives a band (A0 / A1 / A2 / B1).
- **Tech baseline:** a 5-task screening — *open a browser; show me a search; type a sentence; take a screenshot; show me the file you just saved*. Gives a self-described tech level.

All three feed the initial `students/<nickname>.md`. They are **not** repeated; later checks are formative, not placement.

## 10. What we don't do

- **No weekly quiz with a score.** The score is a single number that pretends to summarize a complex thing; it doesn't.
- **No final exam.** The CEFR can-do checks across the 12 weeks are the assessment of record.
- **No public ranking** between learners. The bot speaks only about the learner in front of it, never compares.
- **No surprise tests.** The next session's content is always known in advance.

## What this means operationally

The bot's tool surface includes `lookup_student(name)` so it can read the profile before each session. Before the session starts, the bot loads:

- The learner's most recent self-rating on the previous can-do
- Their pronunciation watchlist
- Their fading chunks (more than 21 days since last reuse)
- Their stated goals

These four inputs shape the pre-task warmup of every session. Without them, the bot is teaching a *generic A2 learner*, not the actual person in front of it.

## References

- *Wiliam, D.* (2011). *Embedded Formative Assessment.* Solution Tree. — practical formative techniques.
- *Truscott, J.* (1996). The case against grammar correction. *Language Learning* 46. — why marking everything is harmful.
- *Ferris, D.* (2004). The "grammar correction" debate in L2 writing. *Journal of Second Language Writing* 13. — the response to Truscott; nuanced position.
- *Council of Europe.* (2020). *CEFR Companion Volume.* — can-do descriptors.
- `students/learner_profile_template.md` — where assessment data lives.
