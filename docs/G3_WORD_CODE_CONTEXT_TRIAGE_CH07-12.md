# G3 — Ch07–12 Candidate Context Triage (2026-10-25)

**Status: HEURISTIC TRIAGE ONLY / NOT VERIFIED / G3 HOLD.** No assertion of independent executability or complete Word source alignment.

From the 1,090 contiguous candidate groups (2,805 paragraph/table-cell units), a conservative second review of group previews found:

| Provisional class | Groups |
|---|---:|
| Python-syntax fragment candidates | 657 |
| Needs original context (possibly explanatory prose, continuation, output) | 406 |
| Output or mathematical-notation candidates | 26 |
| Confirmed noncode: Chapter 7 TOC | 1 |
| **Total** | **1,090** |

Chapter-specific breakdown:

| Chapter | Python fragment | Context review | Output/math | Confirmed noncode | Total |
|---|---:|---:|---:|---:|---:|
| 7 | 1 | 0 | 0 | 1 | 2 |
| 8 | 12 | 0 | 0 | 0 | 12 |
| 9 | 22 | 1 | 1 | 0 | 24 |
| 10 | 221 | 51 | 6 | 0 | 278 |
| 11 | 55 | 0 | 1 | 0 | 56 |
| 12 | 346 | 354 | 18 | 0 | 718 |

**Method:** Preview syntax heuristics (imports, definitions, assignments, control statements etc.) are used only to prioritize review; full original paragraph content and table relationships have **not** been adjudicated for all 1,090 groups. Accordingly, `PYTHON_FRAGMENT_CANDIDATE` does not equal runnable Python or a valid complete block. `NEEDS_CONTEXT_REVIEW` groups must not be discarded. No group was established as complete pseudocode from the preview alone; **zero classified pseudocode is not evidence of no pseudocode**.

Local audit CSV: `G3_Ch07-12_ContextTriage_20261025.csv` (not uploaded here). Each row retains prior IDs/ranges and adds `review_class`, `review_reason`, `execution_status=NOT_TESTED_NOT_PROVEN` and `source_mapping=UNMAPPED`.

**Next verification gate:** inspect full text for the 406 ambiguous groups and boundaries around 657 syntax fragments, reconstruct genuine multi-line examples, record pedagogical status (standalone, snippet, pseudocode, command, output, noncode), and only then map to the GitHub 81-file inventory. Do not mark G3/G4/G5/G6 PASS from pattern counts. Word and Python files were not changed.
