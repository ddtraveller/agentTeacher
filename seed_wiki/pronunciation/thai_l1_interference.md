---
title: Thai L1 Interference — Pronunciation Patterns for Tech English
type: reference
status: live
topic: predictable Thai-speaker pronunciation errors, especially in tech vocabulary
updated: 2026-05-11
---

# Thai L1 Interference — Pronunciation Patterns

This page maps the predictable pronunciation errors Thai L1 speakers make when speaking English, with a particular focus on the **tech and AI vocabulary** Kru Eng teaches. The bot uses it to diagnose, target, and recast.

It is not a prescription for "correct" English. Thai-accented English is intelligible English. The goal is to fix errors that **interfere with comprehension**, not to chase a native-speaker accent.

## How to read this page

Each pattern has:
- **What happens** — the production tendency.
- **Why** — the L1 system mismatch.
- **Tech-specific examples** — where it bites in this course.
- **Drill** — a quick remediation the bot can run.
- **Priority** — high (causes miscomprehension), medium (causes friction), low (cosmetic).

## 1. Final consonants — dropped, softened, or unreleased

**What happens.** Thai L1 speakers tend to drop or soften syllable-final consonants in English. *"work"* → /wəː/, *"like"* → /laɪ/, *"want"* → /wɔn/.

**Why.** Thai phonotactics allow only a very limited set of final consonants (/p/, /t/, /k/, /m/, /n/, /ŋ/, and even these are unreleased — pronounced with the mouth in position but no audible release). English has 24 consonants that can occur finally, most released.

**Tech-specific examples.**

| Word | Thai-likely production | Why it matters |
|---|---|---|
| script | /skrɪ/ | "Run the scri" sounds like "run the scree(n)" → confusion |
| commit | /kəˈmɪ/ | *commit* vs *come it* — same issue |
| push | /pʊ/ | *push* sounds like *poo* — embarrassing |
| network | /nɛʔ.wəː/ | *net* glottal-stops; *work* drops /k/ |
| github | /gɪt.hə/ | Drops the final /b/; sounds like *gita* |
| output | /aʊ.pʊ/ | Drops final /t/ on both syllables |
| prompt | /prɒm/ | Cluster /mpt/ collapses to /m/ |

**Drill.** Final-consonant pairs. Bot says the word twice — first with a strong final, then without. Learner identifies which is the English one. Then learner produces three pairs themselves, with the bot's TTS as the model.

**Priority.** **High.** Final consonants carry meaning in English far more than in Thai. This is the single biggest intelligibility lever.

## 2. Consonant clusters — collapsed

**What happens.** English allows clusters Thai doesn't, especially initially (/spl-/, /str-/, /skr-/) and finally (/-mpt/, /-rdz/, /-sks/). Thai L1 speakers either insert a vowel between them (*"sport"* → *"sa-port"*) or drop a consonant (*"script"* → *"sa-crip"* or *"crip"*).

**Tech-specific examples.**

| Word | Thai-likely production | Better target |
|---|---|---|
| script | /sə.krɪp/ or /krɪp/ | /skrɪpt/ |
| prompt | /prɒm/ or /prɒmt/ | /prɒmpt/ |
| Python | /paɪ.tʰəːn/ | /ˈpaɪ.θən/ |
| extension | /ɛk.tɛn.ʃən/ | /ɪkˈsten.ʃən/ |
| screenshot | /sə.krin.ʃɔt/ | /ˈskriːn.ʃɒt/ |

**Drill.** Cluster onset: minimal pair work. *port / sport / sport / port*. Then *cript / script / script / cript*. The bot models the difference between "vowel-then-cluster" and "cluster-then-vowel".

**Priority.** **Medium.** Listeners usually recover, but the inserted vowel adds a syllable that can throw off prosody and confuse the listener about which word was said.

## 3. /v/ vs /w/ — collapsed

**What happens.** Thai has /w/ but not /v/. Thai L1 speakers substitute /w/ for /v/ → *very* /weɹi/, *vector* /wek.tʰə/.

**Tech-specific examples.**

| Word | Risk |
|---|---|
| variable | *wariable* — fine, intelligible |
| version | *wersion* — common; usually understood |
| VS Code | *we-es Code* — bizarre to hear but understood |
| virtualenv | *wirtual-env* — fine in context |
| TensorFlow | *Ten-sa-flow* — different problem (see schwa below) |

**Drill.** Lip position. /v/ requires the upper teeth on the lower lip (a fricative). /w/ is rounded lips, no teeth. The bot demos the lip position; the learner mirrors.

**Priority.** **Low.** Intelligibility cost is low. Worth fixing for confidence, not for being understood.

## 4. /r/ vs /l/ — collapsed (less than the Japanese stereotype)

**What happens.** Thai has both /r/ and /l/ phonemically, but the /r/ is a tap [ɾ] or trill [r] in formal speech and often realized as [l] in casual speech ("*Rama 4*" → "*Lama 4*" in fast Bangkok speech). English uses an approximant /ɹ/. Thai L1 speakers may substitute [l] or [ɾ] for English /ɹ/.

**Tech-specific examples.**

| Word | Risk |
|---|---|
| run | /lan/ or /ɾan/ instead of /ɹʌn/ — *run a script* → *lan a script* |
| repository | trill the /r/ — sounds bookish; not wrong |
| URL | each letter said in Thai sound system — common |
| router | /laʊ.tʰə/ — *louter* — confusion with *layer* |

**Drill.** Curl-the-tongue exercise. English /ɹ/ has the tongue raised toward the post-alveolar ridge but **not** touching. Demo with a mirror. Hold the /ɹ/ for two seconds: *rrrrun, rrrread, rrrremote*.

**Priority.** **Medium**, mainly for words where the /r/ is initial and content-bearing (*run*, *read*, *remote*, *root*).

## 5. /θ/ and /ð/ — replaced

**What happens.** Thai doesn't have the dental fricatives /θ/ (*think*) and /ð/ (*this*). Thai L1 speakers typically substitute /t/ for /θ/ (*tink*) and /d/ for /ð/ (*dis*). Some use /s/ and /z/ (*sink*, *zis*).

**Tech-specific examples.**

| Word | Common substitution |
|---|---|
| think | /tɪŋk/ — *tink* |
| through | /tru/ — *tru* |
| algorithm | /æl.gə.rɪt.tʰəm/ — *algoritom* |
| Python | /paɪ.tʰən/ — *paitan* (this one is /θ/) |
| this | /dɪs/ — *dis* |

**Drill.** Tongue position. /θ/ — tongue between teeth, exhale (no voice). /ð/ — same position, with voice. The bot models, the learner imitates with a mirror. *Th, th, th. Think, three, through. This, that, the.*

**Priority.** **Low.** Intelligibility usually fine; this is one Thai-accent feature that most English listeners hear without issue. Worth a brief drill, not a campaign.

## 6. Vowel length — collapsed

**What happens.** English distinguishes short and long vowels (*ship* /ʃɪp/ vs *sheep* /ʃiːp/). Thai also has vowel length, but the long-vowel sounds don't always map cleanly. Thai L1 speakers may produce English short vowels that are too long (*ship* /ʃiːp/) or long vowels that are too short.

**Tech-specific examples.**

| Pair | Risk |
|---|---|
| live (verb) / leave | *I leave in Chiang Mai* (oops) |
| bit / beat | *the beat is wrong* (programmer vs musician) |
| feel / fill | *feel the form* / *fill the form* |

**Drill.** Minimal pair discrimination. The bot says one of a pair; the learner says which one they heard.

**Priority.** **Medium.** Most consequential for *live* / *leave*, which comes up early.

## 7. Tone-stress mismatch

**What happens.** Thai is a tonal language: word identity is partly carried by pitch contour. English is a stress-timed language: word and sentence meaning is carried by which syllable is loud and long. Thai L1 speakers often replace English stress with Thai tone, giving flat or sing-song English that loses prominence cues.

**Tech-specific examples.**

| Phrase | Thai-likely pattern | English pattern |
|---|---|---|
| **com**-pu-ter | even tone all three syllables | stress on **com**, schwa on the others |
| Java-**Script** | even or rising | stress on **Ja**, secondary on **Script** |
| **Open** the terminal | rising on each word | strong stress on *open*, *terminal* |
| I **can't** run it. | flat | heavy stress on *can't* (week 8!) |

**Drill.** Two-syllable noun stress. Bot says: *COM-puter, OPEN, TERMinal, SCRIPT-ing*. Learner repeats with **exaggerated** stress. Then unexaggerated.

**Priority.** **High** for imperative verbs (week 10) and for contrasted modals (week 8 *can/can't*).

## 8. Schwa avoidance

**What happens.** Unstressed English vowels reduce to /ə/ (schwa). Thai doesn't have a true schwa; vowels are full. Thai L1 speakers tend to produce **full** vowels in unstressed positions, giving *"com-pu-ter"* with three full vowels instead of /kəmˈpjuː.tə/.

**Tech-specific examples.**

| Word | Native | Thai-likely |
|---|---|---|
| computer | /kəmˈpjuː.tə/ | /kʰɔm.pʰiu.tʰəː/ |
| algorithm | /ˈæl.gə.ɹɪð.əm/ | /ʔɛw.kɔ.ɾi.tʰom/ |
| executable | /ɪgˈzek.jə.tə.bəl/ | /ɛk.se.kʰiu.tʰə.bəːw/ |

**Drill.** Reduce, don't pronounce. Bot says a word three times: clearly, faster, fastest (with schwa). Learner copies the fastest version.

**Priority.** **Medium.** Schwa avoidance makes Thai-accented English sound stilted but is rarely a comprehension blocker.

## Putting it together — diagnostic micro-test

When a new learner starts, the bot listens for the patterns above by asking them to say these ten phrases:

1. *I'm a student.*
2. *I work at a coffee shop.*
3. *Open the terminal and run the script.*
4. *I can't push this to GitHub.*
5. *My computer is slow today.*
6. *I think the algorithm is wrong.*
7. *I live in Chiang Mai.*
8. *I'd like to leave at five.*
9. *The version is wrong.*
10. *We need to write a prompt.*

Scoring: any phrase the bot can't understand on the first listen is a candidate for that pattern's drill. Two miscomprehensions in the same pattern = priority for the next two lessons.

The diagnostic feeds `students/<nickname>.md` → Pronunciation watchlist.

## What we don't try to fix

- **General accent.** Thai-accented English is a legitimate variety. Kru Eng celebrates it.
- **Politeness particles in English** (*krap*, *ka*). They don't transfer to English, but most learners drop them naturally.
- **The Thai *ครับ/ค่ะ* habit** when speaking English. Bot models polite English alternatives (*sir*, *please*, *thank you*) without making a fuss.

## References

- *[ref:Smyth 2002]* — Smyth, D. *Thai: An Essential Grammar* — Thai sound system.
- *[ref:Walker 2010]* — Walker, R. *Teaching the Pronunciation of English as a Lingua Franca* — what to fix vs let go.
- `lessons/w08_what_is_ai_and_what_can_it_do.md` — *can/can't* discrimination case study.
- `lessons/w10_prompt_engineering_basics.md` — imperative stress case study.
