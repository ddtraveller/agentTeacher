---
title: Week 9 — Future and Plans, Python Hello-World
type: lesson
status: live
topic: going to vs will + first Python script
updated: 2026-05-11
week: 9
cefr: A2-B1
duration_min: 60
can_do: I can talk about my plans for next week using going to vs will, and I can run a Python script that produces output.
english_focus: going to (plans), will (predictions and decisions)
tech_focus: installing Python, python -c, writing and running a one-file script
ai_thread: AI predicts the next word; you make future plans — both involve probability, but in very different ways
---

# Week 9 — Future and Plans, Python Hello-World

## Can-do

> I can describe 3 plans I have for next week and 2 predictions about the future, and I can write and run a small Python script that prints text.

## Pre-task (7 min)

The bot asks: *What are you doing this weekend?*

The learner answers however they can. Common A2 attempts:

- *I go to Doi Suthep.* (using present for future — common Thai L1 pattern)
- *I'm going Doi Suthep.* (missing *to*)
- *I will probably home.* (missing verb)

The bot recasts as the target shapes (*I'm going to climb Doi Suthep* / *I'll probably stay home*) without correction, and moves on.

## Input (8 min) — Two short conversations

> **Aey:** What are you doing this Sunday?
> **Tao:** I'm going to visit my parents. They're going to cook a big lunch.
> **Aey:** Nice. What about you, Bee?
> **Bee:** I don't know yet. Maybe I'll just stay home and read. Or I'll go to the market. We'll see.
> **Aey:** Oh — do you want to come with me? I'm going to Doi Suthep on Sunday morning. There's a small ceremony at the temple.
> **Bee:** Hm. OK. I'll come.

Questions:

1. What's Tao doing on Sunday?
2. What was Bee planning when the conversation started?
3. What's Bee doing now?
4. *Noticing:* find every future structure. Some use *going to*, some use *will / 'll*. What's the difference?

## Noticing (6 min) — *going to* vs *will*

**Going to** — for **plans already decided** before now:

> *I'm going to visit my parents.* (planned)
> *They're going to cook lunch.* (decided)
> *I'm going to Doi Suthep on Sunday.* (planned)

**Will / 'll** — for **decisions made right now**, and for **predictions**:

> *OK. I'll come.* (decision just made — in this moment)
> *Maybe I'll just stay home.* (uncertain prediction)
> *The AI will probably get this wrong.* (prediction)

Concept check, under 25 words: "Use *going to* for plans you already made. Use *will* for decisions you make now, or for guesses about the future."

A test:

> *Friend: Do you want pizza or rice for dinner?*
> *You: ___ have pizza.*  → *I'll have pizza.* (decision just made — not *going to*)

> *Mother: What's your weekend like?*
> *You: ___ visit my grandmother on Sunday.*  → *I'm going to visit my grandmother.* (planned, not decided right now)

## Controlled practice (10 min)

**Form-focused.** Going to or will?

1. (decided last week) On Saturday I ___ ___ go to the market. → *am going to*
2. (just now) Phone rings. *Oh — I ___ ___ get it.* → *will / 'll*
3. (prediction) That rain looks heavy. It ___ ___ be a long ride home. → *will*
4. (plan) Next month she ___ ___ visit her sister in Bangkok. → *is going to*
5. (offer) *Don't worry about the dishes. I ___ ___ do them.* → *will / 'll*

**Meaning-focused.** Tell the bot:

- 2 things you're **going to** do this week (already planned).
- 2 things you **'ll probably** do this week (not decided).
- 1 prediction about your own English in 6 months. *"I think I'll be able to ..."*

## The Task (22 min) — First Python script

The learner installs Python (if not yet installed) and writes their first script.

```bash
# Check if Python is installed:
python --version              # or: python3 --version
```

If not installed, the bot guides through the install for the learner's OS. *(Most modern Macs and Linux have it; Windows often needs the Microsoft Store version.)*

**One-liner first:**

```bash
python -c "print('hello, Chiang Mai')"
```

Output: `hello, Chiang Mai`. The bot says:

> *That just ran a Python program. It was one line long. Tomorrow we'll write a longer one.*

Actually now. Create `week09/plan.py`:

```python
# My weekend plan — in Python.

print("Weekend plan:")
print("- On Saturday, I am going to the market.")
print("- On Sunday, I'll probably go to Doi Suthep.")
print("- I am going to study English on both evenings.")
print()
print("Prediction: I will be tired on Monday.")
```

Save. Run:

```bash
python plan.py
```

The bot then asks the learner to **modify** the script — change the plans to match their own real weekend, in English. The bot watches for English errors AND Python errors (missing quotes, missing parentheses) and labels each:

- *That's a Python error — you need a closing quote.*
- *That's an English error — *going to go* sounds awkward; just say *going to the market*.*

Bonus task — make the script ask for input:

```python
name = input("What's your name? ")
print(f"Hi, {name}. What are you going to do this weekend?")
plan = input()
print(f"Cool. I'll remember that. Have fun, {name}.")
```

Run it. The script has a one-turn conversation with the learner.

**Connection to AI:** the bot pauses to point this out:

> *Your script and an AI both produce text. The script always says the same thing — it's predictable. An AI guesses what comes next from a pattern it learned. **Both make predictions**, but yours is exact and the AI's is probabilistic. We'll come back to this in week 11.*

Commit:

```bash
git add week09/plan.py
git commit -m "first python script"
```

## Post-task language focus (5 min)

| Learner says | Recast |
|---|---|
| "I going to market." | "*I'm going to the market* — need *am* and *the*." |
| "I will go to market tomorrow, I decided last week." | "If you decided last week, it's *I'm going to the market tomorrow*. *Will* is for now-decisions." |
| "He will go to come." | "Pick one — *he'll come* OR *he's going to come*. Not both." |

## Wrap (3 min)

1. Tell me one thing you're going to do this week.
2. Tell me one prediction about anything.
3. Did Python feel different from the terminal commands? How?

## Vocabulary / chunk bank

```
- I'm going to + verb              (ฉันจะ + กริยา — แผนล่วงหน้า)         [intro w9]
- I'll + verb                       (ฉันจะ + กริยา — ตัดสินใจตอนนี้)       [intro w9]
- maybe / probably / definitely    (อาจจะ / น่าจะ / แน่นอน)              [hedging, intro w9, reuse w11]
- I think I'll ...                 (คิดว่าจะ...)                          [hedging, intro w9, reuse w12]
- run a script                     (รันสคริปต์ — reuse w1, w2)          [tech]
- write a Python script            (เขียนสคริปต์ Python)                [tech, intro w9]
- print to the screen              (พิมพ์ออกหน้าจอ)                    [tech, intro w9]
- ask for input                    (รับ input)                          [tech, intro w9]
- get a Python error               (เจอ error ของ Python)                [tech, intro w9]
- it predicts the next word        (มันทำนายคำต่อไป)                    [AI, intro w9]
```

## Pronunciation focus — Contractions *'ll* and *'m going to*

In normal speech:

- *I will* → *I'll* /aɪl/
- *I am going to* → *I'm gonna* /aɪm ˈgʌnə/ (in casual speech)
- *I'm going to* /aɪm ˈgoʊɪŋ tə/ (in careful speech)

Both are fine. *Gonna* is **not** sloppy English — it's how natives say it in casual contexts. But don't write *gonna* in formal writing.

Drill — three pairs:
- I will go / I'll go
- I am going to leave / I'm gonna leave
- She will help / she'll help

## Homework

1. **Production (10 min):** modify your `plan.py` to print 5 sentences about next week — 3 going-to plans, 2 will-predictions. Commit it.
2. **Tech (5 min):** write a second tiny Python script — `week09/age_in_dog_years.py` — that asks for the learner's age and prints the age × 7. The bot can help with the math part.
3. **Reuse:** use a frequency adverb (w7 — *usually*, *sometimes*) in one of your prediction sentences.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task |
| Modeled language | Input + Python template in The Task |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Production | The Task |
| Cross-curricular link | Python in The Task |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- `vocabulary/tech_lexical_chunks.md` — Group A (terminal), preview of Group F.
- `lessons/w11_comparing_and_evaluating_ai.md` — the prediction-vs-prediction contrast continues.
