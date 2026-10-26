# G3 Chapter 10 — Fifteen dependent-code units: evidence reconciliation

2026-10-26. Inspected all 15 rows previously tagged `DEPENDENT_EDUCATIONAL_CODE_REVIEW` in the Word-derived 50-declaration-unit register.

## Previously recorded evidence (not fresh tests)

| Scope of evidence | Units |
|---|---:|
| Prior scoped Word behavioral PASS | 9 |
| Prior Word test PASS (including educational test doubles) | 5 |
| Semantic/API correspondence only, no direct Word-block run established | 1 |
| Total | 15 |

The single semantic-only item is Word §10.4.2 `DerivativeModel / StepSolver / Simulation`, paragraphs 2799–2835. Its related repository composition API was examined, but the existing register does **not** establish direct execution of the complete literal Word block. Target this one unit for contextual extraction/execution before using any full-run label.

The other 14 items have a *scoped* prior PASS; none should be automatically described as a fully self-contained, independently runnable Word program. They require referenced imports, definitions and inputs to be attached when presented as running examples. Existing tests should not be rerun merely for repetition.

The 15-row detailed register is `G3_CH10_15_Dependent_Unit_Evidence_And_Gaps_20261026.csv`. This pass performed no new source execution, introduced no new passing test counts, and changed neither Word master nor calculation source. Chapter 10 final unconditional G3 remains HOLD.