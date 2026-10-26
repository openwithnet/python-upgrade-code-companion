# G3 — Chapter 10 Sections 10.1–10.3 and 10.7 Code-Candidate Inventory (2026-10-26)

Word: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, exact read from `word/document.xml`. **Top-level XML paragraphs only**, zero-based and excluding paragraphs inside tables. No Word or Python source modification.

## Section boundaries checked
§10.1 begins p1418, §10.2 p1756, §10.3 p2156, §10.7 p3907; Chapter 11 begins p4075.

## Extraction result
A conservative regex-based scan flagged **314 code-like *paragraphs***: §10.1 68, §10.2 108, §10.3 121, §10.7 17. These are **NOT 314 verified code blocks nor 314 runnable examples**. Provisional labels: 51 `PROGRAM_CONSTITUENT` (mostly def/class/import markers), 246 `DEPENDENT_EXPRESSION_OR_OUTPUT` (including prints, output and partial lines), 17 `DEPENDENT_SUMMARY_SNIPPET`. Labels reflect a heuristic only, **not manual validation**.

Example: p1444–1462 corresponds to a multi-paragraph calibration calculation and its printed output `[0.0, 1.0, 4.0]`. A `def linear_concentration(` at p1471 continues over several separated paragraphs. Printing a list such as p1462 is expected output, not necessarily an independent Python source statement. False positives and missed lines are possible.

Working CSV `G3_CH10_Sections_10_1_10_3_10_7_CodeCandidates_20261026.csv` includes section, source paragraph, style, provisional label and preceding prose. Each candidate requires neighboring-paragraph and indentation reconstruction before being assigned to an executable program. **No new program execution claimed in this pass.**

## Immediate remaining work
- Delimit complete programs using full Word context, verify block boundaries and expected output.
- Compare the GitHub-connector source bodies byte-wise or with normalized hashes against the previous local transcription, then run exact source files.
- Keep `ch10_pipeline.py` as related C3 calibration material, **not** directly aligned to §10.6.
- G3/G4/G5/G6 remain HOLD.
