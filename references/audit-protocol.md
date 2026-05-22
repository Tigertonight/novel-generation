# Audit Protocol

Audit before calling a chapter or batch finalized.

> **Run `references/hard-rules.md` audit snapshot first.** Any P0 from hard-rules.md is also P0 here. The list below extends those rules with continuity-and-style P0/P1 items.

## Severity

P0 - Must Fix
: Contradicts canon, breaks timeline, changes character knowledge impossibly, pays off unplanted key twist, loses required chapter beat, violates user taboo, makes future plan impossible, drops an important object/mechanism without planned payoff/loss/retirement, fails a required romance/intimacy/payoff promise across a batch, **or any hard-rules.md P0**:
  - new named/recurring character enters with fewer than 4/5 entrance anchors
  - key emotional scene has near-zero interiority
  - intimate scene lacks boundary, consequence, or relationship-state change; or treats coercion as reward
  - twice-emphasized mechanism vanishes for 8+ chapters with no retirement
  - commercial project goes 3 chapters with no effective payoff, or any 5-10 chapter batch is >60% one payoff type
  - career line / jargon eats >50% of a chapter in non-workplace projects, or 2+ consecutive chapters are mostly process
  - important relationship goes 5+ chapters with no state-line change in a project that promised romance
  - chapter packet missing POV / value shift / interior goal / new-character anchors / payoff design
  - same ability used 5+ times without cost or enemy counter

P1 - Should Fix
: Weak motivation, thin character impression, invisible world/background, flat pacing, missing dramatic action, missing value shift, style drift from Style DNA, generic AI prose, repeated scene pattern, unclear geography, chapter too short/long, foreshadowing vague, continuity likely to confuse readers, **plus hard-rules.md P1** (3 consecutive P1 of the same type escalates to P0):
  - important character described 2+ chapters with only generic words
  - camera-only passage exceeds ~600 zh-chars / ~400 en-words
  - important relationship appears in scene but isn't tested/deepened/complicated/clarified
  - single ability use without cost or counter
  - payoff without setup or without consequence
  - jargon term not translated into consequence or conflict
  - intimate scene swappable to any other pair (no character-specific desire)

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
- Object/weapon/system/clue ledger state:
- World rules:

## Character
- Motivation:
- First impression / memorability:
- New character entrance clarity:
- New character 5-anchor check (identity / visual / scene-relevance / POV reading / behavioral hook — at least 4/5):
- Identity/role/context anchor for new characters:
- Exterior or behavioral specificity:
- Appearance/current-state specificity:
- Generic-word red flags (漂亮/冷峻/高大/儒雅/危险/气场 stacked without specifics):
- Side-view impression, if entrance matters:
- POV/interiority specificity:
- Interior reaction after major external beats:
- Interior beat types present (instinct / suppressed / body-mind / memory / misread / desire-fear / self-deception / aftertaste):
- Ghost / Lie / Flaw pressure:
- Want / Need tension:
- Relationship changes — was the relationship tested/deepened/complicated/clarified?:
- Heat/intimacy movement, if enabled:
- Heat ladder position before/after:
- Voice consistency:

## World And Background
- World facts naturally shown:
- Institutions/stakes/constraints visible in scene:
- Exposition risk:
- Professional/jargon density:
- Plain consequence after technical detail:
- Career/workline compression:

## Foreshadowing
- Planted:
- Reinforced:
- Paid:
- Risks:

## Reward / Payoff
- Setup honored:
- Payoff delivered or deliberately delayed:
- Payoff type:
- Setup chapters (where the buildup was planted):
- Cost / consequence:
- Variety vs previous chapters (no >60% same-type within batch):
- Next escalation direction:

## Mechanism / Object Use
- Items/systems used this chapter:
- For each: when/why available, cost paid, why not infinite, enemy counter or response, what protagonist learned:
- Items emphasized earlier but absent now (chapters since last appearance):

## Career / Jargon Compression
- Career-or-process share of chapter (% of word count):
- Each new technical term + its plain-language consequence:
- Career beat binding (relationship / rivalry / status / public pressure / money / humiliation / moral choice / payoff):

## Intimacy / Heat, If Enabled
- Explicitness boundary honored:
- Adult consent/agency clear:
- Scene function:
- Desire specific to this pair:
- Physical choreography:
- Emotional turn:
- Aftermath or planned aftermath:
- Relationship state changed:

## Style And Craft
- Pacing:
- Chapter turn or reversal:
- Stage conflict:
- Dramatic action: goal -> obstacle -> result:
- Value shift:
- Interior turn:
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
- Object/mechanism ledger:
- Payoff ledger:

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
- Important appearances/current states rendered or missed:
- POV immersion / interiority:
- Camera-only or report-like passages:
- World/background facts visible through action:
- Chapters that feel procedural or flat:
- Professional terms that caused reading friction:
- Work/career scenes that overtake people/relationship/story:
- Missing mini-climax / reversal before next batch:
- Reward/payoff rhythm:
- Relationship heat/intimacy rhythm, if enabled:

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
