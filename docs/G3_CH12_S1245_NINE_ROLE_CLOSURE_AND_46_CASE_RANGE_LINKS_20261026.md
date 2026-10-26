# G3 Chapter 12 — §12.4–12.5 residual closure and broad-span evidence review (2026-10-26)

Input register: `G3_CH12_Post_12_Block_889_Register_20261026.csv` (889 original Word v37 candidate paragraph positions). All changes made to annotations only; source Word / executable Python unchanged. Output local trace: `G3_CH12_889_Post_S1245_Residual_Classification_20261026.csv`.

## Verified role closure: nine §12.4–12.5 paragraphs
- Narrative: p6027, p6066, p6434, p6483 (4).
- Genuine OMML mathematical objects: p6201, p6202, p6494, p6497 (4).
- Dependent single-line explanatory example `b = a.T`: p6204 (1). Its role is not an independent runnable code example.
- All nine previously `PRIOR_BROAD_SPAN_ONLY` rows remain in the historical 889 register, but gain explicit `S12_4_5_ROLE_CLOSED_*` classifications.

## Broader references reconciled but **not** promoted to execution PASS
- §12.7: 7 candidate paragraphs in existing nine-case numerical audit, involving float32 dtype and floating-point cancellation. The original case report gives reported case ranges and results; this turn does not rerun cases or prove each paragraph independently executable.
- §12.8: 39 candidate paragraphs in the existing 12-case integrated-expression audit; these belong to previously recorded matrix/normalization/axis/error demonstrations. Again **case-range reference**, not line-by-line new execution.
- These 46 rows move to `PRIOR_CASE_RANGE_REFERENCE_RETAINED` to distinguish them from entirely unattributed broad spans. Never add 46 to the 126 checks.

## Updated evidence ledger, 889 candidates
- 9 §12.4–12.5 XML-role closed.
- 46 §12.7–12.8 case-range references distinctly recorded.
- 64 remain `PRIOR_BROAD_SPAN_ONLY` (49 §12.6, 15 §12.9).
- 213 remain in `REVIEW_POSSIBLE_CODE_*` or `REVIEW_OTHER_OR_FRAGMENT` categories; those are separate from the 64.
- Original 126 scoped case successes unchanged.
- Note the reduction 119 -> 64 is **classification of evidence**, not 55 new calculations or 55 newly completed programs.

## Next concrete task
For the 64 remaining broad references, §12.6 p7080–7134 concerns one continuous Euler-solver program and its test/contract code; §12.9 has dependent kinematics code plus Word OMML expressions and prose. Examine whole contiguous Word code boundaries and compare against exact original QA CSV case expressions. Then review the 213 unclassified candidates by group and classify narrative/OMML/output versus executable.

No compute test performed here; no Chapter 6/10 repeat; G3 Chapter 12 IN PROGRESS, G4/G5/G6 HOLD.
