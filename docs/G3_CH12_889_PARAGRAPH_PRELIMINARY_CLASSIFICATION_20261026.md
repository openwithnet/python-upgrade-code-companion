# G3 Chapter 12 — 889 Candidate Paragraphs Preliminary Triage (2026-10-26)

Source Word: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` (Library copy); direct XML `w:body/w:p`, 0-based, Chapter 12 p4451–8621. Candidate input `ch12_candidate_python_paragraphs.csv` (889 unique indices). Paragraph text and immediate neighbors were extracted from `word/document.xml`.

## Preliminary syntax/shape screen
- 505 assignment/array-definition-like paragraphs
- 299 print/import/control-statement-like paragraphs
- 38 dependent expression/call-like paragraphs
- 47 ambiguous, formula, output, or fragment-like paragraphs

These are **heuristic paragraph categories**, not independently runnable blocks or a complete manual classification. `ast.parse` on isolated individual paragraphs is an imperfect completeness test: multiline definitions can parse only when joined. Scientific formula typography can resemble a Python assignment.

## Section distribution
| Section | Candidate paragraph count |
|---|---:|
| 12.1 | 72 |
| 12.2 | 108 |
| 12.3 | 87 |
| 12.4 | 95 |
| 12.5 | 104 |
| 12.6 | 132 |
| 12.7 | 56 |
| 12.8 | 101 |
| 12.9 | 122 |
| 12.10 | 12 |
| **Total** | **889** |

Examples: p4505 `matrix = np.array([` is the beginning of a multi-paragraph statement continued at p4506–4508; p8588–8591 are formula-like prose, not standalone Python; p8498 and p8500 are dependent illustrations. This prevents false claims that 889 Python programs have been identified.

## Relation to 126 prior scoped checks
Previously recorded **126 scoped case checks**, not necessarily disjoint source blocks. No direct case-by-case automated joins to all 889 paragraph indices have been certified in this document. Those joins, along with explicit executable block start/end, code dependencies, and expected output classification, are the next verification stage.

No Python code, Word text, or existing tests were changed. No Chapter 6/10 retests. G3 Chapter 12 remains IN PROGRESS, G4/G5/G6 remain HOLD.
