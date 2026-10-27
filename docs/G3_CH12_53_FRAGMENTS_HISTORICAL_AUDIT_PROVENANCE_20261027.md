# Chapter 12 G3 — Historical QA provenance for 53 fragments

Date: 2026-10-27. Reviewed all 53 fragments lacking direct indexed CSV intersection in the latest 58-fragment queue, against existing Chapter 12 audit documents. No numerical tests were repeated; Word and Python sources unchanged.

Evidence category counts (fragment groups, **not programs or new test passes**):

| Existing evidence kind | Fragment groups |
|---|---:|
| Reconstructed expression-matrix cases, §12.8 | 12 |
| Selected literal Word reduction statements, §12.7 | 9 |
| Reconstructed checks for multiple initial states, where/vectorize and float | 7 |
| Exact Word relative_by_sample function and tests | 7 |
| Scoped literal calculation contexts, §12.9 | 5 |
| Reconstructed Euler solver checks | 4 |
| Word metadata cases | 3 |
| Word broadcasting mismatch and correction | 2 |
| Literal analytical position function | 2 |
| Literal physical identity contract | 2 |
| **Total** | **53** |

Detailed one-to-one fragment-to-document mapping: G3_CH12_53_Fragment_Historical_Audit_Provenance_20261027.csv (intermediate QA workspace).

Specific existing source audits include G3_CH12_12_6_3_12_7_NINE_NUMERIC_CASES.md, G3_CH12_12_7_3_REDUCTION_7_CASES.md, G3_CH12_12_8_INTEGRATED_EXPRESSION_12_CASES.md, G3_CH12_S12_8_RELATIVE_BY_SAMPLE_WORD_CONTRACTS_20261026.md, G3_CH12_12_9_PARTICLE_MOTION_12_CASES.md, G3_CH12_S129_EXACT_WORD_POSITION_FUNCTION_EXECUTION_20261026.md, and G3_CH12_LAST28_FOUR_WORD_CONTEXTS_CANDIDATE_ROLE_ZERO_20261026.md.

**Disposition:** all 53 have a historical audit provenance route, but none receives *whole Word program PASS* solely on basis of source-range/topic overlap. Previously existing literal checks remain valid in their exact scope. Five additional fragments in the 58-item queue had direct source-index CSV intersections in the previous audit; also not automatically whole-block PASS.

G3 FULL HOLD: stable exhaustive executable block manifest and complete source/input/output/QA chain still needed. G4/G5/G6 HOLD. No user action to save intermediate files.