# Novel Generation Skill

Codex skill for planning, generating, auditing, and resuming long-form novel projects with strong continuity.

This skill treats a novel as an auditable production system:

- story bible and ledgers as the source of truth
- architecture and chapter directory before drafting
- anchor chapters before bulk generation
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
│   ├── longtask-autoresume.md
│   ├── reader-experience.md
│   ├── screenwriting-craft.md
│   ├── style-discovery.md
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

The generated workspace includes `source/`, `bible/`, `plan/`, `chapters/`, `summaries/`, `audits/`, `exports/`, and `.codex-longtask/`.

## Core Workflow

1. Project setup and mode choice
2. Architecture checkpoint
3. Directory checkpoint
4. Anchor chapters and voice approval
5. Batch generation
6. Batch audit
7. Ledger updates and directory micro-adjustment
8. Repeat until final audit and export

## Notes

The skill is designed for original fiction and transformed/summarized fanfiction workflows. It should not reproduce long copyrighted passages or imitate living authors' distinctive prose.
