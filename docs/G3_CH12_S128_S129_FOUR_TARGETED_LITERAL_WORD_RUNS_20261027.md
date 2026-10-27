# Chapter 12 G3 — targeted literal Word runtime checks for §12.8 and §12.9 (2026-10-27)

Word v37 was read directly and not modified. Four selected educational contexts received **new, scoped literal Word source executions**, rather than re-running historical PASS cases.

- `S128-02`: original expression matrix setup plus sample totals and gene means — AST / runtime / numeric assertion PASS.
- `S128-05`: original row-wise percent normalization, sum-to-100 contract, and column-wise counterexample — AST / runtime / numeric assertion PASS. This is pedagogical percentage normalization, not a certified RNA-seq normalization method.
- `S128-06`: original log2(x+1) calculation, explicit Python loop, NumPy equivalent and allclose assertion — AST / runtime / numeric assertion PASS.
- `S129-10`: original kinematic initial conditions, `positions_vectorized` definition, and invariant `v² = v0² + 2a(x−x0)` at five times — AST / runtime / assert_allclose PASS, maximum absolute difference zero for this example.

Exact original Word paragraph indices and outcomes are captured in `G3_CH12_S128_Literal_Word_Targeted_Runtime_20261027.csv` and `G3_CH12_S129_Physical_Invariant_Literal_Word_Runtime_20261027.csv`. The first three run with the common original §12.8 Word dataset setup, the fourth with its upstream Word function and initial conditions. These are scoped checks and do not establish full 124-context run PASS.

**Release blocker persists:** §12.8 p7660 separately contains physically concatenated Python lines and is a literal Word-source SyntaxError. Its distinctly labeled reconstruction has matched printed results, but canonical Word v37 has not been edited. Other QA-evidence gaps remain.

Chapter 12 G3 FULL HOLD / IN PROGRESS, G4-G6 HOLD. No production Word or GitHub Python changes. Internal audit; no user archival needed.