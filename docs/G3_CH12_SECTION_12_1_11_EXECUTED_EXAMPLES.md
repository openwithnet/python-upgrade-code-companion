# G3 — Chapter 12 §12.1.1–12.1.2 Context-Reconstructed Examples (2026-10-25)

**Scope: 11 real teaching examples extracted from the current Word G4 QA manuscript, checked with explicit NumPy import context; all 11 exit 0, and all 9 examples with stated outputs match.** This is independent current-turn Python execution, not inferred from prior CI or the 1,090 automatic group count.

| Example | Word paragraph code range/indices (0-based) | Output paragraph | Result |
|---|---|---|---|
| Python list-loop squares | 4599,4601,4603–4604 | none | execution success, no print |
| NumPy squares | 4606,4608 | none | execution success, no print |
| elementwise sum | 4624,4626,4628 | 4630 | `[5 7 9]` |
| elementwise multiplication | 4624,4626,4632 | 4634 | `[ 4 10 18]` |
| inner product | 4624,4626,4639 | 4641 | `32` |
| matrix total sum | 4648–4651,4653 | 4655 | `21` |
| axis 0 sum | 4648–4651,4657 | 4659 | `[5 7 9]` |
| axis 1 sum | 4648–4651,4663 | 4665 | `[ 6 15]` |
| axis 0 mean | 4648–4651,4672 | 4674 | `[2.5 3.5 4.5]` |
| axis 1 mean | 4648–4651,4677 | 4679 | `[2. 5.]` |
| 3 experiment / 4 timepoint mean | 4691–4695,4697–4700,4702 | 4704 | `[1.  0.8 0.6 0.5]` |

**Boundary decisions:** Natural-language paragraphs between the code statements are not executable. The bracketed displays at Word p4619–4622 are *mathematical representations*, not source to copy. All `출력:` markers and their result paragraphs remain separate `EXPECTED_OUTPUT`. The sum and mean examples intentionally share preceding matrix definitions; do not represent these as 11 distinct standalone source files. This section's NumPy import was inserted as an explicit setup dependency for isolated execution.

Comparison used whitespace-token normalized textual stdout (to tolerate NumPy spacing, **not** altered scientific numeric precision). The first two cases had no printed expected results, so only clean execution was asserted.

**Artifacts:** `G3_Ch12_12_1_ContextReconstructed_11_Examples_20261025.csv` stores paragraph IDs, execution return codes, printed expected/actual results and classifications.

**Limitations:** 11 examples from this small section only; G3 entire manuscript and remaining candidate groups not proven. Existing Ch12 representative reconstructions in the source tree were not edited or declared word-for-word equal. Source rights/release gates unchanged, no Word changes.
