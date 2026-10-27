# G3 Chapter 12 — Full dependency-context proposal 249 → 124 (2026-10-27)

Canonical source: unmodified Word v37 (OOXML). This is a **proposed educational source-context register**, not a final independent runnable program inventory, and no runtime calculations were repeated.

All 249 original provisional code groups occur **exactly once** in the full 124-context master crosswalk `G3_CH12_249_To_124_Proposed_Educational_Contexts_Master_20261027.csv`, checked by set equality and uniqueness against the original inventory.

| Section | Provisional groups | Proposed contexts |
|---|---:|---:|
| 12.1 | 29 | 13 |
| 12.2 | 31 | 14 |
| 12.3 | 35 | 16 |
| 12.4 | 36 (35 plus one unclassified) | 16 |
| 12.5 | 24 | 21 |
| 12.6 | 23 (22 plus one unclassified) | 15 |
| 12.7 | 16 | 10 |
| 12.8 | 30 | 9 |
| 12.9 | 25 | 10 |
| **Total** | **249** | **124** |

The two previously section-unknown fragments were identified in Word and mapped without creating additional instructional contexts: p6071 `a[np.ix_([0, 2], [1, 3])]` belongs to §12.4 existing context S124-08; p7087–7111 is a continuation of §12.6 `simulate_euler` function and belongs to S126-10. Original local 12.4 and 12.6 registers remain unchanged, while the consolidated master explicitly corrects their coverage.

§12.8 context roles: expression matrix and metadata setup; reductions; A/B comparison; transpose; per-sample normalization and wrong-axis contrast; log transform explicit loops vs NumPy; `relative_by_sample` implementation; correctness tests; zero-total pytest rejection. Source: 30→9.

§12.9 context roles: analytic kinematics setup; analytic helper; loop/vectorized definitions; equivalence test; Euler solver; timestep sensitivity; multi-initial-velocity broadcasting; timing benchmark; temporary array tradeoff; physical invariant test. Source: 25→10.

**Gate limitations:** inclusive Word paragraph bounds may include explanatory prose and printed expected values; source-group membership and AST checks do not certify literal whole-script execution. A subset of historical QA is scope-passed, but it is not transitive to all 124 contexts. Next audit must produce exact executable statement inventories per proposed context, classify dependently runnable snippets, reconcile case output and provenance, and compare five representative GitHub reference modules without presenting them as all-Word transcription. Chapter 12 G3 FULL HOLD / IN PROGRESS; G4/G5/G6 HOLD. No manuscript or production-code changes. Intermediate artifact, no user archiving required.