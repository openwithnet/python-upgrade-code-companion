# G3 Chapter 12 — Restore Exact QA CSV Evidence for §§12.4, 12.5, 12.9 (2026-10-26)

## Sources and method
Retrieved three preexisting detailed QA CSVs from the user's Library, rather than inferring success from summary prose:
1. `G3_Ch12_AdvancedIndex_ViewCopy_14_Examples_20261026.csv` (14 cases; `code_paragraphs`, `matched`)
2. `G3_Ch12_Strides_7_Executed_20261026.csv` (7 cases; `code_paragraphs`, `match`)
3. `G3_Ch12_12_9_Particle_Motion_12_Cases_20261026.csv` (12 cases; `word_paragraphs`, `passed`)

Each cited code paragraph or paragraph range was joined to the current 889-candidate register `G3_CH12_PostS128_Reconciled_889_Register_20261026.csv`. We changed only previous `PRIOR_BROAD_SPAN_ONLY` rows into `DETAIL_CSV_PARAGRAPH_WITHIN_PASSING_CASE` when a passing detailed case actually referenced that paragraph index or a containing range. Other statuses stay unchanged. The complete 889-row output with `restored_sources` trace is `G3_CH12_Three_Audit_CSV_Exact_Paragraph_Reconciliation_20261026.csv`.

## Results
| Section | Previous broad-span candidates | Linked to passing detailed case CSV | Still broad-only |
|---|---:|---:|---:|
| 12.4 | 71 | 31 | 40 |
| 12.5 | 68 | 56 | 12 |
| 12.9 | 90 | 75 | 15 |
| **Subtotal** | **229** | **162** | **67** |

Chapter-wide broad-only total: 324 -> **162**. The separate 213 candidate paragraphs awaiting code/fragment classification have **not** been reclassified.

**Interpretation:** the 162 is the number of *candidate paragraph positions linked to case records*, NOT the number of runnable programs, independently verified Word paragraphs, or new executions. In particular §12.9's `word_paragraphs` column sometimes lists a **continuous section range**, so the 75 positions mark *within an executed case's reported span*, not that every intervening paragraph was passed as Python code. §12.4 and §12.5 source CSVs often enumerate code positions more finely, but even these require output/comment separation when determining literal source identity.

Case outcomes are reused (no cases rerun), and code inputs/outputs are available in the original CSV files for further audit. The new crosswalk is a preservation of evidence provenance with appropriate limits.

## Next steps
1. Separate §12.9's 75 span positions into code, description, expected output and dependent setup using actual `word/document.xml` and detailed case text.
2. Retrieve additional existing detailed QA CSVs for §12.4 (remaining 40) and §12.5 (12) to recover further exact indices before running anything.
3. Resolve remaining 213 candidate paragraphs where no detailed evidence exists and close only when all executable blocks are classified, not when candidate counts hit zero.

No Word manuscript or Python source changes. Existing 126 checked cases not rerun; Chapter 6/10 calculations untouched. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
