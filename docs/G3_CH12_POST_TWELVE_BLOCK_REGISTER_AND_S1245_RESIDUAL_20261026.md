# G3 Chapter 12 — Apply twelve §12.4–12.5 Word execution records to 889-candidate register

Date: 2026-10-26. Sources: `G3_CH12_889_Register_After_Additional_QA_CSV_20261026.csv`, `G3_CH12_S12_4_5_12_Word_Block_Execution_20261026.csv`, and the original Word v37 XML. Prior audits `docs/G3_CH12_S12_4_5_TWELVE_WORD_BLOCK_EXECUTIONS_20261026.md` and `docs/G3_CH12_S12_4_5_52_WORD_XML_ROLE_CLASSIFICATION_20261026.md` already document execution and roles.

## Strict joining
12 executed contexts list **63 distinct referenced code paragraph IDs**. Of these **45 occur among original 889 syntax candidates**, and **43 previously held PRIOR_BROAD_SPAN_ONLY**. Those 43 positions (35 in §12.4, 8 in §12.5) are promoted to `WORD_NATIVE_12_BLOCK_EXECUTED_EXPLICIT`. Other two previously evidenced candidate positions remain in their original categories. Do not count 63 as 63 runnable programs, or treat the 43 as fresh test executions.

Updated 889-row crosswalk: `G3_CH12_Post_12_Block_889_Register_20261026.csv`. Chapter-wide broad-span-only count **162→119**. Separately unreviewed syntax/fragment candidates remain **213**; they have not silently passed.

## Remaining nine broad-span candidates in §§12.4–12.5
- p6027: `np.shares_memory()` explanatory prose, not source.
- p6066: `np.ix_()` explanatory prose.
- p6201, p6202: Word OMML equation objects, not Python.
- p6204: `b = a.T`, a dependent *illustrative single-line assignment* referring to previous `a`; it is followed by the tested reshape-vs-transpose definition at p6207–6211. Not a newly distinct executable program or failure.
- p6434: explanatory prose on `np.may_share_memory()`.
- p6483: explanatory prose describing `np.float64` itemsize.
- p6494, p6497: Word OMML equations, not Python.

Hence the residual nine are **four prose, four OMML, one dependent illustration**. These are classified at the XML-role level but the source register retains `PRIOR_BROAD_SPAN_ONLY` pending a future mass-role reconciliation, rather than pretending a stand-alone execution PASS.

No additional calculations were run. No Word or GitHub executable Python file changed. Prior 126 scoped Chapter 12 cases and Chapter 6/10 audit evidence were not retested. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
