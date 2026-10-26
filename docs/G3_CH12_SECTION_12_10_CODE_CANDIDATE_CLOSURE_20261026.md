# G3 Chapter 12 — §12.10 Candidate Classification Closure (2026-10-26)

## Source and method
Directly examined `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` Word XML `word/document.xml`, top-level `w:body/w:p` (zero-based). Section 12.10 is p8487–8621. The previously screened 889 candidate paragraphs contain **12 candidate positions** in this section; those candidate positions were reclassified with original XML and surrounding prose. The complete multi-paragraph assertion p8569–8574 was also examined, including the three non-candidate interior/closing paragraphs (p8570,8571,8574).

## Reclassification of 12 earlier candidate positions
| Paragraphs | Verified role | Standalone runnable manuscript program? |
|---|---|---|
| p8498, p8500 | Dependent illustrations (`x`, `data` undefined locally) | No |
| p8519 | Dependent Broadcasting illustration (`data`, `scales` undefined locally) | No |
| p8527, p8529 | Dependent selection illustrations (`values` undefined locally) | No |
| p8546 | Dependent memory-sharing call (`np`, `a`, `b` require context) | No |
| p8569, p8572, p8573 | Parts of **one** six-paragraph illustrative `np.testing.assert_allclose(actual,expected,rtol=1e-6,atol=1e-8)` call, p8569–8574; undefined `actual` and `expected` in this summary section | No |
| p8588, p8589, p8591 | Genuine `m:oMath` / OMML equation objects, **not Python**; text-only extraction can misrender them as programming-like assignments | No |

**All 12/12 §12.10 syntax candidates are classified; 0 new independent runnable Python programs identified.** Six dependent standalone expressions/calls + three candidate indices belonging to one dependent multi-paragraph contract snippet + three OMML equations. This is a **content classification**, not an execution PASS claim. The rendered Word's mathematical equations must remain OMML; do not attempt to convert them to Python.

The original 889 candidate count is preserved as an intentionally inclusive heuristic; these 12 are still counted as candidate positions in the historical CSV and should not be silently deleted or relabeled as 12 failed programs. With this narrower content audit, §12.10 requires no newly fabricated execution harness to reach a scoped content-classification conclusion.

No calculation tests rerun, no Word or Python source changes. Existing Chapter 12 126-case technical checks unchanged. Overall Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
