# Chapter 12 G3: four further Word source-boundary AST recoveries — 2026-10-27

Source: authoritative Word v37 unchanged, read directly from document.xml. Four of the seventeen still-pending source-boundary contexts have now been recovered as actual original source statement selections, with no prose or printed output inserted. Each source passes Python AST parsing. Selection index lists, exact source text and SHA256 are in `G3_CH12_17_Review_Four_Literal_Word_Source_Recovery_AST_20261027.csv`.

- S122-09 p5167–5215: multidimensional data declaration and the replicate/time/variable axis mean statements, AST PASS.
- S123-06 p5485–5527: experimental scaling and time-scaling with multiline corrected arrays, AST PASS.
- S128-09 p7966–7976: independent pytest import and zero-total rejection test. Prior p7961–7964 belongs to preceding source context, not this new test. AST PASS; pytest not executed.
- S129-06 p8277–8301: refined Euler time step and analytic solution error check; AST PASS with dependencies on earlier `simulate_euler_motion` and `positions_vectorized`; runtime not executed.

Previous count 45 review, 28 previously recovered; four more recovered = **32 source-boundary reviews closed, 13 remain**. Previous 79 heuristic AST-pass contexts remain preliminary. No runtime PASS, no changes to Word or production GitHub code. G3 FULL HOLD; G4-G6 HOLD. Intermediate only; user need not save.