# G3 Chapter 1 — Word v37 Paragraph Anchor Corrections (2026-10-26)

Source: Library materialized Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx. XML checked in `word/document.xml`; index is zero-based direct `w:body/w:p`, table paragraphs excluded. GitHub source: `main` after comment-only repairs.

## Verified corrections

- section_1_1_1.py: 10→12 (temperature), 15→17 (temperatures), 19→21 (measurements).
- section_1_2_1.py: 41→43 (array operations).
- section_1_3_1.py: 97→99 (indexing).
- section_1_4_1.py: 144→146 (element-wise operations).
- section_1_5_1.py: 187→189 (expression matrix).

The seven original anchors pointed to descriptive text/headings or an expected-output line, rather than the Python code paragraph. All five GitHub files were updated to replace ONLY comments; no executable Python statement or Word text changed. No Chapter 6/10 calculation retests performed.

## Current inventory (15 files, 31 anchor comments)

| File | Current anchors (zero-based) | Current source blob SHA |
|---|---|---|
| section_1_1_1.py | 12, 17, 21 | `b188a9847df15e697cc3c1e189f286c9df9fe3db` |
| section_1_1_2.py | 28 | `44ca0b1da1486eb80615ba0285c6c6d2e3943ac6` |
| section_1_1_3.py | 34 | `9679773274c368890fc5890ec189a2495666ca5f` |
| section_1_2_1.py | 43 | `73c306948fec99d37aac0b0d999dfeae23463415` |
| section_1_2_2.py | 52, 56 | `a20fbffd4bb07311572217dfef944e3fca6b43a4` |
| section_1_2_3.py | 66, 71, 76, 86, 90 | `c06bb20539f48323f8010617d6f0bdaf4f7007a4` |
| section_1_3_1.py | 99 | `7242621c3450b88d83725a7396c10dbc755c7a1f` |
| section_1_3_2.py | 107, 111 | `286c65e271d6037316c3ffea0f06d9b2c141aaf6` |
| section_1_3_3.py | 120, 124, 131, 136, 139 | `93d193ac2bc83d3e49e7f561cca8127047b14a07` |
| section_1_4_1.py | 146 | `32bda4ac2f859bc1c25d55106c7fd2ceabd93e2d` |
| section_1_4_2.py | 159 | `384eab2d76b6001f1ef5e793b08e7a69bc04b7bb` |
| section_1_4_3.py | 168, 174 | `7dd31c68e668e101817767276ba528743a534ec9` |
| section_1_5_1.py | 189 | `044154a0646bf732d8d288d0f8bd09089ea02462` |
| section_1_5_2.py | 198, 209, 214, 218 | `2086214eabe8578ec6e03e02eb5f5cda8ef31459` |
| section_1_5_3.py | 223 | `51ad592efd2efd2dde303f044a640d65093a6962` |

## Scope and remaining checks

All 31 anchors now point to candidate code paragraphs in the Word v37 top-level paragraph sequence based on extracted plain text and chapter boundaries. This is **anchor-location verification**, not a programmatic full source-code byte-for-byte identity check: Word run and line-break reconstruction, dependency/replayed code, output-only paragraphs, and executable equivalence remain to be audited before unqualified Chapter 1 G3 PASS. Existing source labels `WORD_EXTRACT_REASSEMBLED` and `RETAIN_AS_CANDIDATE_NOT_FROZEN` remain unchanged. Cross-check the whole code text next. Do not generalize an offset rule to other chapters.
