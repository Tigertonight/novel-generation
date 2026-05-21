# Genre-Adaptive Quality Layer

Use this reference when planning, generating, auditing, or repairing long-form fiction. Its purpose is to make the skill genre-adaptive: choose the craft modules that serve the novel's reader promise, and do not mechanically force modules that do not belong.

This layer must be applied before drafting, not only during audit. The design bible, directory, batch design cards, chapter prompts, and repair passes should all use the selected modules.

## Core Principle

A long novel is not just a sequence of events. Each batch should deliver the type of tension the genre promises, change the characters or world state, and leave consequences that matter later.

Different genres need different kinds of pressure:
- A combat-forward progression fantasy needs vivid action, ability pressure, resource costs, and visible growth.
- A mystery needs clue placement, fair misdirection, witness/testimony pressure, deduction chains, and satisfying revelation.
- A romance needs emotional movement, boundaries, subtext, intimacy, misunderstanding, and changed choices.
- A political or faction story needs interests, leverage, public/private positions, alliances, tradeoffs, and institutional consequences.
- A quiet literary or slice-of-life story may need subtle interior movement, social pressure, sensory specificity, and restrained consequence rather than fights or spectacle.

## Genre Promise First

During market positioning, architecture, and before every batch, identify:

```text
Primary genre promise:
Secondary genre promise:
Target channel / platform style:
Reader's expected pleasures:
Reader's expected anxieties:
Modules to enable:
Modules to weaken:
Modules to avoid unless naturally required:
```

Do not add combat, romance, mystery, faction politics, or power-ups merely because the module exists. Use the module only when it fulfills the genre contract or the current arc's natural pressure.

For webnovel projects, use `webnovel-market-positioning.md` before finalizing these choices. If current market fit matters, use `webnovel-market-research.md` as a dynamic supplement. Treat male-channel/female-channel/platform signals as reader-contract evidence, not as rigid gender essentialism.

## Channel And Market Modules

Enable these modules only when they fit the target lane and project promise:

- `Male-Channel Reward Loop`: comeback, rise-to-the-top, upgrade, resource, rank, public correction, territory/faction expansion, or freedom payoff.
- `Female-Channel Relationship / Identity Loop`: identity reversal, social-field pressure, emotional agency, relationship state movement, dignity recovery, competence display, or self-determination.
- `Face-Slap / Public Correction`: false public belief, opponent leverage, protagonist preparation, witness reaction, and consequence.
- `Growth / Upgrade Engine`: trigger, resource, limit, cost, failure mode, next threshold, and enemy counter.
- `Rebirth / Transmigration Advantage`: information advantage, blind spots, changed timeline, old wound, and new consequence.
- `System / Mechanism Engine`: rule, reward, loophole, cost, failure mode, and protagonist agency beyond the system.
- `Protagonist Team`: differentiated roles, desires, limits, loyalty tension, and rotating contribution.
- `Multi-Heroine / Relationship-Light / Single-Heroine Choice`: explicit reader contract, each important character's agency, boundaries, desire, arc, and consequence.
- `Social Field / Institution Pressure`: family, workplace, court, school, sect, entertainment, law, money, reputation, etiquette, taboo, or public opinion.
- `Long-Serial Expansion`: map, stakes, faction pressure, resource scale, secret depth, emotional obligation, and cost expansion.

## Planning Outputs

Before bulk chapter generation, create or update the planning artifacts that match the genre. Use compact files or sections; do not overbuild unused systems.

Recommended baseline:

```text
research/market-research.md       source-cited market signals and comparable matrix when needed
plan/market-positioning.md        channel, platform style, reader contract, hook, trope engine
plan/architecture.md              premise, theme, dramatic question, genre promise
plan/volume-map.md                macro arcs and major turns
plan/directory.md                 chapter/arc directory
bible/character-bible.md          character cards
bible/relationship-map.md         trust, tension, attraction, rivalry, dependency
bible/faction-map.md              organizations, institutions, power blocs
bible/mechanism-map.md            system/magic/law/investigation/social rules as needed
bible/object-mechanism-ledger.md  weapons, artifacts, clues, systems, abilities, resources, contracts
bible/foreshadowing-ledger.md     clues, promises, reveals, payoffs
bible/payoff-ledger.md            reward/payoff rhythm, setup, delivery, consequence, escalation
summaries/chapter-facts.md        chapter-level truth after generation
```

Genre-specific additions:
- Mystery/conspiracy: `bible/clue-ledger.md` or a clue section in the foreshadowing ledger.
- Combat/progression: ability progression, combat style cards, resource/cost ledger.
- Romance/relationship-led: relationship stage map and emotional beat outline.
- Political/faction-led: faction leverage map and public/private position tracker.
- Slice-of-life/literary: interior arc map, social pressure map, motif/sensory palette.
- Commercial/webnovel: payoff ladder and chapter/batch reward rhythm.

## Character Cards

Each major character should have a character dossier before drafting important scenes. Keep it compact enough to use, but detailed enough to make the character visually, emotionally, and relationally stable across a long novel:

```text
Name:
Aliases / titles:
Role in story:
Genre function:
Age / apparent age:
Identity / occupation / social position:
Faction / allegiance / public stance:
Private stance:
Personality:
Temperament under pressure:
Values / moral line:
External want:
Internal need:
Fear/wound:
False belief:
Agency / active methods:
Pressure from plot:
Pressure from relationships:
Detailed appearance:
  Face / expression:
  Body / posture / movement:
  Clothing / styling:
  Distinctive marks / objects:
  Sensory anchors:
  Current presentation / state:
Entrance impression:
Side-view impressions:
Signature behavior:
Voice / speech pattern:
Key relationships:
Relationship changes so far:
Current status:
Abilities / resources:
Limits / vulnerabilities:
Arc direction:
Current cost or wound:
Changes that have happened in-story:
Next test:
```

Use cards during generation. A character card is not just a reference; it should shape what the character notices, chooses, hides, refuses, and risks. Update it after major events so later chapters reflect changed trust, injuries, status, beliefs, appearance, resources, and emotional residue.

Appearance should be specific but not static. Track durable anchors, then let stress, injury, wealth, travel, disguise, grief, confidence, intimacy, battle damage, or status changes alter presentation over time. Important entrances should include a memorable visual/behavioral/social impression and, when useful, a side-view reaction from another character. Avoid repeatedly describing a character with one generic adjective.

## Character Appearance / Entrance Module

Use for all important characters and for scenes where the reader needs a strong first or renewed impression.

For every named or recurring new character, even before they become important, include a minimum entrance:

```text
Identity anchor: name, role, social position, faction, job, relationship, or immediate scene function
Visual/physical anchor: face, build, clothing, age impression, posture, voice, object, injury, scent, or movement
Context anchor: why this person appears here and now
POV/social reading: how the POV or nearby people interpret, misread, fear, respect, desire, resent, or dismiss them
Behavioral hook: one action, line, habit, choice, or pressure response
```

For first-person POV, filter the entrance through the narrator's bias and history. For third-person POV, use close perception, social reaction, or scene pressure. Do not drop a new name into the scene without role, image, and relevance.

Design:

```text
Durable appearance anchors:
Default clothing/styling:
Current state overlay: injury / fatigue / disguise / battle damage / formal wear / poverty / wealth / authority / intimacy
Entrance action: what the character is doing when first seen
POV filter: desire, fear, class bias, rivalry, attraction, resentment, awe, or suspicion
Side-view impression: how an observer reads the person before knowing the truth
Description limit: what not to repeat every appearance
```

Generation rule: describe appearance through action, social reaction, sensory anchors, and current state. Do not pause the story for a static catalog unless the genre intentionally wants a lavish entrance.

## Relationship Map

Track key relationships as changing states:

```text
Pair / group:
Current trust level:
Surface relationship:
Private truth:
Attraction / repulsion:
Power balance:
What A wants from B:
What B wants from A:
Boundary:
Secret / misunderstanding:
Unresolved tension:
Recent change:
Interaction frequency target:
Heat/intimacy stage:
Next pressure test:
Possible deepening:
Possible rupture:
```

Use this while drafting. If a scene includes a major relationship, the scene should either test, deepen, complicate, or clarify it. Do not let relationships remain static across many chapters unless the stasis itself is dramatic.

## Faction / Institution Cards

For every significant organized power, design before heavy use:

```text
Name:
Public identity:
Private agenda:
What it wants:
What it fears:
Resources:
Debts / history:
Secrets:
Internal divisions:
Representative characters:
Leverage over protagonist:
Vulnerability:
How it pressures the current arc:
```

Use faction cards to design scenes. Institutions should not appear only to give quests or block doors; they should exert pressure through reputation, law, money, violence, access, taboo, labor, information, or legitimacy.

## Mechanism Map

For any story engine, create a staged mechanism map:

```text
Mechanism name:
What it appears to be:
What it really is, if known:
Trigger:
User / actor:
Inputs:
Output:
Limit:
Cost:
Failure mode:
Enemy counter:
Upgrade path:
Narrative purpose:
Reader-facing reveal stages:
```

Mechanism can mean system, magic, cultivation, law, investigation procedure, social status, contract, game rule, technology, prophecy, or taboo.

Generation must use the map. Do not introduce new mechanism behavior in a chapter unless it is already planned or is immediately entered into the map/ledger.

## Theme And Curve Design

Theme should become scene pressure, not just an abstract sentence.

Before drafting, define:

```text
Theme / central argument:
Counterargument:
What the protagonist initially believes:
What the antagonist or world believes:
What recurring choices test the theme:
What victory would prove:
What failure would prove:
```

Then design curves:
- Plot curve: external escalation.
- Growth curve: protagonist's changing belief/method.
- Relationship curve: trust, fracture, intimacy, rivalry, or loyalty.
- Mechanism curve: rules discovered, costs paid, counters learned.
- Suspense curve: questions opened, clues planted, partial truths revealed.
- Power/status curve: resources, reputation, ability, rank, access.

Each volume or major arc should move several curves, but not all at the same intensity.

## Adaptive Module Selection

Enable modules by genre and arc need:

- `Combat Craft`: martial arts, xianxia, fantasy action, war, superhero, survival, thriller, game, progression, and any arc whose core tension is physical confrontation.
- `Mystery / Clue Chain`: detective, thriller, conspiracy, investigation, legal/procedural, puzzle-box fantasy, hidden-history arcs, and any arc where revelation is the main pleasure.
- `Relationship Progression`: romance, family drama, team stories, coming-of-age, found family, rivalries, betrayals, and character-driven arcs.
- `Power / Mechanism Clarity`: system fiction, magic, cultivation, superpowers, contracts, time loops, games, rules horror, social mechanisms, procedural law, or any story with a repeatable engine.
- `Faction / Institution Map`: court, sect, clan, corporate, political, military, academia, police, legal, family inheritance, and any arc driven by organized power.
- `Reader Experience Audit`: all novels.
- `Growth Loop`: all character-led long-form novels.
- `Post-Arc Consequence`: all serialized novels.

## Batch Design Card

Before generating a 5-10 chapter batch, create a brief design card. This card is a generation prompt contract, not just an audit checklist:

```text
Batch range:
Genre focus:
Enabled modules:
Weakened/avoided modules:
Core promise:
Protagonist growth loop:
Crisis type mix:
Key relationship movement:
Heat/intimacy movement, if enabled:
POV/interiority target:
Core mechanism reveal/upgrade/cost:
Object/weapon/system continuity needs:
Professional-detail budget:
Reward/payoff mix:
Faction/world pressure:
Action/investigation/emotion set piece:
Consequence to carry forward:
Hook variety:
Exit standard:
```

The card should be short, but generation and audit must honor it. When drafting chapters, deliberately write scenes that fulfill the card: put the crisis on-page, dramatize the relationship movement, reveal or stress the mechanism, deliver the planned reward, and leave the planned consequence.

## Generation Use

During chapter drafting:
- Pull relevant character cards into the chapter prompt/context.
- Pull the current relationship-state line for any major pair in the scene.
- Pull faction/institution pressure when the scene involves organized power.
- Pull mechanism limits/costs before using the mechanism.
- Pull clue/reveal plan before writing mystery or investigation scenes.
- Pull the batch consequence target so the chapter does not resolve too cleanly.

Do not generate a chapter from only the previous chapter summary when the scene depends on character arcs, relationships, factions, or mechanisms.

## Directory Design

Directory is not just event order. For each arc or chapter cluster, mark:

```text
External plot beat:
Character growth beat:
Relationship beat:
Mechanism / clue / world reveal:
Genre-specific set piece:
Cost / consequence:
Hook:
```

This lets later generation aim at designed movement instead of discovering all craft needs during audit.

## Growth Loop

Every small arc should answer:

```text
What does the character currently rely on?
How does the crisis make that reliance fail or become insufficient?
What price is paid?
What new understanding, ability, relationship, or status emerges?
How will this change the next batch?
```

If events happen but nobody changes, repair the batch.

## Crisis Type Rotation

Avoid repeated conflict patterns. Choose pressure types that fit the genre:

- Time pressure: deadline, countdown, evidence decay, rescue window.
- Survival pressure: injury, exhaustion, pursuit, exposure, hunger, limited shelter.
- Combat pressure: enemy style mismatch, terrain disadvantage, forced defense, collateral risk.
- Mystery pressure: false clue, missing witness, contradictory testimony, impossible timeline.
- Relationship pressure: mistrust, misread motive, betrayal, boundary violation, delayed apology.
- Resource pressure: limited magic/tool/access/money/social capital/credibility.
- Rule pressure: law, contract, ritual, institution, taboo, procedure.
- Public pressure: rumor, trial, public shame, propaganda, social media, court opinion.
- Moral pressure: save one vs. expose truth, protect friend vs. obey duty.
- Temptation pressure: shortcut, corrupt power, easy lie, revenge, public glory.

Do not solve every batch with the same pattern.

## Core Mechanism Clarity

For any repeatable story engine, stage clarity over time:

```text
First trigger
First successful use
First limit
First cost
First failure
Enemy counter-use
Protagonist adaptation
Mechanism's deeper truth
```

Mechanism can mean magic, cultivation, systems, law, investigation rules, social status, political procedure, contracts, technology, or narrative constraints.

Every important use should make clear:
- Why it works now.
- What it costs.
- Why it cannot be used infinitely.
- What the protagonist learns from it.
- How an enemy might exploit or counter it.

## Combat Craft Module

Use only when the genre or current scene naturally calls for action.

A strong action scene needs:
- Clear scene goal beyond "win the fight."
- Distinct combat styles tied to character.
- Spatial grounding: distance, cover, terrain, obstacles, bystanders.
- Tactical beats: feint, mistake, adaptation, reversal, cost.
- Sensory specificity: breath, pain, grip, footing, impact, sound.
- Consequence after the fight: injury, resource loss, fear, respect, evidence destroyed, relationship shift.

Avoid generic exchanges of light, force, and shock. Do not let action pause for long exposition unless the genre style supports it.

## Mystery / Clue Chain Module

Use for investigation, hidden-history, conspiracy, legal/procedural, and clue-driven arcs.

Track:
- Question being investigated.
- Known facts.
- Unknowns.
- Clues planted.
- False but fair interpretations.
- Witness reliability.
- Evidence chain of custody.
- Revelation order.
- What the reader can infer before the protagonist.
- What remains unresolved after the reveal.

Rules:
- Do not solve mysteries through unsupported intuition.
- Major reveals should recontextualize earlier details.
- Red herrings must be plausible and meaningful, not random noise.
- The truth should create new consequences, not merely end the puzzle.

## Relationship Progression Module

Use for romance, friendship, rivalry, family, team, mentor/student, or enemy alliances.

Track each key relationship stage:

```text
Strangers / assumptions
Contact / friction
Temporary alignment
First trust
Trust tested
Boundary or wound revealed
Costly choice for the other
Relationship redefined
```

Progress through action, withheld words, misread motives, changed decisions, and shared consequences. Do not rely only on direct confession or exposition.

For romance, avoid treating a character as a reward. Each party needs private desire, fear, agency, boundaries, appetite, hesitation, and the right not to forgive immediately.

When romance, marriage, harem/multi-heroine, desire, or intimate attraction is part of the reader contract, also track a heat/intimacy curve:

```text
Look / notice
Friction / banter
Protective or possessive impulse
Voluntary proximity
Touch with plausible excuse
Private vulnerability
Jealousy or fear of loss
Open desire
Boundary negotiation
Intimacy / fade-to-black / explicit scene according to user boundary
Aftermath: tenderness, awkwardness, leverage, guilt, trust, danger, commitment, rupture
```

Use heat as scene pressure, not decoration. A charged scene should change behavior afterward: more trust, more fear, a new secret, altered power, public risk, emotional dependence, or a harder choice.

## Object / Mechanism Continuity Module

Use for important props, clues, weapons, artifacts, resources, titles, contracts, systems, abilities, opportunities, and recurring mechanisms.

Track each item:

```text
ID:
Name:
Type:
Owner / controller:
Location:
Current state:
Known rule:
Unknown deeper rule:
Cost / limit:
Failure mode:
Enemy counter:
Upgrade / transformation path:
Last on-page use:
Next planned pressure:
Payoff / retirement target:
```

Rules:
- If the story highlights an object or mechanism as important, it must return with payoff, loss, transformation, upgrade, or deliberate retirement.
- Let early advantages become later liabilities, counters, temptations, or costs.
- Weapons and systems should develop usage style, limits, emotional meaning, and enemy responses over time.
- Clues and contracts should keep chain-of-custody and interpretation state, not just appear when convenient.

## Reward / Payoff Ladder Module

Use for commercial genre fiction, webnovels, progression, revenge, romance-forward, system, face-slap, career, faction, and other satisfaction-driven projects.

Before each arc or batch, design a payoff mix:

```text
Baseline frequency:
Major payoff chapters:
Minor payoff chapters:
Reward types to use:
Reward types to avoid repeating:
Setup required:
Witness/public reaction:
Cost/consequence:
Next escalation:
```

Common payoff types:
- competence proof
- public correction / face-slap
- upgrade, skill, rank, title, resource, money, territory, access
- weapon/artifact/system feature reveal
- clue reveal or identity reversal
- rescue, revenge, protection, survival, escape
- romantic heat, intimacy, tenderness, jealousy, commitment, relationship redefinition
- faction gain, ally gain, reputation gain, enemy exposure
- emotional catharsis, dignity recovery, being seen correctly

Payoff design rule: vary the reader reward. A batch that only repeats "enemy mocks -> protagonist wins" will feel shallow even if every scene is technically exciting. Escalate depth by changing who witnesses, what it costs, what new door opens, and what emotional or strategic consequence remains.

## Character Interior Pass

Major characters should not exist only as plot functions. In important scenes, check:
- What does this character want right now?
- What are they afraid to admit?
- What do they misunderstand?
- What line will they not cross?
- What choice costs them something?
- What detail, gesture, or speech pattern belongs only to them?
- What does the scene feel like from inside their body or private logic?
- What thought do they suppress, misread, or leave unfinished?

If a supporting character only confirms the protagonist's correctness, repair or reduce the scene.

## Immersion / Interiority Module

Use when prose feels camera-only, detached, report-like, or insufficiently immersive.

Each important scene should include:
- POV selection: what this character notices because of desire, fear, pride, shame, attraction, resentment, or expertise.
- Body-mind signal: breath, heat, numbness, pulse, posture, delayed pain, nausea, stillness, or a repeated gesture.
- Private interpretation: what the POV thinks another person means, whether right or wrong.
- Suppressed thought: what the POV refuses to say, admit, or finish thinking.
- Interior turn: how the character's private state changes by the scene end.

Do not make every paragraph interior monologue. The target is rhythm: external event -> inner pressure -> action/choice -> consequence -> aftershock.

## Professional Detail / Jargon Control Module

Use for career, workplace, officialdom, business, entertainment, legal, gaming, medicine, military, academic, or any industry-heavy arc.

Professional detail should pass at least one test:
- It changes leverage, access, money, status, safety, reputation, intimacy, trust, or public pressure.
- It reveals character competence under pressure.
- It creates a choice, cost, humiliation, reward, betrayal, or relationship turn.
- It is necessary for the reader to understand a payoff.

Prefer plain consequences over expert explanation. Avoid stacking proper nouns, processes, acronyms, metrics, titles, departments, tools, legal terms, or industry references unless the scene's pleasure is specifically competence, deduction, or strategy.

Default webnovel/commercial budget:
- 0-2 new technical terms per chapter unless this is a planned strategy set piece.
- No more than one compact professional explanation block.
- Every technical term needs an immediate plain consequence or emotional reaction.
- Career/work scenes should be anchored to relationship, rivalry, status, public pressure, reward, or moral cost.

## Faction / Institution Map

For each significant organized power, track:

```text
What it wants:
What it fears:
What resources it controls:
What it owes:
What it hides:
Internal factions:
Public position:
Private position:
Current leverage over protagonist:
Current vulnerability:
```

Faction scenes should move leverage, reputation, obligation, alliance, or exposure. Avoid using institutions as static backdrops.

## Post-Arc Consequence Pass

After each arc or batch, record:
- Physical injuries or exhaustion.
- Tool/resource damage or depletion.
- Reputation/public opinion changes.
- Relationship shifts.
- New enemies or allies.
- Political/institutional response.
- Psychological residue.
- Unresolved evidence.
- New open questions.

Do not jump to the next arc as if the previous win had no cost.

## Reader Experience Audit

During batch audit, evaluate:

```text
Did this batch fulfill its genre promise?
Was there at least one meaningful emotional or tension peak?
Did a major character change, choose, fail, or pay?
Did the crisis feel different from the previous batch?
Was the core mechanism clearer or more interesting by the end?
Did relationships move?
Did the world/faction pressure shift?
Were consequences preserved?
Were hooks varied rather than repetitive?
```

## P0 / P1 / P2 Quality Gates

Use severity levels:

P0: must rewrite before continuing.
- Core mechanism is incoherent.
- Protagonist wins by unexplained convenience.
- Major character behavior contradicts established motivation without cause.
- Batch has no meaningful tension or change.
- Genre promise is violated.
- Important object, weapon, system, clue, or opportunity disappears without payoff, loss, transformation, or deliberate retirement.
- Required romance/intimacy/relationship promise is absent across the batch.
- Payoff rhythm is too thin for the declared webnovel/commercial reader contract.

P1: must repair before finalizing.
- Crisis pattern is repetitive.
- Action, mystery, romance, or faction module is required by genre but underdeveloped.
- Supporting character is reduced to a tool.
- Major win has no consequence.
- Important reveal lacks setup.
- Relationship shift is told but not dramatized.
- Major entrance lacks any memorable appearance, behavior, or side-view impression.
- Reward type repeats without escalation, cost, or new emotional/strategic consequence.
- Intimate or charged relationship scene does not change character behavior, trust, leverage, vulnerability, or future stakes.

P2: polish if time allows.
- Scene atmosphere is thin.
- Body language or sensory detail is generic.
- Dialogue is too on-the-nose.
- Hook type repeats.
- Minor continuity or emphasis issue.

## Final Reminder

Use the right tension for the right novel. The goal is not to maximize spectacle; it is to fulfill the reader contract with growth, pressure, consequence, and emotional movement that belong to the story being written.
