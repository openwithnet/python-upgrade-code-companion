# G3 Chapter 12 — Re-triage 113 provisional groups lacking 16-CSV index intersections (2026-10-27)

## Actual work
Source records: `G3_CH12_Provisional_Source_Block_and_QA_Trace_20261027.csv` (249 gap-based group IDs) and `G3_CH12_249_Blocks_Additional_10_CSV_QA_Intersections_20261027.csv`. Selected **113 groups** for which neither the original six nor subsequent ten detailed CSV inventories listed intersecting paragraph indices. Matched group **start positions** to previously published *scope ranges* in chapter audit documents and screened groups for dependent snippets. No existing numerical validation was rerun. Generated 113-row case/provenance triage `G3_CH12_113_Previously_Unlinked_Group_Provenance_Triage_20261027.csv`.

| Evidence triage for previously unlinked provisional groups | Groups |
|---|---:|
| In previously audited Word paragraph **range**, but no exact block proof from this match | 59 |
| Output or context-dependent expression, not independently runnable | 14 |
| Standalone-looking but dependent illustration, not an independent program | 4 |
| Whole runnable context and specific QA provenance unresolved | **36** |
| **Total** | **113** |

These are new **routing classifications**, not 59 new test successes, 18 dispensable programs or 36 confirmed failing or untested programs. The 59 have only *start index* within a previous reported audit range and may still need exact line/output verification. The 14/4 classifications are first-pass from group sample texts, and need contiguous-source confirmation.

## Unresolved 36 group distribution
- §12.1: 13
- §12.2: 6
- §12.3: 8
- §12.6: 9

§12.4, §12.7, §12.8, §12.9 have no groups left in this provisional **unresolved-context** tier, though full Word and GitHub one-to-one completeness is not thereby established.

### Caveat: heuristic block splitting
The original 249 groups were formed by code-like paragraph gaps and headings, and can split a true program across many source chunks. Therefore this is not a final count of whole executable blocks. In particular §12.1 has elementary NumPy arrays, `print` outputs and means split into distinct provisional entries; an unmatched group may already belong to a verified demonstration but be missing its exact crosswalk.

## What this improves
This audit identifies the specific source contexts to review manually instead of repeatedly rerunning passed cases. Next, build **complete source spans** for the 36 unresolved groups and examine adjacent setup/outputs and existing §12.1/§12.2/§12.3/§12.6 case logs. Then join 21 functions across the five GitHub Chapter 12 representative reference modules to explicit Word span(s), clearly tagging the functions as non-verbatim reconstructions.

No source code or Word manuscript edits. No Chapter 6/10 tests. G3 Chapter 12 **IN PROGRESS / FULL PASS HOLD**, G4/G5/G6 HOLD. User need not save this intermediate QA artifact.
