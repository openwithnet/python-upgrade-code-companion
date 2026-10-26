# G3 Chapter 1 — Word v37 ↔ section Python code content audit (2026-10-26)

## Inputs and method
- Word: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` (Library copy). Extracted `word/document.xml` as ZIP/XML; counted only direct `w:body/w:p`, zero-based and preserved `w:br`, `w:cr`, `w:tab` in text.
- GitHub: private `openwithnet/python-upgrade-code-companion`, `main`, 15 section Python files, fetched directly following prior annotation-only commits.
- Compared the actual lines belonging to each of 31 annotated Word code paragraphs to the text after each matching `# manuscript paragraph` comment. Ignored companion-only source metadata, injected prerequisite blocks, blank separators, and trailing file-newline conventions. This is a line-by-line content review, **not** a cryptographic byte-wise proof of OOXML run serialization.

## Comparison results
| Section source | Word paragraph numbers (0-based) | Result |
|---|---|---|
| 1.1.1 | 12,17,21 | MATCH |
| 1.1.2 | 28 | MATCH |
| 1.1.3 | 34 | MATCH |
| 1.2.1 | 43 | MATCH |
| 1.2.2 | 52,56 | MATCH; prerequisite replay |
| 1.2.3 | 66,71,76,86,90 | MATCH; prerequisite replay |
| 1.3.1 | 99 | MATCH; prerequisite replay |
| 1.3.2 | 107,111 | MATCH; prerequisite replay |
| 1.3.3 | 120,124,131,136,139 | MATCH; prerequisite replay |
| 1.4.1 | 146 | MATCH; prerequisite replay |
| 1.4.2 | 159 | MATCH; prerequisite replay |
| 1.4.3 | 168,174 | MATCH; prerequisite replay |
| 1.5.1 | 189 | MATCH |
| 1.5.2 | 198,209,214,218 | MATCH; replay of §1.5.1 |
| 1.5.3 | 223 | MATCH; prerequisite replay |

**Total: 31/31 annotated paragraph blocks compared, all visually/textually aligned at source line level.** No newly discovered executable statement differences in this bounded review; source/Word code unchanged. Seven stale comment anchors corrected separately in five files in `docs/G3_CH01_WORD_V37_15_FILES_ANCHOR_RECHECK_20261026.md`.

## Scope limitation / next gates
- This is **annotated-block coverage** only. It does not by itself prove no additional unannotated Python blocks occur elsewhere in Chapter 1; a complete chapter-wide code paragraph inventory remains desirable.
- GitHub modules deliberately replay prerequisites; those blocks are not represented as belonging to the current subsection and must not be used for bytewise file-versus-Word paragraph equivalence.
- `section_1_5_3.py`: printed `True` in Word is expected output rather than an executable statement; it remains intentionally omitted from source.
- Literal executions and environment-specific NumPy behavior must be classified separately. G3 Chapter 1 FULL PASS is **HOLD** until completeness and execution evidence are recorded; G4/G5/G6 independently HOLD.
- Chapter 6 and Chapter 10 previous scoped tests were not rerun.
