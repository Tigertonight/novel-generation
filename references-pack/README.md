---
name: references-pack
description: Curated craft samples — original demonstrations of strong openings, character entrances, interiority, and intimacy beats. Use as structural references for the AI to study technique, NOT as text to copy or imitate.
type: reference-corpus
---

# References Pack / 范本库

> 这是一个**结构化范本库**——每个样本都是**Claude 原创**的写作示范 + 技法拆解，用来给模型学习**结构、节奏、技法**，**不是供复制的原文**。
> Curated original samples + technique breakdowns. For studying structure, not copying prose.

---

## 为什么这样做 / Why This Approach

### 不存原文的原因
1. **法律风险**：他人作品的长片段引用涉及版权
2. **风格污染**：模型读原文容易模仿表面措辞，产出"像但不是"的尴尬产品
3. **学习效率低**：原文混合了多种技法，模型难以识别哪一项在起作用

### 存"原创示范 + 拆解"的原因
1. **每个样本只示范 1-2 个核心技法**，可定位、可学习
2. **拆解明确指出"这一句为什么有效"**，模型学的是原理而非套路
3. **可发布、可分享**：因为是原创，没有版权问题
4. **可扩展**：你以后读到好的开头/段落，告诉 Claude 大致结构，由 Claude 生成"同结构原创示范 + 拆解"

---

## 范本目录 / Sample Index

### 开头 Openings
- `openings/01-modern-thriller.md` — 都市悬疑开头：物件钩子 + 时间钩子叠加
- `openings/02-historical-court.md` — 古代宫廷开头：身份悬念 + 视角误读
- `openings/03-xianxia-revenge.md` — 仙侠复仇开头：状态不平衡 + 内心暗流

### 人物出场 Character Entrances
- `entrances/01-hostile-encounter.md` — 敌对人物初次出场（第三人称）
- `entrances/02-romantic-interest.md` — 感情对象初次出场（第一人称）

### 内心与情感 Interiority
- `interiority/01-suppressed-grief.md` — 被压下的悲痛：身体先于意识
- `interiority/02-jealousy-misread.md` — 嫉妒下的误读：POV 偏见过滤

### 亲密节拍 Intimacy Beats
- `intimacy/01-care-as-tension.md` — 照料场景的张力：触碰阈值
- `intimacy/02-restraint-scene.md` — 克制场景：什么没做比什么做了更重要

---

## 范本格式 / Sample Format

每个样本文件遵循以下结构：

```markdown
---
sample_id: [唯一编号]
category: openings / entrances / interiority / intimacy
genre_tag: [都市/古言/仙侠/职场/...]
core_technique: [本样本核心示范的 1-2 个技法]
length: [字数]
pov: 第一人称 / 近距离第三 / ...
---

# Sample [ID]: [简短标题]

## 一句话技法概括

## 原创示范

> [Claude 写的 200-500 字示范片段]

## 技法拆解

### 拆解点 1：[技法名]
- 出现在第 X 段第 X 句
- 原理：……
- 为什么有效：……
- 反面对照（如果不这样写）：……

### 拆解点 2：……

## 可应用规则

1. 当你写 [场景类型] 时，可以这样做：……
2. 这个技法的局限：[不适用于什么场景]

## 警告

- **不要复制本示范的人名、地名、设定**——这些是为示范设计的，不是你作品的素材
- **要学习的是结构和原理**，不是表面措辞
- 不同类型小说要调整应用方式
```

---

## 本地参考槽 / Local-Only Slot

如果你想存放**第三方原文片段**（来自他人作品、读者反馈中的具体段落、自己作品的代表性段落）做学习参考，但**不想推送到 git**，使用：

```
references-pack/_local/
```

该目录被 `.gitignore` 屏蔽，只在你本机存在。详见 `_local/snippets.md`（如果存在）。

Claude 在做诊断、风格反向提炼、生成原创对照示范时**可以读取** `_local/` 下的内容做学习参考，但**不会**把这些内容复制到任何会被推送到 git 的文件中。

## 怎么扩充范本 / How To Extend

### 方式 1：你描述结构，Claude 生成原创示范

```
用户："我读到一个开头很好——主角是个被流放的将军，开头是他在流放地醒来，
       开头第一句是他闻到一种味道想起了战场。这个开头我觉得很妙，
       帮我做一个同结构的原创示范放进范本库。"

Claude：
1. 提炼结构："感官触发记忆 + 状态不平衡（被流放）+ 身份反差（前将军）"
2. 设计完全不同的人物/设定
3. 生成 200-500 字示范
4. 写技法拆解
5. 命名为新 sample 文件加入 index
```

### 方式 2：你提交一个写作问题，Claude 制造对照样本

```
用户："我前 500 字老是被说太平。给我一个开头反例和正例对比。"

Claude：
1. 同一前提下生成"违反诊断器多项的弱开头"
2. 同一前提下生成"命中所有钩子的强开头"
3. 拆解对比
4. 加入范本库 openings/ 下
```

### 方式 3：你贴片段做诊断，Claude 拆解后写原创示范

```
用户："这是我写的开头（贴片段），帮我诊断 + 给一个原创对照示范"

Claude：
1. 跑 flatness-and-hook-diagnostics.md
2. 不复制原片段，写一个**同主题、同人物动机但技法到位**的原创示范
3. 拆解关键差异
4. 视情况加入范本库
```

---

## 使用范本的正确方式 / Correct Usage

### Do
- ✅ 阅读范本拆解，理解**为什么**这样写
- ✅ 把技法拆解里的"可应用规则"抽出来用
- ✅ 用范本作为"我的水准应该往这看"的目标参照
- ✅ 用对照样本理解平淡和强劲的差距

### Don't
- ❌ 复制范本里的句子或段落到你的作品
- ❌ 直接用范本里的人名、地名、设定
- ❌ 不读拆解只看原创示范——你会错过 80% 的价值
- ❌ 把所有作品都往同一个范本风格写——范本是技法库，不是模板

---

## 与其它文件的关系

- `flatness-and-hook-diagnostics.md`：诊断器命中问题时，用对应类别的范本作为修复目标参照
- `optimization-workflow.md`：优化时把范本作为"作者在状态时的水准"的视觉化目标
- `character-entrance-craft.md`：entrances/ 下的样本是该文件理论的实例化
- `intimacy-craft.md`：intimacy/ 下的样本是该文件理论的实例化
- `style-discovery.md`：范本可作为风格 DNA 提炼的练习材料

---

## 北极星 / North Star

> 范本库是写手的"健身房"——通过拆解优秀技法、模仿原理（不是模仿表面）、积累可应用规则，让模型在写作时**有具体的好范例可参照**，而不只是"按规则避免错误"。
> The pack is a craft gym — model learns by understanding why excellent technique works, not by copying surface words.
