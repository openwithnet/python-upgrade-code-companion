# G3 Chapter 12 — §12.4–12.5 52 Broad-Span Word Paragraphs XML Role Review (2026-10-26)

## Source and method
Read actual `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` OOXML `word/document.xml`, direct `w:body/w:p` zero-based, for exactly the **40 §12.4 + 12 §12.5** candidates still tagged `PRIOR_BROAD_SPAN_ONLY` in `G3_CH12_889_Register_After_Additional_QA_CSV_20261026.csv`. Extracted the current text, immediate previous/next paragraph, and `m:oMath` flags. Detailed trace: `G3_CH12_S12_4_5_52_Word_Source_Context_20261026.csv`.

## Grounded role results
- **44** code-form paragraphs or multiline code continuations. This includes assignments, function calls, import, printed results in actual Python statements, and nested argument lines. They are **not 44 independent programs**.
- **4** narrative/reference descriptions rather than executable Python: p6027 `np.shares_memory()` description; p6066 `np.ix_()` description; p6434 `np.may_share_memory()` discussion; p6483 `np.float64` size discussion.
- **4** true OMML mathematical-display paragraphs with no plain extracted Python text: p6201,6202,6494,6497. These were previously misidentified as empty by the text-only parser, and must remain editable Word equations.

## Provisional code-block clusters requiring evidence
- §12.4 p6081–6097: 3D array indexing and shape; requires multiline construction/context.
- §12.4 p6107–6109: repeated integer index selection.
- §12.4 p6139–6169: reshaping with explicit/inferred dimensions, several separate demonstrations.
- §12.4 p6185–6211: transpose, `.T`, reshape-versus-transpose explanatory comparisons; p6201–6202 are mathematical displays, not Python.
- §12.4 p6230–6272: transpose axis order, `np.moveaxis`, `np.swapaxes`; split across multiple paragraphs.
- §12.5 p6327–6367: basic copy/view demonstrations and shape/dtype output with shared setup; individual roles need source/output boundary analysis.

**Conclusion:** These 52 audit-span-only candidates are now **role-classified at the Word/XML level** (44 code-form; 4 narrative; 4 OMML). This does **not** establish that all 44 code-form paragraphs were previously tested, nor that 52 verification cases exist. Preserve the evidence distinction `WORD_XML_ROLE_CLASSIFIED_AUDIT_SPAN_ONLY` until exact code blocks or previous QA case records are joined.

## Impact / next work
- 8 of the 52 can be removed from the executable candidate queue based on role evidence, without deleting historical candidate rows.
- 44 code-form paragraphs should be reconstructed into actual complete blocks and linked to prior QA case proof or isolated verification only if necessary.
- The earlier **126 scoped checks** are not repeated, nor do they independently prove all candidates.
- Word and GitHub executable source untouched. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD. Chapter 6/10 validation not rerun.
