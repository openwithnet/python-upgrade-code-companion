# G3 Chapter 12 — §§12.4–12.5 last ten REVIEW candidate positions (2026-10-26)

## Source and method
Direct Word v37 `word/document.xml`, direct `w:body/w:p` zero-based. Baseline `G3_CH12_889_After_Boolean_QA_and_S123_Shape_20261026.csv` (889 rows); examined four §12.4 and six §12.5 REVIEW positions, with surrounding setup and expected output. Word statements were assembled without changing calculations. Only genuinely missing precise tests were executed; prior Chapter 6/10 work unchanged.

## Five **block-level** execution results
| Block | Word paragraph source | Evidence | Result |
|---|---|---|---|
| 2D element Boolean mask | setup p5930–5935, code p5955–5960 | stdout equals Word p5962–5963, seven values and shape `(7,)` | PASS |
| `normalized` | function p6453–6456 | Reviewer contract: returned values [.25,.5,1.], original unchanged, no shared memory | PASS |
| `scale_measurements` | function p6664–6668 | Reviewer contract: scaled copy, original unchanged, no shared memory | PASS |
| `scale_measurements_inplace` | function p6672–6676 | Reviewer contract: original mutated, implicit `None` return | PASS |
| `np.shares_memory` real example | setup p6713–6717, calls p6719–6720 | exact stdout Word p6722–6723: `True`, `False` | PASS |

Case-level execution detail, original extracted-code SHA-256 and exact output text are in `G3_CH12_S124_S125_Last10_Word_Block_Contracts_20261026.csv`. The `normalized` and scaling function checks are **reviewer-supplied runtime assertions** against literal Word function sources, not tests printed verbatim by the book.

Word p6711 `np.shares_memory(a,b)` is a dependent illustrative expression with no binding for `b` in that line; the neighboring complete Word example is checked. Thus it is correctly role-classified but not itself a standalone runnable PASS.

## Register update
All ten original REVIEW positions receive evidence/role classifications; complete register `G3_CH12_889_After_S124_S125_Last10_Closure_20261026.csv` retains **889** candidate rows. REVIEW count **73 -> 63**: §12.4 0, §12.5 0, §12.6 18, §12.7 17, §12.8 4, §12.9 24. These are *paragraph positions*, not 63 independent programs.

No Word manuscript or GitHub Python source edits. Existing Chapter 12 scoped-case evidence retained, no arithmetic double-counting. G3 Chapter 12 IN PROGRESS, G4/G5/G6 HOLD.
