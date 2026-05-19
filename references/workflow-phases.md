# Workflow Phases

## Phase 0 - Project Setup

Decide:
- project path
- language
- genre and target audience
- target length: chapters, words/characters per chapter, volumes/arcs
- generation mode: assisted, batch, auto-resume

Run `scripts/init_novel_project.py` for a new project. Copy user notes into `source/`.

## Phase 1 - Architecture

Produce `plan/architecture.md` and update:
- `bible/story-bible.md`
- `bible/character-bible.md`
- `bible/world-bible.md`
- `bible/style-bible.md`

Architecture must include:
- core seed: premise, promise, central dramatic question
- ending vector: not every detail, but the thematic destination
- volume/arc map
- protagonist craft chain: Ghost / Lie / Flaw / Want / Need / Truth / Arc
- protagonist first-impression design: exterior signal, behavioral signature, emotional contradiction, opening wound, and reader hook
- major character entrance cards for the opening movement: what the reader should remember after each first appearance
- character arc budget: where false change, regression, crisis choice, and irreversible change should occur
- antagonist or opposing force
- rules of world, power, technology, society
- world reveal layers: surface rules, operating logic, bottom truth
- worldbuilding exposure plan: which 3-5 world facts must be naturally revealed through action in the opening movement
- major reversals and payoffs
- opening pacing curve: stage conflicts, reversals, and mini-climaxes before the long middle begins
- dual-track pacing plan: external plot intensity and internal emotional intensity by arc
- prose style discovery result: comparable reference matrix, selected Style DNA, scene style modes, and anti-style rules
- prose style contract: style must be original, not imitation of a named living author

If the user has not supplied a clear prose style, run `style-discovery.md` before finalizing architecture. Give the user 2-3 style candidates or a recommended blend, then lock the selected direction into `bible/style-bible.md`.

Checkpoint Architecture: stop and ask the user to approve or refine. Do not generate the chapter directory before this is stable.

## Phase 2 - Directory

Produce:
- `plan/volume-map.md`
- `plan/directory.md`
- `plan/generation-plan.md`

Directory format:

```markdown
## Chapter 001 - Title
- Volume/arc:
- Function:
- POV:
- Location/time:
- Required beats:
- Dramatic action:
- Value shift:
- Character impression:
- World/context exposure:
- Stage conflict / reversal:
- Character changes:
- Foreshadowing:
- Payoffs:
- New facts to ledger:
- Cliffhanger/hand-off:
```

Checkpoint Directory: stop and ask the user to review chapter count, arc pacing, ending placement, and any must-have scenes.

For the opening movement, also review:
- whether important characters have memorable first impressions, not just plot functions
- whether the world/background is visible through scenes, institutions, stakes, and constraints
- whether chapters include stage-level escalation and reversals instead of flat clue delivery
- whether each early scene has a goal, obstacle, result, and value shift

## Phase 3 - Anchor Chapters

Generate chapter 1 and one risk chapter, usually:
- first chapter for voice, density, pacing
- one opening-movement engagement chapter to test character attachment, world exposure, and dramatic action
- a mid-arc conflict/reveal chapter for structural stress

If style direction is not yet proven, generate a short style trial first: one scene in 2-3 style candidates or a single recommended blend. Ask the user to approve, mix, or reject the style before bulk chapters.

Audit them. Ask the user to approve:
- prose voice
- chapter length
- scene density
- dialogue style
- emotional intensity
- amount of exposition
- clarity of main character impression
- clarity of world/background without lore dump
- early pacing curve and whether the chapter has a turn
- Style DNA fit, Scene Style Mode fit, and whether the prose avoids the anti-style list

Do not bulk-generate until anchor chapters are approved.

## Phase 4 - Batch Generation

Default batch size: 5-10 chapters.

For each chapter:
1. assemble chapter packet from bible, directory, ledgers, recent chapters, arc summary
2. draft chapter
3. self-check against chapter intent
4. save to `chapters/chapter-NNN.md`
5. save audit to `audits/chapter-NNN-audit.md`
6. append facts to ledger drafts

## Phase 5 - Batch Audit

After each batch, produce `audits/batch-XXX-audit.md`:
- plot coverage
- timeline consistency
- character state changes
- unresolved questions
- foreshadowing planted/paid
- repetition and scene variety
- continuity contradictions
- prose/style drift

Repair P0 issues before continuing.

## Phase 6 - Ledger Updates

Update:
- `summaries/rolling-summary.md`
- `summaries/arc-summary.md`
- `bible/character-bible.md`
- `bible/timeline-ledger.md`
- `bible/foreshadowing-ledger.md`
- `bible/continuity-ledger.md`
- `bible/world-bible.md` when new world facts become canon
- `plan/directory.md` when future chapters need micro-adjustment

## Phase 7 - Repeat

Continue batch -> audit -> ledger update until all queued chapters are complete.

## Phase 8 - Final Audit And Export

Before export:
- verify every directory beat is covered or intentionally changed
- verify all P0/P1 audit items are resolved or accepted
- verify open foreshadowing is paid off or intentionally left open
- assemble `exports/manuscript.md`
