# Bible And Ledgers

Use layered memory. This is the main fix for long-novel drift.

## Files

`bible/story-bible.md`
: Premise, themes, dramatic question, ending vector, arc map, genre promise.

`bible/character-bible.md`
: Stable facts plus current state. Track want/need/flaw, relationships, secrets, abilities, injuries, possessions, voice markers.

`bible/world-bible.md`
: World rules, institutions, magic/technology constraints, geography, calendar, economy, social norms, hard limits.

`bible/style-bible.md`
: POV, tense, diction, chapter rhythm, dialogue style, taboo phrases, desired comparable feel, "do not do" list.

`bible/timeline-ledger.md`
: Chronological event log. Include absolute/relative time, location, participants, consequences.

`bible/foreshadowing-ledger.md`
: Plant/payoff tracking. Every item needs status: planned, planted, reinforced, paid, abandoned.

`bible/continuity-ledger.md`
: Canon facts that must not drift: names, ages, locations, injuries, powers, objects, promises, constraints.

`summaries/rolling-summary.md`
: Short global progress summary, capped for prompt use. It is not the only memory.

`summaries/arc-summary.md`
: One section per volume/arc with current arc state and unresolved tensions.

`summaries/chapter-facts.md`
: Dense bullet facts per chapter. This is often more useful than prose summary.

## Chapter Fact Format

```markdown
### Chapter 012
- Time:
- Location:
- POV:
- Main outcome:
- Character deltas:
- New canon facts:
- Foreshadowing planted:
- Foreshadowing paid:
- Open questions:
- Objects/status changes:
```

## Character State Format

```markdown
## Character Name
- Stable identity:
- Want / need / flaw:
- Current goal:
- Emotional state:
- Physical state:
- Relationships:
- Secrets known:
- Secrets hidden:
- Abilities/resources:
- Possessions:
- Last seen:
- Voice markers:
```

## Foreshadowing Ledger Format

```markdown
| ID | Item | Plant chapter | Reinforce | Payoff target | Status | Notes |
|---|---|---:|---|---|---|---|
| F-001 | ... | 003 | 009, 014 | 027 | planted | ... |
```

## Prompt Assembly Rule

For each chapter prompt include only the needed slices:
- current chapter directory entry
- previous chapter ending
- last 2-3 chapter facts
- relevant arc summary
- relevant character states
- relevant timeline range
- relevant foreshadowing rows
- style contract

Avoid dumping the whole bible unless generating architecture or doing a major audit.

