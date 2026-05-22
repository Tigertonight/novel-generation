---
name: optimization-workflow
description: Workflow for optimizing existing novels rather than generating from scratch. Multi-grain surgery (sentence / paragraph / scene / chapter), diagnostic-driven repair priority, in-place voice preservation. Use when user has existing prose to improve.
type: workflow
---

# Optimization Workflow / 优化已有小说工作流

> 用于"用户已有正文，希望优化"的场景，而非从零生成。核心原则：**最小手术、保留作者语感、按问题严重度匹配粒度**。
> For improving existing prose. Core principle: minimal surgery, preserve author voice, match grain to severity.

---

## 0. 优化模式 vs 生成模式 / Optimize vs Generate

本 skill 默认是**生成模式**（Phase 0-12 的完整工作流）。优化模式是**并行流程**：

| 维度 | 生成模式 | 优化模式 |
|---|---|---|
| 起点 | premise / seed | 已有正文 |
| Phase 0-2 | 必经 | 跳过或简化 |
| 文体 | 通过 style-discovery 设计 | **从已有正文反向提炼**，不重设计 |
| Bible/Ledger | 从空白填 | **从正文回填**（reverse-engineer） |
| 章节生成 | 从无到有 | 不生成新章，**修旧章** |
| 主要工具 | chapter-production.md | 本文件 + flatness-and-hook-diagnostics.md |
| 验收 | 章节包对照 | 诊断报告对照 + 作者认可语感 |

**关键约束**：优化模式下**严禁**用 AI 通用风格覆盖作者风格。每次手术后必须读一遍：原作者的词、句、节奏、口吻是否还在？如果消失了，回退。

---

## 1. 入口与意图分级 / Intake & Intent Triage

接到"帮我优化这部小说"时，先问清意图——不同意图对应不同手术深度：

```
意图 A：抛光润色（preserve）
  保留 90%+ 原文，只调字句、补细节、整节奏
  适合：作者已写完，想小幅提升
  手术粒度：句子级、段落级
  Voice 保留：必须 ~95%

意图 B：定向修复（targeted repair）
  特定问题修复（开头不抓人、感情线塌、爽点弱、节奏平）
  保留 70-80% 原文
  适合：读者反馈集中在几个点
  手术粒度：段落级、场景级（局部）
  Voice 保留：必须 ~85%

意图 C：结构重构（restructure）
  剧情结构、人物弧线、关键章节重写，但语感保留
  保留 40-60% 原文（核心场景重写）
  适合：作者意识到结构性问题
  手术粒度：场景级、章节级
  Voice 保留：必须 ~70%（章节包按本 skill 生成模式重做）

意图 D：续写补强（extend）
  原文不动，续写新章节
  适合：作者写到一半卡壳，或需要扩展
  这种情况切回生成模式，但用本文件的"反向回填"步骤建 Bible
```

**默认假设**：除非用户明确指定，先按意图 B 走（最常见、风险最低）。

---

## 2. 反向回填 Bible / Reverse-Engineer Bible

存量正文没有 bible 和 ledger。优化前必须从正文回填——否则修一处可能砸另一处的连续性。

### 2.1 自动回填顺序

按依赖关系：

```
1. 文体反向提炼  → bible/style-bible.md
   (POV、距离、句长偏好、对话比例、章节长度、作者口头禅、爱用句式)

2. 人物档案回填  → bible/character-bible.md
   (出场顺序、稳定外貌锚点、当前状态、声音标记、欲望/恐惧/缺陷)

3. 关系状态回填  → bible/relationship-map.md
   (谁和谁有关系、当前信任/吸引/张力、最近变化)

4. 关键物机制回填 → bible/object-mechanism-ledger.md
   (出现过的重要道具/系统/能力 + 最后出现章节)

5. 时间线回填    → bible/timeline-ledger.md
   (章 → 时间 → 地点 → 事件)

6. 伏笔账回填    → bible/foreshadowing-ledger.md
   (已埋的伏笔、已回收的、未回收的)

7. 章节事实回填  → summaries/chapter-facts.md
   (每章一段密集要点)

8. 风格 DNA 回填 → bible/style-bible.md 的 Style DNA 字段
   (从作者 5-10 段优秀片段反向归纳)
```

### 2.2 风格 DNA 反向提炼方法

不要用模型笼统的"现代中文都市风"标签。具体反向问：

- 句长分布：抽 500 字样本，统计平均句长、句长方差
- 段落长度：平均段落行数、最长/最短段落
- 对话密度：对话占比、对话句平均长度
- 标点习惯：破折号、省略号、分号的使用频率
- 词汇偏好：作者爱用的动词、形容词、虚词（"竟"、"原是"、"倒"这类）
- 时间过渡：作者怎么处理时间跳跃
- 视角控制：纯 POV / 有限全知 / 偶尔越线
- 信息揭露速度：作者倾向直给还是延迟
- 比喻密度：每千字多少个比喻
- "禁词"：作者从不用的词

把这些写进 `bible/style-bible.md` 的 Style DNA Reverse-Engineered 区。

**重要**：后续所有手术段落的产出都要"听起来像作者写的"——用这份 DNA 做 voice match。

---

## 3. 诊断阶段 / Diagnostic Stage

跑一遍 `flatness-and-hook-diagnostics.md` 完整流程，产出诊断报告。

### 3.1 诊断范围决策

| 用户主诉 | 优先诊断范围 |
|---|---|
| 开头不抓人 | 第 1-3 章逐段诊断 + 钩子诊断 G/H/I/J |
| 节奏平 / 读起来困 | 全文每章抽样平淡诊断 A/B/C |
| 感情线塌 | 关系出现的所有章节 + hard-rules.md 第 4 条审计 |
| 爽点弱 / 不爽 | 全文回扫 hard-rules.md 第 6 条 |
| 人物记不住 | 重要人物每次出场 + character-entrance-craft.md 审计 |
| 中段拖沓 | 中段 5 章抽样 + 平淡诊断 |
| 通泛"读起来不行" | 第 1-3 章全诊 + 全文抽样 5 章 |

### 3.2 诊断报告聚合

把 chapter-level 诊断聚合成 book-level 诊断：

```markdown
# Book-level Diagnostic

## 高频缺陷 Top 5
1. [出现 X 章] 缺感官落点
2. [出现 X 章] 段落开头主语雷同
3. ...

## 章节集中度
- 重灾区章节：CH3, CH7, CH12 (P0 多)
- 优秀样本章节：CH5, CH18 (诊断几乎全过)

## 风险等级
- 全书风险：低 / 中 / 高
- 开头三章风险：低 / 中 / 高

## 建议手术粒度
- 主体粒度：段落级 / 场景级 / 章节级
- 例外章节（需要更深手术）：

## 优秀样本章节作用
这些章节作为"作者在状态时的水准"——其它章节修复目标向它们靠拢。
```

---

## 4. 手术粒度匹配 / Surgery Grain Matching

### 4.1 句子级 (Sentence-level)

**适用**：单段内 < 5 处缺陷；问题主要是"某句不到位"。

**做法**：
- 不动段落结构、不动信息节奏
- 改：替换抽象形容词为具体物；调句长；换段落开头主语；补 1 个感官细节
- 输出：原段落 + 修订段落对比

**voice 保留要求**：~95%

**例**：

原文：
> 她非常生气，狠狠地瞪了他一眼，房间里气氛变得很紧张。

修订（句子级）：
> 她没说话。茶杯放回桌上的力气比该有的大半分。他听见瓷底磕到木头那一声。

**保留**：作者的简短句习惯
**修复**：用具体物代替"非常生气"和"气氛紧张"

### 4.2 段落级 (Paragraph-level)

**适用**：段落内多处缺陷或段落结构需要调整（节奏、视角切换、信息揭露顺序）。

**做法**：
- 重写整段，但保留段落功能、保留作者最强的几句
- 改：补内心节拍、调段落开头方式、调信息揭露顺序、加感官层
- 输出：原段 + 修订段对比 + 修复点说明

**voice 保留要求**：~85%

### 4.3 场景级 (Scene-level)

**适用**：场景结构有问题（goal-obstacle-result 不清、value shift 缺失、对抗性弱）。

**做法**：
- 重做场景包：明确 POV、外部目标、私下情绪目标、价值转变、内心 turn
- 重写场景，但**关键对话/动作锚点保留**（不要把作者标志性的金句写没）
- 输出：场景包 + 修订场景 + 与原场景的差异说明

**voice 保留要求**：~70%

### 4.4 章节级 (Chapter-level)

**适用**：章节功能错位（该有钩子的章节没钩子、该揭密的章节没揭密、该升温的章节没升温）。

**做法**：
- 走完整 chapter packet 流程（按 chapter-production.md）
- 把原章节当"草稿"参考，但章节包按 hard-rules.md 重做
- 重写整章
- 输出：新章节包 + 新章节 + 原章节哪些段落/对话被保留及为什么

**voice 保留要求**：~70%（章节级手术 voice 漂移最大，必须做 voice match 自检）

### 4.5 不要做的（Anti-pattern）

- **不要**整书重写——除非用户明确要求
- **不要**改人物名字、地点名字、设定（除非用户要求）
- **不要**用"AI 通用文学腔"覆盖作者口吻
- **不要**给每段都加比喻或诗意描写——很多作者就是直白派
- **不要**把作者短句改成长句来"显得文笔好"

---

## 5. Voice Match 自检 / Voice Preservation Check

每完成一处手术，做以下自检（任一不过 = 回退）：

- [ ] 修订段落的句长分布与作者 Style DNA 一致（±20%）
- [ ] 修订没有引入作者从不用的词（参考 style-bible 的"禁词"）
- [ ] 修订段落里作者的标志性句式或词被保留至少 1 处
- [ ] 把修订段抹去作者前后文，单读起来仍然像这位作者写的
- [ ] 没有用通泛 AI 文学修辞（"如同……一般"、"仿佛被时间凝固"、"内心仿佛被狠狠刺了一下"等套话）

如果是章节级手术，多做一项：
- [ ] 章节里至少有 1 处保留原作者**未经修改**的对话或动作（标志锚）

---

## 6. 优化输出格式 / Output Format

每次优化交付物结构：

```markdown
# Optimization Delivery — [Chapter X / Scene Y / Range]

## Surgery Grain
sentence / paragraph / scene / chapter

## Diagnostic Findings (Source)
- A 命中：xxx
- B 命中：xxx
- ...

## Voice Anchors Preserved
- 作者标志性句式 X 处保留
- 作者口头禅 X 处保留
- 关键金句保留：……

## Before / After (per surgery point)

### Point 1
**Before**:
> 原文

**After**:
> 修订

**Why this surgery**: 命中诊断 A2、B5
**What's preserved**: 作者的破折号习惯 / 短句节奏 / ……

### Point 2
...

## Voice Match Self-Check
- [x] 句长分布相近
- [x] 没引入作者禁词
- [x] 通读像同一作者
- [x] 没有 AI 套话

## Risk Notes
（如有任何手术可能影响后续连续性，列出供作者确认）
```

---

## 7. 入口模式判定 / Mode Detection

SKILL.md 的 Default Collaboration 应识别以下信号自动进入优化模式：

- 用户提供了已写好的章节文件
- 用户说"帮我改"、"帮我优化"、"我已经写了"、"读者反馈"、"觉得不好"
- 用户说"读起来太平"、"开头不抓人"、"感情线塌"等具体诊断主诉
- 用户上传整本/部分书稿

进入优化模式后的步骤：

1. 询问意图分级（A/B/C/D）；默认 B
2. 反向回填 Bible（详细程度按手术粒度调整）
3. 跑诊断器
4. 提交诊断报告 + 推荐手术粒度，等用户确认
5. 按粒度执行手术
6. 每章手术后做 Voice Match 自检
7. 用户验收 → 更新 Bible/Ledger

---

## 8. 与其它文件的关系

- `flatness-and-hook-diagnostics.md`：第 3 节诊断阶段必读
- `hard-rules.md`：手术目标必须命中其 P0 清单
- `chapter-production.md`：章节级手术走完整章节包流程
- `bible-and-ledgers.md`：反向回填的字段定义
- `style-discovery.md`：风格反向提炼的方法源
- `character-entrance-craft.md`：人物入场修复参考
- `intimacy-craft.md`：亲密线修复参考
- `references-pack/`（如果存在）：作为优秀样本的"目标参照"

---

## 9. 北极星 / North Star

> 优化的成功标准：**作者读完修订版会说"这就是我想写但没写出来的样子"**——而不是"这看起来像别人写的"或"这看起来像 AI 写的"。
> Success: the author says "this is what I wanted to write but couldn't" — not "this looks like someone else" or "this looks like AI."
