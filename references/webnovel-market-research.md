# Webnovel Market Research

Use this reference during project setup, topic selection, market positioning, style discovery, and architecture. Its purpose is to dynamically supplement the baseline industry knowledge in `webnovel-market-positioning.md` with current public information from novel platforms, official sites, rankings, book pages, reviews, author notes, genre tags, and other open web sources.

Do not treat this as copying. Research is for understanding market signals, reader contracts, trope patterns, pacing expectations, title/tag conventions, and comparable positioning. The resulting novel must remain original.

## When To Run

Run dynamic market research when:
- the user asks for a commercial webnovel, genre fiction, serial fiction, male-channel, female-channel, platform-facing, or "popular" project
- the user has only a vague topic and needs help choosing a direction
- the project depends on current platform taste, rankings, tags, or reader expectations
- the user asks for comparable works, benchmark works, platform fit, writing style references, or industry best practices
- style discovery needs market-facing examples rather than only abstract prose preferences

Before browsing, read `webnovel-market-positioning.md` to form baseline questions. Browsing should update, challenge, or specialize those assumptions; it should not replace positioning judgment.

Skip or shorten when:
- the user explicitly wants an experimental, private, literary, or non-market-facing draft
- the user has already supplied a complete positioning brief and comparable list
- browsing or web access is unavailable; in that case, use stable genre knowledge and clearly label it as inferred, not verified

## Source Priority

Prefer public and official or semi-official sources:
- platform official rankings, category pages, tag pages, recommendation pages, book detail pages, author pages, and platform editorial pages
- official publisher/book pages
- public review and catalog pages such as Douban, Goodreads, Bangumi-like catalogs, library/catalog records, or major review sites
- public social discussion only as weak signal; do not let noisy comments override platform/category evidence
- user-provided examples, screenshots, title lists, notes, or links

Chinese webnovel sources may include, when accessible and relevant:
- Qidian / Qidian International / WebNovel
- Jinjiang
- Zongheng
- 17K
- Hongxiu
- Xiaoxiang
- Faloo
- Tomato Novel
- Qimao
- Ciwei Maoyuedu
- platform category charts and official recommendation lists

Use the sources that fit the target audience. Do not force Chinese platform logic onto English genre fiction, and do not force male-channel/female-channel assumptions onto a project that is intentionally cross-channel or non-commercial.

## Copyright And Safety Rules

- Do not reproduce paid chapters, long excerpts, locked content, or distinctive prose.
- Do not scrape behind logins, paywalls, app-only restrictions, or anti-bot barriers.
- Do not paste large chunks from public pages into project files.
- Record short source notes, URLs, dates checked, and your own paraphrased findings.
- Use comparable works to infer expectations, not to imitate living authors or copy plots.
- If a source is current and may change, record the access date.
- Distinguish observed market signal from inference.

## Research Packet

Before architecture, create or update `research/market-research.md` and summarize:

```markdown
# Market Research

## Research Date

## User Seed

## Target Channel / Audience
- Male-channel / female-channel / cross-channel / literary / other:
- Target platform style:
- Target reader:

## Sources Checked
| Source | URL / locator | Date checked | What it was used for | Reliability |
|---|---|---|---|---|

## Comparable Matrix
| Comparable | Platform/category | Why relevant | Reader promise | Hook pattern | Pacing | Character design | Relationship pattern | Long-serial engine | Do not copy |
|---|---|---|---|---|---|---|---|---|---|

## Market Signals
- Popular tags / categories:
- Common premise engines:
- Common protagonist types:
- Common relationship structures:
- Common opening hooks:
- Chapter rhythm / update rhythm:
- Title and blurb conventions:
- Reader anxieties:
- Reader rewards:
- Saturated patterns:
- Differentiation opportunities:

## Positioning Recommendation
- One-line commercial hook:
- Primary reader promise:
- Secondary reader promise:
- Best-fit platform/channel:
- Core trope engine:
- Differentiation:
- Risk:
- Avoid:
```

## Male-Channel Baseline Questions

Use these only as common industry defaults. Do not force them onto every male-channel project.

```markdown
## Male-Channel Positioning
- What is the protagonist's starting disadvantage?
- What creates the first visible reversal or "turning over" moment?
- What is the long climb: power, wealth, status, territory, knowledge, revenge, freedom, recognition, or order-building?
- What is the story engine: system, rebirth, transmigration, cheat ability, profession, business, cultivation, game, officialdom, military, investigation, survival, or faction expansion?
- What is the recurring reward loop: win, reveal, upgrade, resource, face-slap, rescue, territory, rank, secret, ally, romance, or freedom?
- How often does the reader get a concrete payoff?
- What prevents victory from feeling too easy?
- What consequences remain after wins?
- Single heroine, no heroine, multi-heroine, or relationship-light?
- If multi-heroine, what agency, desire, boundary, and arc does each heroine have beyond rewarding the protagonist?
- What does the protagonist team provide: expertise, emotional contrast, comic relief, moral friction, resource access, intelligence, combat, logistics, or institutional legitimacy?
```

Common male-channel modules:
- comeback / underdog reversal
- rise to the top
- face-slapping with setup and public witness
- upgrade loop with visible cost and limit
- resource acquisition and scarcity
- territory, sect, company, kingdom, family, or team expansion
- enemy ladder from local pressure to larger order
- protagonist team with differentiated functions
- multi-heroine or relationship-light design, handled with agency and consequence

## Female-Channel Baseline Questions

Use these only as common industry defaults. Female-channel fiction is not only romance; it often centers relationship pressure, identity, social field, emotional stakes, and personal choice.

```markdown
## Female-Channel Positioning
- What is the protagonist's initial social, emotional, family, career, status, or survival pressure?
- What identity or role is being constrained, misread, replaced, reborn, hidden, or reclaimed?
- What is the central relationship engine: romance, marriage, family, rivals, sisters, workplace, court, entertainment industry, school, clan, or found family?
- What does the protagonist actively choose, refuse, or protect?
- What is the emotional reward: being seen, safety, dignity, revenge, autonomy, competence, intimacy, recognition, or home?
- What is the primary tension: misunderstanding, unequal power, duty versus desire, public reputation, family debt, secret identity, career pressure, trauma recovery, or moral line?
- How do relationship states change across arcs?
- What makes the love interest, rival, family member, or ally an agent rather than a function?
- What are the sweet, painful, satisfying, and empowering moments?
- What keeps the protagonist's growth from being solved only by romance?
```

Common female-channel modules:
- identity reversal, rebirth, transmigration, contract relationship, marriage-first-love-later
- emotional pursuit and restraint
- family, workplace, court, entertainment, campus, or social-field pressure
- dignity recovery and self-determination
- relationship state movement: distrust, bargain, alliance, intimacy, rupture, repair
- satisfying revenge or public correction
- competence display under social constraint
- ensemble emotional network, not only couple scenes

## Topic Selection Card

Use this before writing architecture:

```markdown
# Topic Selection Card

## Seed

## Channel And Platform Fit
- Channel:
- Platform style:
- Target reader:

## Reader Contract
- Core pleasure:
- Core anxiety:
- First promise:
- Long promise:

## Commercial Hook
- One-line hook:
- Title direction:
- Blurb direction:
- First-three-chapter hook:

## Trope Engine
- Main trope:
- Support tropes:
- Expected payoff rhythm:
- Differentiation:
- Saturation risk:

## Character Design Direction
- Protagonist starting pressure:
- Protagonist long arc:
- Key supporting roles:
- Relationship model:
- Antagonist/opposition ladder:

## Serial Engine
- What can generate 100+ chapters?
- What escalates by volume?
- What stays emotionally unfinished?
- What recurring reader reward can repeat without going stale?
```

## Planning Integration

The research packet should feed:
- `plan/market-positioning.md`: channel, audience, hook, trope engine, platform fit, differentiation
- `plan/architecture.md`: premise, promise, dramatic question, arc shape
- `bible/character-bible.md`: protagonist type, support roles, antagonist ladder, relationship structures
- `bible/style-bible.md`: pacing, narration distance, hook density, dialogue directness, exposition tolerance
- `plan/directory.md`: first-three-chapter hook, payoff rhythm, arc escalation, volume turns

During planning, do not simply list market tropes. Convert them into story-specific choices with costs, constraints, and consequences.

## Research Output Standard

A useful research result should answer:
- What do readers in this lane come for?
- What are they tired of?
- What must appear early?
- What can be delayed?
- What should the protagonist want, lack, and repeatedly prove?
- What relationship or team structure best fits the channel?
- What is the long-serial engine?
- What is the project's non-copycat difference?

If the research cannot answer these, gather more sources or narrow the target lane.
