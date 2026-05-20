# Novel Generation Skill

Codex skill for planning, generating, auditing, and resuming long-form novel projects with strong continuity.

This skill treats a novel as an auditable production system:

- story bible and ledgers as the source of truth
- dynamic public-source market research before planning when platform fit matters
- architecture and chapter directory before drafting
- anchor chapters before bulk generation
- genre-adaptive craft modules selected by reader promise
- design bible cards for characters, relationships, factions, mechanisms, and reveal curves
- 5-10 chapter batches by default
- continuity, timeline, foreshadowing, style, and reader-experience audits after each batch
- resumable long-running state in `.codex-longtask/state.json`

## Contents

```text
novel-generation/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── ai-novelgenerator-notes.md
│   ├── audit-protocol.md
│   ├── bible-and-ledgers.md
│   ├── chapter-production.md
│   ├── genre-adaptive-quality.md
│   ├── longtask-autoresume.md
│   ├── reader-experience.md
│   ├── screenwriting-craft.md
│   ├── style-discovery.md
│   ├── webnovel-market-research.md
│   └── workflow-phases.md
└── scripts/
    └── init_novel_project.py
```

## Install

Clone or copy this directory into your Codex skills folder:

```bash
git clone https://github.com/yuanzexiang/novel-generation.git ~/.codex/skills/novel-generation
```

Then start a Codex task with:

```text
$novel-generation
```

## Start A Novel Project

Use the scaffold script to create the recommended project layout:

```bash
python ~/.codex/skills/novel-generation/scripts/init_novel_project.py ./novel-project
```

The generated workspace includes `source/`, `research/`, `bible/`, `plan/`, `chapters/`, `summaries/`, `audits/`, `exports/`, and `.codex-longtask/`.

## Core Workflow

1. Project setup and mode choice
2. Market research and positioning when current platform/category knowledge matters
3. Architecture checkpoint
4. Design bible checkpoint
5. Directory checkpoint
6. Anchor chapters and voice approval
7. Batch design card
8. Batch generation
9. Batch audit and repair
10. Ledger updates and directory micro-adjustment
11. Repeat until final audit and export

## Notes

The skill is designed for original fiction and transformed/summarized fanfiction workflows. It should not reproduce long copyrighted passages or imitate living authors' distinctive prose.
