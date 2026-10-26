# G3 Chapter 12 §§12.2–12.3 — exact historical case provenance and negative-axis contract (2026-10-26)

Word master: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, zero-based Word XML paragraph IDs. Baseline 113 candidate register `G3_CH12_S122_S123_113_Candidate_Context_Roles_20261026.csv`.

## Historical QA case-to-paragraph crosswalk (no reruns)
Cross-referenced original case-level CSVs: `G3_CH12_12_2_Targeted_5_Cases_20261026.csv`, `G3_CH12_Targeted_Unmapped_Cases_20261026.csv`, Library `G3_Ch12_Broadcast_Errors_Boolean_12_Examples_20261026.csv`, `G3_CH12_12_3_Four_Semantic_Contract_Checks_20261026.csv`, and the two explicitly executed Word test functions `test_experiment_scales` / `test_invalid_scale_shape` (already documented in `G3_CH12_S122_S123_113_ROLE_SCREEN_AND_TWO_LITERAL_WORD_TESTS_20261026.md`). The historical 12-case CSV includes both 3D scaling examples p5601–5623: **already verified**, not rerun.

| Section | Candidates already referenced by historical QA cases | Explanatory/non-executable | Remaining not matched by these precise case references | Total |
|---|---:|---:|---:|---:|
| 12.2 | 20 | 14 | 26 | 60 |
| 12.3 | 42 | 0 | 11 | 53 |
| **Total** | **62** | **14** | **37** | **113** |

These counts indicate crosswalk evidence, not 62 independent successful programs, 14 mathematical mistakes, or 37 unverified standalone programs. Among 37 unlinked entries, p5348 and p5507 are clearly Korean prose and should be role-reclassified when updating the canonical 889-row ledger.

Output provenance artifact `G3_CH12_S122_S123_113_Existing_QA_Provenance_Crosswalk_20261026.csv` retains all initial candidate fields plus `preexisting_case_links` and `evidence_decision`.

## New narrowly scoped execution of a Word error-and-fix block
The historical evidence crosswalk did *not* pinpoint p5667–5682. Executed literal text from:
- p5667 `a = np.ones((3, 4))`, p5668 `b = np.ones(3)`
- p5670 `result = a + b` -> **expected `ValueError` raised** (last dimensions 4 and 3 incompatible)
- p5680 `result = a + b[:, None]`, p5682 `print(result.shape)` -> **`(3, 4)` exactly equals Word p5684**

Two **scoped checks PASS**; one is an expected-error contract, not a failed program. Local evidence `G3_CH12_S123_Word_Incompatible_Axis_Contract_20261026.csv`. Do not aggregate these with prior 126 scoped cases without overlap de-duplication.

## Next actual audit
- §12.2 remaining groups: p5167–5215 (3D replicate/time/variable reductions), p5229–5247 (spatial/time means), p5260–5266 (chemical species slice), p5277–5287 (gene mean), p5300–5304 (transpose). Extract full contiguous Word blocks and check older case evidence before tests. p5090 relates to previous `keepdims` demonstration context.
- §12.3 p5738–5743 `np.broadcast_shapes` and p5774 fused temporary-array expression are presently unmatched in these CSVs; classify against Word source and prior audit rather than pretending executed.
- Reconcile rows in the 889-register explicitly; this evidence document alone does not assert the whole chapter passed.

No Chapter 6/10 retests. Word manuscript and GitHub Python production source unchanged. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
