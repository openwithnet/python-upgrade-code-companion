# G3 Chapter 12 — 23 reconstructed Word contexts disposition (2026-10-27)

Canonical source: Word v37, `word/document.xml` direct `w:body/w:p` zero-based. This audit is limited to the 23 contexts produced by the earlier 36-to-23 reconstruction; it is NOT an exhaustive census of all Chapter 12 runnable blocks.

## Executions
- Previously in this audit series, **C01 and C23** were executed directly from Word source (see `docs/G3_CH12_23_CONTEXT_EXECUTION_EVIDENCE_C01_C23_20261027.md`).
- A previous same-session pass executed **C02–C07**: 6/6 compile/run PASS, 6/6 printed Word output match; `G3_CH12_C02_C07_Word_Exact_Output_Verification_20261027.csv`.
- This pass ran **C08–C11, C13–C22**: 14/14 compile/run PASS, 13/13 explicit Word output group comparisons PASS. C20 has no displayed output; reviewer assertion `np.allclose(np.hypot(a,b), np.sqrt(a*a+b*b))` with literal Word source passes. C18 has two output lines; its final NumPy array line equals the Word output exactly, and Python list print is runtime informational.
- **C12** p5090 `row_mean = np.mean(a, axis=1)` is a dependent `keepdims` comparison illustration, not an independent self-contained code program, and was not treated as an error or new stand-alone test.

Thus for the **selected 23 reconstructed contexts**, **22/22 runnable contexts have literal Word-source execution evidence** (C01–C11 and C13–C23), and **1/23 is classified as a dependent non-standalone teaching expression**. The new 14-case exact source hashes, paragraph indices, printed references and observed output are recorded in `G3_CH12_C08_C22_14_Exact_Word_Context_Checks_20261027.csv`.

No failures encountered in these selected computations; the source Word and GitHub executable files are unchanged. The prior Chapter 6/10 computations were not rerun.

## Important gate boundaries
- Do not interpret 22/22 as all Chapter 12 programs tested. The 23 contexts were selected from 36 previously unresolved *provisional split groups*, not from an independently proven exhaustive Word code-block census.
- The original 889 paragraph candidate roles are classified, 28 omitted source continuations were mapped, and 14 Word tables inspected. However the heuristic 249-group grouping is not yet a stable full canonical program block inventory.
- Previous detailed audit case totals have possible semantic overlap; these 22 cannot be added blindly to 126 old scoped cases.
- Five GitHub Chapter 12 modules contain 21 **representative reconstructed** functions, not an exactly matched canonical implementation of all Word examples.
- Therefore **Chapter 12 G3 FULL PASS remains HOLD / IN PROGRESS**; G4/G5/G6 HOLD. Next work: stabilize chapter-wide executable block inventory, map all exact Word source spans and case evidence, and decide the canonical-vs-reference GitHub packaging policy.

**Storage policy:** internal intermediate QA evidence. User need not download/save; only an actual frozen recovery baseline or release would trigger MUST SAVE.