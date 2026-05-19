---
name: novel-generation
description: Design, plan, generate, audit, and resume long-form novel projects with strong continuity. Use when the user wants to create a novel, web novel, serialized fiction, long chaptered story, story bible, volume outline, chapter directory, batch chapter generation, consistency checks, foreshadowing/timeline/character tracking, or an agentic long-running prose workflow inspired by AI_NovelGenerator, web-video-presentation, or long-comic-generation.
---

# Novel Generation

Build long-form novels as an auditable production system: bible first, directory second, chapters in 5-10 chapter batches, then review and ledger updates. Do not try to write an entire long novel in one prompt.

Design inheritance:
- `AI_NovelGenerator`: architecture -> directory -> chapter draft -> finalize -> update summary/character/vector memory.
- `web-video-presentation`: hard checkpoints, anchor-first execution, self-check before reporting.
- `long-comic-generation`: bible/ledger truth source, generation plan, resumable agentic loop, audit trail.

## Workflow

```text
Phase 0  Project setup + mode choice
Phase 1  Architecture: premise, genre promise, volumes, arcs, cast, world, style discovery
   v [Checkpoint Architecture]
Phase 2  Directory: volume map + chapter directory + batch plan
   v [Checkpoint Directory]
Phase 3  Anchor chapters: chapter 1 + one opening-movement engagement chapter + one mid-arc risk chapter
   v [Hard node: user approves voice/quality]
Phase 4  Batch generation: 5-10 chapters per batch
Phase 5  Batch audit: continuity, timeline, character, foreshadowing, style, repetition
Phase 6  Ledger updates + directory micro-adjustment
Phase 7  Repeat Phase 4-6 until complete
Phase 8  Final audit + export
```

Default chapter target: 2500-4000 Chinese characters or comparable prose length. Avoid 8000+ character chapters unless the user explicitly accepts slower, higher-failure generation and more revision passes.

## Start A Project

If creating a new novel workspace, run the scaffold script:

```bash
python <skill_dir>/scripts/init_novel_project.py ./novel-project
```

Then place user source material in `source/` and fill or generate files in this order:

```text
novel-project/
├── source/               raw user ideas, notes, references
├── bible/                story, character, world, style, continuity truth sources
├── plan/                 architecture, directory, batch/generation plan
├── chapters/             chapter-NNN.md files
├── summaries/            rolling, arc, and batch summaries
├── audits/               chapter, batch, and final audit reports
├── exports/              assembled manuscripts
└── .codex-longtask/      state.json for resumable work
```

## Hard Rules

1. Bible and ledgers are the truth source. Do not invent major facts in chapter prompts without updating them.
2. Always create or update `plan/generation-plan.md`; it is the task queue.
3. Use strong models for `plan/architecture.md` and `plan/directory.md`; ask for or wait for user refinement at checkpoints.
4. Generate in 5-10 chapter batches by default, then audit and update ledgers before continuing.
5. Keep multiple memory layers: rolling summary, arc summaries, chapter facts, timeline, foreshadowing, character states, location/world rules.
6. Every generated chapter must have an audit entry before it is considered finalized.
7. The opening movement must establish reader attachment before the story enters its long middle: memorable protagonist impressions, visible world/context, and several stage conflicts or reversals. Calibrate this by story length and format rather than a fixed chapter count. Do not let the opening become pure setup, lore, or procedural clue delivery.
8. If the user cannot describe prose style, run style discovery: infer genre/style targets, research comparable works when useful, translate references into an original Style DNA, and use a short style trial before bulk generation.
9. Do not imitate living authors or copy distinctive prose. Comparable works may inform genre expectations, pacing, narration distance, scene density, and reader promise only.
10. Stop at hard nodes: Architecture checkpoint, Directory checkpoint, anchor approval, repeated P0 audit failures, user-visible plot surgery, early reader-experience failure, unresolved style direction, or conflicting user requirements.
11. Do not rely on one 2000-word global summary. Maintain separate structured ledgers.
12. If the user asks for "auto continue", use `.codex-longtask/state.json`; still do not skip hard nodes.
13. For fanfiction or copyrighted settings, transform and summarize; do not reproduce long passages from source works.

## What To Read When

- `references/workflow-phases.md`: phase-by-phase outputs and checkpoints.
- `references/bible-and-ledgers.md`: memory architecture that fixes long-novel drift.
- `references/chapter-production.md`: anchor chapters, batch size, chapter prompt assembly, finalization.
- `references/audit-protocol.md`: P0/P1/P2 audit rules and repair policy.
- `references/reader-experience.md`: opening attachment, character impression, worldbuilding exposure, pacing curve, early conflict/reversal checks.
- `references/screenwriting-craft.md`: screenwriting-inspired craft layer: dramatic action, Ghost/Lie/Flaw/Want/Need, value shifts, dual-track pacing, world reveal layers, and script-doctor checks.
- `references/style-discovery.md`: prose style discovery for users who cannot name a style; comparable reference scouting, Style DNA, scene style modes, style trials, and style audits.
- `references/longtask-autoresume.md`: resumable state file and agentic loop.
- `references/ai-novelgenerator-notes.md`: design ideas adapted from the GitHub project and what this skill changes.

## Default Collaboration

When the user only says "write/generate a long novel":
1. Ask for or infer premise, genre, target length, audience, tone, and taboo constraints.
2. Create project scaffold.
3. Produce architecture and directory first.
4. Stop for checkpoint review before chapters.

When the user already has a bible/directory:
1. Import it into `bible/` and `plan/`.
2. Audit for missing memory ledgers.
3. Start with anchor chapter(s), then batch generation.

When the user asks to continue an existing project:
1. Read `.codex-longtask/state.json`, `plan/generation-plan.md`, latest batch audit, and relevant ledgers.
2. Resume from the next queued task.
3. Do not restart from chapter 1 unless explicitly asked.
