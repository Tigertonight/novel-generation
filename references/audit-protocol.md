# Audit Protocol

Audit before calling a chapter or batch finalized.

## Severity

P0 - Must Fix
: Contradicts canon, breaks timeline, changes character knowledge impossibly, pays off unplanted key twist, loses required chapter beat, violates user taboo, or makes future plan impossible.

P1 - Should Fix
: Weak motivation, thin character impression, invisible world/background, flat pacing, missing dramatic action, missing value shift, style drift from Style DNA, generic AI prose, repeated scene pattern, unclear geography, chapter too short/long, foreshadowing vague, continuity likely to confuse readers.

P2 - Note
: Preference-level prose polish, optional tightening, future opportunity.

## Chapter Audit Checklist

```markdown
# Chapter NNN Audit

## Verdict
Pass / Needs repair

## Directory Coverage
- Required beats:
- Missing/changed beats:

## Continuity
- Timeline:
- Character knowledge:
- Physical/object state:
- World rules:

## Character
- Motivation:
- First impression / memorability:
- Exterior or behavioral specificity:
- Ghost / Lie / Flaw pressure:
- Want / Need tension:
- Relationship changes:
- Voice consistency:

## World And Background
- World facts naturally shown:
- Institutions/stakes/constraints visible in scene:
- Exposition risk:

## Foreshadowing
- Planted:
- Reinforced:
- Paid:
- Risks:

## Style And Craft
- Pacing:
- Chapter turn or reversal:
- Stage conflict:
- Dramatic action: goal -> obstacle -> result:
- Value shift:
- Dual-track pacing: external plot / internal emotion:
- Subtext through action:
- Style DNA fit:
- Scene Style Mode fit:
- AI-prose / over-explanation risk:
- Scene variety:
- Repetition:
- Prose voice:

## Issues
| Severity | Issue | Evidence | Repair |
|---|---|---|---|
```

## Batch Audit Checklist

```markdown
# Batch XXX Audit

## Chapters
NNN-NNN

## Plot Progress
- What moved:
- What stalled:
- Directory changes needed:

## Continuity Ledger Updates Needed
- Timeline:
- Characters:
- World:
- Objects:

## Foreshadowing Ledger
- Newly planted:
- Reinforced:
- Paid:
- Overdue:

## Repetition Scan
- Similar openings:
- Similar conflicts:
- Similar cliffhangers:
- Reused images/phrases:

## Reader Experience Scan
- Important characters with clear impressions:
- Characters still blurry:
- World/background facts visible through action:
- Chapters that feel procedural or flat:
- Missing mini-climax / reversal before next batch:

## Style Scan
- Style DNA drift:
- Scene Style Modes used:
- Repeated sentence rhythm:
- Overused images/metaphors:
- Abstract summary sentences:
- Dialogue explaining setting/theme:
- Strong memorable prose moments:

## Screenwriting Craft Scan
- Scenes missing goal -> obstacle -> result:
- Chapters missing value shift:
- Arc budget issues: change too fast / too slow / no useful regression:
- Dual-track pacing pattern:
- Secondary characters acting only as information tools:
- Dialogue explaining what action could show:

## Repair Queue
| Priority | Target | Action |
|---|---|---|
```

## Repair Policy

- P0 in current chapter: repair before moving on.
- P0 discovered across batch: pause generation, repair affected chapters or revise directory with user approval.
- Three consecutive P1 style/repetition failures: stop and revise `style-bible.md` or anchor pattern.
- Do not hide plot surgery. Record it in batch audit.
