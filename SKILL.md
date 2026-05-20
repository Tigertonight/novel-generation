---
name: novel-generation
description: Design, plan, generate, audit, and resume long-form novel projects with strong continuity. Use when the user wants to create a novel, web novel, serialized fiction, long chaptered story, story bible, volume outline, chapter directory, batch chapter generation, consistency checks, foreshadowing/timeline/character tracking, or an agentic long-running prose workflow inspired by AI_NovelGenerator, web-video-presentation, or long-comic-generation.
---

# Novel Generation

Build long-form novels as an auditable production system: bible first, directory second, chapters in 5-10 chapter batches, then review and ledger updates. Do not try to write an entire long novel in one prompt.

This skill is genre-adaptive. Do not force every novel to include combat, romance, mystery, faction politics, power progression, or heavy worldbuilding. First identify the story's genre promise and reader contract, then enable only the craft modules that help fulfill that contract.

Design inheritance:
- `AI_NovelGenerator`: architecture -> directory -> chapter draft -> finalize -> update summary/character/vector memory.
- `web-video-presentation`: hard checkpoints, anchor-first execution, self-check before reporting.
- `long-comic-generation`: bible/ledger truth source, generation plan, resumable agentic loop, audit trail.

## Workflow

```text
Phase 0  Project setup + mode choice
Phase 1  Market positioning + optional research: channel, reader contract, commercial hook, trope engine, first-three-chapter promise, public-source market signals when needed
   v [Checkpoint Positioning when market direction is uncertain]
Phase 2  Architecture: premise, genre promise, theme, dramatic question, volumes, arcs, cast, world, style discovery, adaptive craft modules
   v [Checkpoint Architecture]
Phase 3  Design bible: character cards, relationship map, faction/institution map, mechanism map, mystery/foreshadowing plan, emotional and growth curves
   v [Checkpoint Design Bible]
Phase 4  Directory: volume map + chapter directory + batch plan
   v [Checkpoint Directory]
Phase 5  Anchor chapters: chapter 1 + one opening-movement engagement chapter + one mid-arc risk chapter
   v [Hard node: user approves voice/quality]
Phase 6  Batch design card: genre focus, crisis mix, growth loop, relationship/setting/mechanism needs
Phase 7  Batch generation: write to the design card, not just to the previous chapter
Phase 8  Batch audit: continuity, reader experience, growth, crisis, mechanism clarity, character, foreshadowing, style, repetition
Phase 9  Repair/polish until audit exit standard is met
Phase 10 Ledger updates + directory micro-adjustment
Phase 11 Repeat Phase 6-10 until complete
Phase 12 Final audit + export
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
├── research/             market research, comparable matrix, source notes
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
4. Generate in 5-10 chapter batches by default. Before each batch, create or mentally assemble a batch design card: genre focus, enabled modules, crisis types, protagonist growth, relationship movement, mechanism/world reveal, consequence, and hook type.
5. Keep multiple memory layers: rolling summary, arc summaries, chapter facts, timeline, foreshadowing, character states, location/world rules.
6. Every generated chapter must have an audit entry before it is considered finalized.
7. The opening movement must establish reader attachment before the story enters its long middle: memorable protagonist impressions, visible world/context, and several stage conflicts or reversals. Calibrate this by story length and format rather than a fixed chapter count. Do not let the opening become pure setup, lore, or procedural clue delivery.
8. If the user cannot describe prose style, run style discovery: infer genre/style targets, research comparable works when useful, translate references into an original Style DNA, and use a short style trial before bulk generation.
9. Do not imitate living authors or copy distinctive prose. Comparable works may inform genre expectations, pacing, narration distance, scene density, and reader promise only.
10. Stop at hard nodes: Architecture checkpoint, Directory checkpoint, anchor approval, repeated P0 audit failures, user-visible plot surgery, early reader-experience failure, unresolved style direction, or conflicting user requirements.
11. Do not rely on one 2000-word global summary. Maintain separate structured ledgers.
12. If the user asks for "auto continue", use `.codex-longtask/state.json`; still do not skip hard nodes.
13. For fanfiction or copyrighted settings, transform and summarize; do not reproduce long passages from source works.
14. Match craft modules to genre. Combat craft is required for combat-forward genres but should not be forced into quiet literary, domestic, romance, or pure mystery work unless the story naturally calls for it. Mystery clue-chain craft is required for mystery/investigation arcs. Relationship progression craft is required for romance and character-driven arcs. Faction/power-map craft is required for political, sect, court, family, corporate, or institutional stories.
15. Long-form events must change something. Each batch should produce at least one meaningful change in character psychology, capability, relationship, status, knowledge, or world pressure. If a batch only moves facts around, repair it.
16. Crisis patterns must rotate according to genre promise. Avoid solving every conflict with the same pattern. Mix relevant pressure types such as time, survival, moral choice, relationship fracture, resource scarcity, public opinion, rule/procedure, investigation, temptation, combat, or political cost.
17. Core mechanisms must be legible and staged. For systems, magic, investigations, games, contracts, social rules, or other story engines, reveal trigger, use, limit, cost, failure mode, enemy counter, and upgraded use over time. Do not let the protagonist win through unclear authorial convenience.
18. Arc wins must leave consequences. Track injuries, tool/resource costs, relationship shifts, reputation changes, political reactions, psychological residue, unresolved evidence, or newly opened threats.
19. Apply adaptive quality during planning, not only audit. Character cards, relationship maps, faction maps, mechanism maps, mystery/foreshadowing plans, emotional curves, growth curves, and volume outlines should encode the enabled modules before chapters are drafted.
20. During generation, write toward the planned craft targets. Do not wait for audit to add growth, emotion, clue logic, action specificity, faction pressure, or mechanism clarity. Audit is a guardrail and repair loop, not the first place craft appears.
21. For every important character, maintain a character dossier with role, personality, stance/allegiance, desire, fear/wound, false belief, agency, detailed appearance, signature behavior/voice, key relationships, in-story changes, arc movement, current status, and current cost. Use these cards while drafting scenes and update them after major events.
22. For every important relationship, maintain a relationship-state line: current trust level, unresolved tension, what each side wants from the other, what changed recently, and what would test or deepen the bond.
23. For every major organization or institution, maintain a faction/institution card with wants, fears, resources, debts, secrets, internal divisions, public/private positions, leverage, and vulnerability.
24. For mystery, conspiracy, hidden-history, or mechanism-heavy stories, design clue/reveal curves before drafting: question, clue, misread, contradiction, partial reveal, cost of knowing, and later payoff.
25. When market direction matters, run dynamic webnovel market research before architecture. Use public official platform pages, rankings, category/tag pages, book detail pages, public reviews, and user-provided examples to build a source-cited market research packet. Do not scrape locked content, reproduce long excerpts, or copy plot/prose; convert findings into original positioning, reader contract, trope engine, character design, and style constraints.
26. For webnovel projects, use baseline market positioning knowledge even without browsing: male-channel/female-channel/cross-channel reader contracts, payoff rhythm, first-three-chapter promise, long-serial engine, protagonist/team/relationship design, and trope engines such as comeback, rise-to-the-top, face-slap, rebirth, transmigration, system, faction expansion, identity reversal, and relationship pull. Treat these as market patterns, not rigid formulas.

## What To Read When

- `references/workflow-phases.md`: phase-by-phase outputs and checkpoints.
- `references/webnovel-market-positioning.md`: baseline webnovel industry knowledge for male-channel/female-channel/cross-channel positioning, reader contracts, trope libraries, protagonist/team/relationship design, first-three-chapter hooks, long-serialization engines, and benchmark usage.
- `references/webnovel-market-research.md`: dynamic public-source research for platform/category signals, male-channel/female-channel reader contracts, comparable matrices, topic selection cards, and market-informed planning.
- `references/bible-and-ledgers.md`: memory architecture that fixes long-novel drift.
- `references/chapter-production.md`: anchor chapters, batch size, chapter prompt assembly, finalization.
- `references/audit-protocol.md`: P0/P1/P2 audit rules and repair policy.
- `references/reader-experience.md`: opening attachment, character impression, worldbuilding exposure, pacing curve, early conflict/reversal checks.
- `references/genre-adaptive-quality.md`: genre-adaptive planning and generation, character/relationship/faction/mechanism design, module selection, reader-experience audits, growth loops, crisis rotation, mechanism clarity, combat/mystery/relationship/faction modules, and P0/P1/P2 quality gates.
- `references/screenwriting-craft.md`: screenwriting-inspired craft layer: dramatic action, Ghost/Lie/Flaw/Want/Need, value shifts, dual-track pacing, world reveal layers, and script-doctor checks.
- `references/style-discovery.md`: prose style discovery for users who cannot name a style; comparable reference scouting, Style DNA, scene style modes, style trials, and style audits.
- `references/longtask-autoresume.md`: resumable state file and agentic loop.
- `references/ai-novelgenerator-notes.md`: design ideas adapted from the GitHub project and what this skill changes.

## Default Collaboration

When the user only says "write/generate a long novel":
1. Ask for or infer premise, genre, target length, audience, tone, and taboo constraints.
2. Create project scaffold.
3. If the project is market-facing or the direction is vague, use webnovel market positioning; when current platform signals matter, run webnovel market research and produce a positioning card before architecture.
4. Produce architecture, design bible, and directory first.
5. Stop for checkpoint review before chapters.

When the user already has a bible/directory:
1. Import it into `bible/` and `plan/`.
2. Audit for missing memory ledgers plus missing character cards, relationship map, faction/institution map, mechanism map, and genre-specific clue/action/emotional curve plans.
3. Start with anchor chapter(s), then batch generation.

When the user asks to continue an existing project:
1. Read `.codex-longtask/state.json`, `plan/generation-plan.md`, latest batch audit, and relevant ledgers.
2. Resume from the next queued task.
3. Do not restart from chapter 1 unless explicitly asked.
