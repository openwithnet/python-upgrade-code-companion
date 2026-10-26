# G3 — Chapters 1, 6, 12 Evidence Consolidation and Acceptance Gaps (2026-10-26)

**Result: evidence reconciled; no unconditional full-chapter G3 PASS awarded.** This consolidates already performed audits; it is not a new run of all Word examples.

| Chapter | Confirmed existing evidence | Remaining acceptance work |
|---|---|---|
| 1 | All **15** section files inventoried and source-comment paragraph anchors revised against current Word. §1.5.3's printed `True` was separated from executable code. | Verify content, dependencies and expected output of each section file against the exact Word blocks; a corrected anchor does not prove whole-file equivalence. |
| 6 | Word §6.5.2 program extracted at p898–907; repository `p1_particle_trajectory.py` matched after stripping three metadata header lines and normalizing a terminal newline. Recorded output and numerical trajectory align. | Determine whether other code throughout Chapter 6 requires independent mapping; this exact match covers **§6.5.2 only**, not the entire chapter. |
| 12 | **126 previously executed scoped checks** across §§12.1–12.9; five related reconstructed source modules mapped; §12.10 code expressions classified as dependent illustrations. | Establish the full Word executable-group denominator and function-by-function API/data/expected-output trace; 126 case checks are not 126 fully extracted scripts. |

## Sources reviewed
- `docs/G3_CH01_15_FILE_CONSOLIDATED_CHECKPOINT.md`
- `docs/G3_CH01_VERIFIED_REANCHOR_25.md`
- `docs/G3_CH06_EXACT_CODE_COMPARISON.md`
- `docs/G3_CH12_FIVE_SOURCE_CONSOLIDATED_MAPPING.md`
- `docs/G3_CH12_SECTION_12_1_11_EXECUTED_EXAMPLES.md`
- `docs/G3_CH12_12_9_PARTICLE_MOTION_12_CASES.md`

Local evidence matrix: `G3_CH01_CH06_CH12_Gate_Evidence_20261026.csv`.

## Prioritized next tasks
1. **Ch6 first:** directly inventory Word's other chapter-level code outside §6.5.2; the existing exact-match scope is already narrow and well-established.
2. **Ch1 second:** compare all 15 source files' in-code paragraph anchors and expected output to the current master Word; avoid re-testing before finding actual uncovered cases.
3. **Ch12 third:** reconcile the 126 executed cases with coherent Word example groups and five reconstructed modules, recording no-promise semantic mapping rather than verbatim claims.

**G3 CH1 / CH6 / CH12 = scoped evidence accepted, full-chapter HOLD.** Book-wide G3 and G4/G5/G6 continue HOLD. The latest recorded CI success and Chapter 10 scoped closure remain unaffected. No Word manuscript or executable GitHub source edited.