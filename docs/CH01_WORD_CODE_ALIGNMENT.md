# G3 Chapter 1 — Section-anchored Source Audit (2026-10-25)

**Decision: 15 section-level runnable study files mapped to Word v37 Chapter 1 §§1.1.1–1.5.3. G3 complete book-level 1:1 is NOT proven.** The source files are labeled `WORD_EXTRACT_REASSEMBLED`, not untouched originals.

| Source | Word section / zero-based starting paragraph | Check |
|---|---|---|
| `sections/section_1_1_1.py` | §1.1.1, p9, source anchors 10/15/19 | temperature scalar/list/2D measurements |
| `sections/section_1_2_1.py` | §1.2.1, p41 | NumPy array addition, multiplication and dot product |
| `sections/section_1_3_1.py` | §1.3.1, p97 | indexing; includes predecessor 1.1.3 NumPy construction to be standalone |
| `sections/section_1_4_1.py` | §1.4.1, p144 | elementwise scientific calculations and matrix product; contains predecessor import |
| `sections/section_1_5_1.py` | §1.5.1, p187 | gene-expression 2D array shape/type |
| `sections/section_1_1_2.py` through `section_1_5_3.py` (remaining 10 files) | §§1.1.2–1.5.3 corresponding Word headings | mapped by file number; full paragraph-block contents and outputs not yet individually certified |

## Evidence and limits

Five representative source files were directly fetched and compared with Word section headings/paragraph ranges. They carry source-code comments identifying Word paragraph anchors. The 15 section scripts previously passed Windows/Python 3.11 CI chapter-entry checks, but that does not prove every explanatory snippet in §1.1–1.5 was executed independently. Source files may replay prerequisite definitions to support independent execution and should not be mistaken for a byte-identical single manuscript block.

Source role: `EXECUTABLE`; provenance: `WORD_EXTRACT_REASSEMBLED`; release: `RETAIN_AS_CANDIDATE_NOT_FROZEN` for all 15. No new Python source edits or independent run in this audit. Third-party rights and full book coverage G3 remain open.

## Next acceptance conditions

- Per-file Word code spans, prerequisite imports, expected outputs, and pseudocode classification verified for remaining 10 files.
- A 17-chapter coverage table distinguishes scoped tested anchors, style-driven candidate extraction and complete explicit runnable corpus.
- G4 Word native rendering and G5 redistribution rights must be independently cleared before G6.
