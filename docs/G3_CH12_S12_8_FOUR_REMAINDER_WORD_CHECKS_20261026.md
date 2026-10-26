# G3 Chapter 12 §12.8 — Four remaining Word-native checks (2026-10-26)

## Reproducible method
- Word master: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` read directly from Library copy.
- Extracted `word/document.xml` direct `w:body/w:p`, zero-based. Crucially preserved `w:br` line breaks, in particular **p7660**, a complete multi-line runnable excerpt stored in a single Word paragraph with style `Normal`.
- Replayed Word setup from p7591, 7593–7598, 7600–7603, 7605–7608, 7610, and executed *Word-extracted statements*, not reconstructed GitHub modules. Captured exact stdout and separately evaluated no-print `assert` contracts.
- Source-only reproducer: `verify_ch12_s128_20261026.py` in QA working space; detailed execution register `G3_CH12_S12_8_FOUR_REMAINDER_CHECKS_20261026.csv` (working artifacts). No existing 126 case checks were rerun.

| Check | Word paragraphs (zero-based) | Actual validation |
|---|---|---|
| Data/metadata/shape/nonnegative/finite asserts | 7636,7638,7640–7642,7644–7645 | PASS, all assertions pass, no printed output |
| dtype | 7652 | PASS: exact `float64` printed result vs p7654 |
| Non-square axis semantics | 7660 | PASS: exact `[100. 102. 100.]` and `[20.6667 16.     27.6667 36.3333]` vs prose expected p7661 |
| Transpose | 7752,7754 | PASS: actual 4x4 transposed matrix matches printed Word p7756–7759 |

**4/4 passed; three output-bearing cases matched Word (including a prose-stated result); one assertion-only case passed.** These four supply precise paragraph-level evidence beyond the earlier 12-case §12.8 audit. The previous 126 scoped chapter checks must not be arithmetically combined without overlap reconciliation.

## Status and next work
- The newly checked exact paragraphs may be reclassified from `REVIEW_POSSIBLE_CODE_*` to `WORD_NATIVE_EXPLICIT_VERIFIED`, but **do not** reclassify the entire 889 candidates or 324 broad-span references.
- Continue by identifying actual code-block boundaries among other unlinked §§12.1–12.9 candidates and reconciling audit CSV evidence. Candidate count is not executable-program count.
- Chapter 12 G3 remains IN PROGRESS; G4/G5/G6 HOLD. No Word/Python source modifications. No Chapter 6 or 10 calculation retests.
