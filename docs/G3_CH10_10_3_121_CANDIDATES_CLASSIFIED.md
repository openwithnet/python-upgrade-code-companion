# G3 Chapter 10.3 — 121 Candidate Paragraph Classification

Date: 2026-10-26. Source: current Word v37 G4 QA and prior candidate inventory. Paragraph numbers are zero-based top-level Word paragraphs.

**All 121 auto-flagged §10.3 paragraphs have been context-assigned**: 117 code constituents, 2 explanatory API notations (p2511,p2515), 1 printed output (p2223), 1 Korean prose false positive (p2349). This is a classification of previously flagged lines, not guaranteed exhaustive capture of unflagged Word code.

Twelve context groups:
B01 2193–2223 decay function; B02 2252–2264 signed derivative; B03 2280–2310 Euler callback; B04 2316–2322 lambda callback; B05 2328–2349 dataclass callback; B06 2358–2368 nonlinear derivative; B07 2379–2410 Euler/Midpoint; B08 2424–2444 initial-condition data; B09 2452–2468 Trajectory contract; B10 2485–2499 decay step; B11 2511–2515 explanatory notation; B12 2533–2563 simulation composition.

**Prior scoped executions**: B01,B02,B03,B07,B09,B12 (6 checks). B04,B05,B06,B08,B10 lack independent execution evidence in this section. B11 is explanatory notation, not an executable program. Do not count dependent invocation fragments or explicit printed output as independent programs.

Working evidence file: `G3_CH10_10_3_121_Candidates_Context_Classified_20261026.csv`. Together with prior §10.1 68, §10.2 108 and §10.7 17 classification, **314/314 originally flagged candidate paragraphs** now have an assigned context class. This does NOT establish that every real code span in the whole Chapter 10 was flagged, nor Chapter 10 G3 PASS; §§10.4–10.6 have separate incomplete audits.

No new executions or Word/Python code changes. G3/G4/G5/G6 HOLD.
