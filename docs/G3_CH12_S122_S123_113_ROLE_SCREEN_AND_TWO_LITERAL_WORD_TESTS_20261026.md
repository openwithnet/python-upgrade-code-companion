# G3 Chapter 12 — §§12.2–12.3 113-candidate role screen and literal manuscript tests (2026-10-26)

## Inputs
- Word: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, parsed directly from OOXML `word/document.xml`, top-level `w:body/w:p`, zero-based.
- Candidate register: `G3_CH12_889_Post_S1245_Residual_Classification_20261026.csv`. Selected the currently `REVIEW_*` candidates in §§12.2 (60) and 12.3 (53), **113 candidate paragraph positions**. No global 889 count was altered.
- Working trace CSV: `G3_CH12_S122_S123_113_Candidate_Context_Roles_20261026.csv`.

## Preliminary role screen (not a 113-test PASS)
- §12.2: 25 assignment/continuation; 20 dependent code expression; 9 axis/keepdims labels; 5 explanatory prose; 1 fragment requiring contextual review.
- §12.3: 22 assignment/continuation; 2 control lines; 8 dependent code expressions; 8 lines belonging to the Word function source; 12 lines belonging to the Word's own test examples; 1 fragment requiring contextual review.
These roles are *heuristic* and should be confirmed at complete contiguous block level. In particular, individual continued function/array lines are not independent Python examples.

## Newly executed **literal Word-authored tests**
- Function `apply_experiment_scales`: Word p5708–5728, with exact multi-paragraph form and validation branches retained.
- Imported setup: Word p5783 `import numpy as np`, p5812 `import pytest`.
- Test `test_experiment_scales()`: Word p5786–5809; passes exact-value `np.testing.assert_allclose` expected result.
- Test `test_invalid_scale_shape()`: Word p5815–5823; `pytest.raises(ValueError)` passes for data shape (3,4) and four scales.
- Method: direct Word paragraph text assembled in manuscript order, Python compiled, functions called, exceptions/assertions checked. No unrelated source edits or reviewer substitutions to the two test bodies.
- **2/2 Word-authored test functions PASS.** Combined extracted source SHA-256: `53a1b22dc6fd2a196a6844072a950d97b5b24cef22827264bc264f030ef148fb`.
- Existing §12.3 four reviewer contract checks concerned related function behavior but did not by themselves demonstrate that both **literal Word test functions** had actually run. This new record adds precisely scoped provenance. It does not claim two *semantically unique* checks versus previous Chapter 12 126 cases.

## Next actual work
For §12.2, join continued statements to actual code groups and match specific displayed outputs and earlier exact case IDs; do not rerun previously green 12.2 checks. For §12.3, prioritize the remaining p5601–5623 3D scaling examples, p5667–5682 invalid/valid broadcasting, p5738–5743 shape precheck, and p5774 temporary-array explanation; classify rather than presume error. The separate `REVIEW_*` candidate positions in §§12.1, 12.4–12.9 remain untouched.

**Gate:** Chapter 12 G3 IN PROGRESS, G4/G5/G6 HOLD. Existing Chapter 6/10 calculation checks were not rerun; Word and GitHub executable files unchanged.
