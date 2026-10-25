# G3 — Second-pass Word code candidate extraction (Chapters 7–12, 2026-10-25)

**Status: HEURISTIC CANDIDATES / NOT VERIFIED / NOT FROZEN.** The previous first pass grouped only paragraphs styled `code`, `Code QA` and `Source Code`, hence reported zero for Chapters 7–12. That zero was a **false coverage impression**, not proof of no code.

Second pass scans **Normal and other body styles plus table cells** for Python-like syntax and indented output/continuation, retaining Word paragraph positions and small previews in local CSV `G3_Word_Code_SecondPass_Ch07-12_20261025.csv` (working QA artifact; not uploaded to GitHub).

| Chapter | Body paragraph candidates | Table-cell candidates | Total |
|---|---:|---:|---:|
| 7 | 14 | 0 | 14 |
| 8 | 57 | 0 | 57 |
| 9 | 73 | 0 | 73 |
| 10 | 934 | 4 | 938 |
| 11 | 220 | 1 | 221 |
| 12 | 1,494 | 8 | 1,502 |
| **Total** | **2,792** | **13** | **2,805** |

Across the 2,805 individual **candidate text units**, heuristic categories are `PYTHON_SYNTAX_CANDIDATE` 2,147 and `OUTPUT_OR_CONTINUATION_REVIEW` 658. These are **not 2,805 executable blocks**, not confirmed code snippets, and not proof of complete capture. False positives and multi-line fragments remain; displayed counts cannot be added directly to the previous first-pass 2,072 grouped blocks.

**Example cross-checks:** §7.5 has `DNASequence` narrative/constructor expressions; §8.4 `LinearCalibration` and `QuadraticCalibration` formula text; §9.5 has `from c3_validation import SignalMeasurement`, `measurement = ...`, `assert ...`; §12.8 has multiline `np.array([...])` code fragments in Normal paragraphs. Chapters 10 and 12 contain extensive Normal-style fragments.

**Next gate:** Group sequential candidate lines into coherent fragments, classify as executable example / explanatory snippet / explicit pseudocode / shell command / expected output, deduplicate vs first pass and map to `docs/CODE_FILE_CATALOG.md` and the six scoped G3 evidence records. Independently test only blocks explicitly represented as runnable, keeping intentionally incomplete snippets and pseudocode labelled. Do not claim full 17-chapter coverage, release rights, or G3 PASS.

**No Word or Python source files changed.**
