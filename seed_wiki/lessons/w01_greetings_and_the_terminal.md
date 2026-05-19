---
title: Week 1 — Greetings and the Terminal
type: lesson
status: live
topic: introductions + first terminal session
updated: 2026-05-11
week: 1
cefr: A1
duration_min: 60
can_do: I can greet someone, introduce myself, and run a few commands on a computer.
english_focus: verb "to be" (am / is / are), simple Wh-questions
tech_focus: opening a terminal; pwd, ls, cd, echo
ai_thread: what does it mean to "give an instruction" to a computer (and, later, to an AI)?
---

# Week 1 — Greetings and the Terminal

## Can-do

By the end of this lesson, the learner can:

> I can greet someone, introduce myself in three or four sentences, and run a few simple commands on a computer.

## Pre-task (10 min) — Activation

Open the session like a real-world meeting between two people who haven't met before. The bot says:

> Hello. I'm Kru Eng. What can I call you?

After the learner gives their name, the bot follows up:

> Nice to meet you, <name>. Where are you from?

Then one more question — *what do you do?* or *what do you like?* — that the learner can answer with a single word or chunk.

This is **not** controlled practice yet. The bot accepts any utterance — including Thai, broken English, a one-word answer — and recasts it back as a complete English sentence:

> Learner: "Chiang Mai"
> Bot: "Ah, you're from Chiang Mai. Me too — kind of."

The point: the learner produces *something*, and immediately hears a slightly more complete version. That's the first piece of input.

## Input (10 min) — A first meeting, in dialogue

Read this aloud (or play the audio recording, if available). The learner listens, doesn't repeat.

> **Aey:** Hi. My name is Aey. What's your name?
> **Tao:** I'm Tao. Nice to meet you, Aey.
> **Aey:** Nice to meet you too. Where are you from, Tao?
> **Tao:** I'm from Chiang Rai. And you?
> **Aey:** I'm from Chiang Mai, but I live in Lampang now.
> **Tao:** Oh, what do you do in Lampang?
> **Aey:** I'm a barista. I work at a coffee shop near the train station.
> **Tao:** That's cool. I'm a student. I study computer science.

After the input, ask three meaning-focused questions:

1. Where is Aey from? Where does she live now?
2. What does Tao study?
3. Whose job involves coffee?

And one noticing question:

4. Listen again. How does Aey say *I'm from Chiang Mai*? Does she say "I am" or "I'm"? Both? Why?

## Noticing (5 min) — *to be* in introductions

Pull these out of the dialogue:

- *I'm* Aey. *I'm* a barista. *I'm* from Chiang Mai.
- *You're* from Chiang Rai.
- *He's* a barista. (or *She's* — we know Aey is *she*).

Notice with the learner:

- The shape: **subject + am / are / is + something**.
- The contracted form: *I'm*, *you're*, *she's*. Native speakers contract by default.
- The meaning: *to be* connects you to a name, a place, a job, a state.

Concept check, under 25 words: "We use *am* with **I**, *is* with **he / she / it**, and *are* with **you / we / they**. We almost always say the short version."

## Controlled practice (10 min)

**Form-focused.** Fill in *am / is / are*:

1. I ___ a teacher.
2. She ___ from Lampang.
3. They ___ in the coffee shop.
4. We ___ students.
5. He ___ my brother.
6. You ___ tired today.

(Answers: am, is, are, are, is, are.)

**Meaning-focused.** The bot says one of these; the learner says which is true *about themselves*:

- I'm a student. / I'm a teacher. / I'm a barista. / I'm a programmer.
- I'm from Chiang Mai. / I'm from Chiang Rai. / I'm from Bangkok. / I'm from somewhere else.

The learner picks and produces the matching sentence aloud.

## The Task (15 min) — Self-introduction in the terminal

This is the destination. The learner:

1. Opens a terminal on their device. (The bot walks them through this if needed — Mac: *Terminal.app*; Windows: *PowerShell*; iPad/phone: *Termux* or any SSH client.)
2. Types these three commands, one at a time:

```bash
echo "Hello, my name is <name>."
echo "I am from <place>."
echo "I am a <job or student>."
```

3. Reads the output aloud — that's their self-introduction. The terminal "introduced" them.

Then the bot extends with two real terminal commands:

```bash
pwd      # where am I?
ls       # what's here?
```

The bot models how to *say what each command does* in English:

- `pwd` — *Print working directory*. It tells me where I am.
- `ls` — *List*. It shows me what's here.

The task isn't to memorize the commands. It's to get the learner to **say in English what they're doing on the computer**. The two skills braid: English narration + tech action.

## Post-task language focus (5 min) — Reformulation

Likely errors and their recasts:

| Learner says | Bot's recast |
|---|---|
| "I am come from Chiang Mai." | "Ah, *I'm from* Chiang Mai. *Come from* and *am from* mean the same thing — we usually pick one." |
| "She a teacher." | "*She's* a teacher. We always need *is* or *'s* in the middle." |
| "I from Lampang." | "*I'm* from Lampang. Don't drop the *am*." |

Pick **one** of the errors the learner actually made today. Recast it on the screen, ask the learner to say it once, move on. Don't drill all three.

## Wrap (5 min) — Reflection

Three questions, the learner answers as best they can:

1. What's one thing you can say in English now that you couldn't say at the start of the lesson?
2. What's still hard about *am / is / are*?
3. What's one new word from the terminal that you want to remember?

The bot writes the answers to `students/<nickname>.md` → `## Auto-log`.

## Vocabulary / chunk bank

```
- my name is ...                 (ฉันชื่อ...)                  [register: neutral]
- nice to meet you               (ยินดีที่ได้รู้จัก)              [register: neutral]
- where are you from?            (มาจากไหน)                   [register: neutral]
- I'm from ...                   (ฉันมาจาก…)                   [register: neutral]
- what do you do?                (ทำงานอะไร)                  [register: neutral]
- I'm a ...                      (ฉันเป็น...)                   [register: neutral]
- open the terminal              (เปิด terminal)               [register: tech]
- run a command                  (รันคำสั่ง)                    [register: tech]
- print the working directory    (แสดงตำแหน่งโฟลเดอร์ปัจจุบัน)  [register: tech]
- list the files                 (แสดงรายการไฟล์)              [register: tech]
```

## Pronunciation focus — Final consonants

Thai often drops or softens final consonants. In *to be* this matters most for:

- *am* — the /m/ at the end is voiced and lips closed. Hold the /m/ briefly.
- *is* — ends in /z/ (a buzz, not /s/). *He's* ends in /z/.
- *are* — final /r/ is light in most English accents; vowel matters more.

Quick drill: *am, am, I am, I am Aey. is, is, she is, she's Aey. are, are, you are, you're Aey.*

For *terminal-specific* words this week:

- **echo** /ˈek.oʊ/ — two syllables, stress on the first. Not /ee-ko/.
- **list** /lɪst/ — final /st/ cluster. Close mouth on the /t/.

## Homework

1. **Production (3 min):** record a 30-second voice memo introducing yourself with at least three sentences using *am / is / are*. Send it to Kru Eng.
2. **Listening (3 min):** listen to the input dialogue again. Note one thing Aey says that you'd like to be able to say.
3. **Reuse — none yet** (this is week 1; reuse starts in week 2 by bringing back today's chunks).

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation of prior knowledge | Pre-task |
| Modeled language | Input (dialogue) |
| Concept-checking | Noticing Q3, Q4 |
| Controlled practice with feedback | Controlled practice |
| Communicative production | The Task |
| Error correction | Post-task language focus |
| Learner reflection | Wrap |

## References

- *[ref:Lewis 1993]* — chunks over isolated words.
- *[ref:Ellis 2003]* — task as destination, not as exercise.
- `pronunciation/thai_l1_interference.md` — final consonants section.
