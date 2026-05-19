---
title: Week 11 — Comparison, Evaluating AI Output
type: lesson
status: live
topic: comparatives / superlatives / hedging + spotting AI errors
updated: 2026-05-11
week: 11
cefr: B1
duration_min: 60
can_do: I can compare two AI outputs in English with reasons, and I can identify when an AI answer is probably wrong.
english_focus: comparatives (more / -er / less), superlatives, hedging verbs (seems, might, probably)
tech_focus: ground truth vs generated text; verifying citations; spotting hallucinations
ai_thread: hallucination — what it is, why it happens, when it's cheap and when it's expensive
---

# Week 11 — Comparison, Evaluating AI Output

## Can-do

> I can compare two AI outputs and say which is more accurate, more useful, or more biased, with reasons. I can identify at least two cases where the AI confidently says something wrong, and I can describe each one in 2–3 sentences.

## Pre-task (7 min)

The bot asks the learner to remember week 10's task — iterating prompts. *What was your best version?* The learner answers briefly.

Then the bot pivots:

> Today the question isn't *how to write a prompt* — it's *how to know if the answer is any good*. Sometimes the AI sounds confident but is wrong. We're going to learn how to spot that.

## Input (8 min) — Three sentences, side by side

The bot shows three sentences. Each was produced by an AI asked: *In one sentence, what is Doi Suthep?*

> **Sentence A:** Doi Suthep is a famous mountain temple in Chiang Mai, Thailand, dedicated to Buddhism and known for its golden chedi.
>
> **Sentence B:** Doi Suthep, named after the hermit Vasudeva, is a mountain in Lampang province with a temple founded in the 11th century by King Mengrai.
>
> **Sentence C:** Doi Suthep is a sacred mountain near Chiang Mai. The temple on its summit, Wat Phra That Doi Suthep, was reportedly founded around 1383 according to local tradition.

Questions:

1. Which one is the most confident-sounding?
2. Which one is the most accurate?
3. Which one is the most honest about uncertainty?
4. *Noticing:* what words do the sentences use to **show uncertainty**? Words like *reportedly*, *according to*?

(Reality check: A is broadly right but vague. B is wrong on three counts — wrong province, wrong century, wrong founder. C is right and appropriately hedged. The bot reveals this after the discussion.)

## Noticing (8 min) — Comparatives, superlatives, hedging

**Comparatives** — comparing two things:

> **Short adjective + -er + than**: *bigger than*, *faster than*, *cheaper than*
> **Long adjective: more + adjective + than**: *more accurate than*, *more useful than*, *more confident than*
> **Irregular**: *good → better than*, *bad → worse than*

**Superlatives** — comparing three or more:

> **Short: the + -est**: *the biggest*, *the fastest*
> **Long: the most + adjective**: *the most accurate*, *the most useful*
> **Irregular**: *the best*, *the worst*

**Hedging** — making a claim **less strong**, which is **more honest** when you're not sure:

> *seems / appears* — *Sentence B seems wrong about the dates.*
> *might / may / could* — *The AI might be confusing two temples.*
> *probably / possibly / reportedly* — *Reportedly* / *according to* — gives a source for the uncertainty.
> *I'm not sure, but ...* (reuse from w8)

Concept check, B1 level: which is more honest?

- *The AI is wrong.*
- *The AI is probably wrong about the date.*
- *The AI **seems** wrong about the date, but I'd want to check a source.*

(The third is the most academically honest. The first overclaims.)

## Controlled practice (10 min)

**Form-focused.** Make a comparative or superlative:

1. ChatGPT is ___ ___ Claude. (fast)  → *faster than*
2. Local Ollama is ___ ___ ChatGPT. (slow)  → *slower than*
3. Of the three AIs, this one is ___ ___. (accurate)  → *the most accurate*
4. Sentence C is ___ ___ sentence B. (honest)  → *more honest than*
5. Wikipedia is ___ ___ a random tweet. (reliable)  → *more reliable than*

**Form-focused, hedging.** Rewrite as hedged statements:

1. *The AI is lying.* → *The AI seems wrong here. It might be confabulating.*
2. *Doi Suthep is in Lampang.* → *Reportedly, Doi Suthep is in Lampang.* (← actually false; the hedge doesn't fix wrongness)
3. *The model knows nothing.* → *The model might not have current data on this topic.*

## The Task (22 min) — Audit an AI

The learner chooses one of two jobs.

**Job A — Cultural fact-check.** Ask any AI 10 factual questions about Thailand. Suggested questions:

1. When is Loy Krathong celebrated?
2. What is the population of Chiang Mai?
3. Who founded the Lanna kingdom?
4. What does *khao soi* contain?
5. Which province is Pai in?
6. When was Chiang Mai founded?
7. What is the most-visited temple in Chiang Mai?
8. Who is the current governor of Chiang Mai?
9. What does *sai oua* mean?
10. What language do most people speak in Chiang Mai's old city today?

For each, the learner writes:
- The AI's answer.
- A verification check (Wikipedia, the wiki, a friend who knows).
- A verdict: **confident and right**, **confident but wrong**, **honestly uncertain**, or **refused to answer**.

The learner produces 3 sentences in English, using **comparatives and hedging**:

> *The AI was more accurate on traditional culture than on recent politics. It seems to make up names of current officials. It was honestly uncertain about Lanna history, which is probably the right move.*

**Job B — Cite verification.** Ask any AI: *Give me 5 citations for the history of the Lanna kingdom, with author and year.* Then **verify each citation** — search for the author, the book title, the year. The learner reports how many citations are real, how many are partial (real author, wrong title), and how many are completely invented.

This is a famously cheap way to spot hallucinations: AIs often invent plausible-sounding citations.

Result: a small report in English (4–6 sentences) using comparatives and hedging.

## Kru Eng mentions her own limits

Before the wrap:

> I have to be honest. I sometimes make things up too. I try not to, but I can't always tell when I am. The way to catch me is what you just did — **check the source**. If I cite something, ask me where it's from. If I can't say, I'm probably making it up.

The learner asks the bot one question they expect she'd be wrong on. She gives an answer, then **rates her own confidence** (1–5) before they verify. This is **calibration training** — both for the learner and a little bit for the bot.

## Post-task language focus (5 min)

| Learner says | Recast |
|---|---|
| "ChatGPT is more accurater than Claude." | "*More accurate* OR *more correct*, not both. Pick one." |
| "It's the most accurater." | "*The most accurate* — drop the -er when you use *most*." |
| "It probably wrong." | "*It's probably wrong* — need the *to be*." |

## Wrap (4 min)

1. What's one thing you'll do differently the next time an AI gives you an answer?
2. *Sentence C is more honest than sentence A* — say this in your own words, with reasons.
3. What does *hallucination* mean for an AI?

## Vocabulary / chunk bank

```
- more / less ___ than            (มากกว่า / น้อยกว่า)                  [comparative, intro w11]
- the most / the least            (มากที่สุด / น้อยที่สุด)               [superlative, intro w11]
- better / worse than             (ดีกว่า / แย่กว่า)                    [irregular, intro w11]
- it seems ...                    (ดูเหมือนว่า...)                       [hedge, intro w11]
- it might / may be ...           (มันอาจจะ...)                          [hedge, intro w11, reuse w12]
- probably / possibly             (น่าจะ / เป็นไปได้)                     [hedge, intro w11]
- reportedly / according to       (รายงานว่า / ตามที่...)                  [hedge with source, intro w11]
- verify a citation               (ตรวจสอบการอ้างอิง)                    [tech, intro w11]
- spot a hallucination            (จับคำตอบที่กุขึ้น)                      [AI, intro w11]
- ground truth                    (ความจริงตามข้อมูล)                    [AI, intro w11]
- confidence vs accuracy          (ความมั่นใจ vs ความถูกต้อง)             [AI/meta, intro w11]
- I'd want to check ...           (อยากเช็ค...)                          [hedge, intro w11, reuse w12]
```

## Pronunciation focus — Stress on the comparative

In *Sentence C is more **AC**-curate than Sentence A*, the stress falls on the **adjective**, not on *more*. *More* is a function word and reduces.

Drill — three times, stressing the adjective:
- more AC-curate
- more US-eful
- the most HON-est

Thai L1 speakers often stress *more* and *most* — they sound like emphasis words. They aren't; they're grammatical. Reduce them.

## Homework

1. **Production (10 min):** in `week11/audit.md`, write a 5-sentence report of Job A or Job B from the lesson. Use at least 3 comparatives and 3 hedging structures. Commit.
2. **Reuse:** include one *if-then* sentence (w10 first conditional) in your audit. *"If I had used a more specific prompt, the AI would probably have ..."*
3. **Prep for next week:** read the headline of one AI-related news story this week. Bring it to week 12 — we'll use it.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task |
| Modeled language | Input (three sentences) |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Production | The Task |
| Critical thinking | The Task + Kru Eng's own-limits section |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- *[ref:Ji et al 2023]* — survey on hallucination in NLG; the cheap-to-spot vs expensive-to-spot distinction.
- `lessons/w08_what_is_ai_and_what_can_it_do.md` — capability framing for *can / can't* and *makes things up*.
- `lessons/w10_prompt_engineering_basics.md` — first conditional reused in homework.
- `vocabulary/tech_lexical_chunks.md` — Group F (evaluation).
