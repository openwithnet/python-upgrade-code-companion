# G3 Chapter 12 — Completeness Reverse-Screen and Gate Decision (2026-10-27)

## Canonical inputs
- Word v37: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` (read-only); Chapter 12 spans direct top-level Word paragraphs **4451–8621**.
- Final 889-row candidate-role register: `G3_CH12_889_All_Candidates_Classified_20261026.csv`.
- Five GitHub Chapter 12 modules explicitly marked `CODE_COMPANION_ROLE: REFERENCE`, `CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION`, and `RETAIN_AS_CANDIDATE_NOT_FROZEN`.
- Historical Chapter 12 scoped QA logs and matching source CSVs; this review does not rerun those tests.

## Reverse screen beyond the initial 889
The 4,171 Chapter-12 top-level `w:p` objects contain **889 classified candidate positions** and **3,282 paragraphs not in that candidate table**. A separate code-prefix / NumPy-token screen on the 3,282 surfaced **76 additional review hits**:
- **27** source-code continuation or dependent statement positions, such as Word p5319/p5320 (function type signature), p5709–5711 (array argument signature), p7638 (`n_samples, n_genes = expression.shape`), and p8243/p8280 (multiline Euler call assignment).
- **1** dependent indexing expression p6071.
- **4** shape displays/ explanatory pseudo-code outputs.
- **44** prose/headings mentioning code/NumPy.
The combined **28 code-form outside-889 hits** were not independent new programs; they are predominantly inner lines of larger examples. This is **proof that 889 is an incomplete direct paragraph-code inventory**, not proof of a computation defect. The screening does not ensure all unrecognized source formats are caught. Evidence CSVs: `G3_CH12_Outside_889_Word_Paragraph_Screen_20261027.csv` (full 3,282 rows), `G3_CH12_76_Outside_889_Token_Screen_Roles_20261027.csv` (76 reviewed hits). No 889 original rows or classifications deleted.

## Other document-structure limit
Chapter 12 also contains **14 top-level Word tables**; the existing 889 candidate count and this reverse screen are both indexed only by top-level `w:p`, *not* all `w:tbl/w:tr/w:tc/w:p` table-cell paragraphs. Preliminary table reading suggests explanatory comparisons and matrices; nevertheless table-cell code completeness has **not** been individually audited here. Word text boxes/other stories are not claimed covered either.

## GitHub code provenance
The five extant Chapter-12 modules (21 top-level `def` functions) are small **representative reconstructions**, not verbatim complete extraction of every Word code example:
- `ch12_canonical_examples.py` (3 functions)
- `ch12_indexing_memory_examples.py` (6)
- `ch12_remaining_examples.py` (6)
- `ch12_6_10_verified_examples.py` (4)
- `ch12_additional_manuscript_examples.py` (2)
Their header `RETAIN_AS_CANDIDATE_NOT_FROZEN` is consistent with G3 remaining open, not source-completeness PASS. The five sources were read directly from connected GitHub in this review. No source edits.

## Decision (scoped and honest)
- 889 **heuristic candidate role classification**: COMPLETE (889/889).
- Reverse check on 3,282 excluded top-level paragraphs: PERFORMED, 76 potential hits triaged; **28 code-form continuations discovered outside initial register**.
- Whole-manuscript code-block identity/coverage (including 14 tables and possible alternate stories): **NOT DEMONSTRATED**.
- Five-reference-module 1:1 exact source/case coverage: **NOT DEMONSTRATED**.
- Existing scoped case checks: retained as valid *within their stated test boundaries*, not summed naively into full coverage.
- Chapter 12 **G3 FULL PASS: HOLD (IN PROGRESS)**. G4/G5/G6 HOLD.

## Required next gate work, no redundant computation
1. Make a deterministic **complete Word code-block inventory**, including code continuations absent from 889 and all Chapter-12 table-cell paragraphs; one block/ID with exact source span and whether runnable, dependent snippet, formula, output, or prose.
2. Join each runnable block ID to a specific historical QA case / raw direct Word execution evidence, clearly differentiating contract assertions, exact stdout, and broader case-range links.
3. Crosswalk five representative GitHub module functions against actual Word blocks and flag representative-only code as such; decide whether a separate canonical per-block source collection is required.
4. Reassess G3 only after resolving unsupported executable blocks and provenance gaps. Do not change Word or production code without demonstrated defects, and do not re-run Chapters 6/10.

No changes to Word or GitHub Python executable source were made.