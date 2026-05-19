# AI_NovelGenerator Design Notes

This skill adapts the useful architecture of `YILING0013/AI_NovelGenerator` while avoiding its main long-form weaknesses.

## Keep

- Multi-stage workflow:
  architecture -> chapter directory -> chapter draft -> finalize.
- Separate LLM roles:
  strong model for architecture/directory, drafting model for chapters, review model for audits.
- Chapter generation context:
  global summary, character state, previous chapter ending, chapter directory, next chapter hint, retrieved context.
- Finalization:
  update summary, character state, and retrieval memory after each chapter.
- Batch generation:
  generate several chapters sequentially, not one monolithic novel.

## Change

- Replace one short global summary with layered memory:
  rolling summary, arc summary, chapter facts, timeline, foreshadowing, continuity ledger.
- Make `directory.md` and `generation-plan.md` explicit human checkpoints.
- Add anchor chapters before bulk generation.
- Add mandatory chapter and batch audits.
- Use 5-10 chapter batches by default.
- Use structured ledgers instead of relying only on vector search.
- Treat vector retrieval as optional assist, not truth source.
- Keep chapter length realistic: 2500-4000 Chinese characters by default.

## Why

Long novels fail through slow drift:
- forgotten promises
- repeated scene shapes
- power/ability inconsistency
- timeline impossibilities
- characters knowing things they never learned
- over-compressed summaries

The fix is not just "more context"; it is separate, updateable memory surfaces and review checkpoints.

