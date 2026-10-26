# G3 Chapter 12 — XML-Aware Refinement of 889 Candidate Paragraphs (2026-10-26)

## Sources
- Word v37: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`; `word/document.xml` direct `w:body/w:p`, zero-based indices.
- Existing `G3_CH12_889_Evidence_Paragraph_Crosswalk_20261026.csv` and G3 §12.1 six-case / targeted five-case records; no re-execution of previous 126 cases.
- A reproducible tabular snapshot was produced: `G3_CH12_889_Refined_Evidence_and_XML_Roles_20261026.csv`.

## Improved evidence classifications
| Classification | Candidate paragraph count | Meaning |
|---|---:|---|
| PRIOR_EXACT_REFERENCE | 201 | Specific index already named in earlier scoped G3 evidence |
| PRIOR_BROAD_SPAN_ONLY | 324 | Inside wide logged audit range; not verified individually |
| NEW_EXPLICIT_CHECK_REFERENCE | 52 | Individual paragraph index appears in *recently* documented additional six/five-case check locations; NOT 52 new tests |
| OMML_MATH | 53 | Actual Word math object among previously unreferenced candidates, not Python |
| REVIEW_POSSIBLE_CODE_STATEMENT | 217 | Previously unreferenced Python-like statement requiring contiguous-block review |
| REVIEW_POSSIBLE_CODE_CONTROL | 39 | Previously unreferenced def/loop/conditional-like paragraph requiring contiguous-block review |
| REVIEW_OTHER_OR_FRAGMENT | 3 | Remaining ambiguous text fragments |
| **Total** | **889** | Paragraph candidates, NOT programs |

Another 13 OMML-bearing candidate paragraphs reside in previously cited broad/exact audit categories; in total 66/889 have an OMML element. The 53 figure represents the newly separable, otherwise unreferenced OMML class, not the total OMML count.

## Concrete remaining queue (examples)
- §12.2 p4963–4964: reduction output expressions require earlier array context; no independent source block.
- §12.2 p5072–5080: a multi-paragraph mean/centering excerpt using `keepdims=True`. Must reconstruct complete arguments and capture print.
- §12.2 p5098–5109: multi-axis mean and result shape, with multiline array creation and dependency.
- §12.2 p5121 onward: `std`/sample `ddof` passages; ensure that Word printed results and library version assumptions are not confused.

## Status
This is **better inventory classification**, NOT newly executed tests or verified run results. The 259 remaining unreferenced non-OMML paragraph candidates are *review work items*, and many are narrative mentions, fragments, dependencies or outputs. The 324 broad-audit cases do not become full exact checks by proximity alone. Previous 126 scoped checks and later targeted checks remain untouched. G3 Chapter 12 IN PROGRESS; G4/G5/G6 HOLD. No Python or Word source modifications.
