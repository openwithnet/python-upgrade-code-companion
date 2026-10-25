# G3 — Word Code Boundary Verification Samples (Ch10 and Ch12, 2026-10-25)

**State: two confirmed examples, 1,088 other candidate groups NOT PROVEN.** Source: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`. Positions are zero-based python-docx paragraph indices.

| Chapter | Word paragraph span | Classification | Result |
|---|---|---|---|
| 10 | 1444–1460 (excluding blank paragraphs) | One independent executable educational snippet | Calibration (signals 1,3,9, slope 2, intercept 1) prints `[0.0, 1.0, 4.0]` |
| 10 | 1461–1462 | Output label and expected output, NOT executable source | Matches print output |
| 12 | 4493 | Mathematical notation, not a source code block | `x=3` notation |
| 12 | 4499–4508 (excluding blanks) | One NumPy array-initialization block | Defines `scalar`, `vector`, `matrix` |
| 12 | 4510–4512 | Dependent executable print snippet | Prints `0`, `1`, `2` after initialization |
| 12 | 4513–4516 | Output label and three expected-output lines | Matches ndim computation |

**Execution evidence:** Both reconstructed examples were evaluated in the working Python environment; their outputs matched Word. The previous automatic grouping incorrectly split complete programs at empty paragraphs and misclassified numeric outputs/math as code fragments. This is why a group count is not a count of runnable examples.

**Source mapping:** The Chapter 10 calibration arithmetic is conceptually comparable to C3 examples elsewhere; no exact byte-level repository file identity established. Chapter 12 NumPy example has no verified GitHub matching path yet. **Do not mark `manuscript_1to1` as PROVEN for either.**

This is sample-level evidence only; it does not validate all 1,090 Chapter 7–12 candidate groups or all 17 chapters. Word and Python repository files were not modified. G3/G4/G5/G6 remain open.
