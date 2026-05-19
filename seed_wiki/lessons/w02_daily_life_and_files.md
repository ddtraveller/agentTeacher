---
title: Week 2 — Daily Life and Files
type: lesson
status: live
topic: present simple + filesystem operations
updated: 2026-05-11
week: 2
cefr: A1
duration_min: 60
can_do: I can describe my daily routine and create, move, and delete files on my computer.
english_focus: present simple (positive), 3rd person -s, time expressions
tech_focus: mkdir, touch, mv, rm, basic paths
ai_thread: files are how computers remember; AIs handle memory very differently
---

# Week 2 — Daily Life and Files

## Can-do

> I can describe what I do every day in 3–5 sentences, and I can create, move, and delete files on my computer from the terminal.

## Pre-task (8 min)

The bot greets in English (reusing week 1's *I'm from …*) and asks: *What time do you wake up?* / *What do you eat for breakfast?*

The learner answers however they can — single words, broken English, Thai. The bot recasts each answer into a full sentence:

> Learner: "Seven."
> Bot: "Ah, you wake up at seven."

After two or three exchanges, the bot says: *Today we'll talk about your day, and we'll teach the computer a few new tricks too.*

## Input (10 min) — A daily routine

Read aloud:

> Aey works at a coffee shop in Lampang. She wakes up at six. She walks to the shop at six-thirty. She opens the shop at seven. She makes coffee, takes orders, and talks to customers all morning. At noon, she eats lunch with her colleague. In the afternoon, she cleans the shop and counts the money. She closes the shop at six and walks home.

Questions:

1. Where does Aey work?
2. What does she do at noon?
3. *Noticing:* Aey *walks*, *opens*, *makes*, *takes*. Why all the -s endings?

## Noticing (5 min) — Present simple, 3rd person -s

Pull from the input. Shape:

> **Subject + verb (+ -s for he/she/it) + the rest**

Concept check, 20 words: "When the subject is *he*, *she*, or *it*, we add -s to the verb. With *I*, *you*, *we*, *they*, the verb has no -s."

Three quick tests:
- *They open the shop.* (no -s)
- *She opens the shop.* (-s)
- *I open the shop.* (no -s)

## Controlled practice (10 min)

**Form-focused.** Add -s where needed:

1. I (wake) ___ up at six.
2. She (wake) ___ up at five.
3. They (work) ___ at the office.
4. He (eat) ___ rice for breakfast.
5. We (live) ___ in Chiang Mai.
6. The bot (run) ___ on a local computer.

(Answers: wake, wakes, work, eats, live, runs.)

**Meaning-focused.** The learner produces three sentences about themselves and three about a family member, using present simple:

> *I wake up at seven. My brother wakes up at eight.*

## The Task (18 min) — Build your course folder

The learner sets up the folder structure they'll use for the rest of the course, narrating in English as they go. The bot watches the screen.

```bash
cd ~                              # I'm going to my home folder.
mkdir kru-eng                     # I make a new folder called kru-eng.
cd kru-eng                        # I go into kru-eng.
mkdir week01 week02 homework      # I make three folders inside.
touch journal.md                  # I create a journal file.
ls                                # I list everything I just made.
```

The bot prompts at each command: *what does this command do? say it in English.*

Then the learner writes today's first journal entry. In `journal.md`:

```markdown
# My week

## Week 2 — Tuesday

I wake up at seven. I eat rice for breakfast.
Aey wakes up at six. She works at a coffee shop.
```

Save the file. Run `ls` again. Move the file: `mv journal.md week02/`. List again to confirm.

## Post-task language focus (5 min)

Likely errors:

| Learner says | Recast |
|---|---|
| "She wake up at six." | "She *wakes* up — don't forget the -s for she." |
| "He don't eat rice." (anticipating week 3) | "He *doesn't* eat rice — we'll do this next week, just notice it for now." |
| "I makes coffee." | "*I make* coffee. -s is only for *he*, *she*, *it*." |

## Wrap (4 min)

1. Tell me one thing you do every day in English.
2. What was the hardest English word in today's lesson?
3. What terminal command will you use the most?

## Vocabulary / chunk bank

```
- wake up at ...                 (ตื่นนอนตอน...)               [neutral]
- go to work / go to school      (ไปทำงาน / ไปโรงเรียน)         [neutral]
- eat breakfast / lunch / dinner (กินข้าวเช้า/เที่ยง/เย็น)        [neutral]
- in the morning / afternoon     (ตอนเช้า/บ่าย)                 [neutral]
- make a folder                  (สร้างโฟลเดอร์)                 [tech, reuse w1]
- create a file                  (สร้างไฟล์)                     [tech]
- move a file                    (ย้ายไฟล์)                      [tech]
- delete a file                  (ลบไฟล์)                        [tech]
- go to my home folder           (กลับไป home folder)            [tech]
- list the files                 (ดูรายการไฟล์)                  [tech, reuse w1]
```

## Pronunciation focus — The -s ending

Three sounds for the -s ending in present simple:

- /s/ after voiceless consonants: *walks* /wɔːks/, *makes* /meɪks/, *takes* /teɪks/
- /z/ after voiced consonants and vowels: *runs* /rʌnz/, *opens* /ˈoʊpənz/, *lives* /lɪvz/
- /ɪz/ after sibilants: *watches* /ˈwɒtʃɪz/, *finishes* /ˈfɪnɪʃɪz/, *closes* /ˈkloʊzɪz/

Thai L1 speakers often drop the -s entirely (final-consonant interference, see `pronunciation/thai_l1_interference.md`). The drill: bot says three pairs, learner identifies *with* or *without*.

## Homework

1. **Production (3 min):** write 5 sentences in `week02/routine.md` describing one family member's daily routine. Commit it... actually, that's week 5. Just save for now.
2. **Listening (3 min):** find a 30-second clip of someone describing their morning in English (YouTube, Instagram). Note any 3rd-person -s you hear.
3. **Reuse:** in your routine.md, use *I'm a ...* or *I work at ...* from week 1 somewhere.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task |
| Modeled language | Input |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Communicative production | The Task |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- `lessons/LESSON_TEMPLATE.md`
- `pronunciation/thai_l1_interference.md` — final consonants, -s endings.
- `vocabulary/tech_lexical_chunks.md` — Group A.
