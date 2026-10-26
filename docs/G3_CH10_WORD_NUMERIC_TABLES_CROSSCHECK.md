# G3 Chapter 10 — Word Numeric Tables and Test-Plan Cross-check

Date: 2026-10-26. Read Word v37 G4 QA document and anchored every table by its preceding top-level paragraph.

Chapter 10 contains 13 Word tables (indices 10–22). Most are conceptual, contract, design, or comparison tables.

Numerical table index 13, after paragraph 3371, has 6 times (0–5) and 12 displayed numerical results. All 12 match independent computations to 6 decimal places, for C0=1, k=0.2, dt=1. Euler values: 1, .8, .64, .512, .4096, .32768. Analytic values: 1, .818731, .670320, .548812, .449329, .367879.

Test-plan table index 14, after paragraph 3408, lists 10 descriptive test contracts (rate, zero-step, Euler, analytic, zero rate, invalid coefficients, boolean coefficient, excessive dt, boolean steps, convergence). These ten entries were **not** re-executed as new tests. Existing original-blob pytest verification remains separate.

Table index 24 (Euler/Midpoint/analytic five-second comparison) follows paragraph 4283, which is Chapter 11; it must not be counted as a Chapter 10 table. Chapter 11 begins paragraph 4075.

Evidence CSV: G3_CH10_Word_Tables_Numeric_And_Contracts_20261026.csv. Reproduction script: check_ch10_tables_20261026.py.

No Word or GitHub Python source edits. Numerical-table values PASS; Chapter 10 G3 entire chapter still HOLD, likewise G4/G5/G6.