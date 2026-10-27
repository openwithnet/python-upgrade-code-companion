# Chapter 12 G3 Tier B — original Word source boundaries

Date: 2026-10-27. Read-only canonical manuscript: Word v37, direct OOXML top-level paragraph indices. No past numerical computations repeated.

Nine selected source components were extracted with original indentation and individually parsed using Python AST; **9/9 AST PASS**. These are components selected to cover the seven previously identified tier-B parent topics, not nine independent executable programs:

| Component | Original Word paragraphs | Prior scope |
|---|---|---|
| Multiple initial Euler states | 7146,7148,7150,7151,7153,7154,7156 | Nine numeric cases |
| np.where values | 7167,7169,7171–7175,7177 | Nine numeric cases |
| np.where eager-log warning | 7167,7184,7186–7190 | Nine numeric cases; expected warning |
| np.vectorize and direct expression | 7167,7200–7201,7203–7205,7207,7209,7213 | Nine numeric cases |
| float32 dtype | 7167,7282–7285,7287 | Nine numeric cases |
| floating-point cancellation | 7391–7392,7394,7396 | Nine numeric cases |
| reduction addition-order demonstration | 7453–7455,7457–7458 | Seven reduction cases |
| motion readability loop | 8404,8406–8408 | Dependent snippet: input definitions required |
| motion array expression | 8395–8397 | Dependent snippet: input definitions required |

Working CSV `G3_CH12_TierB_Word_Source_Boundary_20261027.csv` contains each source SHA256, exact paragraph IDs and AST result. **Static parse PASS is not runtime verification**. For the first seven blocks, previous scoped numerical QA claims retain their own evidence; byte-for-byte identity with previously executed reconstructed source was not asserted. The last two need prior setup to become runnable and should not be counted as failed programs.

Next gate: reconcile complete Word source/setup/output of remaining tier-B demonstrations and historical QA identity; explicitly join reduction cases and motion performance results without benchmarking timing thresholds. Full Chapter-12 executable block manifest remains open. Chapter 12 G3 FULL HOLD, G4/G5/G6 HOLD. Word and production GitHub code unchanged. Intermediate audit; user need not save.