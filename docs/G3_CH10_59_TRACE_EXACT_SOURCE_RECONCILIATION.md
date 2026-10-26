# G3 Chapter 10 — 59-Unit Trace Register Reconciled to Exact GitHub Source

Date: 2026-10-26. Input: existing 59-row integrated Word/source/test CSV and verified eight-source Git blob hash/pytest record. Updated CSV: `G3_CH10_Integrated_59_Trace_UPDATED_Exact8_20261026.csv`.

## Verified source-level evidence

- All **8 of 8** reviewed GitHub module/test/dependency files have exact Git blob SHA parity in the isolated verification directory.
- On these files, **31/31** pytest cases PASS (Python 3.13.5, pytest 9.0.2).
- Separate GitHub Actions run 40255432567 on commit 6b1dc4dd passed all 18 Linux Python 3.11 jobs.
- This establishes the original repository files' tests for the *eight-file scope*, not exact identity between independent Word paragraph examples and source functions.

## 59 logical trace rows — source relationship labels

| Label | Count |
|---|---:|
| Exact GitHub file verified, semantic Word relation only | 16 |
| Exact repository file available, direct Word parity unproven | 33 |
| No direct GitHub source identified | 6 |
| Dependent Word summary snippet | 4 |
| Total | 59 |

These counts refer to **trace rows**, not 59 scripts or 59 tested programs. The existing logical-unit boundaries and Word paragraph anchors are unchanged.

## G3 decision

**Chapter 10: NOT YET APPROVED.** Remaining gates are: (a) independently show complete Word-to-source/test correspondence for each actual executable block instead of treating related or representative implementations as verbatim; (b) evaluate six rows with no direct source; (c) confirm no code escaped the paragraph-boundary inventories; (d) formally separate `ch10_pipeline.py` (archived C3 calibration pipeline) from Word §10.6 (design versus over-abstraction); (e) maintain the independent publication/provenance review for G5.

The formerly identified three unexecuted Word functions were separately exercised in `G3_CH10_10_1_10_2_THREE_GAP_CHECKS.md`, but using a local C3 environment. No Word master or executable GitHub Python source changed in this audit. G4/G5/G6 HOLD.
