# G3 Chapter 10.1 — Four Word-derived program executions

Date: 2026-10-26. Manuscript: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`. Word positions are zero-based `python-docx Document.paragraphs` indexes, excluding paragraphs in tables.

Four examples were reconstructed from paragraph text with indentation restored and executed as distinct Python programs:

| Word paragraphs | Case | Verified stdout | Verdict |
|---|---|---|---|
| 1444–1460 | Procedural calibration for signals 1,3,9 | `[0.0, 1.0, 4.0]` | PASS |
| 1471–1492 | Pure function `linear_concentration` plus comprehension | `[0.0, 1.0, 4.0]` | PASS |
| 1504–1525 | Dataclass `LinearModel` with method | `4.0` | PASS |
| 1570–1585 | Staged processing with conversion, computation and print | `[0.0, 1.0, 4.0]` | PASS |

These programs are **Word-excerpt reconstructions**, not independently runnable verbatim Word text (Word code spans are broken across paragraphs and lost indentation). Their selected output matches are exact strings. The examples deliberately omit robust scientific input validation; passing nominal values does not establish edge-case safety or source-file parity.

Local evidence: `G3_CH10_10_1_1_Four_Programs_20261026.csv` and executing harness `ch10_1_1_verify.py`. This pass added four **new** checks; previous local-copy 30/30 tests are separate, and should not be conflated with the Word examples.

The earlier goal of byte-level GitHub vs local execution-copy parity is **not yet fulfilled** in this audit; do not assert exact source equivalence.

No Word or GitHub Python implementation changed; G3/G4/G5/G6 remain HOLD.