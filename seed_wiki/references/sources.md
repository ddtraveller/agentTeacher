---
title: Sources — Bibliography of [ref:...] Citations
type: reference
status: live
topic: full citations for every [ref:short_name] used in the wiki
updated: 2026-05-11
---

# Sources

Every `[ref:short_name]` citation across the wiki resolves here. Entries are alphabetical by short name. Each has:

- Full citation
- **Topic tag** — what area of the literature it speaks to
- **Why cited** — the wiki claims that depend on it
- **Used in** — the pages that link to it

When a claim has multiple ref keys (`[ref:Krashen 1985, Swain 1985]`), each resolves independently.

## How `[ref:...]` keys are constructed

- **Author + year** for journal articles and books — `[ref:Lewis 1993]`, `[ref:Kohnke et al. 2023]`.
- **Institution + year** for standards documents — `[ref:CEFR Companion Volume 2020]`.
- **Author + page-style suffix** for specific within-source claims — `[ref:CEFR can-do A2]`, `[ref:CEFR B1 can-do]` both point to the same CEFR Companion Volume entry below.
- Hyphens, ampersands, and accents are stripped from the key (so *García* in the citation, *Garcia* in the key would also resolve — but as a project convention we keep the accent).

## Index by topic

- **TEFL methodology** — Ellis 2003, Willis & Willis 2007, Long 2015, Harmer 2007, DeKeyser 2007
- **SLA theory** — Krashen 1985, Swain 1985, Long 1996, Vygotsky 1978, Walqui 2006, Hymes 1972, Savignon 1991
- **Lexical approach** — Lewis 1993, Wray 2002
- **Cognitive science of learning** — Cepeda 2008, Karpicke & Roediger 2008, Roediger & Karpicke 2006
- **Error correction** — Truscott 1996, Ferris 2004
- **Translanguaging / bilingualism** — García & Wei 2014, Cenoz & Gorter 2021
- **CALL & AI-mediated learning** — Chapelle 2001, Kohnke et al. 2023, Godwin-Jones 2024
- **Standards** — CEFR Companion Volume 2020
- **Formative assessment** — Wiliam 2011, Truscott 1996, Ferris 2004
- **Critical AI literature** — Bender et al. 2021, Crawford 2021, Eubanks 2018
- **AI/NLP technical** — Reynolds & McDonell 2021, Ji et al. 2023
- **Thai linguistics & pronunciation** — Smyth 2002, Walker 2010
- **Tool docs** — NotebookLM docs
- **Tech industry news 2026** — HN Zero discussion 2026, MarkTechPost Zero 2026, TechTimes Zero compiler 2026, TheStack Zero 2026, Vercel Zero launch 2026

## Entries

### Bender et al. 2021
Bender, E.M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? 🦜 *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (FAccT '21), 610–623. https://doi.org/10.1145/3442188.3445922
**Topic:** Critical AI literature.
**Why cited:** Origin of the "stochastic parrot" framing — language models pattern-complete fluent text without grounded understanding. Source for "the AI makes things up" pedagogy.
**Used in:** lessons/w08, lessons/w12.

### CEFR Companion Volume 2020
Council of Europe (2020). *Common European Framework of Reference for Languages: Learning, Teaching, Assessment — Companion Volume.* Strasbourg: Council of Europe Publishing. https://rm.coe.int/common-european-framework-of-reference-for-languages-learning-teaching/16809ea0d4
**Topic:** Standards. Also resolves: `[ref:CEFR 2020]`, `[ref:CEFR can-do A2]`, `[ref:CEFR B1 can-do]`.
**Why cited:** Source for can-do descriptors that anchor each lesson's `can_do` frontmatter and the syllabus' A1→B1 trajectory. Also the basis for using can-do statements as the assessment scale.
**Used in:** curriculum/syllabus_12week.md, lessons/w08, lessons/w12, references/teaching_methods.md.

### Cenoz & Gorter 2021
Cenoz, J. & Gorter, D. (2021). *Pedagogical Translanguaging.* Cambridge: Cambridge University Press.
**Topic:** Translanguaging / bilingualism.
**Why cited:** Argument for *pedagogical* (planned, principled) translanguaging in formal classrooms — the basis for Kru Eng's "strategic Thai" policy rather than English-only purism.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### Cepeda 2008
Cepeda, N.J., Vul, E., Rohrer, D., Wixted, J.T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science*, 19(11), 1095–1102. https://doi.org/10.1111/j.1467-9280.2008.02209.x
**Topic:** Cognitive science of learning. Also resolves: `[ref:Cepeda et al. 2008]`.
**Why cited:** Empirical basis for the spaced-retrieval schedule (day 1/2/7/21/60) the bot uses for vocab and chunks.
**Used in:** school/about_kru_eng.md, vocabulary/tech_lexical_chunks.md, references/teaching_methods.md.

### Chapelle 2001
Chapelle, C.A. (2001). *Computer Applications in Second Language Acquisition.* Cambridge: Cambridge University Press.
**Topic:** CALL (Computer-Assisted Language Learning).
**Why cited:** Foundational treatment of how computers participate in SLA — predates the AI-mediated framing and informs Kru Eng's design as a CALL system with an AI in the loop.
**Used in:** references/teaching_methods.md.

### Crawford 2021
Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence.* New Haven: Yale University Press.
**Topic:** Critical AI literature.
**Why cited:** Environmental and labor costs of AI — input for the week 12 ethics discussion (electricity, data extraction, the "cost" line in Kru Eng's self-critique).
**Used in:** lessons/w12.

### DeKeyser 2007
DeKeyser, R. (ed.) (2007). *Practice in a Second Language: Perspectives from Applied Linguistics and Cognitive Psychology.* Cambridge: Cambridge University Press.
**Topic:** TEFL methodology / SLA.
**Why cited:** Why examples-before-rules works: the brain attaches abstract rules to concrete instances, not the reverse. Anchors the LESSON_TEMPLATE's Noticing-after-Input sequence.
**Used in:** lessons/LESSON_TEMPLATE.md.

### Ellis 2003
Ellis, R. (2003). *Task-based Language Learning and Teaching.* Oxford: Oxford University Press.
**Topic:** TEFL methodology / TBLT.
**Why cited:** The canonical TBLT reference. Source for "the task drives the form" and the critique of PPP's form-before-meaning sequence.
**Used in:** school/about_kru_eng.md, curriculum/syllabus_12week.md, lessons/LESSON_TEMPLATE.md, lessons/w01, references/teaching_methods.md.

### Eubanks 2018
Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor.* New York: St. Martin's Press.
**Topic:** Critical AI literature.
**Why cited:** The biased-attendance-camera pattern in week 12's pre-task story is the *kind* of case Eubanks documents — automated systems amplifying existing inequity. Source for the framing that bias is a structural, not just technical, problem.
**Used in:** lessons/w12.

### Ferris 2004
Ferris, D.R. (2004). The "grammar correction" debate in L2 writing: Where are we, and where do we go from here? (and what do we do in the meantime…?) *Journal of Second Language Writing*, 13(1), 49–62. https://doi.org/10.1016/j.jslw.2004.04.005
**Topic:** Error correction. Counter to Truscott 1996.
**Why cited:** The nuanced rebuttal to Truscott — *selective, focused* feedback works; comprehensive correction does not. Basis for the bot's "one error per turn" recast policy.
**Used in:** assessment/formative_techniques.md.

### García & Wei 2014
García, O. & Wei, L. (2014). *Translanguaging: Language, Bilingualism and Education.* London: Palgrave Macmillan.
**Topic:** Translanguaging / bilingualism.
**Why cited:** Theoretical foundation for treating Thai + English as a single bilingual repertoire rather than two separate "tools" — Kru Eng's persona policy on when to use Thai.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### Godwin-Jones 2024
Godwin-Jones, R. (2024). Distributed agency in second language learning and teaching through generative AI. *Language Learning & Technology*, 28(2), 5–31.
**Topic:** AI-mediated language learning.
**Why cited:** Current-decade framing of how learner / teacher / AI share agency in a language-learning task. Informs Kru Eng's role-shift from teacher → pair-programmer in the post-W12 Track A.
**Used in:** references/teaching_methods.md.

### HN Zero discussion 2026
Hacker News (2026, May). *Discussion thread: "Zero — a programming language for AI agents (vercel-labs)".* Most-upvoted critique replies argue that contemporary LLMs already parse human-readable compiler errors adequately and that agentic code failures are dominated by planning/context limits, not by error-message parsing.
**Topic:** Tech industry news / critical reception of Vercel Zero.
**Why cited:** Source for the "the premise is contested" framing in `references/vercel_zero_explainer.md`. Use whenever a learner asks whether Zero will succeed.
**Used in:** references/vercel_zero_explainer.md.

### Harmer 2007
Harmer, J. (2007). *The Practice of English Language Teaching* (4th ed.). Harlow: Pearson Longman.
**Topic:** TEFL methodology.
**Why cited:** Source for the **ESA cyclical** (Engage → Study → Activate) alternative to PPP — one of the precedents for the LESSON_TEMPLATE's task-cycle shape.
**Used in:** references/teaching_methods.md.

### Hymes 1972
Hymes, D. (1972). On communicative competence. In Pride, J.B. & Holmes, J. (eds.), *Sociolinguistics: Selected Readings* (pp. 269–293). Harmondsworth: Penguin.
**Topic:** SLA theory / CLT origins.
**Why cited:** Origin of *communicative competence* — the principle that knowing a language means knowing how to use it appropriately, not just knowing its grammar. Anchors Kru Eng's "form serves function" stance.
**Used in:** references/teaching_methods.md.

### Ji et al. 2023
Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y.J., Madotto, A., & Fung, P. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), 1–38. https://doi.org/10.1145/3571730
**Topic:** AI/NLP technical.
**Why cited:** Taxonomy of hallucination types and the cheap-to-spot-vs-expensive-to-spot distinction the W11 task exploits (fact-checking is cheap; bias is expensive).
**Used in:** lessons/w11.

### Karpicke & Roediger 2008
Karpicke, J.D. & Roediger, H.L. (2008). The critical importance of retrieval for learning. *Science*, 319(5865), 966–968. https://doi.org/10.1126/science.1152408
**Topic:** Cognitive science of learning.
**Why cited:** Retrieval *practice* — not just exposure — drives durable learning. Justifies why Kru Eng's homework is production-heavy, not review-heavy.
**Used in:** references/teaching_methods.md.

### Kohnke et al. 2023
Kohnke, L., Moorhouse, B.L., & Zou, D. (2023). ChatGPT for language teaching and learning. *RELC Journal*, 54(2), 537–550. https://doi.org/10.1177/00336882231162868
**Topic:** AI-mediated language learning.
**Why cited:** Current-state review of how generative AI fits into language pedagogy — distinguishes AI-as-tool, AI-as-conversation-partner, and AI-as-object-of-study, the three roles Kru Eng plays.
**Used in:** references/teaching_methods.md.

### Krashen 1985
Krashen, S. (1985). *The Input Hypothesis: Issues and Implications.* London: Longman.
**Topic:** SLA theory.
**Why cited:** Source of comprehensible input (i+1) and the natural order hypothesis. The first half of Kru Eng's input + output ratio.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### Lewis 1993
Lewis, M. (1993). *The Lexical Approach: The State of ELT and a Way Forward.* Hove: Language Teaching Publications.
**Topic:** Lexical approach.
**Why cited:** The foundational lexical-approach text. Justifies teaching chunks (*open the terminal*, *make a commit*) rather than isolated words. Direct basis for vocabulary/tech_lexical_chunks.md.
**Used in:** school/about_kru_eng.md, vocabulary/tech_lexical_chunks.md, lessons/LESSON_TEMPLATE.md, lessons/w01, lessons/w10, references/teaching_methods.md.

### Long 1996
Long, M.H. (1996). The role of the linguistic environment in second language acquisition. In Ritchie, W.C. & Bhatia, T.K. (eds.), *Handbook of Second Language Acquisition* (pp. 413–468). San Diego: Academic Press.
**Topic:** SLA theory.
**Why cited:** Source of the **interaction hypothesis** — meaning negotiation in conversation drives acquisition. Counters PPP's implicit one-way (teacher → learner) flow.
**Used in:** references/teaching_methods.md.

### Long 2015
Long, M.H. (2015). *Second Language Acquisition and Task-Based Language Teaching.* Chichester: Wiley-Blackwell.
**Topic:** TEFL methodology / TBLT.
**Why cited:** The mature statement of TBLT as a research-grounded program. Used together with Ellis 2003 and Willis & Willis 2007 as the TBLT triumvirate.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### MarkTechPost Zero 2026
MarkTechPost (2026, May 15). *Vercel Labs introduces Zero, a systems programming language designed so AI agents can read, repair, and ship native programs.* https://www.marktechpost.com/
**Topic:** Tech industry news / Vercel Zero launch coverage.
**Why cited:** Source for the structured-JSON compiler output framing and the "no GC / no implicit async / no globals" design rationale in `references/vercel_zero_explainer.md`.
**Used in:** references/vercel_zero_explainer.md.

### NotebookLM docs
Google. *NotebookLM Help and Documentation.* https://notebooklm.google.com — accessed 2026-05-11.
**Topic:** Tool docs.
**Why cited:** Operational reference for the day-zero asset-generation pass.
**Used in:** references/notebooklm_bootstrap.md.

### Reynolds & McDonell 2021
Reynolds, L. & McDonell, K. (2021). Prompt programming for large language models: Beyond the few-shot paradigm. *Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems.* https://doi.org/10.1145/3411763.3451760
**Topic:** AI/NLP technical / prompt engineering.
**Why cited:** Early systematic treatment of prompt-as-program — role, context, format, examples. Anchors the four-part prompt pattern taught in W10.
**Used in:** lessons/w10.

### Roediger & Karpicke 2006
Roediger, H.L. & Karpicke, J.D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
**Topic:** Cognitive science of learning.
**Why cited:** Original "testing effect" demonstration — *being* tested causes more learning than re-reading. Indirectly justifies the formative-check-heavy assessment design.
**Used in:** references/teaching_methods.md.

### Savignon 1991
Savignon, S.J. (1991). Communicative language teaching: State of the art. *TESOL Quarterly*, 25(2), 261–277. https://doi.org/10.2307/3587463
**Topic:** SLA theory / CLT.
**Why cited:** Useful retrospective on CLT's first wave — what worked, what didn't. Informs Kru Eng's CLT-flavoured but not CLT-pure stance.
**Used in:** references/teaching_methods.md.

### Smyth 2002
Smyth, D. (2002). *Thai: An Essential Grammar.* London: Routledge.
**Topic:** Thai linguistics.
**Why cited:** Reference for the Thai sound and grammar systems whose mismatches drive `pronunciation/thai_l1_interference.md` (final consonants, cluster handling, tone vs stress).
**Used in:** pronunciation/thai_l1_interference.md.

### Swain 1985
Swain, M. (1985). Communicative competence: Some roles of comprehensible input and comprehensible output in its development. In Gass, S.M. & Madden, C.G. (eds.), *Input in Second Language Acquisition* (pp. 235–253). Rowley, MA: Newbury House.
**Topic:** SLA theory.
**Why cited:** Origin of the **output hypothesis** — input alone is insufficient; learners need to be pushed to produce. The second half of Kru Eng's input + output ratio.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### TechTimes Zero compiler 2026
Tech Times (2026, May). *Vercel Labs' Zero compiler speaks JSON to AI agents.* https://www.techtimes.com/
**Topic:** Tech industry news / Vercel Zero compiler architecture.
**Why cited:** Source for the v0.1.1 maturity caveats (no package registry, no stable compiler spec, borrow checker immature) in `references/vercel_zero_explainer.md`. Also the "Vercel Labs describes Zero as an experiment, not a production dependency" framing.
**Used in:** references/vercel_zero_explainer.md.

### TheStack Zero 2026
The Stack (2026, May). *Vercel soft-launches machine-friendly language Zero.* https://www.thestack.technology/
**Topic:** Tech industry news / Vercel Zero launch traction.
**Why cited:** Source for the May 15 2026 launch date, the "~900 GitHub stars in 24 hours" traction figure, and the deliberate timing on the eve of Google I/O 2026 in `references/vercel_zero_explainer.md`.
**Used in:** references/vercel_zero_explainer.md.

### Truscott 1996
Truscott, J. (1996). The case against grammar correction in L2 writing classes. *Language Learning*, 46(2), 327–369. https://doi.org/10.1111/j.1467-1770.1996.tb01238.x
**Topic:** Error correction.
**Why cited:** The radical case that comprehensive grammar correction is at best useless and at worst harmful. Read together with Ferris 2004 as the rationale for selective, not comprehensive, feedback.
**Used in:** assessment/formative_techniques.md.

### Vercel Zero launch 2026
Vercel Labs (2026, May 15). *Zero (zerolang) — a programming language for agents.* GitHub: https://github.com/vercel-labs/zerolang. Apache-2.0 licence. Authors: Chris Tate, Matt Van Horn.
**Topic:** Tech industry news / Vercel Zero primary source.
**Why cited:** The canonical primary source for any factual claim about Zero (launch date, authorship, licence, capability-based I/O design, structured compiler output). Resolves the assertion that capability-based I/O is older than the marketing implies (cited Haskell as a forty-year-old precedent).
**Used in:** references/vercel_zero_explainer.md.

### Vygotsky 1978
Vygotsky, L.S. (1978). *Mind in Society: The Development of Higher Psychological Processes* (ed. M. Cole, V. John-Steiner, S. Scribner, & E. Souberman). Cambridge, MA: Harvard University Press.
**Topic:** SLA theory / sociocultural.
**Why cited:** Origin of the **zone of proximal development** (ZPD) — the basis for Kru Eng's *modeled → guided → independent* scaffolding gradient.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### Walker 2010
Walker, R. (2010). *Teaching the Pronunciation of English as a Lingua Franca.* Oxford: Oxford University Press.
**Topic:** Pronunciation pedagogy.
**Why cited:** What to fix and what to leave alone in non-native English. Source for the *priority* rankings (high / medium / low) in pronunciation/thai_l1_interference.md.
**Used in:** pronunciation/thai_l1_interference.md.

### Walqui 2006
Walqui, A. (2006). Scaffolding instruction for English language learners: A conceptual framework. *International Journal of Bilingual Education and Bilingualism*, 9(2), 159–180. https://doi.org/10.1080/13670050608668639
**Topic:** SLA theory / scaffolding.
**Why cited:** A practical taxonomy of scaffolding moves — bridging, contextualizing, modeling, schema-building, re-presenting, developing metacognition. The taxonomy the bot uses to choose between recast / elicit / focused mini-explanation.
**Used in:** school/about_kru_eng.md, references/teaching_methods.md.

### Wiliam 2011
Wiliam, D. (2011). *Embedded Formative Assessment.* Bloomington, IN: Solution Tree Press.
**Topic:** Formative assessment.
**Why cited:** Practical handbook for formative-assessment techniques in real classrooms. Source for several of the techniques in `assessment/formative_techniques.md` (exit ticket, CCQ, listen-and-do).
**Used in:** assessment/formative_techniques.md *(implicit; not yet using the [ref:] marker — to be added in a future pass)*.

### Willis & Willis 2007
Willis, D. & Willis, J. (2007). *Doing Task-Based Teaching.* Oxford: Oxford University Press.
**Topic:** TEFL methodology / TBLT.
**Why cited:** The most practical TBLT handbook — pre-task → task → language focus is their sequence, lifted directly into LESSON_TEMPLATE.md.
**Used in:** school/about_kru_eng.md, curriculum/syllabus_12week.md, lessons/LESSON_TEMPLATE.md, references/teaching_methods.md.

### Wray 2002
Wray, A. (2002). *Formulaic Language and the Lexicon.* Cambridge: Cambridge University Press.
**Topic:** Lexical approach / formulaic language.
**Why cited:** Empirical foundation for the claim that adult language users store and retrieve formulaic sequences as wholes. Read together with Lewis 1993 as the lexical-approach pair.
**Used in:** school/about_kru_eng.md, vocabulary/tech_lexical_chunks.md, references/teaching_methods.md.

## Maintenance

When you add a new `[ref:short_name]` citation anywhere in the wiki:

1. **First**, check whether an existing entry already covers the source — `[ref:Lewis 1993]` is the same as a freshly-coined `[ref:lexical_approach]` would be. Reuse the existing key.
2. **If genuinely new**, add an entry here following the format above (full citation + topic + why + used-in).
3. `hermes-night` periodically scans the wiki for `[ref:...]` keys that don't appear in this file. Broken refs are reported in the night-pass summary. Fix them when they appear.

## See also

- `INDEX.md` — wiki schema map.
- `references/teaching_methods.md` — the prose discussion of these sources.
- `references/notebooklm_bootstrap.md` — operational reference for NotebookLM.
