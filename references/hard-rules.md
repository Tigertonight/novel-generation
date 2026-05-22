---
name: hard-rules
description: Non-negotiable craft rules for character entrance, interiority, intimacy, relationships, mechanism continuity, payoff design, jargon control, chapter packet, and audit. Read before every chapter packet, every chapter draft, and every audit. Bilingual (Chinese primary, English summary).
type: hard-rules-spec
---

# Hard Rules / 硬性约束

> 这是 novel-generation skill 的"宪法"。Phase 6（章节包）、Phase 7（章节生成）、Phase 8（审计）开始前必须读完本文件。
> Read this file before Phase 6 (chapter packet), Phase 7 (chapter drafting), and Phase 8 (audit). Violations are P0 (must fix) or P1 (should fix), not optional polish.

These rules apply during planning, generation, and audit — **not as final-pass polish**. If a rule is violated and the chapter is treated as finalized, the audit must reopen it.

---

## 0. 优先级总则 / Priority

- 这 9 条规则**优先于**任何"风格优先"、"信息密度优先"、"商业节奏优先"的局部决策。
- 如果章节包、章节正文、审计三者之一遗漏了本文件中的硬性字段，按 P0 处理。
- 第 1、3、5、6、7、9 条违反时，章节**必须**重写或修复。第 2、4、8 条违反时**应**修复，连续 3 章违反同一条升 P0。

EN: These nine rules outrank local decisions about style, information density, or commercial pacing. If any required field is missing from packet, draft, or audit, that's P0. Items 1/3/5/6/7/9 are mandatory rewrite triggers; items 2/4/8 escalate to P0 after 3 consecutive violations.

---

## 1. 人物出场与外貌描写 / Character Entrance & Appearance

任何重要人物、命名人物、反复出现的人物**第一次出场**时，不能只丢一个名字或职位。详细模板见 `character-entrance-craft.md`。最低门槛 5 锚点：

1. **身份锚点**：他是谁——职位、关系、阵营、社会位置或当前场景功能
2. **外貌/物理锚点**：脸、身形、年龄感、衣着、姿态、声音、动作、气味、伤痕、随身物件，至少一项具体细节
3. **场景关联锚点**：为什么此刻在这里，和当前冲突什么关系
4. **POV/社会阅读锚点**：主角或旁人如何理解、误解、忌惮、轻视、尊敬、欲望或排斥他
5. **行为钩子**：一句话、一个动作、一个习惯、一个选择、一个压力反应

**第一人称**：通过叙述者的偏见、记忆、情绪、欲望过滤——不要冷镜头平铺。
**第三人称**：通过近距离感知、旁人反应或场景压力建立——不要冷冰冰的镜头平铺。

**人物卡叠加**：重要人物建立稳定外貌锚点 + 当前状态叠加（受伤、战损、疲惫、伪装、礼服、贫穷/富贵展示、权力地位变化、情绪变化）。后续描写禁止反复使用"漂亮""冷峻""高大"等泛词；要用可记忆的外貌、姿态、行为和他人反应。

走过场的功能性人物：至少给"角色 + 一个视觉/行为细节 + 当下相关性"。

**P0 必修**：新出场重要人物只有名字或职位，没有上面 5 锚点中至少 4 项。
**P1 应修**：重要人物连续 2 章只用泛词描写、没有可记忆的外貌或行为细节。

EN: Every named or recurring character must enter with 5 anchors: identity, visual/physical, scene-relevance, POV/social reading, behavioral hook. First person filters through narrator bias; third person uses close perception or social reaction. Maintain stable anchors + current-state overlays. Avoid generic "beautiful/cold/tall" repetition. P0 if a major entrance hits fewer than 4 of 5 anchors. See `character-entrance-craft.md`.

---

## 2. 人物内心与沉浸感 / Interiority & Immersion

当前文本容易像第三视角事件汇报，缺少内心，沉浸感不足。每个重要场景必须有**外部事件变化 + 内部状态变化**。

每个重要场景至少包含一种**内心节拍**：

- **本能反应**：还没控制住的第一反应
- **被压下去的念头**：不愿说出口、甚至不愿想完的内容
- **身体-心理桥接**：呼吸、心跳、手指僵硬、喉咙发紧、胃部发沉、迟来的疼痛
- **记忆碎片**：一句旧话、一个画面、一个伤口被当下触发
- **误读与判断**：POV 如何理解对方动作（可能正确也可能错误）
- **欲望/恐惧闪念**：他想要什么，为什么这件事危险
- **自我欺骗**：角色在这一刻骗自己的话
- **情绪余波**：对话、亲密、胜利、羞辱、失败之后留下的内在回响

**节奏**：外部事件 → 内心压力 → 行动选择 → 后果 → 情绪余波。**禁止**长篇心理解释；用短促但有效的内心落点。

**章节包必须写明 `POV/interior turn`**：本章结束时，角色的私下理解、欲望、恐惧、自欺、信任、羞耻发生了什么变化。

**P0 必修**：一个重要情绪场景（重要对话、亲密、羞辱、胜利、失败之后）几乎没有内心描写。
**P1 应修**：章节出现镜头式、汇报式、纯第三视角段落连续超过约 600 字（中文）/ 400 词（英文）。

EN: Every important scene needs both an external event change and an internal state change. Required interior beat types: instinct, suppressed thought, body-mind bridge, memory shard, misread, desire/fear flash, self-deception, emotional aftertaste. Rhythm: external event → inner pressure → action → consequence → aftertaste. Chapter packet must specify `POV/interior turn`. P0 if a key emotional scene has near-zero interiority. P1 if camera-only passages exceed ~600 zh-chars / 400 en-words.

---

## 3. 亲密关系与激情描写机制 / Intimacy as Mechanism

如果项目包含感情线、暧昧、婚恋、多女主/后宫、欲望或床戏，亲密**不能**只是奖励或插入段落。亲密必须是关系推进机制。详细模板已在 `intimacy-craft.md`，本节是**硬性附加要求**：

**亲密设计卡**（每组重要亲密关系一份）：关系前提；双方欲望线（想要但不敢承认）；双方恐惧线（害怕失去什么）；边界（什么可以、什么不可以、什么暂时不可以）；禁忌压力（身份、阵营、道德、职业、阶级、婚姻、秘密）；热度语言（斗嘴/沉默/凝视/触碰/照料/吃醋/救援/日常/危险）；第一次暧昧；第一次自愿脆弱；第一次触碰或险些触碰；第一次私密场景；第一次破裂；第一次修复；第一次亲密或淡出；事后模式；长期变化。

**热度阶梯（0-10）**——禁止跳级，除非剧情和心理基础足够：

```
0  注意到对方
1  摩擦/斗嘴/误解
2  开始在意细节
3  被迫靠近或共享空间
4  保护欲、占有欲、吃醋
5  触碰阈值：意外触碰、疗伤、整理衣物、训练
6  私密脆弱：羞耻、旧伤、恐惧被看见
7  欲望间接显露：玩笑、克制、回避、梦境、行动式告白
8  边界协商：可以、不可以、还不行、除非……
9  亲密：接吻、淡出、感官亲密、明确成人场景
10 事后：温柔、尴尬、秘密、愧疚、承诺、关系破裂或危险升级
```

**场景功能**（每个亲密/暧昧场景必须明确）：诱惑/照料/权力测试/吃醋/边界协商/信任/破裂/修复/亲密完成/事后余波。

**亲密场景必须改变至少一项**：信任、权力、秘密、依赖、承诺、恐惧、关系状态、外部风险、后续选择。**没有后果的亲密场景是可删段落**——必须重写。

**伦理底线**：成人、同意、边界与用户设定的露骨程度。强迫、伤害、无同意**不能**写成奖励；如属剧情，必须以伤害和后果方式处理。

**P0 必修**：亲密场景没有边界、没有后果或没有关系状态变化；强迫/伤害被当成奖励；热度跳级且无心理铺垫。
**P1 应修**：场景换成任意一对人物都成立（缺乏角色专属欲望）；无事后落点。

EN: Intimacy is a relationship engine, not a reward. Each pair gets an intimacy design card. Strict 0-10 heat ladder — no skipping without psychological setup. Every intimate scene declares one function (temptation/care/power/jealousy/boundary/trust/rupture/repair/consummation/aftermath) and must change at least one of: trust/power/secret/dependency/commitment/fear/relationship state/external risk/future choice. P0 if scene lacks boundary/consequence/state change, or treats coercion as reward, or skips heat tiers without basis. See `intimacy-craft.md`.

---

## 4. 感情线与人物关系推进 / Relationship Progression

事业线不能压过感情线。每个重要关系维护**关系状态线**（详细字段见 `bible-and-ledgers.md` 的关系状态格式）：

- 当前信任程度
- 表面关系 / 私下真实关系
- 吸引/排斥
- 权力平衡
- A 想从 B 得到什么 / B 想从 A 得到什么
- 边界
- 秘密/误会
- 最近变化
- 互动频率目标
- 热度/亲密阶段
- 下一次压力测试
- 可能加深的方式 / 可能破裂的方式

**强制规则**：只要一个场景中出现重要关系，就必须**测试、加深、复杂化或澄清**这段关系。不能很多章关系静止不动。

**推进方式**：行动、误读、克制、代价、共同秘密、照料、保护、争执、修复——而**不是**只靠表白或解释。

**P0 必修**：重要感情线/关系连续 5 章关系状态线无任何变化（仍处理同一信任/权力/边界状态），且项目包含感情线承诺。
**P1 应修**：重要关系出现在场景中但未被测试、加深、复杂化或澄清。

EN: Career line cannot crush relationship line. Each important relationship has a state line; whenever it appears in a scene, the scene must test/deepen/complicate/clarify it. Progression via action, misread, restraint, cost, shared secret, care, protection, conflict, repair — not declarations or explanations. P0 if 5+ consecutive chapters leave a promised romance line stagnant.

---

## 5. 关键道具、线索、武器、系统、机制不能写丢 / Mechanism Continuity

重要道具、线索、武器、系统、机缘、能力、资源、契约、称号、身份要有贯穿性和成长性。前期重点写了，后面**不能**消失。

**关键物/机制台账**字段（详细格式见 `bible-and-ledgers.md`）：

- ID / 名称 / 类型（武器/系统/道具/线索/资源/契约/能力）
- 当前拥有者 / 控制者
- 当前地点 / 当前状态
- 已知规则 / 未知深层规则
- 使用代价 / 限制
- **失败模式**（这次没用上时为什么）
- **敌方反制方式**（敌人如何应对）
- 升级/变形路径
- 上一次出场或使用 / 下一次压力测试
- 回收、升级、损毁、转化或退场目标

**贯穿规则**：被强调过的物件/机制必须以下列方式之一回归——payoff、损毁、升级、转化、反噬、被敌人克制、正式退场。**不能无声消失**。

**反爽规则**：系统、武器、能力**不能**只让主角无脑赢。每次使用必须说明：为什么此刻能用、什么代价、为什么不能无限用、敌人如何应对、主角学到了什么。

**P0 必修**：前期被强调过 2 次以上的道具/系统/武器/机缘连续 8 章未出现且无退场说明；同一能力连续无代价无反制使用 5 次以上。
**P1 应修**：单次使用未说明代价或敌方反制。

EN: Important objects/clues/weapons/systems must persist and evolve — never silently disappear. Ledger tracks failure mode and enemy counter as required columns. Each use shows when/why available, cost, why not infinite, enemy response, what the protagonist learned. P0 if a twice-emphasized mechanism vanishes for 8+ chapters with no retirement; or if an ability is used 5+ times with no cost or counter.

---

## 6. 爽点设计 / Payoff Design: Frequency, Depth, Variety, Growth

爽文不能只靠"敌人嘲讽 → 主角打脸"单一模式。爽点要有**节奏、种类、升级、代价**。

**爽点/回报台账**字段：

- 章节 / 爽点类型
- **前置铺垫**（哪几章铺的）
- 当场回报
- 代价/后果
- **下一次升级方向**

**爽点类型库**（必须轮换，避免单一）：

- 能力证明
- 打脸 / 公开纠偏
- 升级、技能、等级、称号
- 资源、金钱、地盘、权限
- 武器/神器/系统功能揭示
- 身份反转
- 线索揭露
- 救援、复仇、保护、逃脱
- 亲密升温、吃醋、承诺、关系重新定义
- 阵营扩张、盟友加入、声望提升
- 尊严恢复、被正确看见、情绪宣泄

**批次设计要求**：每个 5-10 章批次必须设计**爽点组合**，不是重复同一种。爽点要通过**见证者、代价、后续敌人、关系变化、身份变化、世界压力升级**来加深。

**P0 必修**：商业/爽文项目连续 3 章无任何有效爽点；或一个批次（5-10 章）内同一爽点类型出现超过 60%。
**P1 应修**：爽点没有铺垫或没有后续代价。

EN: Avoid single-mode payoff (insult → face-slap). Each payoff entry tracks setup, on-page reward, cost/consequence, and next escalation direction. Rotate from a typed library; deepen through witnesses, cost, enemy response, relationship/identity/world-pressure shifts. P0 if a commercial project goes 3 chapters with no effective payoff, or if any 5-10 chapter batch is >60% one type.

---

## 7. 事业线、工作线与专业术语降噪 / Career & Jargon De-Noise

事业类、工作类、行业专业名词偏多会让读者跳戏。详细模板见 `immersion-and-jargon-control.md`，本节是**硬性附加要求**：

**写任何术语/流程/行业规则/公司制度/法律/金融/娱乐圈/医学/电竞/商业**之前先问：

- 读者是否真的需要这个术语，还是只需要知道**后果**？
- 这个信息影响了**谁的欲望或恐惧**？
- 它**改变了什么关系**？
- 它制造了什么**选择、羞辱、风险、金钱、地位、权限或亲密压力**？
- 能不能通过**行动、文件、最后期限、公众反应、具体代价**来表现？
- 能不能等读者**关心之后**再解释？

**术语翻译阶梯**——默认用 1-3，少用 5：

```
1. 只写后果：如果失败，她明早就会失去合同。
2. 通俗说法：赞助商可以撤资。
3. 一个精确术语 + 立刻给上下文。
4. 通过冲突或对白做短解释。
5. 完整专业解释（仅当专业能力本身是爽点时）。
```

**事业线压缩**：除非用户明确要职场专业文，工作场景通常应**短于**关系、冲突、情绪后果、爽点场景。**不要**连续多场写会议、文件、指标、流程、策略、术语。

**事业线必须绑定至少一项**：人物关系变化 / 竞争背叛暧昧信任 / 地位变化 / 公众压力 / 金钱或资源代价 / 羞辱或尊严恢复 / 道德选择 / 爽点回报。

专业能力应该表现为**压力下的行为**，而不是讲课。

**P0 必修**：事业线/专业解释挤压人物关系超过章节 50% 篇幅，且项目不是职场专业文；连续 2 章主要内容是流程/会议/文件/术语而无情感/关系/爽点回报。
**P1 应修**：单个专业术语未翻译为后果或冲突。

EN: Translate jargon into consequence first. Use ladder rungs 1-3 by default; rung 5 only when expertise is itself the payoff. Career scenes shorter than relationship/conflict/payoff scenes unless workplace-procedural is the contract. Career beat must bind to at least one of: relationship shift / rivalry-betrayal-flirtation-trust / status / public pressure / money or resource cost / humiliation or dignity / moral choice / payoff. P0 if career/jargon eats >50% of a chapter in non-workplace projects, or 2+ consecutive chapters are mostly process.

---

## 8. 章节生成前必须有章节包 / Chapter Packet Required

每章生成前**不能**只看上一章概要。完整模板已在 `chapter-production.md`，章节包必须填齐以下字段：

- **本章任务**：剧情功能、必写事件、必须铺垫或回收的内容
- **POV 角色**
- **本章外部目标**
- **本章私下情绪目标**（与外部目标分轨）
- **角色内心压力**
- **本章价值转变**（trust→suspicion / safety→danger / 等）
- **新人物出场**与入场 5 锚点（按第 1 条逐项）
- **人物外貌/当前状态描写需求**
- **关系推进/热度推进**
- **亲密场景功能和边界**（如果有）
- **关键物/系统/线索状态**（前后对比）
- **本章爽点/回报**及与最近 3 章爽点的差异化
- **专业信息预算**（最多新术语数）
- **必须避免的术语堆砌**（明确列出哪些不要用）
- **结尾钩子或情绪余波**

生成章节时**写向章节包**，不是只顺着上一章续写。

**P0 必修**：章节包缺少 POV / 价值转变 / 内心目标 / 新人物锚点（如有）/ 爽点设计（爽文项目）任一字段。

EN: Before drafting any chapter, assemble a packet with all fields above. The chapter writes toward the packet, not toward the previous chapter's flow. P0 if packet is missing POV, value shift, interior goal, new-character anchors, or payoff design (for commercial projects).

---

## 9. 审计标准 / Audit Standard

每章和每个批次必须审计以下问题。详细 checklist 已在 `audit-protocol.md`，本节列出**必修 P0 与应修 P1 的明确划分**：

### 章节级审计问题
- 新人物是否有身份、外貌/物理、场景关联、POV/社会阅读、行为锚点？
- 重要人物是否有可记忆的外貌、行为或侧面反应？
- 章节是否有内心转变，而不只是外部事件？
- 是否有镜头式、汇报式、纯第三视角段落过长？
- 感情线是否推进？
- 暧昧/亲密是否有场景功能、边界、后果？
- 关键道具、系统、武器、线索是否有状态更新？
- 前期重要机制是否被遗忘？
- 爽点频率是否足够？爽点类型是否重复？
- 事业/工作/专业内容是否压过人物和关系？
- 专业术语是否可以改成后果、冲突或情绪压力？
- 本章是否真正改变了人物、关系、状态、认知、资源、地位或世界压力？

### P0 必修清单（出现即必须修复）

1. **新人物只出现名字或职位，没有 5 锚点中至少 4 项介绍**
2. **重要人物出场没有外貌、行为或他人反应**
3. **一个重要情绪场景几乎没有内心描写**
4. **亲密场景没有边界、后果或关系状态变化；强迫/伤害被写成奖励**
5. **前期被强调过 2 次以上的道具/系统/武器/机缘连续 8+ 章消失且无退场说明**
6. **商业/爽文项目连续 3 章没有有效爽点；或单批次 60%+ 同一爽点类型**
7. **事业线和专业解释喧宾夺主——挤压人物关系超过章节 50%（非职场文项目）**
8. **专业术语让阅读产生明显断点（未翻译为后果或冲突）**
9. **重要关系连续 5+ 章状态线无变化（含感情线承诺的项目）**
10. **章节包缺失第 8 条要求的关键字段**
11. **同一能力连续 5 次无代价无反制使用**

### P1 应修清单（连续 3 次升 P0）

- 重要人物连续 2 章只用泛词描写
- 镜头式段落连续超过约 600 字（中文）/ 400 词（英文）
- 重要关系出现在场景中但未被测试、加深、复杂化或澄清
- 单次能力使用未说明代价或敌方反制
- 爽点没有铺垫或没有后续代价
- 单个专业术语未翻译为后果或冲突
- 亲密场景换成任意一对人物都成立

### 整体目标 / North Star

> 小说应该更像**贴着人物呼吸推进的故事**，而不是设定说明、事业报告或事件流水账。读者要记得住人，看得见人，感受到关系升温，期待关键物和机制回收，持续获得变化丰富的爽点，并始终被人物命运和关系牵引。

EN: A novel that breathes alongside its characters — not a setting manual, career report, or event ledger. Readers remember people, see them, feel relationships warming, anticipate mechanism payoffs, receive varied escalating rewards, and stay pulled by character fate and relationships.

---

## 章节包快速模板 / Quick Chapter Packet (Copy-Paste)

```markdown
# Chapter NNN Packet

## 本章任务 / Mission
- 剧情功能：
- 必写事件：
- 必须铺垫：
- 必须回收：

## POV
- POV 角色：
- 叙述距离（close / medium-close / cinematic+interior）：

## 双轨目标 / Dual Goals
- 外部目标：
- 私下情绪目标：

## 内心压力 / Inner Pressure
- 主导情绪（耻/欲/惧/骄/疚/疑/望/妒/痛）：
- 身体-心理桥接：
- 被触发的记忆/旧伤：
- 留作未完成的念头：

## 价值转变 / Value Shift
- 起点状态 → 终点状态（如 trust → suspicion）：

## 新人物 / New Character Entrances
（每个新人物逐项填，按硬规则第 1 条 5 锚点）
- 姓名：
  - 1 身份锚点：
  - 2 外貌/物理锚点：
  - 3 场景关联锚点：
  - 4 POV/社会阅读锚点：
  - 5 行为钩子：

## 人物外貌/当前状态 / Appearance State
- 谁需要更新：
- 稳定锚点 vs 当前叠加（伤、累、伪装、礼服、贫富、权势、情绪）：

## 关系推进 / Relationship & Heat
- 涉及关系（A/B）：
- 起点状态 → 终点状态：
- 推进方式（行动/误读/克制/代价/共同秘密/照料/保护/争执/修复）：
- 热度阶梯位置：N → N'

## 亲密场景（如有）/ Intimacy
- 场景功能：
- 边界与同意：
- 必须改变的至少一项：

## 关键物/系统 / Mechanism State
- 涉及条目（ID）：
- 章前状态 → 章后状态：
- 本次代价/反制/学到什么：

## 爽点 / Payoff
- 类型：
- 前置铺垫（哪几章）：
- 当场回报：
- 代价/后果：
- 与最近 3 章爽点的差异化：
- 下一次升级方向：

## 专业信息预算 / Jargon Budget
- 允许新术语数（默认 0-2）：
- 必须避免的术语堆砌：
- 每个术语的后果/冲突翻译：

## 结尾 / Hand-off
- 结尾钩子：
- 情绪余波：
- POV/interior turn 一句话总结：
```

---

## 审计快照清单 / Audit Snapshot (Copy-Paste)

```markdown
# Chapter NNN Audit Snapshot — Hard Rules Pass

## P0 必修（任意一项命中即重写或修复）
- [ ] 新人物 5 锚点齐全（至少 4/5）
- [ ] 重要情绪场景有内心描写
- [ ] 亲密场景有边界 + 后果 + 关系状态变化（如有亲密）
- [ ] 前期重点道具/机制未无声消失（≥8 章未现需说明）
- [ ] 爽点类型无同批 60%+ 重复（爽文项目）
- [ ] 事业/术语未挤压关系超 50%（非职场文）
- [ ] 重要关系未连续 5 章静止（含感情线承诺项目）
- [ ] 章节包字段齐全
- [ ] 能力使用有代价或反制

## P1 应修
- [ ] 无连续 600 字以上镜头式段落
- [ ] 关系出现即被测试/加深/复杂化/澄清
- [ ] 爽点有铺垫和代价
- [ ] 专业术语已翻译为后果
- [ ] 亲密场景具角色专属性

## 北极星问题
本章是否真正改变了：人物 / 关系 / 状态 / 认知 / 资源 / 地位 / 世界压力？（至少一项）
```
