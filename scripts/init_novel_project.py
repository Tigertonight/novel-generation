#!/usr/bin/env python3
"""Scaffold an auditable long-form novel project."""

from __future__ import annotations

import json
import sys
from pathlib import Path


FILES = {
    "source/.gitkeep": "",
    "bible/story-bible.md": "# Story Bible\n\n## Core Seed\n\n## Genre Promise\n\n## Central Dramatic Question\n\n## Ending Vector\n\n## Volume / Arc Map\n\n## Themes\n\n## Must Not Break\n\n",
    "bible/character-bible.md": "# Character Bible\n\n## Character Name\n- Stable identity:\n- Want / need / flaw:\n- Current goal:\n- Emotional state:\n- Physical state:\n- Relationships:\n- Secrets known:\n- Secrets hidden:\n- Abilities/resources:\n- Possessions:\n- Last seen:\n- Voice markers:\n\n",
    "bible/world-bible.md": "# World Bible\n\n## Rules\n\n## Locations\n\n## Institutions\n\n## Power / Tech / Magic Constraints\n\n## Calendar And Geography\n\n## Hard Limits\n\n",
    "bible/style-bible.md": "# Style Bible\n\n## POV And Tense\n\n## Prose Texture\n\n## Dialogue Style\n\n## Chapter Rhythm\n\n## Accepted Anchor Decisions\n\n## Avoid\n\n",
    "bible/timeline-ledger.md": "# Timeline Ledger\n\n| Chapter | Time | Location | Event | Consequence |\n|---:|---|---|---|---|\n",
    "bible/foreshadowing-ledger.md": "# Foreshadowing Ledger\n\n| ID | Item | Plant chapter | Reinforce | Payoff target | Status | Notes |\n|---|---|---:|---|---|---|---|\n",
    "bible/continuity-ledger.md": "# Continuity Ledger\n\n## Canon Facts\n\n## Object States\n\n## Injuries And Limits\n\n## Promises And Oaths\n\n## Open Questions\n\n",
    "plan/architecture.md": "# Novel Architecture\n\n## Premise\n\n## Cast\n\n## World\n\n## Plot Architecture\n\n## Volume Map\n\n## Ending Vector\n\n",
    "plan/volume-map.md": "# Volume Map\n\n| Volume | Chapters | Arc Promise | Major Turn | Ending State |\n|---|---|---|---|---|\n",
    "plan/directory.md": "# Chapter Directory\n\n## Chapter 001 - Title\n- Volume/arc:\n- Function:\n- POV:\n- Location/time:\n- Required beats:\n- Character changes:\n- Foreshadowing:\n- Payoffs:\n- New facts to ledger:\n- Cliffhanger/hand-off:\n\n",
    "plan/generation-plan.md": "# Generation Plan\n\n| Status | Chapter | Task | Inputs | Outputs | Audit |\n|---|---:|---|---|---|---|\n| pending | 001 | draft + audit + finalize | bible + directory | chapters/chapter-001.md | audits/chapter-001-audit.md |\n\n",
    "summaries/rolling-summary.md": "# Rolling Summary\n\n",
    "summaries/arc-summary.md": "# Arc Summary\n\n",
    "summaries/chapter-facts.md": "# Chapter Facts\n\n### Chapter 001\n- Time:\n- Location:\n- POV:\n- Main outcome:\n- Character deltas:\n- New canon facts:\n- Foreshadowing planted:\n- Foreshadowing paid:\n- Open questions:\n- Objects/status changes:\n\n",
    "audits/.gitkeep": "",
    "chapters/.gitkeep": "",
    "exports/.gitkeep": "",
}


STATE = {
    "project_type": "novel",
    "current_phase": "setup",
    "auto_resume": False,
    "hard_node": True,
    "target_chapters": None,
    "current_batch": None,
    "next_chapter": 1,
    "batch_size": 5,
    "last_completed_chapter": 0,
    "next_action": "Fill source material and generate architecture.",
    "generation_plan": "plan/generation-plan.md",
    "last_audit": None,
}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: init_novel_project.py <project-dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    for relative, content in FILES.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    state_path = root / ".codex-longtask" / "state.json"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    if not state_path.exists():
        state_path.write_text(json.dumps(STATE, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Novel project scaffolded at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
