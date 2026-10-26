# G3 Chapter 1 — SourceCode paragraph completeness (2026-10-26)

Input: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, direct `w:body/w:p` of `word/document.xml` (zero based), Chapter 1 through paragraph 225. Word paragraphs with style `SourceCode` were inventoried without assuming every such paragraph contains executable Python.

## Classification
- 31 authored code-containing paragraphs, all 31 already mapped to the 15 GitHub section files and checked in `G3_CH01_WORD_V37_31_CODE_BLOCKS_CONTENT_AUDIT_20261026.md`.
- Additional `SourceCode` paragraphs consist of displayed outputs rather than independent Python programs (examples: p14 `25.3`, p19 `25.4`, p36 array output, p225 `True`).
- Some code paragraphs immediately followed by prose or inline code may have no adjacent output block (for example p136); this is not an omission.
- No additional unanchored `SourceCode` executable program identified in this main Chapter 1 range.

**Gate scope:** This closes top-level `SourceCode` paragraph inventory for Chapter 1, *not* nested-table/shape text or a proof that output strings match all current NumPy environments. Chapter 1 G3 remains scoped until execution/output verification. Chapter 6 and Chapter 10 tests were not rerun.
