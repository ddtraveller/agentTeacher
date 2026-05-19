---
title: Week 8 — What Is AI, and What Can It Do?
type: lesson
status: live
topic: AI literacy + modal "can/can't" for ability
updated: 2026-05-11
week: 8
cefr: A2
duration_min: 60
can_do: I can describe what an AI tool can and can't do, using "can" and "can't" correctly.
english_focus: modal can / can't (ability), be able to, comparison via these
tech_focus: trying ChatGPT, Claude, and the local Ollama side-by-side
ai_thread: what a language model actually does — pattern completion, not understanding
---

# Week 8 — What Is AI, and What Can It Do?

## Can-do

> I can describe what an AI tool can and can't do, using *can* and *can't* correctly, and give one example of each.

This is the lesson where AI stops being a magic black box. By the end, the learner can name **what kind of thing** a language model is, can use *can/can't* to talk about it accurately, and has tried at least two different AI tools side-by-side.

## Pre-task (10 min) — What do you think AI is?

Open with one open question, in Thai if the learner needs it, in English if they don't:

> What's the first thing that comes to mind when I say *AI*? Don't filter — just say.

Common answers and how the bot handles them:

| Learner answer | Bot's move |
|---|---|
| "ChatGPT." | "Right — ChatGPT is one. Today we'll meet a few others." |
| "Robot." | "Sometimes! But the kind of AI we'll talk to today doesn't have a body. It only has words." |
| "Like in movies?" | "Movie AI and real AI are very different. Today we look at real." |
| "It's scary." | "That's a real feeling. We'll talk about that in week 12. Today: just look at what it does." |
| "ไม่รู้." | "That's fine. After this lesson, you'll have an answer of your own." |

This is **opinion activation**, not knowledge testing. The point is to surface whatever the learner already thinks so today's lesson can attach to it.

## Input (10 min) — Three short demos

The bot shows the learner three things in sequence. The learner watches; doesn't have to do anything yet.

**Demo 1 — Translation.** The bot pastes a Thai sentence into a chat with the local Ollama model:

> ฝนตกหนักมากตั้งแต่เมื่อคืน

The model returns:

> *It has been raining heavily since last night.*

The bot narrates in English:

> The AI can translate Thai into English. It did that in two seconds. A human can do it too, but slower.

**Demo 2 — Code.** The bot asks the same model:

> Write a one-line Python program that prints "hello, Chiang Mai".

The model returns:

```python
print("hello, Chiang Mai")
```

Narration:

> The AI can write small programs. This one is simple. Some are not.

**Demo 3 — A trick question.** The bot asks the model:

> What did Kru Eng do yesterday?

The model says something plausible — maybe:

> *Kru Eng prepared lessons for her students and reviewed their homework.*

Narration:

> Pause. Did I do that yesterday? Actually I don't have a *yesterday* in the way you do. I don't remember between conversations. The AI **made up** what sounded right. That's important.

After the three demos, two meaning-focused questions and one noticing question:

1. Which demo surprised you most?
2. In demo 3, the AI's answer was confident. Was it right? How do you know?
3. *Noticing:* I just used *can* a lot. *It can translate. It can write code. It can make things up.* What word do you think the opposite is?

## Noticing (5 min) — *can* and *can't*

Pull the chunks from the input:

- The AI **can** translate Thai into English.
- It **can** write a small program.
- It **can't** remember yesterday.
- It **can't** tell you when it's wrong.

The shape:

> **subject + can / can't + verb (base form) + the rest**

The meaning: *can* says it's possible / it knows how to. *can't* says it's not possible / it doesn't know how to.

The pronunciation note (which matters for Thai speakers — see *Pronunciation focus* below): *can't* in American English is /kænt/, in British English /kɑːnt/. Both end in /t/. Hold the /t/ — that's how listeners hear the difference between *can* and *can't*.

A more formal alternative: *is able to / isn't able to*. Same meaning, more formal register.

> The AI **is able to** translate. The AI **isn't able to** remember.

## Controlled practice (10 min)

**Form-focused.** True or false about the AI we just used? Fill in *can* or *can't*:

1. The AI ___ translate Thai to English.
2. The AI ___ tell you what I did yesterday accurately.
3. The AI ___ write Python code.
4. The AI ___ admit when it doesn't know something. *(This is a real bias — many models default to confident answers even when wrong.)*
5. The AI ___ remember our last conversation. *(Without special tooling, no.)*
6. The AI ___ read a PDF you give it. *(Depends on the tool — some yes, some no.)*

(Answers: can, can't, can, sometimes can't, can't, depends.)

Notice how the answers aren't all crisp. AI capabilities are **not** binary. That's part of the literacy.

**Meaning-focused.** Compare three AI tools the learner can actually open in a browser:

| Capability | ChatGPT (cloud) | Claude (cloud) | Local Ollama (this stack) |
|---|---|---|---|
| Translate Thai → English | ✅ | ✅ | ✅ |
| Search the internet | depends on version | depends on version | ❌ (we turned this off) |
| Remember last week's conversation | with memory feature | with projects | ❌ (resets each chat) |
| Run code | with tools | with tools | ❌ |
| See an image | ✅ | ✅ | depends on model |
| Work without internet | ❌ | ❌ | ✅ |

The learner picks two rows and says them aloud using *can / can't*:

> "ChatGPT can search the internet, but local Ollama can't."
> "Claude can see an image, and ChatGPT can too."

## The Task (15 min) — Build the comparison

The learner does this themselves, with bot assistance. Open three browser tabs:

1. https://chat.openai.com (or whichever ChatGPT is available)
2. https://claude.ai
3. http://localhost:11434 *(or the orchestrator's chat UI — whichever is the front door to the local Ollama)*

Give each one the **same** prompt:

> Translate this Thai sentence into casual English: "ฉันกินข้าวเช้าตอนเจ็ดโมง"

Compare the three answers. The learner produces (orally, then in writing) at least three sentences using *can / can't*, comparing the tools:

> "All three can translate. ChatGPT can give more options. Claude can explain why it chose those words. The local one is faster but can't search the web."

If the learner is more advanced, push them to a harder question — *can these tools answer a Thai cultural question accurately?* Try:

> What does ลอยกระทง mean and when is it celebrated?

The three answers will differ in tone, accuracy, and confidence. Discuss in English.

## Post-task language focus (5 min) — Reformulation

Likely errors and the recasts:

| Learner says | Bot's recast |
|---|---|
| "AI can to translate." | "AI *can translate*. No *to* after *can*." |
| "She can't remembers." | "She *can't remember*. After *can* and *can't*, the verb is plain — no *-s*." |
| "AI cannot does math sometimes." | "AI *can't always do* math. Or: AI *sometimes can't do* math. *Cannot* is one word, by the way." |

Pick one error the learner actually made. Recast, ask them to say the correct version once, move on.

## Wrap (5 min) — Reflection

1. Finish this sentence in English: *"AI can..."*
2. Finish this sentence: *"AI can't..."*
3. Has your idea of what AI is **changed** today? How?

Write the answers to `students/<nickname>.md`. They feed into week 12's ethics discussion.

## Vocabulary / chunk bank

```
- can + verb              (สามารถ + กริยา)              [ability, neutral]
- can't + verb            (ไม่สามารถ + กริยา)           [inability, neutral]
- be able to              (สามารถ — ทางการกว่า)         [formal alternative]
- it depends              (แล้วแต่)                     [hedging, neutral]
- it makes things up      (มันมั่ว / กุขึ้นมา)            [AI-specific, useful]
- it's plausible but ...  (มันฟังดูสมเหตุสมผล แต่...)    [hedging, register: neutral]
- ask the model           (ถามโมเดล)                   [tech, neutral]
- write a prompt          (เขียน prompt)               [tech, neutral]
- check the output        (ตรวจ output)                [tech, neutral]
```

## Pronunciation focus — *can* vs *can't* (and why Thai speakers often blur them)

This is one of the most common comprehension failures for Thai L1 listeners. The bot should hammer it briefly.

- **can** (unstressed, in normal speech): /kən/ — *I can translate* → /aɪ kən ˈtrænzleɪt/.
- **can't**: /kænt/ (US) or /kɑːnt/ (UK). Always with the final /t/, always with a full vowel.

The trick: when *can* is unstressed, it's almost a *kuh*. When *can't* is stressed, the vowel is full and the /t/ is audible. Native speakers tell them apart **by stress and vowel length**, not by the /t/ alone.

Drill (the bot says, learner repeats):

- I can ˈtranslate. (stress on *translate*; *can* is small)
- I ˈcan't translate. (stress on *can't*; *can't* is loud)
- She can ˈrun it. / She ˈcan't run it.

Final consonants matter here too. The /t/ in *can't* often disappears for Thai speakers; the workaround is to hit the vowel hard instead.

## Homework

1. **Production (5 min):** ask the same AI three questions about northern Thailand — one about food, one about history, one about a place. Write down where each answer is **confident but wrong**, **confident and right**, or **honestly uncertain**. Bring the list to next lesson.
2. **Listening (3 min):** watch one short YouTube clip (1–2 min) of a Thai person speaking English. Count how many times you hear *can* and *can't*. Note any you didn't catch.
3. **Reuse:** use *I'm from ...* and *I'm a ...* (week 1) to introduce yourself in your first prompt to an AI: "I'm a student from Chiang Mai. Can you ...". The chunks should travel.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation of prior knowledge | Pre-task |
| Modeled language | Input (three demos) |
| Concept-checking | Noticing |
| Controlled practice with feedback | Controlled practice |
| Communicative production | The Task |
| Error correction | Post-task language focus |
| Learner reflection | Wrap |
| Cross-curricular link (tech) | The Task |

## References

- *[ref:Bender et al 2021]* On the dangers of stochastic parrots — for the *"it makes things up"* framing.
- *[ref:CEFR can-do A2]* — *can describe in simple terms aspects of his/her background, immediate environment and matters in areas of immediate need.*
- `pronunciation/thai_l1_interference.md` — *can / can't* discrimination.
- `vocabulary/tech_lexical_chunks.md` — AI-specific chunks.
