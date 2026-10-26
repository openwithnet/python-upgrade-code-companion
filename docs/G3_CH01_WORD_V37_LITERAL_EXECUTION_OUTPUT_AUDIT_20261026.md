# G3 Chapter 1 — Word v37 Literal Execution and Displayed Output Audit (2026-10-26)

## Evidence
- Source Word: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` (retrieved from Library).
- Method: Python `zipfile` and `lxml` extraction of direct `w:body/w:p`, zero-based, retaining `w:t`, `w:br`, `w:cr`, and `w:tab` contents. Executed the **actual Word extracted code text** in paragraph sequence per section, with prerequisite definitions replayed as declared in the GitHub section-file comments. Used `ast.parse`, `compile`, `exec`, `contextlib.redirect_stdout`.
- GitHub source: `chapters/chapter01/sections/section_1_1_1.py` through `section_1_5_3.py` (15 files), previously mapped to 31 Word code paragraphs in `docs/G3_CH01_WORD_V37_31_CODE_BLOCKS_CONTENT_AUDIT_20261026.md`.
- No Chapter 6/10 testing repeated.

## Findings

| Status | Count | Evidence |
|---|---:|---|
| Executed Word code paragraphs without exception | 31/31 | 15 sections, original Word code texts |
| Exact stdout match to displayed Word `SourceCode` output | 28/28 | Whitespace and line breaks retained; stdout compared as text after final newline |
| No stdout generated, as intended | 2 | Word p21 (list), p28 (objects) |
| Stdout generated but no standalone printed-result block in Word | 1 | Word p136: `(3,)` and `(1, 3)` |
| Unexpected error | 0 | Ragged array example p90 catches `ValueError` as intended |

`§1.5.3` p223 printed `True` as expected, matching display p225. This printed output is not a Python statement and must not be appended to the executable source. For `§1.3.3` p136, absence of a display block is an editorial choice/coverage gap, not evidence of a Python code defect. No source-code or manuscript modification was made.

## Interpretation / remaining gates
- **Chapter 1 G3 — scoped annotated Word-code execution/output PASS:** 31/31 runnable passages; 28/28 printed outputs match. Source text and anchors already compared separately.
- The in-chat check executed actual Word extracted text, not GitHub file bytes freshly downloaded into the local execution container. The GitHub source files had already been fetched and their source lines compared in the earlier G3 audit. Consequently this is a combined body-content + Word-execution evidence, **not** an independent newly executed GitHub checkout or proof of cross-platform conda behavior.
- G1 Linux CI, G2 Windows/Conda on current HEAD, G4 Word formatting/OMML, G5 rights/provenance, G6 final release all remain independently gated; do not claim book-wide or unconditional Chapter 1 final freeze.
- Logical next step: inspect Chapter 12 existing 126 case checks and five corresponding source modules against the full Word code inventory without rerunning previously passed Chapter 6/10 calculations.
