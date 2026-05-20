# Kru Eng — Local AI English Tutor for Thai Schools

<p align="center">
  <img src="https://krueng.ai/imgs/agentTeacher/hero.png"
       alt="The Local AI Advantage: data sovereignty, radical cost savings, an AI office agent for administrative tasks and institutional knowledge, with a hardware-vs-performance reality check."
       width="900">
</p>

**ครูอิงค์ — ผู้ช่วยสอนภาษาอังกฤษด้วย AI ที่ทำงานในเครื่องของโรงเรียน**

**Kru Eng — 在学校自有电脑上运行的 AI 英语助教**

A voice-in / voice-out English tutor that runs entirely on your school's
own PC. No student audio ever leaves the building. No subscription. No
account. No data shared with any cloud AI provider.

Built for Thai schools, Thai PDPA, and a Thai network connection that
isn't always cooperative.

> **ภาษาไทย:** ผู้ช่วยสอนภาษาอังกฤษแบบรับ-ส่งเสียง ที่ทำงานบนคอมพิวเตอร์ของโรงเรียนคุณเองทั้งหมด เสียงของนักเรียนไม่ส่งออกนอกอาคาร ไม่มีค่าสมาชิกรายเดือน ไม่ต้องลงทะเบียนบัญชี ไม่แชร์ข้อมูลใด ๆ กับผู้ให้บริการ AI บนคลาวด์
>
> ออกแบบมาเพื่อโรงเรียนในประเทศไทย ให้สอดคล้องกับ พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) และรองรับเครือข่ายอินเทอร์เน็ตในไทยที่อาจไม่เสถียรเสมอไป
>
> โครงการนี้เปิดเป็นโอเพนซอร์ส (สัญญาอนุญาต MIT) สำหรับโรงเรียนรัฐ โรงเรียนเอกชน สถาบันสอนภาษา และมหาวิทยาลัยในประเทศไทย — นำไปติดตั้งและปรับแต่งให้เหมาะกับโรงเรียนของคุณได้ฟรี

> **中文：** 完全运行在学校自有电脑上的 AI 语音英语家教。学生的语音不会离开校园，无月费，无需账号，不向任何云端 AI 提供商共享数据。
>
> 专为泰国学校设计，符合泰国个人资料保护法 (PDPA)，能在不稳定的本地网络下正常工作。
>
> 本项目以 MIT 开源协议发布，面向泰国的公立学校、私立学校、语言机构和大学免费使用 — 您可以自由部署，并根据贵校的需求定制。

```
[mic] -> Whisper (speech-to-text) -> Qwen 2.5 (language model)
                                          |
[speakers] <- Edge TTS / XTTS v2 <- reply text
```

## Why this exists

> **ภาษาไทย — ทำไมต้องมีระบบนี้?**
>
> โรงเรียนที่ใช้ ChatGPT หรือ AI บนคลาวด์ส่งคำพูดของนักเรียนทุกประโยคออกไปยังผู้ให้บริการในสหรัฐอเมริกา ภายใต้ พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) ของไทย เรื่องนี้สร้างความเสี่ยงทางกฎหมายแก่โรงเรียน โดยเฉพาะเมื่อข้อมูลเป็นของผู้เยาว์
>
> สถานการณ์ข้างหน้ายิ่งน่าเป็นห่วง:
>
> 1. **ChatGPT แพ็กเกจฟรีกำลังจะมีโฆษณา** OpenAI ส่งสัญญาณชัดเจนว่าจะหารายได้จากผู้ใช้แพ็กเกจฟรีผ่านโฆษณาและพาร์ตเนอร์ทางการตลาด หมายความว่าบทสนทนาของนักเรียนจะกลายเป็นข้อมูลฝึกโมเดลและสัญญาณกำหนดเป้าหมายโฆษณา — โรงเรียนไม่ใช่ลูกค้า แต่กลายเป็นสินค้า
> 2. **การส่งข้อมูลจำนวนมากไปยังผู้ให้บริการ AI ในสหรัฐฯ มีความเสี่ยงทางกฎหมายเพิ่มขึ้น** ทั้ง PDPA ของไทย, GDPR ของยุโรป และคำวินิจฉัยล่าสุดในภาคการศึกษาชี้ไปในทิศทางเดียวกัน
>
> ระบบนี้ทำงาน **ทั้งหมดบนคอมพิวเตอร์ของโรงเรียน** — เสียงนักเรียนไม่ออกนอกอาคาร หลักสูตร เอกสารครู และข้อมูลความก้าวหน้าของนักเรียนทั้งหมดอยู่ที่โรงเรียน ไม่ถูกอัปโหลดไปไหน

> **中文 — 为什么需要这个？**
>
> 学校使用 ChatGPT 或其他云端 AI 进行学生英语练习时，每一句学生话语都被发送到美国的服务提供商。根据泰国《个人资料保护法》(PDPA)，这给学校带来了真实的合规风险 — 尤其是涉及未成年人时。
>
> 两个趋势让情况进一步恶化：
>
> 1. **ChatGPT 免费版即将引入广告。** OpenAI 已明确表示将通过广告和合作伙伴关系将免费用户变现，这意味着学生的对话将成为模型训练数据和广告定向信号。使用免费云端 AI 的学校不是客户 — 而是产品。
> 2. **向美国 AI 服务商批量传输数据的法律风险正在上升。** 泰国 PDPA、欧盟 GDPR 以及近期教育领域的相关裁决都指向同一方向：学生话语（特别是未成年人）的批量跨境传输正在成为待暴露的合规漏洞。
>
> 本系统**完全运行在学校自有的电脑上**：Whisper 在本地完成语音识别，Qwen 2.5 在本地生成回复，Edge TTS 处理语音输出（只发送文本，不上传学生录音）。学生的声音永远不会离开学校的网络。学校的课程、学生进度数据、老师自制教材 — 全都不会被上传到任何地方。

Schools using ChatGPT or other cloud AI for student English practice send
every student utterance to a US-based provider. Under Thailand's PDPA,
that exposes the school to a real compliance question — especially for
minors.

Two things make this worse going forward:

1. **ChatGPT's free tier is moving to ad-supported.** OpenAI has signaled
   plans to monetize free-tier users with advertising and partnerships,
   which means student conversations become training and targeting
   signal. Schools sending student queries to a free-tier US AI service
   are not the customer — they're the product.
2. **Mass data transfer to American AI providers is an emerging legal
   risk.** Thailand's PDPA, the EU's GDPR-influenced rules, and recent
   education-sector data rulings all point the same direction: bulk
   transfer of student utterances — especially minors' — to overseas
   processors is exposure waiting to happen. Schools that haven't been
   audited yet probably will be.

This stack runs **entirely on your school's PC**. Whisper does speech
recognition locally. Qwen 2.5 generates replies locally. Edge TTS
handles voice output (free Microsoft service, voices only — no user
audio sent). Your students' voices never leave your network. Your
school's curriculum, your students' progress data, your teachers'
custom materials — none of it gets uploaded anywhere.

## What you get

> **ภาษาไทย — ในแพ็คเกจนี้มีอะไรบ้าง**
>
> - **ฝึกสนทนาเสียง** — นักเรียนกดปุ่มค้างไว้ พูด ระบบตอบกลับเป็นเสียง ใช้งานผ่านเว็บเบราว์เซอร์ทั่วไป
> - **หลักสูตร 12 สัปดาห์ A1→B1** — ภาษาอังกฤษผสมเทคโนโลยีและ AI literacy ทุกอย่างเป็น markdown ใน `seed_wiki/` แก้ให้ตรงกับหลักสูตรของโรงเรียนได้
> - **เครื่องมือบทเรียน PPP** — Presentation → Practice → Production มี Past Simple และ Past Continuous ให้เป็นตัวอย่าง
> - **ปฏิทินโรงเรียน** — รวมเหตุการณ์จากสามแหล่ง: ของโรงเรียนที่เขียนไว้ใน git (วันเปิดเทอม วันหยุด สัปดาห์สอบ) เหตุการณ์ที่ครูเพิ่มผ่าน UI (เก็บที่เซิร์ฟเวอร์) และเหตุการณ์ส่วนตัวของนักเรียน (เก็บในเบราว์เซอร์เท่านั้น ไม่ส่งออกที่ไหน)
> - **เครื่องมือสร้างข้อสอบ** — สร้างได้สามวิธี: ใช้ CLI เรียก LLM ในเครื่องผลิตข้อสอบจากบทเรียน, ใช้ UI พิมพ์ข้อสอบเอง (ติ๊ก ✓ ถูก / ✗ ผิด แต่ละข้อ), หรือโหลดจากไฟล์ JSON การตรวจให้คะแนนเป็น deterministic ไม่ใช้ LLM
> - **กระดานวาด** — เครื่องมือปากกา เส้น สี่เหลี่ยม ยางลบ พร้อมคีย์บอร์ดบนหน้าจอสำหรับพิมพ์ตัวอักษรลงบนกระดาน บันทึกเป็น PNG (`/whiteboard`)
> - **โคลนเสียงครู (ทางเลือก)** — วางไฟล์เสียงครู 6 วินาทีใน `voices/` XTTS v2 จะโคลนเสียงให้
> - **โอเพนซอร์สทั้งหมด** ใบอนุญาต MIT

> **中文 — 系统包含哪些功能**
>
> - **语音对话练习** — 学生按住按钮说话，系统语音回复。Web UI 在任何现代浏览器中运行
> - **12 周 A1→B1 课程大纲** — 英语 + 科技与 AI 素养。所有内容是 `seed_wiki/` 中的 markdown，可按贵校大纲、学生名单、教学风格自行编辑
> - **PPP 课程引擎** — Presentation → Practice → Production。已包含 Past Simple 和 Past Continuous 示例课程
> - **学校日历** — 三种事件源合并到月视图：仓库中预置的学校事件（学期、节假日、考试周，在 git 中维护）、运行时通过 UI 添加的共享事件（保存到服务器）、学生的个人事件（仅留在浏览器 `localStorage`，绝不发送到服务器）
> - **试题生成器** — 三种生成方式：CLI 调用本地 LLM 从已有课程生成新题目；UI 手动构建（每个选项标记 ✓ 正确 / ✗ 错误）；JSON 文件导入。评分为确定性，评分流程不调用 LLM
> - **数字白板** — 画笔、直线、方块、橡皮工具，以及屏幕字母键盘（点击字母在画布上输入文字）。保存为 PNG（`/whiteboard`）。后端还提供本地视觉模型反馈接口 `POST /whiteboard/analyze`（使用 `qwen2.5vl:3b`）
> - **声音克隆（可选）** — 放入 6 秒教师 WAV 到 `voices/`，XTTS v2 会克隆出来
> - **完全开源** MIT 许可证

- **Voice conversation practice** — students hold a button, speak, get a reply spoken back. Web UI works on any modern browser.
- **A 12-week A1→B1 curriculum** — English combined with Tech and AI literacy. Lives in `seed_wiki/` as plain markdown. Edit it to match your syllabus, your students' names, your teaching style.
- **A scaffolded PPP lesson engine** — Presentation → Practice → Production. Sample lessons included (Past Simple, Past Continuous).
- **School calendar** — three event sources merged in a month view: docs-loaded school events (term dates, holidays, exam weeks shipped in the repo and edited in git), shared events added at runtime via the web UI, and personal events that stay in the student's browser (`localStorage`) and never touch the server.
- **Exam creator** — three ways to produce graded fill-blank or multiple-choice exams: a CLI that calls the local LLM to generate fresh exercises from an existing lesson, a manual builder UI where the teacher types prompts and answers (with a ✓ Correct / ✗ Incorrect toggle per option), and a JSON file-load path. Grading is deterministic — no LLM in the scoring path.
- **Whiteboard** — a drawing canvas with pen, line, square, eraser, and an on-screen alphabet keyboard for typing labels onto the canvas. Save the result as a PNG (`/whiteboard`). Backend includes an optional vision-model endpoint for English-tutor feedback on a student's drawing (`POST /whiteboard/analyze`, uses `qwen2.5vl:3b`).
- **Voice cloning, optional** — drop a 6-second WAV of any teacher's voice into `voices/`; XTTS v2 will clone it.
- **All open source.** MIT licensed.

## What schools can do with it

> **ภาษาไทย — โรงเรียนใช้ระบบนี้ทำอะไรได้บ้าง?**
>
> ระบบเดียวกันนี้ทำได้มากกว่าฝึกพูดภาษาอังกฤษ ใช้กับงานในโรงเรียนได้หลากหลายโดยข้อมูลทั้งหมดยังอยู่ในเครื่องของโรงเรียน
>
> **ใช้ได้ทันทีจากชุดติดตั้งนี้:** คู่ฝึกพูดอังกฤษ 24 ชั่วโมงสำหรับนักเรียนที่เขินอายไม่กล้าพูดในห้อง • ผู้ตรวจการบ้านที่ไม่เหนื่อย ตรวจตามเกณฑ์ที่ครูตั้งไว้ • ผู้ช่วยวางแผนการสอนและสร้างข้อสอบตามหลักสูตรของโรงเรียน • ผู้ช่วยสอนรายบุคคลที่จดจำระดับและความสนใจของนักเรียนแต่ละคน • ระบบถาม-ตอบเรื่องโรงเรียน (คู่มือนักเรียน ระเบียบการ ตารางสอบ ปฏิทินวันหยุด) • ทางเลือกที่ปลอดภัยจาก ChatGPT สำหรับให้นักเรียนทดลองใช้ AI • รองรับหลายภาษา (อังกฤษ ไทย จีน ญี่ปุ่น เกาหลี)
>
> **ต่อยอดได้ภายในไม่กี่ชั่วโมง:** บอท LINE สำหรับสื่อสารกับผู้ปกครองและนักเรียน • ส่งคำศัพท์รายวันเข้า LINE อัตโนมัติ • เปิดให้นักเรียนเข้าใช้งานผ่าน Wi-Fi โรงเรียนจากมือถือ/แท็บเล็ต • สร้างภาพประกอบบทเรียนเองในเครื่อง (ไม่ต้องสมัคร Canva) • โคลนเสียงครูแต่ละคนเพื่อทำสื่อการสอน • บทสนทนาจำลองระหว่าง AI สองตัว (ลูกค้า-ร้านค้า, หมอ-คนไข้) สำหรับให้นักเรียนฝึก
>
> **ขยายเป็นโครงการใหญ่ได้:** "ยามดิจิทัล" — โมเดลวิสัยทัศน์ที่ดูภาพจากกล้องวงจรปิดในเครื่อง แจ้งเตือนเฉพาะเหตุการณ์ผิดปกติ ภาพไม่ออกนอกอาคาร • ผู้ช่วยอัจฉริยะสำหรับครูและเจ้าหน้าที่ • ครูสอนวิชาอื่นนอกเหนือจากอังกฤษ (คณิต วิทย์ ไทย) • คลังความรู้ของโรงเรียน เก็บความเชี่ยวชาญของครูอาวุโสไว้ก่อนเกษียณ
>
> **สิ่งสำคัญที่สุด:** เอกสารและสื่อดิจิทัลที่โรงเรียนมีอยู่แล้ว — PDF เอกสาร Word สไลด์ บันทึกการสอน ข้อสอบเก่า รูปกระดานในห้องเรียน — นำมาทำเป็นคลังความรู้ให้ AI ใช้ตอบคำถามได้ และความรู้นั้นยังเป็นของโรงเรียน ไม่หลุดออกไปไหน รายละเอียดทั้งหมดอยู่ในส่วนภาษาอังกฤษด้านล่าง

> **中文 — 学校能用它做什么？**
>
> 同一套本地 AI 系统可以做的远不止英语口语练习。它可以应用于学校的多种场景，而且所有数据始终留在校内电脑上。
>
> **开箱即用：** 24 小时英语口语陪练（适合不敢在课堂上开口的害羞学生）• 不知疲倦的作业批改员（按老师设定的评分标准）• 课程规划与测验生成助手（基于贵校自己的课程大纲）• 因材施教的教学助手（记住每位学生的水平和兴趣）• 校务问答机器人（学生手册、规章制度、考试日程、节假日历）• 给学生探索 AI 的安全替代品（替代 ChatGPT）• 多语言支持（英语、泰语、中文、日语、韩语）
>
> **几小时内即可扩展：** LINE 聊天机器人（与家长和学生沟通）• 自动推送每日单词到 LINE • 让学生通过校园 Wi-Fi 从手机/平板访问 • 在本地生成课堂插图（无需订阅 Canva）• 克隆各位老师的声音用于教学素材 • 多智能体对话模拟（顾客-店员、医生-病人）供学生练习
>
> **更大的项目：** "数字保安" — 本地视觉模型监控摄像头画面，仅在异常事件时报警，画面不出大楼 • 面向教师和职员的全校智能助理 • 英语之外其他学科的辅导（数学、科学、泰语）• 学校知识库 — 在资深教师退休前保存其专业经验
>
> **关键之处：** 贵校已有的数字资料 — PDF、Word 文档、PPT、课堂录音、过往试卷、白板照片 — 都可以转化为 AI 的知识库，让 AI 根据贵校自己的资料回答问题。这些知识仍然属于学校，不会泄露到任何地方。详细内容见下方英文部分。

The same local-AI stack underneath Kru Eng can power a lot more than
English speaking practice. Below: what's possible today with what ships
in this repo, what's a small extension away, and what you could grow
into. All of it stays on your PC.

### Today, with what ships in this repo

- **A 24/7 English speaking partner.** Students who never speak in
  class because they're embarrassed will talk to a bot. The bot doesn't
  judge, doesn't get tired, doesn't run out of patience.
- **A tireless homework grader.** Plug your rubric into
  `seed_wiki/assessment/`, drop student work into a chat, get
  consistent feedback in seconds. Teachers spot-check; the bot drafts.
- **A lesson planner and quiz generator.** Ask for a 45-minute lesson
  on a topic; the bot drafts presentation slides, practice exercises,
  and an exit ticket — grounded in your school's curriculum, not a
  generic textbook.
- **A teaching assistant that knows your students.** Per-learner
  markdown profiles in `seed_wiki/students/` let the bot adapt
  difficulty, remember a student's interests, and follow up on
  previous conversations. Add or remove students by editing files.
- **An institutional Q&A bot.** Drop your school handbook, dress code,
  schedule, holiday calendar, and SOPs into the wiki. Students, parents,
  and staff can ask in natural language and get cited answers — never
  invented.
- **A safe alternative to ChatGPT for student exploration.** The same
  curiosity-driven "let me ask the AI" instinct, redirected to a system
  the school controls. Schools can decide what topics the bot will and
  won't discuss by editing the persona file.
- **A multilingual tutor.** English, Thai, Chinese, Japanese, Korean —
  all handled. Useful for international students, EP programs, and
  Chinese-Thai dual-language schools.

### A small extension away (a few hours of work each)

- **A LINE chatbot for parents and students.** Same agent, accessed via
  Thailand's dominant chat app. Push daily vocab cards, homework
  reminders, exam-prep prompts. Kids practice English while waiting for
  the bus.
- **Scheduled tasks.** "Push 5 vocabulary cards to M4/2 at 7 AM every
  weekday." "Email the principal a summary of student questions every
  Friday afternoon." Cron + the local agent = zero monthly cost.
- **A local website on the school LAN.** The orchestrator already
  serves a web UI. Open the port to the LAN and any phone, tablet, or
  PC on the school network can use it — no app install, no internet,
  no per-seat license. Students get one URL; staff get another with
  different permissions.
- **Local image generation for classroom materials.** SDXL Turbo runs on
  any decent GPU. Worksheets, slide illustrations, vocab flashcards —
  generated on demand from a teacher's prompt, sized correctly,
  printable. No Canva subscription.
- **Voice cloning for specific teachers.** Already in the box. Record a
  teacher's voice once, and the bot can deliver lessons in their voice
  — useful for absent-teacher cover, accent modeling, or recordings
  that sound like the actual classroom teacher.
- **Multi-agent role-play.** Two instances of the bot with different
  personas talking to each other (Customer + Shopkeeper, Doctor +
  Patient, Teacher + Student). Students join the dialogue or watch and
  transcribe — a TEFL technique that's expensive with humans, free
  with two local agents.

### A bigger project (worth doing if it matches your school's needs)

- **A digital security guard.** Local vision models (Qwen-VL, LLaVA,
  Llama Vision) can watch a camera feed and flag anomalies — a student
  in a restricted area, an open gate after hours, a fall in a stairwell.
  Runs on the same GPU. Nothing leaves the building. Privacy-preserving
  by design — the model sees frames; only flagged events get logged.
- **Whole-school staff agent.** HR FAQs, leave-request walkthroughs,
  finance-form lookups. Most internal admin questions are repetitive —
  let staff ask the bot and free your office for the hard cases.
- **Curriculum-specific tutoring beyond English.** Math, science,
  Thai-language exam prep — change the seed wiki, change the persona,
  same infrastructure. One local AI, many subjects.
- **Knowledge preservation.** Every veteran teacher who retires takes
  hard-won expertise with them. Capture it in markdown over a year of
  conversations, and the institution keeps the knowledge — without
  ever uploading it to a third party who would train on it.

### Using your school's existing digital media as the AI's knowledge

A school doesn't start with an empty bot. Most schools already have
years of materials gathering dust on shared drives — and all of it can
become the AI's corpus:

- **PDFs and Word documents** — lesson plans, worksheets, parent
  handbooks, policy documents, course outlines. The shipped index
  pipeline reads markdown only (by design — keeps the corpus clean),
  so convert these to `.md` first. `pandoc input.docx -o output.md`
  handles Word in one line; PDFs are stickier — try `pandoc`,
  `pdftotext`, or `marker` (best for layout-heavy PDFs) and review the
  output. See the "Adding your own knowledge files" section below for
  the full recipe.
- **Slide decks** — PowerPoint files convert to markdown easily. The
  bot then references "Slide 12 of the Photosynthesis deck" when a
  student asks about chloroplasts.
- **Recorded lectures and audio** — feed them through Whisper (already
  in this stack) to produce text transcripts. The bot can then answer
  "what did Ajarn Som say about the Sukhothai period last term?"
- **Scanned books and handwritten notes** — OCR them (Tesseract works
  well for Thai + English) and the text joins the corpus. A school's
  out-of-print textbooks become searchable.
- **Past exam papers** — become practice material. The bot generates
  variations grounded in your school's actual exam style, not generic
  textbook patterns.
- **Photos of classroom whiteboards** — vision models can extract the
  text. A semester of whiteboard work becomes a study reference.
- **Old teacher emails, parent newsletters, school magazines** — your
  institutional voice and history. The bot learns to *sound like your
  school*, not like a generic tutor.

The pattern is always the same: text-bearing artifact → wiki markdown
→ indexed → the bot uses it. Once a school commits to feeding its
existing materials in, the AI rapidly becomes more useful than any
cloud tutor could be — because it knows things only your school knows.

### What stays safe

Local AI is the only deployment model where **your school's special
knowledge** can be used by AI *and* stay yours. Everything that lives
in `seed_wiki/` — past exam patterns, your school's pedagogical method,
the rubrics you've refined over a decade, your students' progress
notes, parent communication templates, internal SOPs — feeds the bot
without leaking to anyone. The model uses it; nobody trains on it.

Compare to a cloud AI: every question your teachers type, every
student utterance, every uploaded document becomes training data,
targeting signal, or both. Your school's hard-won expertise becomes
free fuel for someone else's product.

### What it can produce

- **Text** — lesson plans, rubrics, parent communications, worksheets,
  exam questions, vocab lists, story prompts.
- **Audio** — narrated lessons, pronunciation models, audiobooks in
  Thai or English, voice-cloned teacher recordings.
- **Images** — classroom illustrations, vocab flashcards, worksheet
  graphics (with a GPU and SDXL Turbo).
- **Structured data** — student progress reports, class summaries,
  attendance digests, exam analytics — all in formats your existing
  systems can ingest.

## System requirements

> **ภาษาไทย — ความต้องการของระบบ**
>
> **ขั้นต่ำสุดที่ใช้งานได้:** คอมพิวเตอร์ Windows / macOS / Linux พร้อม RAM 8 GB, พื้นที่ว่าง 20 GB, ติดตั้ง Docker Desktop, มีไมโครโฟนและลำโพง บนซีพียูล้วนใช้งานได้แต่ตอบช้า (ประมาณ 8-20 วินาทีต่อคำตอบ) เหมาะกับการฝึกการบ้านมากกว่าใช้ในห้องเรียนสด
>
> **แนะนำ:** คอมพิวเตอร์ที่มีการ์ดจอ NVIDIA RTX 3060 ขึ้นไป (VRAM 6 GB+) หรือ Mac M2/M3 ที่มี RAM 16 GB+ จะตอบเร็วประมาณ 1-3 วินาที เหมาะกับการใช้งานสดในห้องเรียน แนะนำให้ใช้คอมพิวเตอร์ตั้งโต๊ะ ไม่ใช่โน้ตบุ๊ก เพราะโน้ตบุ๊กจะร้อนเกินไปเมื่อใช้ AI นาน ๆ
>
> **พอร์ตที่ใช้:** เปิดพอร์ต **8000** ให้นักเรียนเข้าผ่านเครือข่ายของโรงเรียน พอร์ตอื่น (11434, 9000, 8001) ใช้ภายในเครื่องเท่านั้น
>
> **สำหรับ Windows:** ต้องเปิดใช้งาน WSL2 ก่อนติดตั้ง Docker Desktop หากต้องการใช้การ์ดจอ NVIDIA ต้องติดตั้ง NVIDIA Container Toolkit ภายใน WSL2 ด้วย รายละเอียดดูจากตารางภาษาอังกฤษด้านล่าง

> **中文 — 系统要求**
>
> **最低配置（能用但慢）：** 任何 Windows / macOS / Linux 电脑，8 GB 内存，20 GB 可用磁盘空间，已安装 Docker Desktop，配备麦克风和扬声器。纯 CPU 模式下可以运行但响应较慢（每次回复约 8-20 秒），更适合作业练习而非课堂实时使用。
>
> **推荐配置（可用于课堂实时教学）：** 配备 NVIDIA RTX 3060 或以上显卡（显存 6 GB+）的电脑，或 Mac M2/M3 配 16 GB 以上统一内存。响应时间可缩短到 1-3 秒。建议使用台式机而非笔记本电脑（笔记本在长时间 AI 运算下会发热降频）。
>
> **使用的端口：** 对学生开放 **8000** 端口（通过校园网访问）。其他端口（11434、9000、8001）仅供主机内部使用。
>
> **Windows 用户注意：** 需要先启用 WSL2 才能安装 Docker Desktop。如需使用 NVIDIA 显卡，还需在 WSL2 中安装 NVIDIA Container Toolkit。具体细节见下方英文表格。

### Minimum (works, but slow on CPU)

- **OS:** Windows 10/11, macOS 12+, or Linux (any modern distro)
- **CPU:** Any 64-bit x86 or Apple Silicon, 4 cores
- **RAM:** 8 GB (16 GB strongly recommended)
- **Disk:** 20 GB free (~15 GB for AI models + 5 GB for Docker images and indices)
- **Docker:** Docker Desktop with Compose v2 (Linux: Docker Engine 24+ with the compose plugin)
- **Network:** Internet for first install (Docker images + Ollama model downloads). After that, only Edge TTS needs internet — Whisper, Ollama, and the wiki all work fully offline
- **Browser:** Chrome, Edge, Firefox, or Safari — recent versions, with microphone permission
- **Microphone + speakers** (or headset) on the host machine

### Recommended (responsive for live classroom use)

- **GPU:** NVIDIA card with **6 GB+ VRAM** and a recent CUDA driver (RTX 3060, 4060, or better). Or a Mac with Apple Silicon M2/M3 and 16+ GB unified memory running Ollama natively on the host
- **RAM:** 32 GB if running qwen2.5:7b or larger
- **Disk:** 50 GB free if you plan to add custom models, more lessons, image generation, or video
- **A dedicated PC** the school can leave on 24/7 in a quiet corner — laptops thermally throttle under sustained AI load

### Ports the stack uses

The Docker stack publishes these ports on the host. Make sure nothing
else is listening on them, or remap in `docker-compose.yml`:

| Port | Service | What it serves |
|---|---|---|
| **8000** | orchestrator | Web UI + REST API (the thing students/teachers open in a browser) |
| **11434** | ollama | Language model inference (internal — only the orchestrator calls it) |
| **9000** | whisper | Speech-to-text (internal) |
| **8001** | tts | Text-to-speech (internal — useful to hit directly for testing) |

For a school LAN deployment, only port 8000 needs to be reachable from
student devices — the rest stay private to the host.

### Windows-specific notes

- Docker Desktop requires **WSL2 backend**. Enable WSL2 before installing
  Docker Desktop.
- For GPU on Windows, you also need **NVIDIA Container Toolkit**
  inside WSL2. The compose file has the GPU stanza commented out —
  uncomment it once the toolkit is set up.
- Path lengths: keep the install directory short (e.g.,
  `C:\krueng\`) — deep paths can trip Docker volume mounts on Windows.

## Quick start

> **ภาษาไทย — เริ่มต้นใช้งาน**
>
> ต้องติดตั้ง [Docker Desktop](https://docs.docker.com/desktop/) พร้อมส่วนเสริม Compose v2 ก่อน
>
> เปิด Terminal (หรือ PowerShell ถ้าเป็น Windows) แล้วรันคำสั่งภาษาอังกฤษด้านล่างตามลำดับ:
>
> 1. โคลนโค้ดจาก GitHub
> 2. คัดลอกไฟล์ตัวอย่าง `.env` (ค่าเริ่มต้นใช้ได้เลย ปรับเปลี่ยนภายหลังก็ได้)
> 3. รัน `docker compose up -d --build` — ครั้งแรกใช้เวลา 10-20 นาที (ดาวน์โหลดประมาณ 2 GB)
> 4. รัน `python scripts/pull_models.py` เพื่อดาวน์โหลดโมเดลภาษา Qwen 2.5 (ประมาณ 2 GB)
>
> เมื่อเสร็จแล้ว เปิดเว็บเบราว์เซอร์ไปที่ **http://localhost:8000** กดปุ่ม **🎙 Hold to talk** ค้างไว้ พูดเป็นภาษาอังกฤษ แล้วปล่อย ระบบจะตอบเป็นเสียงให้ฟัง

> **中文 — 快速开始**
>
> 首先需要安装 [Docker Desktop](https://docs.docker.com/desktop/) 以及 Compose v2。
>
> 打开终端（Windows 用户使用 PowerShell），依次运行下方的英文命令：
>
> 1. 从 GitHub 克隆代码仓库
> 2. 复制 `.env` 示例文件（默认值可直接使用，以后再调整）
> 3. 运行 `docker compose up -d --build` — 首次运行需要 10-20 分钟（下载约 2 GB）
> 4. 运行 `python scripts/pull_models.py` 下载 Qwen 2.5 语言模型（约 2 GB）
>
> 完成后，在浏览器中打开 **http://localhost:8000** 并按住 **🎙 Hold to talk** 按钮，用英语说话，然后松开。系统会用语音回复。

You need [Docker Desktop](https://docs.docker.com/desktop/) with Compose v2.

```bash
git clone https://github.com/ddtraveller/agentTeacher.git
cd agentTeacher
cp .env.example .env                     # edit if you want; defaults work
docker compose up -d --build             # first build pulls ~2 GB
python scripts/pull_models.py            # pulls Qwen 2.5 (~2 GB for 3b, ~4.4 GB for 7b)
```

Then open **http://localhost:8000**. You should see a green health row at the
bottom. Hold the **🎙 Hold to talk** button, speak, release. The reply plays
back through your speakers.

### What to open in a browser

| URL | What you'll see |
|---|---|
| **http://localhost:8000/** | Web UI — mic + speaker chat with Kru Eng. Click "🎙 Hold to talk", speak, release. The landing page also has chips linking to the four feature pages below. |
| **http://localhost:8000/lesson** | 📚 Scaffolded PPP lesson UI — Past Simple and Past Continuous, presentation → practice → production. |
| **http://localhost:8000/calendar** | 📅 Month-view school calendar — docs events (in-repo), shared events (server-saved), and personal events (browser-local). |
| **http://localhost:8000/exam** | 📝 Exam list + take + results. "+ New exam" builds a multi-choice exam by hand; load-from-file imports a JSON. |
| **http://localhost:8000/whiteboard** | 🎨 Drawing canvas — pen, line, square, eraser, alphabet keyboard, Save PNG. |

## Hardware honestly

This is the section every other "local AI" project glosses over. The model
that makes this useful runs slowly on CPU. Plan accordingly.

| Setup | Reply latency | Verdict |
|---|---|---|
| 8th-gen i5 / 16 GB RAM / no GPU, qwen2.5:3b | 8–20s per reply | Usable for homework practice; not for live classroom |
| Ryzen 7 / 32 GB RAM / no GPU, qwen2.5:7b | 15–40s per reply | Painful. Don't. |
| Any decent NVIDIA GPU (RTX 3060+) / qwen2.5:7b | 1–3s per reply | This is the real experience |
| Mac M2/M3 with 16+ GB / qwen2.5:7b (host Ollama) | 2–4s per reply | Comparable to a GPU |

**Recommended setup for a school:** one mid-range gaming PC (~฿30,000 used)
with a used RTX 3060 or 4060, running this stack 24/7 in a corner of the
computer lab. Students take turns using it.

You need ~12 GB disk for the models, plus another ~5 GB for Whisper and XTTS.

## Customizing Kru Eng for your school

The `seed_wiki/` directory is the bot's brain. It's all plain markdown.
Edit it however you want, then restart the orchestrator and the bot
uses your changes.

### Quick wins (files you can edit today)

- `seed_wiki/school/about_kru_eng.md` — change the school name, your
  pedagogical philosophy, what you want the bot to know about your
  institution.
- `seed_wiki/staff/kru_eng_persona.md` — the bot's voice and tone. Make
  her formal, casual, more authoritative, whatever fits your school.
- `seed_wiki/students/` — one markdown file per student. The bot adapts
  to individual learners' levels and interests. Template included.
- `seed_wiki/lessons/` — twelve weekly lessons covering English + tech +
  AI. Each follows a common template (Presentation, Practice,
  Production). Add, edit, remove freely.

The wiki is in English because English is the language Qwen reasons best
in. Native-script terms can be quoted inline (`market (ตลาด)`), but
don't translate whole sentences — that's the bot's job at output time.

### Adding your own knowledge files (step by step)

Use this when you have school-specific content the default wiki doesn't
cover: your handbook, your past exams, your syllabus, your teachers'
notes, your subject curriculum. The bot then cites your file when a
student asks something covered there.

**1. Turn on retrieval.** Edit `.env` and set:

```
RAG_ENABLED=true
```

This is `false` by default because the empty wiki doesn't need RAG and
turning it on costs ~30s at first startup (one-time index build). Once
you have your own content, you want it on.

**2. Put your file in the right place.** Filename in
`lower_snake_case.md`, dropped into the directory that matches its
topic:

```
seed_wiki/
├── school/        ← school identity, mission, philosophy
├── staff/         ← the bot's persona (only one file expected)
├── students/      ← one file per real learner
├── curriculum/    ← week-by-week scope, term plans
├── lessons/       ← lesson plans
├── vocabulary/    ← lexical chunks, term lists
├── pronunciation/ ← phonics, common-error patterns
├── grammar/       ← grammar references
├── assessment/    ← rubrics, exam patterns, formative techniques
└── references/    ← methodology, bibliography, recipes
```

If none of those fit, create a new top-level directory — e.g.,
`seed_wiki/handbook/` for your school handbook chapters, or
`seed_wiki/policies/` for SOPs. The indexer recurses automatically.

**3. Add frontmatter at the top of every file** (strongly recommended,
not strictly required):

```yaml
---
title: Year 10 Marking Rubric
type: assessment
status: live
topic: rubrics, exam marking, year 10
updated: 2026-05-19
---

# Year 10 Marking Rubric

(your content starts here)
```

The frontmatter helps you and the bot navigate. `status: live` is the
convention for "this is real, please use it"; pages without it are
treated as drafts. `topic:` is a free-text tag — list whatever a student
might ask about that should land them here.

**4. Force a reindex.** The orchestrator persists the index to disk, so
new files aren't picked up automatically — restart the orchestrator and
delete the index cache:

```bash
docker compose down
docker volume rm kru-eng-classroom_wiki_index
docker compose up -d
```

Watch the logs to confirm the rebuild ran:

```bash
docker compose logs orchestrator | grep -i index
```

You should see `building wiki index from /data/wiki (this happens once)`
followed by `wiki index built: N documents indexed`. If `N` is what you
expect (existing docs + your new ones), you're good.

**5. Verify it landed.** Ask the bot something only your new file
answers:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What is the Year 10 marking rubric for essays?","history":[]}' \
  | tail -c 200
```

The reply should include the content, and the orchestrator's response
metadata will include a `citations` array naming the file (e.g.,
`["assessment_year10_rubric"]`). If you get a generic reply with no
citation, the file either didn't index or RAG isn't enabled.

### What file formats actually work

The shipped indexer reads **`.md` files only** — that's by design
(corpus stays clean and reviewable; the bot reads the same files a
teacher can read). For other formats, convert to markdown first:

| You have | Tool | One-liner |
|---|---|---|
| `.docx` (Word) | pandoc | `pandoc handbook.docx -o handbook.md` |
| `.pdf` (text PDFs) | pandoc / pdftotext | `pdftotext -layout doc.pdf - > doc.md` |
| `.pdf` (scanned / layout-heavy) | marker | `marker_single scan.pdf out_dir` (best results) |
| `.pptx` (PowerPoint) | pandoc | `pandoc slides.pptx -o slides.md` |
| `.xlsx` (Excel) | pandoc / python | `pandoc data.xlsx -o data.md` (small tables); script for big sheets |
| Audio (lectures) | Whisper (already in this stack) | `curl -F "audio_file=@lecture.m4a" http://localhost:9000/asr?output=txt > lecture.md` |
| Images (whiteboards, handwriting) | A vision model — Ollama can run `qwen2.5vl` locally | Ask the model to transcribe; save output as `.md` |
| Scanned books (OCR) | Tesseract (`tesseract` CLI; supports Thai + English) | `tesseract page.png page -l tha+eng` |

**One topic per file.** A 200-page handbook is better split into
`handbook_chapter_1_admissions.md`, `handbook_chapter_2_dress_code.md`,
etc. The indexer chunks content automatically, but retrieval works
better when each file is internally coherent.

**Skip media files.** Don't put `.mp3`, `.png`, `.mp4` directly in the
wiki — they're ignored by the indexer. Transcribe or describe them in
markdown instead.

### Pointing the bot at a directory outside the repo

If your school's content lives somewhere else (a SharePoint mount, a
shared drive), you don't have to copy it into `seed_wiki/`. Point the
`WIKI_PATH` env var at the external directory instead, and bind-mount
that path into the orchestrator container. Edit `docker-compose.yml`:

```yaml
orchestrator:
  environment:
    WIKI_PATH: /data/wiki
  volumes:
    - /mnt/school-shared/kru-eng-content:/data/wiki:ro  # was ./seed_wiki
    - wiki_index:/data/wiki_index
```

Then a teacher dropping a new `.md` file into the shared drive is
indexed on the next reindex — no docker compose copy step.

### When to reindex

- **Adding new files** → reindex.
- **Substantively editing existing files** → reindex.
- **Fixing a typo** → don't bother; the chunks already in the index are
  fine for most retrieval.
- **Deleting files** → reindex (orphan chunks otherwise hang around).

## Customizing through Docker — three different ways

> **ภาษาไทย — ปรับแต่งระบบให้เข้ากับโรงเรียนของคุณ**
>
> มี 4 วิธีในการปรับแต่งระบบผ่าน Docker ขึ้นอยู่กับว่ากำลังจะแก้อะไร:
>
> 1. **แก้ไขแบบทันที** สำหรับเนื้อหาวิกิ (`seed_wiki/`) — ข้อมูลโรงเรียน บุคลิกของบอท โปรไฟล์นักเรียน หลักสูตร บทเรียน คำศัพท์ แค่แก้ไฟล์ในเครื่องแล้วรีสตาร์ต orchestrator (ไม่ต้องสร้างอิมเมจใหม่)
> 2. **สร้างอิมเมจใหม่** สำหรับโค้ดและไฟล์บทเรียน JSON — เปลี่ยน System Prompt หรือเพิ่มบทเรียนใหม่ ใช้คำสั่ง `docker compose up -d --build orchestrator`
> 3. **โหมดแก้บทเรียนแบบทันที** — เพิ่มเส้นทาง bind-mount ในไฟล์ override สำหรับครูที่กำลังเขียนบทเรียนใหม่และต้องการแก้ไขรวดเร็ว
> 4. **เข้า Container โดยตรง** สำหรับการทดลองสั้น ๆ (ข้อมูลหายเมื่อรีสตาร์ต)
>
> ตัวอย่างที่ใช้บ่อย: เพิ่มบทเรียนใหม่ • แก้บุคลิกครู (ครูจริงจัง ครูสบาย ๆ ครูแบบล้านนา) • ใส่ข้อมูลเกี่ยวกับโรงเรียน (คู่มือ ระเบียบ ปฏิทินวันหยุด) • เปลี่ยนโมเดลภาษาให้ใหญ่/เล็กลงตามฮาร์ดแวร์ • ปรับเสียงพูดของบอท — คำสั่งทั้งหมดดูจากส่วนภาษาอังกฤษด้านล่าง

> **中文 — 为贵校定制系统**
>
> 通过 Docker 定制系统有 4 种方式，根据要修改的内容来选择：
>
> 1. **热加载** — 修改 wiki 内容（`seed_wiki/`）：学校信息、机器人人设、学生档案、课程大纲、课程、词汇等。在本机编辑文件后重启 orchestrator 即可（无需重新构建镜像）。
> 2. **重新构建** — 修改代码和课程 JSON 文件：更改 System Prompt 或添加新课程。使用 `docker compose up -d --build orchestrator`。
> 3. **课程实时编辑模式** — 在 override 文件中添加 bind-mount 路径，适合正在编写新课程并需要快速迭代的老师。
> 4. **直接进入容器** — 用于短暂实验（数据会在重启后丢失）。
>
> 常见用例：添加新课程 • 修改老师人设（严厉型、轻松型、兰纳风格）• 添加贵校相关信息（手册、规章、节假日历）• 根据硬件调整模型大小 • 调整机器人的语音 — 完整命令见下方英文部分。

There are three places a school's customizations live, and each has its
own update path. Knowing which is which saves a lot of time.

| What you're changing | Where it lives | How it's wired |
|---|---|---|
| School info, persona, students, curriculum, lessons (wiki), grammar references, vocab lists | `seed_wiki/**/*.md` | **Bind-mounted** read-only into the orchestrator container — host edits land instantly inside the container |
| Lesson plans for the PPP engine (`/lesson` UI) | `orchestrator/lessons/*.json` | **Baked into the orchestrator image** at build time |
| The hard-coded `SYSTEM_PROMPT`, lesson grading code, endpoints | `orchestrator/main.py` | **Baked into the orchestrator image** at build time |
| Model choice, generation params, RAG settings, Edge voice names | `.env` | **Read at compose-up time** as environment variables |
| Voice clone reference WAVs | `voices/*.wav` | **Bind-mounted** read-only into the tts container |

### Way 1 — Hot reload (for wiki content)

Use this when you're editing **anything under `seed_wiki/`**: the
persona, the school identity, student profiles, curriculum, lessons
(the markdown ones, not the JSON), grammar, vocab, references.

```bash
# 1. Edit the file on the host (any editor)
notepad++ "C:\Users\Admin\claude\kru-eng-classroom\seed_wiki\school\about_kru_eng.md"

# 2. Restart just the orchestrator (~5 seconds)
docker compose restart orchestrator

# 3. If RAG is enabled and you added/edited substantive content, force a reindex
docker compose down
docker volume rm kru-eng-classroom_wiki_index
docker compose up -d
```

Why this is fast: `./seed_wiki` is bind-mounted into the container at
`/data/wiki`, so your host edit is the container's view. No image
rebuild, no Docker layer caching to fight.

### Way 2 — Rebuild (for code, system prompt, and lesson JSONs)

Use this when you're changing **`orchestrator/main.py`** (system prompt,
endpoints, grading logic) or **`orchestrator/lessons/*.json`** (the PPP
lesson plans). These are baked into the image at build time, so the
running container has a frozen copy — you have to rebuild.

```bash
# 1. Edit the file on the host
notepad++ "C:\Users\Admin\claude\kru-eng-classroom\orchestrator\lessons\past_simple.json"

# 2. Rebuild and restart (~30 seconds — Docker reuses cached layers)
docker compose up -d --build orchestrator
```

For lesson JSONs specifically, the loader picks them up automatically
on orchestrator startup — `_load_lessons()` scans `/app/lessons/*.json`
at import time. Add a file, rebuild, and it appears in
`GET /lesson/list` next time you call it.

### Way 3 — Hot reload for lessons too (optional setup)

If you're iterating fast on lesson JSONs and don't want to rebuild
every time, add a bind mount in your `docker-compose.override.yml`:

```yaml
services:
  orchestrator:
    volumes:
      - ./orchestrator/lessons:/app/lessons:ro
```

Then host edits to `orchestrator/lessons/*.json` show up after
`docker compose restart orchestrator` — no rebuild needed. Useful for
lesson authors; not needed for school admins who only edit lessons
once in a while.

### Way 4 — Live exec (for quick experiments only)

For a five-second tweak before you decide whether to commit, you can
edit inside a running container. Lost on the next restart, so this is
only for "let me try something":

```bash
# Get a shell inside the orchestrator
docker exec -it krueng-orchestrator sh

# Inside the container:
vi /data/wiki/staff/kru_eng_persona.md   # if you have vi installed
# or:
apk add nano 2>/dev/null || apt-get install -y nano   # depending on base image
nano /data/wiki/staff/kru_eng_persona.md
```

Edits to `/data/wiki/...` ARE persisted to the host (because it's
bind-mounted), so this is actually the same as Way 1 with extra steps.
Edits to `/app/...` (orchestrator code or lessons) are container-only
and disappear on restart.

### Recipes

**To add a new lesson** (e.g., "present perfect"):

```bash
cp orchestrator/lessons/past_simple.json orchestrator/lessons/present_perfect.json
# Edit present_perfect.json — change id, title, p1_examples, p2_exercises, p3_scenarios, p3_system_prompt
docker compose up -d --build orchestrator
curl http://localhost:8000/lesson/list   # verify it appears
```

**To modify the teacher's personality** (the bot's voice and style):

```bash
# Edit the persona file
notepad++ seed_wiki/staff/kru_eng_persona.md
# Restart — no rebuild needed
docker compose restart orchestrator
```

Note that the **runtime system prompt is hardcoded** in
`orchestrator/main.py`, separate from the persona doc. The persona doc
shapes the bot's behavior only through RAG retrieval. If you want a
fundamental change to how the bot opens every conversation, edit the
`SYSTEM_PROMPT` constant in `orchestrator/main.py` (Way 2).

**To add information about the school** (handbook, history, mission,
phone numbers, holiday calendar, anything the bot should answer about
your institution):

```bash
# Pick a topic, write a markdown file with frontmatter
notepad++ seed_wiki/school/holiday_calendar_2026.md
# Restart + reindex
docker compose down
docker volume rm kru-eng-classroom_wiki_index
docker compose up -d
```

The `school/` subdirectory is the conventional home for institution-
identity content. For volume (whole handbook chapters, SOP libraries),
make a new top-level directory like `seed_wiki/handbook/` or
`seed_wiki/policies/`.

**To change the model** (e.g., switch from `qwen2.5:3b` to `qwen2.5:7b`
or `llama3.2:3b`):

```bash
# 1. Make sure the model is pulled into Ollama
python scripts/pull_models.py   # uses MODEL from .env

# 2. Edit .env
notepad++ .env   # change MODEL=qwen2.5:7b

# 3. Restart — .env is read fresh on container start
docker compose up -d
```

No rebuild needed because the model name is an env var, not baked into
the image.

**To tune voice settings** (e.g., switch the English Edge TTS voice
from Jenny to Aria):

```bash
# Edit .env
notepad++ .env   # change EDGE_VOICE_EN=en-US-AriaNeural

# Restart the tts service
docker compose up -d tts
```

[List of available Edge TTS voices](https://github.com/rany2/edge-tts#changing-the-default-voice)
— common ones: `en-US-AriaNeural`, `en-US-GuyNeural`, `en-GB-SoniaNeural`,
`th-TH-PremwadeeNeural`, `th-TH-NiwatNeural`.

### Putting it together — a typical school customization session

```bash
# Stop everything cleanly
docker compose down

# Update your school identity
notepad++ seed_wiki/school/about_kru_eng.md

# Add a new student profile
cp seed_wiki/students/learner_profile_template.md seed_wiki/students/somchai.md
notepad++ seed_wiki/students/somchai.md   # fill in name, level, interests

# Add a new lesson based on past_simple
cp orchestrator/lessons/past_simple.json orchestrator/lessons/present_continuous.json
notepad++ orchestrator/lessons/present_continuous.json   # rewrite content

# Adjust the model and turn on RAG
notepad++ .env   # MODEL=qwen2.5:7b, RAG_ENABLED=true

# Bring it back up — single command, rebuilds the orchestrator (for the
# new lesson), restarts everything else, picks up .env, rebuilds the
# index (because we just blew away the volume below)
docker volume rm kru-eng-classroom_wiki_index 2>/dev/null
docker compose up -d --build

# Verify
curl http://localhost:8000/health
curl http://localhost:8000/lesson/list
```

That's the full customization loop.

## Endpoints

> **ภาษาไทย — Endpoints (API ของระบบ)**
>
> หน้าเว็บสำหรับนักเรียนและครูอยู่ที่ **http://localhost:8000** ตารางด้านล่างเป็นรายการ REST API ทั้งหมด ใช้เมื่อต้องการสร้างแอปพลิเคชันของคุณเองที่เชื่อมต่อกับ Kru Eng (เช่น บอท LINE ของโรงเรียน หรือระบบแสดงผลการเรียนของนักเรียน)
>
> Endpoint หลักที่น่าสนใจ:
> - `GET /` — หน้าเว็บใช้งานจริง (ไมค์ + ลำโพง) มีลิงก์ไปหน้าฟีเจอร์อื่น ๆ ด้านบน
> - `GET /health` — ตรวจสอบว่าระบบพร้อมใช้งาน
> - `POST /chat` — ส่งข้อความ ได้คำตอบเป็นสตรีม
> - `POST /converse` — ส่งเสียง ได้คำตอบเป็นเสียงพร้อมเนื้อหา
> - `GET /lesson` — หน้าเว็บบทเรียนแบบมีโครงสร้าง (PPP: Presentation → Practice → Production)
> - `GET /calendar` + `GET/POST/DELETE /calendar/events` — ปฏิทินโรงเรียน (เหตุการณ์ของโรงเรียน + เหตุการณ์ที่เพิ่มผ่าน UI)
> - `GET /exam` + `GET /exam/list` + `GET/POST /exam` + `POST /exam/{id}/submit` — สร้างและทำข้อสอบ (ตรวจให้คะแนนแบบ deterministic)
> - `GET /whiteboard` + `POST /whiteboard/analyze` — กระดานวาด พร้อมตัวเลือกขอความคิดเห็นจากโมเดลภาพ (`qwen2.5vl:3b`)

> **中文 — Endpoints (系统 API)**
>
> 学生和老师使用的网页在 **http://localhost:8000**。下方表格列出所有 REST API — 当您需要构建自己的应用程序与 Kru Eng 集成时使用（例如学校的 LINE 机器人，或学生成绩展示系统）。
>
> 主要 endpoint：
> - `GET /` — 实际使用网页（麦克风 + 扬声器），顶部有指向其他功能页的链接
> - `GET /health` — 检查系统是否就绪
> - `POST /chat` — 发送文本，获取流式回复
> - `POST /converse` — 发送语音，获取语音回复（含文本）
> - `GET /lesson` — 结构化课程网页（PPP: Presentation → Practice → Production）
> - `GET /calendar` + `GET/POST/DELETE /calendar/events` — 学校日历（docs 事件 + UI 添加的共享事件）
> - `GET /exam` + `GET /exam/list` + `GET/POST /exam` + `POST /exam/{id}/submit` — 试题创建与提交（评分为确定性）
> - `GET /whiteboard` + `POST /whiteboard/analyze` — 白板，可选视觉模型反馈（`qwen2.5vl:3b`）

The orchestrator exposes these on port 8000:

| Endpoint | Purpose |
|---|---|
| `GET  /` | Web UI (mic + speaker) with nav chips to Lesson / Calendar / Exam / Whiteboard |
| `GET  /health` | Per-backend status (used by UI footer) |
| `POST /chat` | `{message, history}` → streaming text reply |
| `POST /converse` | Multipart audio in → `{user, bot, audio, visemes}` |
| `POST /speak` | `{text}` → audio (TTS only — handy for testing) |
| `GET  /lesson` | Scaffolded PPP lesson UI |
| `GET  /lesson/list` | List available lesson plans |
| `GET  /calendar` | Month-view calendar HTML page |
| `GET  /calendar/events` | List docs + shared events. Optional `?from=YYYY-MM-DD&to=YYYY-MM-DD` filter (Asia/Bangkok) |
| `POST /calendar/events` | Add a shared event. Off-by-default `X-Teacher-Pass` gate via `CLASSROOM_CALENDAR_TEACHER_PASS` env |
| `DELETE /calendar/events/{id}` | Remove a shared event. Returns 400 for docs events (immutable — edit `seed_wiki/calendar/school_events.json` in git instead) |
| `GET  /exam` | Exam list / take / results UI |
| `GET  /exam/list` | List every exam on disk (metadata only — no questions or answers) |
| `GET  /exam/{id}` | Fetch an exam with answer keys stripped (server still knows which options are correct for grading) |
| `POST /exam` | Create a teacher-authored exam. JSON body: `{title, lesson_id, cefr, exercises: [{prompt, options or blanks, ...}]}` |
| `POST /exam/{id}/submit` | `{answers: [[str,...], ...]}` → score + per-question grading. Deterministic, no LLM in the scoring path |
| `GET  /whiteboard` | Drawing canvas page |
| `POST /whiteboard/analyze` | `{image: "data:image/png;base64,..."}` → `{description, vocab, encouragement}` via `qwen2.5vl:3b` vision model |

## Day-2 operations

```bash
docker compose ps                # check all services are up
docker compose logs -f orchestrator
docker compose logs -f tts       # watch on first request — XTTS download is slow
docker compose down              # stop
docker compose down -v           # stop + delete model volumes (frees ~15 GB)
```

## Configuration reference

All knobs live in `.env`. See `.env.example` for the full annotated list.
The headline ones:

| Variable | Default | What it does |
|---|---|---|
| `MODEL` | `qwen2.5:3b` | Any tag from https://ollama.com/library |
| `WHISPER_MODEL` | `small` | `tiny` / `base` / `small` / `medium` / `large-v3` |
| `TTS_DEVICE` | `cpu` | Set to `cuda` once you wire GPU into the tts image |
| `RAG_ENABLED` | `false` | Set to `true` to ground replies in `seed_wiki/` |

## Known limitations

- **First `/synthesize` for ja/ko is slow** — XTTS v2 weights (~2 GB)
  download lazily on first non-en/th/zh call. English, Thai, and Chinese
  go through Edge TTS so they have no warmup penalty.
- **CPU XTTS is slow.** ~0.3× realtime for ja/ko. Switch the tts Dockerfile
  to a CUDA torch wheel + uncomment the GPU stanza in compose for usable
  latency on those languages.
- **No persistent chat history.** `/converse` is single-turn server-side.
  The UI keeps history in JS and passes it to `/chat`. Add a session store
  (Redis/SQLite) when you want multi-device continuity.
- **GPU on Windows** needs Docker Desktop WSL2 + NVIDIA Container Toolkit.
  The compose file has the GPU block commented out — uncomment when set up.
- **Edge TTS needs internet.** It's a free Microsoft service. If your
  school's connection is offline, English/Thai TTS falls back to nothing.
  For fully-offline TTS, swap Edge TTS for Piper in `tts/server.py`.

## File layout

```
kru-eng-classroom/
├── docker-compose.yml
├── .env.example
├── README.md (this file)
├── LICENSE (MIT)
├── orchestrator/                 # FastAPI app: STT → LLM → TTS glue
│   ├── Dockerfile
│   ├── main.py                   # /chat, /converse, /speak, /lesson, /health
│   ├── requirements.txt
│   ├── static/                   # Web UI (mic + speaker, lesson page)
│   └── lessons/                  # Lesson plan JSONs (PPP scaffolds)
├── tts/                          # TTS service: Edge TTS + XTTS v2 + Rhubarb
│   ├── Dockerfile
│   ├── server.py
│   └── requirements.txt
├── voices/                       # Drop WAV reference clips here for XTTS cloning
│   └── README.md
├── seed_wiki/                    # The bot's brain — edit this for your school
│   ├── INDEX.md
│   ├── README.md
│   ├── school/                   # Identity, mission, methodology
│   ├── staff/                    # Bot persona (the system prompt)
│   ├── students/                 # Per-learner profiles
│   ├── curriculum/               # 12-week scope
│   ├── lessons/                  # Weekly lesson markdown
│   ├── vocabulary/               # Lexical chunks
│   ├── pronunciation/            # Thai L1 interference patterns
│   ├── grammar/                  # Form-meaning-use
│   ├── assessment/               # Formative techniques
│   └── references/               # Methodology + bibliography
└── scripts/
    └── pull_models.py            # Bootstrap Ollama after first compose up
```

## What this is not

- **Not a SaaS.** There is no cloud version. There is no account. You run it.
- **Not a finished commercial product.** It's a working tool, polished
  where it needed to be, rough where it didn't. PRs and forks welcome.
- **Not a replacement for a teacher.** It's a practice partner. Use it for
  the speaking drills your teachers don't have time for.
- **Not legal advice.** If your school's PDPA officer wants a data-flow
  diagram, the architecture section above is your starting point. Talk to
  them.

## Contributing

PRs welcome. The code is intentionally small — ~700 lines of Python for
the orchestrator, ~300 for the TTS service. Read both files before
proposing structural changes.

Issues from teachers who've tried to deploy this are particularly valuable
— if you got stuck somewhere, that's a documentation bug.

## License

Code: MIT (see [LICENSE](./LICENSE)).

AI models you'll download are governed by their own licenses (Qwen, Whisper,
XTTS v2, Edge TTS) — also documented in [LICENSE](./LICENSE). The default
configuration routes English, Thai, and Chinese through Edge TTS, leaving
XTTS v2 only for Japanese/Korean — keep that in mind for commercial use,
since XTTS is non-commercial.

## Credits

Built in Chiang Mai by the [krueng.ai](https://krueng.ai) project — a free
bilingual TEFL site for Thai learners of English. If this stack helps your
school, the best thank-you is a note saying so.

Made with care for Thai students. ขอบคุณค่ะ.
