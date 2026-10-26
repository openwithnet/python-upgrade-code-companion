# G3 Chapter 12 — Integrate §§12.2–12.3 Word block and historical QA evidence (2026-10-26)

## Inputs
Word v37 original-paragraph register (889 positions); prior 113-paragraph §§12.2–12.3 case crosswalk; six Word-native exact-output executed blocks (existing commit `11481870`); §12.3 broadcasting mismatch error/repair contract (existing commit `f10d3ac9`). **No calculations rerun.**

## Evidence changes
**41** previously unclassified candidate positions receive roles from the latest actual Word source review: 32 positions in **six** tested blocks (not 32 programs), 5 positions in an expected `ValueError` / fixed broadcast contract (not five new tests), 2 explanatory prose, 1 dependent `keepdims` no-standalone one-line comparison p5090, and 1 dependent `a * b + c` temporary-array teaching expression p5774.

A further **70** previously unclassified positions are assigned using historical detailed QA crosswalk: 62 directly linked to preexisting QA case indices and 8 non-executable axis labels/prose. Existing category assignments and already-documented successful case counts are not overwritten or double-counted. The 14 non-executable roles originally documented in the 113-paragraph file include 8 that were still unclassified at this integration pass; the others had been classified in earlier evidence.

Net **111 of original 213 REVIEW candidate positions** are now role/evidence-classified; **102 still REVIEW**. All **889 original candidate positions retained**.

## Residual candidate distribution
| Section | Still REVIEW |
|---|---:|
| 12.1 | 2 |
| 12.2 | 0 |
| 12.3 | 2 |
| 12.4 | 24 |
| 12.5 | 6 |
| 12.6 | 19 |
| 12.7 | 17 |
| 12.8 | 8 |
| 12.9 | 24 |
| **Total** | **102** |

The only two §12.3 still in REVIEW are p5673 `print(a.shape)` and p5674 `print(b.shape)` in the same already-tested shape mismatch illustration. They were not themselves recorded as part of the narrowly scoped expected-error and corrected-axis checks, and are **not** silently marked literal-output PASS.

The p5090 `row_mean = np.mean(a, axis=1)` follows Word p5072–5084 keepdims-centering and contrasts shape `(3,)` with `(3,4)`; it is a dependent comparison, not a self-contained program. Existing keepdims checks were not repeated. The p5774 temporary-array expression is also dependent illustrative syntax with undefined local a,b,c in its immediate passage.

## Files
- `G3_CH12_889_After_S122_S123_Evidence_Integration_20261026.csv`: complete 889-row updated evidence register.
- `G3_CH12_Recent_Exact_Block_Paragraph_Promotions_20261026.csv`: 41 source-block/role changes.
- `G3_CH12_Existing_QA_and_Nonexec_Paragraph_Promotions_20261026.csv`: 70 historical QA/role changes.

## Gates
No production Word or Python source edits. No Chapter 6/10 calculations. Chapter 12 **G3 IN PROGRESS**, G4/G5/G6 HOLD. Next: verify §12.3 p5673/p5674 original expected displayed results, and prioritize 102 REVIEW candidates in §§12.4–12.9, especially those with no prior specific source evidence.
