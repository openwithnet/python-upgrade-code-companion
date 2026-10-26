# G3 Chapter 12 §12.9 — 75 Candidate Positions in Passing-Case Ranges (2026-10-26)

## Inputs
- Word-derived current register `G3_CH12_Three_Audit_CSV_Exact_Paragraph_Reconciliation_20261026.csv`.
- Retrieved **original QA CSV** `G3_Ch12_12_9_Particle_Motion_12_Cases_20261026.csv` from the user's Library.
- The 12 original scoped check results were **not** re-executed.
- The 75 Word paragraph candidate indices tagged as within existing passing-case **ranges** were each linked to the actual CSV `case` labels and inspected for whether the candidate text was a code statement or a continuation fragment.
- Working trace: `G3_CH12_S12_9_75_Paragraph_Within_Case_Range_Classification_20261026.csv`.

## Verified crosswalk
All **75 of 75** candidate indices occur within at least one *reported passing-case paragraph range* in the previous QA CSV. Examples include p8026–8034 (time grid), p8044–8052 (velocity), p8054–8062 (closed-form position), p8107–8169 (loop/vectorization), p8184–8257 (Euler solver), p8277–8303 (step-refinement), and p8311–8328 (multi-initial-condition calculation).

**This is NOT a 75/75 line-by-line execution PASS.** The original CSV identifies ranges of setup, complete function definitions, arguments and printed outputs; it does not list individually executed Word statement indices. The 75 are code-form candidate positions rather than descriptions/output-only positions in this particular screening. Several are continuation/argument lines rather than standalone Python statements. Each one is now traceable to case labels while retaining status `WITHIN_PASSING_CASE_REPORTED_RANGE_NOT_LINE_EXECUTION_PROOF`.

## Outstanding evidence
In §12.4 and §12.5, **40 + 12 = 52** positions remain `PRIOR_BROAD_SPAN_ONLY`. Existing detailed 14-case advanced-index / view-copy and seven-case stride CSVs were already incorporated in the prior 162-position crosswalk. No further individual paragraph proof for these 52 positions has been recovered from those same three CSVs; the next step is to inspect the other QA records (especially Boolean/error and memory-integrity) or classify the actual Word syntax and neighboring expected output without inferring that whole ranges were run.

The 213 unclassified positions elsewhere in Chapter 12 are still not resolved by this audit.

No Word or Python source changes; no Chapter 6/10 calculations repeated. Chapter 12 G3 remains IN PROGRESS, G4/G5/G6 HOLD.
