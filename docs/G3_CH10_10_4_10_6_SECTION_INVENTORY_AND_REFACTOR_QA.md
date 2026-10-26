# G3 — Chapter 10.4–10.6 Section Inventory and Two New Scoped Executions

Date: 2026-10-26. Source: Word v37 G4 QA, top-level zero-based Document.paragraphs locations.

A 14-region inventory of §§10.4.1–10.6.4 was constructed by reading the actual Word paragraphs. CSV `G3_CH10_10_4_10_6_Section_Inventory_20261026.csv` contains section boundary, role, def/class/import markers, expected output markers and preliminary status. This is **section-level sampling and status inventory, not complete paragraph-by-paragraph classification**.

New local Word-derived checks:
1. §10.6.2 paragraphs 3545–3563: reconstructed `first_order_concentration(1,0.2,5)` matches the Word expected value 0.36787944117144233 using `pytest.approx`; PASS.
2. §10.6.4 paragraphs 3801–3842: pre-/post-refactoring `decay_step` formulas produce the same outputs for four reviewer-selected input sets; nominal `decay_step(1,.2,1)` matches Word test expectation 0.8; PASS.

Working program `G3_CH10_10_6_two_scoped_checks.py` was executed in the current Python environment with return code 0. The four parameter comparisons are one scoped refactoring verification, not four separately authored Word programs; test input combinations beyond the nominal check were reviewer-added. These are reconstructive checks, not verbatim full-document Python programs.

Prior §10.4.3 Euler/Midpoint and §10.4.4 ConstantDerivative tests remain recorded separately and are not counted again. §10.5.5 p3409 states 12 pytest test cases passed in the manuscript; repository `test_kinetics.py` has 12 pytest **parameterized cases** but this audit does not claim verbatim identical test-body sources.

§10.6.3 contains educational anti-patterns (`UniversalProcessor`, filesystem examples) that must not be treated as production programs or validated scientific analyses. §10.6 Word title is Good Design and Over-Abstraction; archived C3 `ch10_pipeline.py` remains a related example, not a proven direct §10.6 implementation.

G3 remains incomplete: formal section-wide exact executable block boundaries, all Word source-to-test trace IDs, unflagged paragraph check and publication rights still outstanding. G4/G5/G6 HOLD. Neither Word master nor Python source was modified.
