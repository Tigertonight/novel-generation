# Bible And Ledgers

Use layered memory. This is the main fix for long-novel drift.

## Files

`bible/story-bible.md`
: Premise, themes, dramatic question, ending vector, arc map, genre promise.

`bible/character-bible.md`
: Stable facts plus current state. Track want/need/flaw, relationships, secrets, abilities, injuries, possessions, voice markers, appearance anchors, current presentation, and entrance impressions.

`bible/relationship-map.md`
: Relationship states and movement. Track trust, tension, attraction, boundaries, wants, secrets, recent changes, next pressure tests, and intimacy/heat curves when relevant.

`bible/object-mechanism-ledger.md`
: Important objects, weapons, clues, artifacts, resources, contracts, titles, systems, abilities, and recurring opportunities. Track owner, location, state, rules, costs, limitations, upgrades, use history, and payoff targets.

`bible/payoff-ledger.md`
: Commercial reward and reader-satisfaction tracking. Track face-slaps, upgrades, reveals, resources, romance heat, public recognition, revenge, faction expansion, freedom gains, catharsis, and their consequences.

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
- Appearance/state changes:
- Relationship/heat changes:
- New canon facts:
- Foreshadowing planted:
- Foreshadowing paid:
- Payoffs delivered:
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
- Appearance anchors:
- Current presentation:
- Entrance impression:
- Side-view impressions:
- Relationships:
- Secrets known:
- Secrets hidden:
- Abilities/resources:
- Possessions:
- Last seen:
- Voice markers:
```

## Appearance And Entrance Format

Use this for major characters and for any scene where a character's first impression matters.

```markdown
## Character Name - Appearance
- Durable anchors: face, eyes, build, posture, movement, voice, scent/sensory cue, distinctive mark/object
- Default styling: clothing, grooming, color/material preferences, status signals
- Current state: injury, fatigue, disguise, battle damage, formal wear, travel wear, poverty/wealth display
- First entrance promise: what the reader should remember after the first appearance
- POV impression notes: how different characters misread or recognize this person
- Update triggers: injury, promotion, disgrace, disguise, intimacy, grief, public victory, loss
```

Do not repeat the same generic beauty/handsomeness line. Reuse anchors, then change presentation according to state, power, emotion, setting, and the POV character's desire or bias.

## Relationship State Format

```markdown
## A / B
- Surface relationship:
- Private truth:
- Trust level:
- Attraction / repulsion:
- Power balance:
- What A wants:
- What B wants:
- Boundary:
- Secret / misunderstanding:
- Recent change:
- Interaction frequency target:
- Heat/intimacy stage:
- Next pressure test:
- Possible deepening:
- Possible rupture:
```

When romance or intimate tension is enabled, define the project's explicitness boundary before drafting. Intimate scenes should change trust, leverage, vulnerability, commitment, conflict, status, or future choices.

## Object / Mechanism Ledger Format

```markdown
| ID | Item / mechanism | Owner | Location | State | Rule / use | Cost / limit | Last used | Upgrade / change path | Payoff target | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| O-001 | ... | ... | ... | active | ... | ... | Ch. 003 | ... | Ch. 018 | planted |
```

Use this ledger for weapons, artifacts, clues, contracts, titles, systems, abilities, resources, and recurring opportunities. If an item was important enough to hook the reader, it needs a payoff, transformation, loss, upgrade, or explicit retirement.

## Payoff Ledger Format

```markdown
| Chapter | Payoff type | Setup source | On-page reward | Cost / consequence | Next escalation |
|---:|---|---|---|---|---|
| 003 | public correction | Ch. 001 insult | opponent exposed before witnesses | new enemy notices | faction retaliation |
```

Rotate payoff types across a batch. A strong batch usually mixes external win, emotional movement, mechanism clarity, relationship heat, and a new cost rather than repeating one reward pattern.

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
- relevant appearance/current presentation notes
- relevant relationship and heat-state lines
- relevant timeline range
- relevant foreshadowing rows
- relevant object/mechanism rows
- recent payoff rows and next payoff target
- style contract

Avoid dumping the whole bible unless generating architecture or doing a major audit.
