#!/usr/bin/env python3
"""Scaffold an auditable long-form novel project."""

from __future__ import annotations

import json
import sys
from pathlib import Path


FILES = {
    "source/.gitkeep": "",
    "research/market-research.md": "# Market Research\n\n## Research Date\n\n## User Seed\n\n## Target Channel / Audience\n- Male-channel / female-channel / cross-channel / literary / other:\n- Target platform style:\n- Target reader:\n\n## Sources Checked\n\n| Source | URL / locator | Date checked | What it was used for | Reliability |\n|---|---|---|---|---|\n\n## Comparable Matrix\n\n| Comparable | Platform/category | Why relevant | Reader promise | Hook pattern | Pacing | Character design | Relationship pattern | Long-serial engine | Do not copy |\n|---|---|---|---|---|---|---|---|---|---|\n\n## Market Signals\n- Popular tags / categories:\n- Common premise engines:\n- Common protagonist types:\n- Common relationship structures:\n- Common opening hooks:\n- Chapter rhythm / update rhythm:\n- Title and blurb conventions:\n- Reader anxieties:\n- Reader rewards:\n- Saturated patterns:\n- Differentiation opportunities:\n\n## Positioning Recommendation\n- One-line commercial hook:\n- Primary reader promise:\n- Secondary reader promise:\n- Best-fit platform/channel:\n- Core trope engine:\n- Differentiation:\n- Risk:\n- Avoid:\n\n",
    "bible/story-bible.md": "# Story Bible\n\n## Core Seed\n\n## Genre Promise\n\n## Central Dramatic Question\n\n## Ending Vector\n\n## Volume / Arc Map\n\n## Themes\n\n## Must Not Break\n\n",
    "bible/character-bible.md": "# Character Bible\n\n## Character Name\n- Stable identity:\n- Want / need / flaw:\n- Current goal:\n- Emotional state:\n- Physical state:\n- Relationships:\n- Secrets known:\n- Secrets hidden:\n- Abilities/resources:\n- Possessions:\n- Last seen:\n- Voice markers:\n\n",
    "bible/world-bible.md": "# World Bible\n\n## Rules\n\n## Locations\n\n## Institutions\n\n## Power / Tech / Magic Constraints\n\n## Calendar And Geography\n\n## Hard Limits\n\n",
    "bible/style-bible.md": "# Style Bible\n\n## POV And Tense\n\n## Prose Texture\n\n## Dialogue Style\n\n## Chapter Rhythm\n\n## Accepted Anchor Decisions\n\n## Avoid\n\n",
    "bible/timeline-ledger.md": "# Timeline Ledger\n\n| Chapter | Time | Location | Event | Consequence |\n|---:|---|---|---|---|\n",
    "bible/foreshadowing-ledger.md": "# Foreshadowing Ledger\n\n| ID | Item | Plant chapter | Reinforce | Payoff target | Status | Notes |\n|---|---|---:|---|---|---|---|\n",
    "bible/continuity-ledger.md": "# Continuity Ledger\n\n## Canon Facts\n\n## Object States\n\n## Injuries And Limits\n\n## Promises And Oaths\n\n## Open Questions\n\n",
    "plan/market-positioning.md": "# Market Positioning\n\n## Channel And Platform Fit\n- Channel:\n- Platform style:\n- Target reader:\n\n## Reader Contract\n- Core pleasure:\n- Core anxiety:\n- First promise:\n- Long promise:\n\n## Commercial Hook\n- One-line hook:\n- Title direction:\n- Blurb direction:\n- First-three-chapter hook:\n\n## Trope Engine\n- Main trope:\n- Support tropes:\n- Expected payoff rhythm:\n- Differentiation:\n- Saturation risk:\n\n## Character Design Direction\n- Protagonist starting pressure:\n- Protagonist long arc:\n- Key supporting roles:\n- Relationship model:\n- Antagonist/opposition ladder:\n\n## Serial Engine\n- What can generate 100+ chapters:\n- What escalates by volume:\n- What stays emotionally unfinished:\n- What recurring reader reward can repeat without going stale:\n\n",
    "plan/architecture.md": "# Novel Architecture\n\n## Market Positioning Summary\n\n## Premise\n\n## Cast\n\n## World\n\n## Plot Architecture\n\n## Volume Map\n\n## Ending Vector\n\n",
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
    "next_action": "Fill source material, run market research if needed, then generate positioning and architecture.",
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
