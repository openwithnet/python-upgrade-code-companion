# G3 Chapter 10.1 — Context Classification of All 68 Automatically Flagged Paragraphs

Date: 2026-10-26. Source: Word v37 G4 QA, zero-based top-level paragraphs. Reviewed all 68 §10.1 rows from the prior candidate inventory against nearby Word source/example structure.

- 62: `PROGRAM_CONSTITUENT` lines belonging to **8 logical example groups**, not 62 separate programs.
- 3: `EXPECTED_OUTPUT` at p1462, p1494 and p1653.
- 2: `KOREAN_PROSE_FALSE_POSITIVE` at p1720 and p1724.
- 1: `EXPLANATORY_NOTATION` at p1643.

Groups: P01 procedural calibration p1444–1460; P02 functional calibration p1471–1492; P03 model class p1504–1525; P04 processing pipeline p1570–1585; P05 voltage conversion p1595–1602; P06 quadratic model p1611–1625; P07 Celsius conversion p1664–1667; P08 orchestration fragment p1698–1707.

**Evidence:** `G3_CH10_10_1_68_Candidates_Context_Classified_20261026.csv` (one row per flagged paragraph). Cross-reference the prior four-program and additional-four §10.1 audit notes for **scoped execution**, noting reviewer-supplied input in some examples and synthetic dependencies for P08. Output, prose and notation were not run as standalone Python. Candidate detection can miss unflagged code lines; this marks 68 flagged rows as classified, NOT complete independent proof of every code block in §10.1.

Remaining candidates in §10.2: 108, §10.3: 121. §10.7's 17 previously manually classified. Thus §10.1+§10.7 classify 85 of the original 314 candidates, leaving 229 candidate paragraphs for contextual classification, excluding any unseen missed lines. No new execution or Word/source edits; gates G3–G6 HOLD.