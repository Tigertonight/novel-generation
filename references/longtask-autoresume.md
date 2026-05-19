# Longtask Autoresume

Use this only when the user requests long-running, batch, auto-continue, or unattended generation.

## State File

Create `.codex-longtask/state.json`.

```json
{
  "project_type": "novel",
  "current_phase": "directory",
  "auto_resume": false,
  "hard_node": true,
  "target_chapters": 80,
  "current_batch": null,
  "next_chapter": 1,
  "batch_size": 5,
  "last_completed_chapter": 0,
  "next_action": "Wait for user approval of architecture and directory.",
  "generation_plan": "plan/generation-plan.md",
  "last_audit": null
}
```

## Rules

- `plan/generation-plan.md` is the queue truth source.
- `state.json` is only the scheduler pointer.
- Update state after every chapter, audit, ledger update, batch, and hard node.
- Auto-resume may cross normal chapter production steps.
- Auto-resume must not cross hard nodes:
  - Architecture checkpoint
  - Directory checkpoint
  - Anchor approval
  - P0 audit failure
  - major plot surgery
  - repeated quality failures
  - user asks to pause or review

## Agentic Loop

```text
read state.json
read generation-plan.md
if hard_node: report and stop
pick next incomplete task
build chapter packet
generate or repair artifact
audit
if P0: set hard_node true and stop
update ledgers
update state
continue while budget/time allows
```

## Resume Prompt Shape

When resuming, read:
1. `.codex-longtask/state.json`
2. `plan/generation-plan.md`
3. latest batch audit
4. relevant bible/ledgers
5. latest chapters only as needed

Then continue from `next_action`.

