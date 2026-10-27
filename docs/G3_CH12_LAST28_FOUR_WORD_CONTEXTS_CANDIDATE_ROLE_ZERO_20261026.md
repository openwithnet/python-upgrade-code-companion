# G3 Chapter 12 — Final 28 candidate-role reconciliation (2026-10-26)

Canonical source: Word v37 OOXML direct top-level Word paragraphs, zero based. Input: `G3_CH12_889_After_S126_S127_35_Reconciliation_20261026.csv`. All **28 remaining REVIEW positions** were grouped into four runnable Word-derived contexts; all four executed PASS. Word and production GitHub Python source unchanged.

| Section | Original candidate positions | Test/role |
|---|---:|---|
| §12.8 | 4 (p7600,p7605,p7610,p7677) | Word-native sample/gene/group metadata; shape stdout `(4,)` exact; arrays checked in supplementary reviewer assertions |
| §12.9 | 11 (p8341–8380 selected code positions) | Word-native loop and NumPy performance example on 1,000,000 input points. Built-in `np.testing.assert_allclose` passes; no time thresholds claimed |
| §12.9 | 5 (p8395,8404,8406,8407,8411) | Readability illustration: equivalent loop and vector position results with Word function definitions and illustrative times. These are dependent snippets, not 5 programs |
| §12.9 | 8 (p8439,8443,8447,8449,8451,8456,8459,8460) | Word-native `v^2 = v0^2 + 2a(x-x0)` identity via original `np.testing.assert_allclose` |

Working execution detail, stdout and source hashes: `G3_CH12_Last28_Four_Word_Contexts_20261026.csv`. New 889-row register with updated statuses: `G3_CH12_889_All_Candidates_Classified_20261026.csv`. Both produced directly in current session and retain all original 889 paragraph IDs.

## Evidence gate, critically distinct from role gate
**All 889 syntax-detected paragraph positions now have a role/evidence category; 0 remain `REVIEW_*`.** This is a *candidate-role classification* milestone and **not proof** of full document-wide source/execution coverage, because: heuristic candidates may omit actual code; some original QA citations cover broad section/case ranges rather than exact literal source; five GitHub chapter-12 reference modules are representative reconstructions rather than exact manuscript extraction; historical chapter scoped cases may overlap. A release-quality canonical G3 FULL PASS therefore requires independently demonstrated code-block completeness, exact source provenance, and gate-specific evidence reconciliation, with no invented arithmetic totals.

The four scoped execution contexts are not 28 independently executable code programs. Timing outputs are environment specific; printed timing magnitude was deliberately **not** compared to any universal criterion. No previous Chapter 6/10 validations were rerun.

Status: **Chapter 12 G3 IN PROGRESS / CANDIDATE ROLE TRIAGE COMPLETE**; G4/G5/G6 HOLD.
