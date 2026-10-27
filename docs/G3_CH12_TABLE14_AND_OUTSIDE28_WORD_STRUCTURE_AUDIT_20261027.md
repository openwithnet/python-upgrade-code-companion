# G3 Chapter 12 — Table-cell audit and 28 omitted code-form paragraph adjacency (2026-10-27)

## Inputs and counting
Read the original **Word v37** file `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` directly. Inspected Word OOXML `word/document.xml` **14 top-level tables** embedded in Chapter 12, their `w:tc//w:p` cells, and paragraph roles. Matched 28 code-form/continuation candidate indices from prior reversed screen against original 889-candidate positions. No computation tests were repeated; manuscript and Python code unchanged.

## Table-cell completeness, within actual inspected OOXML tables
- **14/14 Chapter 12 tables inspected; 230 table-cell paragraphs**.
- Tables contain scientific metadata, axis descriptions, Broadcasting shape compatibility, View/Copy and stride comparisons, performance considerations, 4×4 gene expression numbers, physics constants and trajectory output tables.
- A naive assignment-token scan identified **8** row labels like `axis=0` / `axis=1` / `axis=2` in **three tables** (after Word paragraph 4797, 5175 and 7628). These are **table labels describing NumPy axes**, not free-standing Python programs. No independent runnable Python code blocks were identified in the 14 inspected tables.
- Detailed per-table audit including Word paragraph insertion point and cell text: `G3_CH12_14_Word_Tables_Contents_Audit_20261027.csv`.

## Outside-889 source-like candidates
The previous reverse screen identified **27 multi-line source continuations** plus **1 dependent code expression**, or **28 code-form items** absent from the initial 889. Each of the 28 has an existing 889-candidate paragraph within **six top-level paragraphs**; attached link positions, text and distances are in `G3_CH12_28_Outside_Candidate_Code_Adjacency_20261027.csv`.

The 28 do **not** appear to be separately independent programs based on their source role and adjacency; typical examples are continued function parameter lines, dependent indexing and line-wrapped Euler calls. **Adjacency alone cannot prove block integrity or execution.** An exact block-span crosswalk remains required, and this matching should not be treated as 28 successful computations.

## Chapter-wide gate assessment
- Original 889 heuristic candidate roles: **classified**.
- Newly found 28 source-like positions: **identified, linked to near existing candidate context**; require exact block-span incorporation.
- Chapter 12 table cells: **14 tables/230 paragraph positions examined**; no standalone runnable source identified.
- Five GitHub modules: **representative non-verbatim references**, 21 functions, not comprehensive canonical Word source extraction.
- Remaining risk: precise end-to-end **block identity and per-block QA source provenance**, unrecognized story types / shapes, and verification evidence levels. No full G3 PASS claimed.

**G3 Chapter 12 remains IN PROGRESS / HOLD for full approval; G4/G5/G6 HOLD.** Chapter 6/10 checks not rerun. Word and GitHub Python executable sources unchanged.
