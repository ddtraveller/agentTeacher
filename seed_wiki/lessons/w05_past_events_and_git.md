---
title: Week 5 — Past Events, Git Basics
type: lesson
status: live
topic: simple past + version control with git
updated: 2026-05-11
week: 5
cefr: A2
duration_min: 60
can_do: I can talk about 3–5 things I did yesterday, and I can save my work as commits in git.
english_focus: simple past (regular -ed + high-frequency irregulars)
tech_focus: git init, git add, git commit -m, git log, git diff
ai_thread: AI doesn't remember between conversations; git remembers between commits — why the asymmetry?
---

# Week 5 — Past Events, Git Basics

## Can-do

> I can describe 3–5 things that happened yesterday using simple past, and I can save my work into a git repository with meaningful commit messages.

## Pre-task (8 min)

The bot asks one question: *What did you do yesterday?*

The learner tries. Common output at A1/A2: *I go to market.* (present, missing past)  /  *Yesterday I eat rice.* The bot recasts as full past simple, naturally, without explicit correction yet.

> Bot: *Ah, you went to the market and ate rice. What did you buy at the market?*

The recast does three things at once: switches to past, models the irregular forms (*went, ate*), and pushes for more language with a follow-up.

## Input (10 min) — A short story

Read aloud:

> Yesterday Tao woke up late. He looked at his phone — eight-fifteen. He had a class at nine. He got dressed, grabbed his laptop, and ran out the door. He didn't eat breakfast. On the way to school, he stopped at the 7-Eleven and bought a coffee and a sausage. The class was already started when he arrived. His teacher saw him, smiled, and said nothing. After class, Tao went to the library and finished the homework he should have done the night before.

Questions:

1. Why was Tao in a hurry?
2. What did he eat for breakfast?
3. What did the teacher do when he arrived?
4. *Noticing:* find five past-simple verbs in the story. Which ones end in -ed, and which ones don't?

## Noticing (5 min) — Simple past

Two shapes:

**Regular verbs**: add **-ed**.

> *walk → walked, look → looked, stop → stopped, finish → finished*

**Irregular verbs**: completely different forms. Memorize the common ones.

> *go → went, eat → ate, see → saw, have → had, do → did, run → ran, buy → bought, get → got, make → made, take → took, come → came, say → said*

The shape for negative and questions uses **did + not + base verb** and **did + subject + base verb**:

> *He **didn't eat** breakfast.* (not *didn't ate*)
> ***Did he eat** breakfast?* (not *did he ate*)

Concept check, under 20 words: "After *did* and *didn't*, the verb is plain. The past form is already inside *did*."

## Controlled practice (10 min)

**Form-focused.** Put the verb in simple past:

1. Yesterday I (go) ___ to Doi Suthep.
2. She (not / eat) ___ breakfast.
3. (you / see) ___ that movie?
4. We (buy) ___ coffee at the market.
5. He (run) ___ to school because he (be) ___ late.

(Answers: went, didn't eat, did you see, bought, ran / was.)

**Meaning-focused.** True for you yesterday? Yes / No, then expand:

- *Did you wake up before seven?*
- *Did you eat rice?*
- *Did you call someone?*
- *Did you watch any video?*

For each *yes*, add one detail: *Yes, I woke up at six. Yes, I ate rice with my mother.*

## The Task (20 min) — Git your journal

The learner turns their `kru-eng/` folder into a real git repository and records yesterday in commits.

```bash
cd ~/kru-eng
git init                            # I initialized a git repository.
git status                          # I checked the status.
git add week02/routine.md week03/place.md
git status                          # Now those files are staged.
git commit -m "weeks 2 and 3"       # I made my first commit.
git log                             # I checked the history.
```

The bot narrates each command in English, in **past tense after the command runs**:

> *You just **initialized** a git repository.*
> *You **added** two files.*
> *You **made** your first commit.*

Then the learner writes a new journal entry in `week05/yesterday.md` describing 3–5 things they did yesterday, **using simple past**. Save. Commit:

```bash
git add week05/yesterday.md
git commit -m "yesterday journal"
```

Finally, the learner reads aloud their journal entry, narrating in English, and checks `git log` to see both commits in sequence.

If time permits, a small bonus: the learner edits `yesterday.md`, then runs `git diff` to see exactly what changed. The bot points out: *git remembers everything you change. The AI doesn't remember our conversations the same way. Why?* Hold the question for week 8.

## Post-task language focus (5 min)

| Learner says | Recast |
|---|---|
| "I go to market yesterday." | "*I went* to the market yesterday — *go* becomes *went* in past." |
| "Did you ate breakfast?" | "*Did you eat* — after *did*, the verb is plain." |
| "I don't went there." | "*I didn't go* there — *didn't* + base verb." |
| "He runned to school." | "*He ran* to school. *Run* is irregular — *run / ran / run*." |

## Wrap (3 min)

1. Tell me one thing you did yesterday — in English, past tense.
2. What was the trickiest verb today?
3. Does git remember things the way you do? How is it different?

## Vocabulary / chunk bank

```
- went / had / saw / did / made   (ไป / มี / เห็น / ทำ / ทำ-สร้าง)   [irregular past, intro w5]
- bought / got / took / came      (ซื้อ / ได้ / เอา / มา)             [irregular past, intro w5]
- yesterday / last week / last night (เมื่อวาน / สัปดาห์ที่แล้ว / เมื่อคืน) [time, intro w5]
- I didn't ...                    (ฉันไม่ได้...)                      [negative past, intro w5]
- check the status                (เช็ค status)                       [tech, intro w5]
- stage the changes               (stage การเปลี่ยนแปลง)              [tech, intro w5]
- make a commit                   (commit / บันทึก)                    [tech, intro w5, reuse w9, w12]
- check the log                   (ดู log)                            [tech, intro w5]
- see what changed                (ดูว่าอะไรเปลี่ยน)                   [tech, intro w5]
```

## Pronunciation focus — The -ed ending

Three sounds for -ed in regular past:

- /t/ after voiceless: *walked* /wɔːkt/, *stopped* /stɒpt/, *finished* /ˈfɪnɪʃt/
- /d/ after voiced: *opened* /ˈoʊpənd/, *called* /kɔːld/, *cleaned* /kliːnd/
- /ɪd/ after /t/ or /d/: *waited* /ˈweɪtɪd/, *needed* /ˈniːdɪd/, *started* /ˈstɑːrtɪd/

Common Thai L1 issue: the /t/ and /d/ endings are dropped entirely → *walk* and *walked* sound identical. This is one of the **highest priority** errors because it removes the past marker.

Drill: minimal pairs. Bot says *walk / walked / walk / walked.* Learner identifies which is past.

## Homework

1. **Production (5 min):** write 5 sentences about last weekend in `week05/weekend.md`. Use at least 3 irregular past verbs. Commit it with `git add` and `git commit -m "weekend journal"`.
2. **Listening (3 min):** find a short video where someone tells a story. Count how many past verbs you hear.
3. **Reuse:** use one Wh-question (w4) in your weekend.md — write a question to your future self about what you'll remember from this weekend.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task |
| Modeled language | Input (story) |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Production | The Task |
| Cross-curricular link | Git in The Task |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- `vocabulary/tech_lexical_chunks.md` — Group C (git).
- `pronunciation/thai_l1_interference.md` — final consonants on -ed.
