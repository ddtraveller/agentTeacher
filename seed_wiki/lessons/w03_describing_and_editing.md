---
title: Week 3 — Describing People and Things, Editing Text
type: lesson
status: live
topic: adjectives + have/have got + text editor basics
updated: 2026-05-11
week: 3
cefr: A1
duration_min: 60
can_do: I can describe a person or a thing in 4–5 sentences, and I can edit and save a text file.
english_focus: adjectives, word order, have got vs have
tech_focus: text editors (nano, VS Code), open / edit / save
ai_thread: AIs "have" weights and training data, but no body and no memory
---

# Week 3 — Describing People and Things, Editing Text

## Can-do

> I can describe a person or a place in 4–5 sentences using adjectives correctly, and I can open, edit, and save a text file in an editor.

## Pre-task (8 min)

The bot shows two short descriptions:

> A: *Doi Suthep is a mountain near Chiang Mai. It is tall and green. There is a famous temple on top. The view from the temple is beautiful, especially in the morning when the mist is low.*
>
> B: *Mountain near Chiang Mai. Tall. Green. Temple on top. Beautiful view.*

Question: which one is a description? Which one is a list? Why?

The point: a description has **adjectives in sentences**, not just nouns.

## Input (10 min) — A person

Read aloud:

> My grandmother is small and has white hair. She is seventy-five years old, but she's very strong. She has got a vegetable garden behind her house in Mae Rim. She grows lemongrass, basil, and chillies. She walks to the market every morning to sell what she grew yesterday. She speaks Northern Thai at home, a little Standard Thai at the market, and three words of English: "hello," "thank you," and "no."

Questions:

1. How old is the grandmother?
2. What does she grow?
3. *Noticing:* I said *she is small* and *she has got a garden*. What's the shape of each?

## Noticing (5 min) — Adjectives, *have* / *have got*

**Adjectives** come **before nouns** (*a small garden*, not *a garden small*). Or after **to be** (*she is small*).

**Have** and **have got** mean the same thing:

> *She has a garden.* / *She has got a garden.* / *She's got a garden.*

*Have got* is more British, more spoken. *Have* is more American, more written. Both are fine.

Concept check: *She is got a garden.* — correct or wrong? (Wrong. It's *she has got*. *Got* needs *has* / *have*.)

## Controlled practice (10 min)

**Form-focused.** Put the words in order:

1. cat / black / a / small
2. coffee / hot / a / cup of
3. is / friendly / he / very
4. has got / phone / new / a / she

(Answers: *a small black cat; a cup of hot coffee; he is very friendly; she has got a new phone.*)

**Meaning-focused.** Describe each in one sentence:

- your phone
- a friend
- your favorite food

Use at least two adjectives. *"My phone is old but reliable."* / *"My friend Aey is funny and very tall."*

## The Task (18 min) — Edit your journal in a real editor

The learner opens their `week02/routine.md` from last week in a text editor:

```bash
cd ~/kru-eng/week02
code routine.md         # VS Code, if installed
# or:
nano routine.md         # always available on Linux/Mac/Termux
```

Add a description section, using adjectives. The bot prompts:

- Describe yourself in 2 sentences.
- Describe one family member in 2 sentences.
- Describe your phone or computer in 1 sentence.

The learner types directly in the editor. The bot watches for editor-flow issues (saving, accidentally closing without saving, recovering from a typo) and labels each action in English:

> "You just **saved** the file with Ctrl+S."
> "You **closed** the file. Open it again with `code routine.md`."

Save the file. Then a small technical extension: the learner opens the file with `cat`:

```bash
cat routine.md
```

The terminal **prints** the file contents. The bot points out: *the editor lets you change the file; cat just shows you what's in it.*

## Post-task language focus (5 min)

Common errors:

| Learner says | Recast |
|---|---|
| "She is have a garden." | "*She has* a garden. Or *she has got* a garden. Don't stack *is* and *have*." |
| "He has a big cat black." | "*A big black cat*. Adjectives come before the noun." |
| "It's house small." | "*It's a small house*. Don't drop *a*, and put *small* before the noun." |

## Wrap (4 min)

1. Describe yourself in one sentence with two adjectives.
2. What was the hardest thing about the text editor?
3. What's one chunk from today you want to remember?

## Vocabulary / chunk bank

```
- has got / has                  (มี)                            [have, neutral]
- is small / tall / old / young  (เล็ก/สูง/แก่/หนุ่ม-สาว)         [adjective patterns]
- behind / in front of / next to (ด้านหลัง / ด้านหน้า / ข้าง)      [position, intro w3, reuse w6]
- a vegetable garden             (สวนผัก)                       [noun phrase]
- in the morning / evening       (ตอนเช้า / เย็น)                [time, reuse w2]
- open the file                  (เปิดไฟล์)                      [tech]
- edit the file                  (แก้ไขไฟล์)                     [tech]
- save the file                  (บันทึกไฟล์)                    [tech, reuse w2]
- close the file                 (ปิดไฟล์)                       [tech]
- print the contents             (แสดงเนื้อหา)                   [tech, register: tech]
```

## Pronunciation focus — Adjective–noun stress

In *a small black cat*, the **stress** falls on **cat** (the noun). Adjectives are unstressed or lightly stressed.

Drill — say twice, then with stress on the noun:

- a SMALL black CAT → a small black CAT
- a NEW phone → a new PHONE
- a TALL strong WOMAN → a tall strong WOMAN

Thai L1 speakers often stress every word equally. Push the last content word (the noun) and reduce the rest.

## Homework

1. **Production (5 min):** write a 5-sentence description of your village or neighborhood in `week03/place.md`. Use at least 4 different adjectives. Save it.
2. **Listening (3 min):** ask the local Ollama bot: *Describe Chiang Mai in 5 sentences using simple adjectives.* Read its description out loud.
3. **Reuse:** include one terminal command from week 1 in your description (e.g., *I ran the script and it worked*) — even if it's not strictly true. The chunk should travel.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task (A vs B) |
| Modeled language | Input |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Production | The Task |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- `vocabulary/tech_lexical_chunks.md` — Group A (file operations).
- `pronunciation/thai_l1_interference.md` — stress patterns.
