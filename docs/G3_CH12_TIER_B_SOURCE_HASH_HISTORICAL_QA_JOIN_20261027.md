# Chapter 12 G3 — Tier B literal source identity and prior QA evidence link (2026-10-27)

Canonical input: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, direct OOXML top-level paragraphs, unchanged. Re-extracted the exact nine selected source components documented in `G3_CH12_TIER_B_WORD_SOURCE_BOUNDARY_STATIC_AUDIT_20261027.md` and recalculated SHA-256 of their Word paragraph text.

**Source identity: 9/9 SHA-256 matches the previous static audit.** This demonstrates integrity of the current Word-selected snippets against the previous *static extraction*, not identity with the older historical reconstructed code actually executed.

**Historical evidence links:** seven components (multiple Euler initial conditions, `np.where` values, expected log warning, `np.vectorize`, float32 dtype, cancellation, order-dependent reduction) correspond to the prior `G3_CH12_12_6_3_12_7_NINE_NUMERIC_CASES.md` and `G3_CH12_12_7_3_REDUCTION_7_CASES.md`. Their existing scoped execution results are retained: warnings are expected warning contracts, and Word stdout applies only where explicitly printed. The two motion readability expressions are dependent snippets requiring `times`, `x0`, `v0`, `a`, not independently runnable examples; neither is declared FAIL.

Detailed nine-record intermediate evidence with Word indices, static source SHA, matching result, output or warning reference and gate: `G3_CH12_TierB_Exact_Source_Expected_QA_Evidence_20261027.csv`.

**Gate limitations:** This is documentary/static comparison: no new numerical tests were run; it does not prove older execution bytes matched current literal Word source or that Chapter 12's complete block inventory has been certified. Tier-B literal source integrity PASS; historical behavior QA in its prior scope PASS; complete source-to-execution attribution PARTIAL; G3 FULL HOLD / G4-G6 HOLD.

No Word, OMML or GitHub executable Python modifications. Intermediate audit, user need not save.