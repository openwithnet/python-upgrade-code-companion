# Chapter 10 G3 — Formal Scope and Role Register (2026-10-26)

**Decision: Chapter 10 scoped technical evidence ACCEPTED; unconditional Chapter 10 G3 PASS / final freeze remains HOLD.** This document freezes the *review classification* of 59 known logical units, not the book text or executable source.

## Stable role taxonomy for 59 traced units
- **44 WORD_TEACHING_CODE_RECONSTRUCTED_OR_RELATED_SOURCE**: runnable/behavioral Word examples or reconstructed related functions. Retain exact Word anchors, execution checks and explicit dependencies. GitHub source may be related rather than verbatim. **Do not imply 44 independently executed exact-source programs**.
- **10 NON_STANDALONE_CONCEPT_OR_SUMMARY**: diagrams, notation or prior-code reuse. No separate Python file is required; preserve explanatory labels.
- **5 WORD_ONLY_DESIGN_ILLUSTRATION**: §10.6 pedagogy and over-abstraction illustrations. They do not become `ch10_pipeline.py` simply because the file is located under Chapter 10.

The complete row-level scope classification is `G3_CH10_59_Unit_Role_Scope_Freeze_20261026.csv` (working QA evidence). It derives from the previous 59-item adjudication with explicit `final_code_role`, `source_relation`, `g3_unit_disposition`, and `publication_code_policy` fields. It does **not** add new run results or prove every Word fragment has been discovered.

## Technical evidence already verified
- GitHub module/test/dependency source blobs: **8/8 exact Git blob SHA** at inspected revision; local original-content pytest **31/31 PASS**. Following the C3 docstring correction, that changed blob was again matched and 31 tests passed.
- GitHub Actions `40263298708` for correction commit `86b89940`: **completed SUCCESS** under Linux Python 3.11.
- Chapter 10 Euler/analytic display table: **12/12 displayed numerical values matched**.
- Extra Word scans uncovered no additional standalone program in the registered candidate sample, but lexical scanners cannot establish completeness in all document encodings/layouts.

## What is closed, and what still blocks unconditional G3
Closed for this defined scope: the specific local source-blob mismatch, selected functionality/regression checks, corrected C3 pipeline role description, expected output comparison and **59-row role disposition**.

Still required:
1. A final **manual editorial check** of Word executable versus explanatory snippets, including nonstandard formatting, beyond automated detection. Mark runnable, dependent, demonstration, pseudocode and expected output accurately.
2. Keep clear per-example manuscript↔GitHub relationship labels; semantic analogues must not be labeled exact Word extraction, and avoid manufacturing files for diagrams.
3. The Word master itself needs G4 equation/layout QA; latest Windows/Conda result and G5 rights/provenance remain separate release criteria.

**Gate labels:** Chapter 10 G3 = CONDITIONAL_SCOPE_REVIEWED / FINAL_HOLD; book-wide G3 = IN PROGRESS; G4/G5/G6 = HOLD. No Word manuscript, test or executable Python source was altered by this classification.
