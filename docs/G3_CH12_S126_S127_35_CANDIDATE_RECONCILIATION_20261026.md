# G3 Chapter 12 §§12.6–12.7 — last 35 REVIEW candidates (2026-10-26)

Word source: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, direct OOXML top-level paragraph indices. Baseline: `G3_CH12_889_After_S124_S125_Last10_Closure_20261026.csv`.

## Existing evidence retained
`G3_CH12_12_6_3_12_7_NINE_NUMERIC_CASES.md` documents 9 scoped prior checks (Euler solver, invalid steps, multi-initial conditions, `np.where`, log warning, `np.vectorize`, explicit float32, cancellation). `G3_CH12_12_7_3_REDUCTION_7_CASES.md` documents 7 scoped aggregation cases. These were read and **not rerun**.

## Actual newly executed Word-native contexts
Six complete contexts compiled and executed with selected direct Word paragraphs:
1. p6873–6897 with 6907–6910: list comprehension vs NumPy, exact numerical `assert_allclose` passes; performance times merely informational, hardware-dependent, not exact Word expected times.
2. p7273/7275/7277: `float64` matches Word p7279.
3. p7302: `False` for `0.1+0.2 == 0.3` matches p7304.
4. p7311/7313/7314: machine epsilon strings exactly `1.1920929e-07` and `2.220446049250313e-16`, matches p7316–7317.
5. p7324–7337 with NumPy import: `4000000`, `8000000`, exactly p7339–7340.
6. p7348–7353 with NumPy import: `int8`; literal source executed, no separate printed output reference claimed for this dtype example.

**6/6 scoped contexts PASS**, the stated explicit outputs agree with Word. Exact extracted source SHA256, indices and actual stdout: `G3_CH12_S126_S127_Six_Word_Blocks_20261026.csv`.

## Two dependent expressions, not runnable independent programs
- p6924: `y = 2.0 * x + 1.0`, a general intermediate-array illustration with no local `x` binding. Do not assert a standalone PASS.
- p7221: beginning of pairwise broadcast difference illustrating quadratic memory growth; actual million-by-million allocation would require approximately 8 TB just for float64 output, so no such allocation was attempted or warranted. This is a conceptual example, not an execution gap that should be solved by huge allocation.

## Ledger result
Among original 35 REVIEW paragraph positions: 33 code/continuation positions linked to the six executed contexts, and two dependent educational illustrations role-classified. Full original 889 candidate rows retained. `REVIEW` count **63 → 28**; §§12.1–12.7 now have zero unclassified candidate paragraphs. Residual: §12.8 four, §12.9 twenty-four. This does not imply complete formal G3 certification of all source code blocks, and historical case overlap remains distinguished.

Updated register: `G3_CH12_889_After_S126_S127_35_Reconciliation_20261026.csv`.

Production Word and GitHub Python source unchanged; Chapter 6/10 tests not repeated. Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
