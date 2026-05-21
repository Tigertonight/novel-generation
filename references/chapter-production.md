# Chapter Production

## Recommended Defaults

- Chapter length: 2500-4000 Chinese characters.
- Batch size: 5-10 chapters.
- Review cadence: every batch, plus anchor chapters.
- Generation order: sequential unless the user explicitly accepts continuity risk.

## Anchor Chapters

Generate chapter 1 and one structurally difficult chapter before bulk work. Use them to lock:
- voice
- paragraph density
- dialogue ratio
- exposition style
- scene granularity
- ending hook style
- character entrance style
- worldbuilding-through-action style
- early conflict/reversal density

After anchors, write accepted decisions into `bible/style-bible.md`.

## Chapter Packet

Before writing a chapter, build a packet:

```markdown
# Chapter Packet NNN

## Mission
<directory entry: function, beats, changes, required payoff/plant>

## Reader Experience
- character impression to strengthen
- new characters introduced and their entrance anchors
- appearance/current-state impression to render, if relevant
- side-view reaction to the character, if useful
- POV/interiority target: what the reader should feel from inside the character
- world/context detail to reveal through action
- stage conflict or reversal in this chapter
- reward/payoff expectation for this chapter
- emotional question the reader should carry forward

## Dramatic Craft
- scene-level dramatic action: goal -> obstacle -> result
- value shift: what changes from chapter start to end
- character arc pressure: Ghost / Lie / Flaw / Want / Need involved
- dual-track pacing: external plot intensity + internal emotional intensity
- interior turn: how the POV's private understanding, desire, fear, shame, trust, or self-deception changes
- subtext/action plan: what should be shown through behavior rather than explained

## Context
- previous chapter ending
- last 2-3 chapter facts
- current arc summary

## Canon Constraints
- relevant character states
- relevant appearance/current presentation notes
- relevant relationship and heat-state lines
- intimacy design card and explicitness boundary, if enabled
- relevant object/mechanism rows
- relevant timeline rows
- relevant world rules
- relevant continuity facts

## Immersion / Jargon Control
- POV character:
- narrative distance: close / medium-close / cinematic with interior beats / other
- dominant inner pressure:
- body-mind signal:
- memory/wound touched:
- line of thought to leave unfinished:
- professional-detail budget:
- new technical terms allowed:
- plain-language consequence for each technical detail:
- career/workline content to compress or omit:

## Foreshadowing
- must plant
- must reinforce
- must pay off
- must not reveal yet

## Payoff / Continuity Objects
- payoff to deliver or delay
- important object/weapon/system/clue state before chapter
- object/weapon/system/clue state after chapter
- cost, loss, upgrade, or consequence to carry forward

## Intimacy / Heat Craft, If Enabled
- scene function: temptation / care / power / jealousy / boundary / trust / rupture / repair / consummation / aftermath
- starting relationship state
- ending relationship state
- POV desire and fear/restraint
- boundary/consent beat
- physical choreography
- sensory palette
- subtext
- interruption/risk
- emotional turn
- aftermath hook

## Style Contract
<style-bible slice>
- Style DNA:
- Scene Style Mode:
- Golden Sample / Anti Sample guidance:
- Comparable references to borrow from only at the level of genre expectations, pacing, narration distance, and scene density:

## Output Contract
- prose only unless user asks otherwise
- no markdown headings inside chapter
- target length
- no recap dump
```

## Drafting Guidance

Ask the model to produce a full chapter with:
- 2-4 scenes unless directory demands otherwise
- clear scene objective and turn
- clear dramatic action in every major scene: a character pursues something, meets resistance, and leaves with a changed situation
- one emotional movement
- one plot movement
- one interior movement: a private reaction, misread, suppressed thought, bodily aftershock, memory shard, or self-deception shift
- one designed reader reward when the genre/channel calls for it: competence proof, reveal, upgrade, public correction, relationship heat, dignity recovery, resource gain, or emotional catharsis
- one value shift such as trust -> suspicion, safety -> danger, control -> loss of control, hope -> dread, intimacy -> distance, ignorance -> burdened knowledge
- at least one concrete characterizing detail for important POV/major characters: exterior signal, current clothing/state, habit, contradiction, sensory detail, side-view impression, or pressure response
- for every named or recurring new character, a minimum entrance: identity/role anchor, visual or physical anchor, context/relevance anchor, POV/social reading, and one behavioral hook
- for walk-on functional characters, at least role + one visual/behavioral detail + immediate relevance
- for major entrances, a memorable appearance/behavior/social impression shaped by the observing POV
- for romance or intimate-tension scenes, a visible relationship movement through action, subtext, touch/proximity, restraint, boundary, vulnerability, choreography, sensory specificity, or aftermath according to the project's explicitness boundary and intimacy design card
- for important objects, weapons, systems, clues, or recurring opportunities, a continuity-aware use, absence, cost, upgrade, pressure, or payoff rather than silent disappearance
- at least one world/context detail dramatized through action, cost, setting, institution, interface, public reaction, or constraint; avoid encyclopedia exposition
- professional/industry details translated into plain consequences, leverage, public cost, money/status/access pressure, or relationship movement; avoid terminology dumps
- a chapter-level turn: new pressure, reversal, reveal, choice, cost, or changed relationship
- one continuity-aware hand-off to the next chapter
- prose that follows the active Scene Style Mode; do not write every chapter in the same voice if the scene function differs
- no author imitation, no copied phrasing, no generic "literary" inflation, and no AI-like abstract summary

In the opening movement, avoid long stretches where the only movement is investigation or explanation. If a chapter is mostly clue analysis, add a human cost, public pressure, relationship fracture, false choice, or mini-reversal.

Do not ask for "outline then chapter" in one giant output if it causes length failure. For high-risk chapters, generate:
1. micro-outline
2. scene draft(s)
3. stitched chapter
4. audit and repair

## Finalization

After a chapter is accepted:
1. save chapter
2. create chapter audit
3. append chapter facts
4. update character states
5. update timeline
6. update foreshadowing
7. update continuity facts
8. update rolling and arc summaries
9. mark generation plan row complete

## Directory Micro-Adjustment

After each batch, adjust future directory entries when:
- character motivation changed
- a reveal moved earlier/later
- pacing became too fast/slow
- an unplanned but useful subplot emerged

Record changes in `audits/batch-XXX-audit.md`; do not silently rewrite the plan.
