# G3 Word Code Inventory — First Pass (2026-10-25)

**STATUS: PRELIMINARY / NOT FROZEN.** Source: current G4 QA Word candidate `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, 26,994 paragraphs. Generated inventory is a local CSV mapping zero-based Word paragraph ranges; **no code has been newly executed for this inventory**.

## First-pass code-style groups

Extracted consecutive nonempty paragraphs whose Word style is `code`, `Code QA`, or `Source Code`; grouped into **2,072 blocks**.

| Chapter | Blocks | Chapter | Blocks |
|---|---:|---|---:|
| 1 | 59 | 2 | 48 |
| 3 | 6 | 4 | 22 |
| 5 | 16 | 6 | 8 |
| 7 | 0 | 8 | 0 |
| 9 | 0 | 10 | 0 |
| 11 | 0 | 12 | 0 |
| 13 | 282 | 14 | 325 |
| 15 | 353 | 16 | 208 |
| 17 | 745 |  |  |

**Crucial coverage caveat:** Chapters 7–12 show *zero code-styled groups* under this extraction method, NOT zero examples. Their code may be embedded in `Normal` or other styles, as table content, or inline. This is an incomplete style-filtered inventory, not a chapter-by-chapter source completeness matrix.

## Heuristic classification (NOT VERIFIED)

- Python-code candidates: **1,737**
- Explanatory text/output candidates: **286**
- Output candidates: **31**
- Interactive snippets: **16**
- Commands: **1**
- Pseudocode candidates: **1**

Counts are rough content heuristics and must not be used to infer that a block is standalone executable or that only one pseudocode block exists. Every block is marked `UNREVIEWED_NOT_PROVEN`.

## Follow-on verification protocol

1. Second-pass extraction across **all styles, tables and inline code**, especially Chapters 7–12; detect fragments without overcounting prose.
2. Human/semantic classify into `EXECUTABLE_STANDALONE`, `EXPLANATORY_SNIPPET`, `PSEUDOCODE`, `SHELL_COMMAND`, `EXPECTED_OUTPUT`, or `NONCODE`.
3. Associate Word chapter/section/paragraph positions with the matching files listed in `CODE_FILE_CATALOG.md` and source role/hash inventory.
4. Verify dependencies, runnable examples and claimed outputs while preserving intentional bugs and non-executable pseudocode.
5. Require explicit source/rights evidence before moving publication gates G3/G5/G6 from HOLD.

**This audit does not modify Word or Python files.** Previous six representative alignment audits remain valid only within their stated scopes.
