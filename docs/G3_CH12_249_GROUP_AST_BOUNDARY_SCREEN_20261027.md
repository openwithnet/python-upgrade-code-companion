# G3 Chapter 12 — 249 provisional-group AST boundary screen (2026-10-27)

Source of truth: unmodified Word v37 `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, direct OOXML body paragraphs. Existing gap-based `G3_CH12_Provisional_Source_Block_and_QA_Trace_20261027.csv` supplies the exact selected paragraph lists for **249 provisional groups**.

## Actual new static test

Re-extracted selected paragraph texts from Word, preserving `w:br`, `w:cr`, and `w:tab`; joined texts within each provisional group without inventing calculation statements, then ran `ast.parse` on each group **without executing code**.

| Structural disposition | Groups |
|---|---:|
| AST parse succeeds as an extracted syntax fragment | **108** |
| AST parse fails, requiring fuller source context/boundary review | **141** |
| **Total** | **249** |

Section-level results:
| Section | AST succeeds | Needs source context |
|---|---:|---:|
| 12.1 | 19 | 10 |
| 12.2 | 9 | 22 |
| 12.3 | 14 | 21 |
| 12.4 | 20 | 15 |
| 12.5 | 14 | 10 |
| 12.6 | 8 | 14 |
| 12.7 | 6 | 10 |
| 12.8 | 13 | 17 |
| 12.9 | 4 | 21 |
| Unassigned by prior section parser | 1 | 1 |

Per-group source indices, Python syntax error category, and prior case-evidence tier: `G3_CH12_249_Provisional_Group_AST_Standalone_Screen_20261027.csv`. Reproducer: `ch12_249_static_structure.py` in temporary QA workspace.

## Interpretation and decision

- **141 AST failures are NOT 141 manuscript syntax defects or failing programs.** Most provisional groups are deliberately broken fragments of a program because gap-based segmentation selected noncontiguous Word code lines and excluded continuation/setup lines. Their full parent source context must be reconstructed before any source-level validity judgement.
- **108 AST passes are NOT 108 runnable programs or computational QA PASS**. A syntactically valid expression may still depend on undefined names or represent an incomplete lesson snippet.
- Thus a stable canonical Chapter 12 executable-block inventory cannot be obtained by relabeling 249 heuristic groups.
- Correct next step is to reconstruct **semantic complete code contexts** from contiguous Word source definitions, include out-of-889 continuations, and link the complete source/execution logs; recover prior test evidence before any reruns. Keep five GitHub representative reference modules separate from literal manuscript source.
- This new screen provides a direct, reproducible reason for retaining **G3 FULL HOLD**, despite all previously recorded scoped numerical PASS findings.

No manuscript / OMML / executable GitHub code modifications. No old Chapter 6 or 10 QA rerun. Intermediate audit record: user need not save.
