---
title: Week 6 — Describing Spaces, HTML Structure
type: lesson
status: live
topic: prepositions of place + there is/are + HTML basics
updated: 2026-05-11
week: 6
cefr: A2
duration_min: 60
can_do: I can describe a place using prepositions, and I can write a basic HTML page with headings, paragraphs, and a list.
english_focus: prepositions of place, there is / there are
tech_focus: HTML — html, head, body, h1, p, ul, li
ai_thread: HTML tells the browser what things are; prompts tell the AI what to do — both are instructions for non-humans
---

# Week 6 — Describing Spaces, HTML Structure

## Can-do

> I can describe a place in 5–7 sentences using *there is*, *there are*, and prepositions of place. I can write an HTML page that opens in a browser with a heading, three paragraphs, and a list.

## Pre-task (8 min)

The bot asks the learner to describe their room or workspace, right now, in English. Whatever comes out is fine. Common output:

> Learner: *Have a desk. On the desk computer. Behind the desk a window.*

The bot recasts into the target structure:

> *Ah — there's a desk, with a computer on it, and there's a window behind the desk.*

The learner notices the recast has different shape. That's the teaching moment.

## Input (8 min) — A room

Read aloud:

> My grandmother's house has one main room. On the left, there is a small kitchen with a gas stove and an old refrigerator. In the middle, there is a wooden table with four chairs. On the table, there's a teapot and a bowl of fruit. On the right, there's a doorway to the bedroom. There are two windows: one above the kitchen and one next to the doorway. Outside, behind the house, there is a small garden with lemongrass and chillies.

Questions:

1. How many windows are there?
2. What's on the table?
3. Where is the garden?
4. *Noticing:* the writer uses *there is* and *there are*. When does each one appear?

## Noticing (6 min) — *There is / there are*, prepositions

**There is** (singular) / **There are** (plural):

> *There is a window.* / *There **are** two windows.*
> *There's a chair.* / *There **are** four chairs.*

Note the contraction: *there's*. We don't usually say *there're*.

**Prepositions of place** — the locator words:

> on, in, under, behind, in front of, above, below, next to, between, on the left, on the right, in the middle, outside, inside

Concept check: *There are a chair in the room.* — wrong or right? (Wrong. *Chair* is singular, so *there is a chair*. *There are* needs a plural.)

## Controlled practice (8 min)

**Form-focused.** *There is* or *there are*?

1. ___ a table in the middle.
2. ___ four chairs around the table.
3. ___ two cats on the bed.
4. ___ a notebook and a pen on the desk. *(careful — a notebook **and** a pen, plural)*

(Answers: there is, there are, there are, there are.)

**Meaning-focused.** Describe the room you're in right now, in 4 sentences. Use *there is / there are* twice each and at least 3 different prepositions.

## The Task (22 min) — Write your *about me* page

This is a substantial task. The learner builds their first HTML file.

In `~/kru-eng/week06/`:

```bash
cd ~/kru-eng
mkdir -p week06
cd week06
touch about_me.html
code about_me.html      # or: nano about_me.html
```

The bot walks through the structure, line by line:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>About Me</title>
  </head>
  <body>
    <h1>About Me</h1>

    <p>Hello. My name is <YOUR NAME>. I am from <YOUR PLACE>. I live in Chiang Mai.</p>

    <p>I am learning English and a little bit of technology. Right now, there are five other students in my class. There is one teacher, and her name is Kru Eng.</p>

    <p>In my room, there is a desk, a chair, and a small bed. There are two windows behind the desk.</p>

    <h2>Three things I like</h2>
    <ul>
      <li>khao soi</li>
      <li>the morning market</li>
      <li>this lesson</li>
    </ul>
  </body>
</html>
```

The learner fills in their own content. The bot narrates each tag in English:

- *`<h1>` is a **heading** — the biggest title on the page.*
- *`<p>` is a **paragraph** — a block of text.*
- *`<ul>` is an **unordered list** — like bullet points.*
- *`<li>` is a **list item** — one bullet.*

Save the file. Then **open it in a browser**:

- Mac: `open about_me.html`
- Linux: `xdg-open about_me.html`
- Windows: `start about_me.html`
- Or just double-click it in the file manager.

The learner sees their first webpage. Live. In a real browser. The bot says:

> *This file is on your computer, not on the internet yet. Anyone with this file can see what you wrote. The browser **read** your HTML and **drew** the page.*

## Post-task language focus (5 min)

| Learner says | Recast |
|---|---|
| "There are a table." | "*There is a table* — singular." |
| "Have a window behind the desk." | "*There's a window* behind the desk. We don't usually say *have* for places." |
| "On left there is a kitchen." | "*On **the** left* — keep the *the*." |

## Wrap (3 min)

1. Open your `about_me.html` in the browser. Read one sentence aloud.
2. What's one HTML tag you remember?
3. What surprised you about how a webpage works?

## Vocabulary / chunk bank

```
- there is / there's              (มี — เอกพจน์)                    [intro w6]
- there are                       (มี — พหูพจน์)                     [intro w6]
- on the left / on the right      (ทางซ้าย / ทางขวา)                [position, intro w6]
- in the middle                   (ตรงกลาง)                         [position]
- in front of / behind            (ด้านหน้า / ด้านหลัง — reuse w3)    [position]
- next to / between               (ข้าง / ระหว่าง)                   [position]
- write a heading                 (เขียนหัวข้อ)                      [tech, intro w6]
- add a paragraph                 (เพิ่มย่อหน้า)                      [tech, intro w6]
- open it in a browser            (เปิดในเบราว์เซอร์)                [tech, intro w6]
- the browser drew the page       (browser วาดหน้านี้)                [tech, intro w6, vivid]
```

## Pronunciation focus — Schwa in unstressed words

In *there is a table*, the function words *is* and *a* are unstressed and reduce to schwa:

> /ðɛrz ə ˈteɪbəl/  ← *there's a table*, in normal speech

Thai L1 speakers tend to give *is* and *a* full vowels: */ˈðɛr ɪs ʔeɪ ˈtʰeɪpʰʊː/*. This sounds careful but unnatural. Reduce.

Drill — three times, faster each:
- there's a table → there's a table → there'zə table
- on a chair → on a chair → on'a chair
- it's a book → it's a book → it'sa book

## Homework

1. **Production (10 min):** add two more sections to your `about_me.html`: a section about one place you love, and a section about your weekly schedule. Use at least 3 *there is/there are* sentences. Commit with git.
2. **Listening (3 min):** view source on any small webpage you like (right-click → "View page source"). Find one `<h1>` and one `<p>` you didn't write.
3. **Reuse:** in your *about me* page, use a Wh-question (w4) addressed to the reader. *"What do you do in Chiang Mai?"*

## DSS-OTP mapping

| DSS observable | Section |
|---|---|
| Clear lesson aim | Can-do |
| Activation | Pre-task |
| Modeled language | Input + HTML template in The Task |
| Concept-checking | Noticing |
| Controlled practice | Controlled practice |
| Production | The Task |
| Cross-curricular link | HTML in The Task |
| Error correction | Post-task |
| Reflection | Wrap |

## References

- `vocabulary/tech_lexical_chunks.md` — Group B (web).
- `pronunciation/thai_l1_interference.md` — schwa avoidance.
