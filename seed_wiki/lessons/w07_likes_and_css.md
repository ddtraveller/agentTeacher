---
title: Week 7 — Habits, Preferences, Style with CSS
type: lesson
status: live
topic: like / love / hate + frequency adverbs + CSS basics
updated: 2026-05-11
week: 7
cefr: A2
duration_min: 60
can_do: I can describe what I like and how often I do things, and I can style my web page with colors, fonts, and spacing.
english_focus: like / love / hate + -ing or noun; frequency adverbs (usually, sometimes, never)
tech_focus: CSS — color, font-size, background, padding; selectors
ai_thread: CSS selectors and prompt filters both narrow down "which thing" — precision is the skill
---

# Week 7 — Habits, Preferences, Style with CSS

## Can-do

> I can describe in 5 sentences what I like and how often I do things, and I can style my `about_me.html` page so it looks like mine, not generic.

## Pre-task (7 min)

The bot asks the learner to look at their `about_me.html` from week 6 in a browser. Then:

> What do you think? Is it pretty?

Probable answer: *Not really. It's plain.* The bot agrees:

> Right. Black text on white background. Every webpage in 1995 looked like this. Today we'll fix that with CSS — and we'll teach some English about *liking* things along the way.

## Input (8 min) — Personal preferences

Read aloud:

> I like coffee. I drink it every morning, usually with milk. I love khao soi. I eat it about once a week, when I'm at the market. I don't like meetings. I have to go to one every Monday morning, and I always sit in the back. I never check email after eight o'clock at night. That's my rule.

Questions:

1. How often does the speaker drink coffee?
2. Does the speaker enjoy meetings?
3. What does the speaker never do after 8pm?
4. *Noticing:* find the words *usually*, *always*, *never*. Where do they go in the sentence?

## Noticing (5 min) — Like / love / hate + frequency adverbs

**Like / love / hate + -ing or noun**:

> *I like **coffee**.* (noun)
> *I like **drinking coffee**.* (-ing form)
> *I love **khao soi**.* (noun)
> *I hate **waiting**.* (-ing form)

After *like / love / hate*, the next word is either a noun or an -ing verb. **Not** the plain verb.

> ✗ *I like drink coffee.*
> ✓ *I like drinking coffee.* / *I like coffee.*

**Frequency adverbs**: *always, usually, often, sometimes, rarely, never*. Position rule, in 12 words:

> Before the main verb. After *to be*.

> *I **usually** drink coffee.* (before main verb)
> *I'm **usually** tired.* (after *to be*)
> *She **never** checks email late.* (before main verb)

## Controlled practice (10 min)

**Form-focused.** Pick the right form:

1. I like (coffee / to coffee / coffees). → *coffee*
2. She loves (run / running / runs) in the morning. → *running*
3. He doesn't like (wait / waiting / waits) for the bus. → *waiting*
4. We hate (the meeting / meeting / to meet) at 8am. → *meeting / the meeting* both ok

**Form-focused, frequency.** Put the adverb in the right place:

1. I (always) wake up at six.  → *I always wake up at six.*
2. She (sometimes) is late.  → *She is sometimes late.*
3. We (never) drink soda.  → *We never drink soda.*
4. They (usually) eat at home.  → *They usually eat at home.*

**Meaning-focused.** Say 5 sentences about yourself using each frequency adverb once: always, usually, sometimes, rarely, never.

## The Task (22 min) — Style your page

The learner adds CSS to the `about_me.html` from week 6. The bot walks through.

Open the file. Inside `<head>`, add a `<style>` block:

```html
<head>
  <title>About Me</title>
  <style>
    body {
      font-family: sans-serif;
      background-color: #fdf6e3;
      color: #333;
      padding: 30px;
      max-width: 700px;
      margin: 40px auto;
    }
    h1 {
      color: #b58900;
    }
    h2 {
      color: #268bd2;
    }
    ul {
      background: #eee8d5;
      padding: 15px 30px;
      border-radius: 8px;
    }
  </style>
</head>
```

The bot narrates each piece, in English, as the learner types:

- *`body` is a **selector** — it says "this style applies to the whole page".*
- *`color` is the text color.*
- *`background-color` is the page background.*
- *`padding` is space inside an element.*
- *`#b58900` is a color code — it's gold.*

Save and refresh the browser. The page now has color, breathing room, a centered narrow column.

Then the learner **customizes**: changes the colors, the font, the padding. The bot prompts them to **say in English** what they're doing:

> *I changed the background to dark blue. I made the h1 white. I removed the padding on the list because I didn't like it.*

This is past-simple production (week 5) reused inside the CSS task.

**A small connection to AI:** the bot says:

> CSS `selectors` (like `h1`, `body`, `ul`) tell the browser **which thing** to style. When you write a prompt to an AI later — week 10 — you'll do the same kind of thing: tell it which thing to focus on. *"Only the summary, not the whole article."* CSS and prompts both need **precision about scope**.

## Post-task language focus (5 min)

| Learner says | Recast |
|---|---|
| "I like to drinking coffee." | "*I like to drink coffee* OR *I like drinking coffee* — pick one form, not both." |
| "I never don't check email." | "*I never check email* — *never* is already negative, don't add *don't*." |
| "She always is late." | "*She is always late* — after *to be*, the adverb comes after." |

## Wrap (3 min)

1. Tell me one thing you always do and one thing you never do.
2. Show me your styled page. What did you change?
3. Why do you think someone might want a webpage to look a certain way?

## Vocabulary / chunk bank

```
- I like / love / hate + -ing       (ฉันชอบ / รัก / เกลียด + กริยา-ing)   [pattern, intro w7]
- I like / love / hate + noun       (ฉันชอบ + คำนาม)                    [pattern, intro w7]
- usually / sometimes / never       (ปกติ / บางครั้ง / ไม่เคย)            [frequency, intro w7]
- I have to ...                     (ฉันต้อง...)                        [obligation, intro w7]
- give it a style                   (ใส่ style)                         [tech, intro w7]
- change the color                  (เปลี่ยนสี)                          [tech, intro w7]
- change the font                   (เปลี่ยนฟอนต์)                      [tech, intro w7]
- a selector                        (selector — ตัวเลือก)                [tech, intro w7]
- add padding                       (เพิ่ม padding / ระยะห่าง)          [tech, intro w7]
- the page looks good now           (หน้าเว็บดูดีขึ้นแล้ว)                [neutral, intro w7]
```

## Pronunciation focus — Frequency adverb stress

Frequency adverbs are **unstressed** in normal speech, even though they're often near the beginning. The verb is stressed.

Drill — say each, stressing the verb (in CAPS):
- I usually DRINK coffee.
- She always WAKES up at six.
- We never EAT after eight.

Thai L1 speakers tend to stress *usually*, *always*, *never* because they "feel important". They don't, in English. Reduce them.

## Homework

1. **Production (5 min):** in `week07/preferences.md`, write 5 sentences about your habits using 5 different frequency adverbs. Commit.
2. **Tech (10 min):** open the `about_me.html` of a friend (or one we look at in class). Try to figure out, by reading the CSS, what each rule does. Send Kru Eng a 3-line note in English describing what you found.
3. **Reuse:** use *there is / there are* (w6) somewhere in your preferences.md to describe your usual coffee setup or breakfast.

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task (look at last week's page) |
| Modeled language | Input + CSS template in The Task |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Production | The Task |
| Cross-curricular link | CSS — selector → AI precision parallel |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- `vocabulary/tech_lexical_chunks.md` — Group B (web, CSS).
- `lessons/w10_prompt_engineering_basics.md` — selectors-as-precision parallel.
