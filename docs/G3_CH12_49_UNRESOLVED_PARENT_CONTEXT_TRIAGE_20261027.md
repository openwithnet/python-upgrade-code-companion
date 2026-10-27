# Chapter 12 G3 — 49 unresolved provisional fragment parent-context triage (2026-10-27)

Authoritative source: original Word v37 OOXML. This audit processes exactly 49 groups remaining after the 141-group boundary recovery screen. It is a structural triage, NOT execution QA.

## Findings

- **26/49** provisional fragments overlap an already identified enclosing Word source/test context: `apply_experiment_scales` tests, `scale_in_chunks`, Euler decay solver, expression analysis, `relative_by_sample` and its Word-authored tests, analytic/motion loops, or Euler particle-motion solver. Previous PASS evidence retains its earlier limited scope; linking a fragment to its parent is not a fresh full-block PASS.
- **23/49** require precise parent boundaries or role filtering before source-level closure. Many are introductory calculations and other examples separated by prose/output.
- Classification of observed syntactic fragmentation causes: **27** intervals have prose/non-code cue text among selected Word paragraphs; **13** represent indented continuation without its enclosing definition; **9** require a longer expression or setup context. These categories are heuristic routing notes, not manuscript algorithm failures.

The 49-row trace `G3_CH12_49_Parent_Function_Context_Triage_20261027.csv` records exact paragraph ranges, existing parent links, nearby function headers, and a status that explicitly denies whole-block runtime PASS. Original 141-row and 249-row registers remain intact.

## Next narrow task

Review 23 missing-parent contexts by exact Word source and output, reconciling with previously executed 22 selected contexts and older QA reports before any new test. For 26 parent-attached fragments, check code-role purity, and for the 26 AST-restored but lexically ambiguous groups use Python AST node line ranges to separate valid nested arrays from printed output. Only then consolidate a stable chapter-wide program/block index; five GitHub modules remain representative references.

No numerical tests rerun; Word and executable GitHub source unchanged. Chapter 12 G3 FULL HOLD / IN PROGRESS; G4/G5/G6 HOLD. Intermediate audit record; no user saving required.