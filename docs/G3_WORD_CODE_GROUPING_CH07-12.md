# G3 — Chapters 7–12 Contiguous Candidate Grouping (2026-10-25)

**Status: second-pass candidate grouping, NOT verified code blocks, NOT FROZEN.**

Second-pass candidate units (body paragraphs and table cells): **2,805**. Consecutive candidate positions within the same chapter and location were grouped into **1,090 groups**. Gaps or style boundaries may split real code; adjacent outputs/narrative may be mistakenly merged. Table position identifiers are not guaranteed equivalent to body paragraph indexes. Do not add these groups to the first-pass 2,072 blocks.

| Chapter | Code-fragment candidates | Ambiguous text/output groups | Total groups |
|---|---:|---:|---:|
| 7 | 1 | 1 | 2 |
| 8 | 12 | 0 | 12 |
| 9 | 23 | 1 | 24 |
| 10 | 241 | 37 | 278 |
| 11 | 55 | 1 | 56 |
| 12 | 582 | 136 | 718 |
| **Total** | **914** | **176** | **1,090** |

Code-fragment heuristic requires recognizable Python syntax in a grouped preview; it does NOT establish syntax completeness or standalone execution. All grouped rows remain `UNREVIEWED_NOT_PROVEN`; explicit `PSEUDOCODE` vs illustration/expected output still needs semantic classification. The local audit CSV `G3_Ch07-12_Contiguous_Candidate_Groups_20261025.csv` records ranges and short previews.

**Identified false positive:** Chapter 7 TOC/bullet paragraphs were previously classified as output/continuation. This demonstrates why candidate counts are not instructionally meaningful before review. Chapters 10 and 12 contain very large numbers of Normal-style fragments, requiring additional segmentation and source matching.

**Next actions:** (1) recover original full Word text by group ranges; (2) exclude headings, pure prose and expected output; (3) split/merge actual code structures; (4) label each as `EXECUTABLE_STANDALONE`, `EXPLANATORY_SNIPPET`, `PSEUDOCODE`, `COMMAND`, `OUTPUT`, or `NONCODE`; (5) map to repository files and test claims without converting intentional fragments to executable code. G3, G4, G5 and G6 remain open. Word and Python source unchanged.
