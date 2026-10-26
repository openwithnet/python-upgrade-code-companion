# G3 Chapter 12 §12.8 — Word v37 relative_by_sample contract verification (2026-10-26)

## Scope / literal source
- Word master: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`.
- Extracted from direct `word/document.xml` body paragraphs (zero-based) using `zipfile` and `lxml`.
- Function `relative_by_sample(values)` reconstructed solely from Word code paragraphs p7892–7936, excluding interleaved explanatory text, with indentation and printed docstring preserved.
- Word test definitions: `test_relative_by_sample` p7943–7964 and `test_zero_total_is_invalid` p7969–7976.
- Added `import numpy as np` and `pytest` to isolated execution context. Executed the two Word-authored test functions, followed by eight reviewer-generated behavioral probes.
- Extracted program UTF-8 SHA-256: `87c11c67bac8416c80b5a8ef11b70eba2dbbb0967b2914f6ad6c8fb21f293389`.

## Results
| Behavior | Outcome |
|---|---|
| Word test: values -> [[25,75],[50,50]], each row sums 100 | PASS |
| Word test: zero-total input must raise ValueError | PASS |
| Invalid 1-D input | PASS (ValueError) |
| Invalid 3-D input | PASS (ValueError) |
| NaN input | PASS (ValueError) |
| Infinite input | PASS (ValueError) |
| Negative measurement | PASS (ValueError) |
| Zero-sum row | PASS (ValueError) |
| Row-wise normalization on valid unequal row values | PASS |
| Huge finite inputs: overflow when summing row | PASS (NumPy RuntimeWarning, then ValueError due to nonfinite totals) |

**10/10 case assertions PASS (two printed Word tests; eight reviewer-added probes).** This confirms the literal Word-extracted function/test behavior under the current Python/NumPy environment. It does NOT add ten new independent manuscript examples to prior 126 case checks; reconciliation is still required. The checks verify an educational row-percentage transformation, **not** scientifically accepted RNA-seq normalization.

Existing §12.8 12-case audit covered matrix statistics, row normalization and log transformation but did not separately give paragraph-level test execution for these function definitions. Previous §12.8 twelve cases and prior Chapter 10/6 audits were not rerun.

No source or Word edits made. Chapter 12 G3 remains IN PROGRESS, G4/G5/G6 HOLD.
