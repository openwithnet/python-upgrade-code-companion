# G3 Chapter 10.1 — Four additional executed checks

Date: 2026-10-26. Word paragraph anchors (zero-based): 1595–1602, 1611–1625, 1664–1667, 1698–1707.

Four reconstructed examples executed successfully: voltage conversion yielded 9.0, quadratic model yielded 2.0, Celsius to Kelvin yielded 273.15, and an orchestration demonstration yielded [0.0, 1.0, 4.0]. Only the voltage case contains a direct Word assert. Other expectations and the last case's required dependencies were supplied by the reviewer; these are scoped behavior checks, not literal Word printed-output matches.

Evidence files in working QA directory: G3_CH10_10_1_Additional_4_Cases_20261026.csv and verify_ch10_1_more.py. These four do not duplicate four earlier Chapter 10.1 verified programs. No source or Word changes. Gates G3–G6 remain pending.