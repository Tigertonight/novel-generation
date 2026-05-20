# Style Discovery

Use this when the user wants a novel but cannot clearly describe prose style, tone, narrative voice, or reader experience. The goal is to help the user discover a workable original style through comparable market references and short trials.

Do not imitate a living author's distinctive style. Do not copy prose, sentence patterns, metaphors, or signature diction from reference works. Use comparable works only to infer genre expectations, reader promise, pacing, narration distance, scene density, and market positioning.

## When To Run

Run style discovery when:
- the user says "随便", "你看着来", "类似热门小说", "我不知道文风"
- the premise has a clear genre but no prose direction
- anchor chapters feel generic, flat, or inconsistent
- the user rejects output with vague feedback such as "不够好看", "没味道", "不像小说"

Skip or shorten when:
- the user provides a strong style guide or golden sample
- the project is a quick draft where prose quality is secondary
- the user explicitly asks to proceed without style calibration

## Workflow

```text
1. Identify project genre and reader promise
2. Build or reuse comparable reference matrix from `research/market-research.md`
3. Translate references into Style DNA candidates
4. Present 2-3 style directions or a recommended blend
5. Generate a short style trial
6. User approves / mixes / rejects
7. Lock style into bible/style-bible.md
8. Use Style Audit after chapters and batches
```

## Comparable Reference Matrix

When browsing is available and current market awareness matters, research comparable works from reputable sources such as platform rankings, publisher pages, Goodreads, Douban, Qidian/Jinjiang ranking pages, major review sites, or user-provided examples.

Do not paste copyrighted excerpts. Summarize style dimensions only.

For market-facing webnovels, prefer using `webnovel-market-research.md` first, then translate the market research packet into style choices. Do not only ask "what prose style"; also infer the platform's reading rhythm and tolerance for exposition, hooks, dialogue directness, and payoff frequency.

Use at least three categories:

```markdown
### Same-Topic References
- Works/platforms checked:
- What reader expectations they imply:
- Borrowable dimensions:
- Do not borrow:

### Same-Pacing References
- Works/platforms checked:
- Hook style:
- Reveal frequency:
- Chapter-ending strategy:
- Do not borrow:

### Same-Mood References
- Works/platforms checked:
- Narration distance:
- Emotional temperature:
- Sensory density:
- Dialogue texture:
- Do not borrow:

### Same-Platform / Same-Channel References
- Works/platforms checked:
- Male-channel / female-channel / cross-channel assumptions:
- Platform rhythm:
- Hook density:
- Payoff frequency:
- Exposition tolerance:
- Dialogue directness:
- Chapter ending habit:
- Do not borrow:
```

If no browsing is available, infer comparable categories from stable genre knowledge and state that the matrix is inferred, not market-verified.

## Style DNA

Translate reference learning into original control parameters:

```markdown
- Prose position: market-facing / literary-leaning / cinematic / web-serial / hybrid
- Narrative distance: close / medium / cool observer / shifting POV
- Sentence rhythm: terse / balanced / flowing / fragmented / variable by scene
- Information density: low / medium / high
- Sensory density: low / medium / high
- Emotional temperature: cold / restrained / warm / feverish
- Metaphor strategy: sparse / object-based / poetic / ironic / none
- Description priority: action / atmosphere / interiority / objects / institutions / social detail
- Dialogue texture: casual / sharp / restrained / subtext-heavy / comedic
- Chapter hook style: question / reversal / cost / cliffhanger / emotional aftershock
- Platform rhythm: fast-hook web-serial / immersive long-scene / short-chapter punch / slow-burn emotional / literary
- Payoff density: low / medium / high
- Exposition tolerance: low / medium / high
- Forbidden habits: over-explanation, abstract theme statements, generic AI eloquence, repeated paragraph shape
```

## Scene Style Modes

Most novels need more than one prose mode. Define modes in `style-bible.md`:

```markdown
### Investigation / Reasoning
- Sentence rhythm:
- Detail priority:
- Avoid:

### Confrontation
- Sentence rhythm:
- Dialogue texture:
- Subtext/action rule:
- Avoid:

### Emotional Cost
- Sentence rhythm:
- Sensory focus:
- Interior/exterior balance:
- Avoid:

### World Reveal
- Reveal method:
- Institution/space/cost to show:
- Avoid:

### Action / Climax
- Sentence rhythm:
- Camera distance:
- Hook strategy:
- Avoid:
```

Adapt modes to genre. Romance, fantasy, horror, historical, comedy, and literary novels may need different modes.

## Golden Sample And Anti Sample

After the user likes a trial passage, save it or summarize it in `bible/style-bible.md`.

```markdown
## Golden Sample Notes
- What works:
- Sentence rhythm:
- POV feel:
- Description style:
- Dialogue style:
- Emotional handling:

## Anti Sample Notes
- What to avoid:
- Common rejected phrasing:
- AI-prose symptoms:
- Overused images:
```

If the user provides their own writing sample, analyze it into Style DNA. Do not merely say "match this style"; extract operational rules.

## Style Candidate Presentation

When the user does not know what they want, give concrete options:

```markdown
## Candidate A - <name>
- Best for:
- Reader feel:
- Strength:
- Risk:

## Candidate B - <name>
...

## Recommended Blend
- A __% + B __% + C __%
- Why this fits the premise:
```

Use names that describe reader experience, e.g. "冷感技术悬疑", "都市群像阴谋", "强钩子网文悬疑", "温热成长现实", "黑色幽默怪谈".

## Style Trial

Before bulk generation, write 800-1500 Chinese characters or one compact scene. Options:
- one scene in 2-3 candidate styles
- one recommended blend
- one scene plus a rewrite in a different style mode

Ask the user to approve, mix, or reject:
- Which version feels closest?
- Too cold or too emotional?
- Too literary or too plain?
- Too slow or too hook-driven?
- Dialogue too explanatory or too cryptic?

Then lock the result in `bible/style-bible.md`.

## Style Audit

Use this after chapters and batches:

```markdown
- Active Style DNA:
- Active Scene Style Mode:
- Fit: pass / drift / needs repair
- Sentence rhythm:
- Description specificity:
- Dialogue texture:
- Emotional handling:
- AI-prose symptoms:
- Over-explanation:
- Memorable line or image:
- Repair:
```

## Safety And Originality

Allowed:
- "Use comparable works to understand genre expectations."
- "Borrow pacing density, narration distance, and scene organization."
- "Create an original Style DNA inspired by market category."

Not allowed:
- "Write like <living author>."
- "Copy the sentence style of <specific book>."
- "Rewrite this in the exact voice of <modern author>."
- Pasting or generating long copyrighted excerpts.

When the user asks for a named living author's style, redirect:

```text
我不能仿写某位在世作者的独特文风，但可以提取你喜欢的维度，比如叙述距离、节奏、情绪温度、对白密度和场景质感，然后做成原创风格。
```
