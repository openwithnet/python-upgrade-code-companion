# Chapter 10 G3 — 50 declaration-bearing Word units, contextual block inventory

2026-10-26. Parsed the actual Word v37 QA document XML and matched the corrected 59-unit G3 registration ranges. This is a **declaration-and-dependency inventory**, not a new run of all 50 Word examples.

**Observed:** 50 of the 59 units include Python `def` / `class` / `import` lines. Grouped by preliminary teaching role:
- 25 teaching-code examples for which standalone/context dependencies remain to be proven;
- 15 educational blocks in §§10.4–10.5 requiring context review;
- 8 illustrative, dependent or abbreviated blocks (including §10.6 design comparisons);
- 2 reused summary function snippets (§10.7).

The categories are **preliminary triage**, not 25 proven standalone programs or 15 failed programs. The CSV contains original Word spans, extracted names/import lines, previous execution status and relationship to repository modules: `G3_CH10_50_Declaration_Blocks_Dependencies_20261026.csv`.

Special cases confirmed: `simulate_euler` runs through Word paragraph 3306; the short `derivative` in §10.5.6 is explanatory; §10.6.3 shows dependent `run_model` and `UniversalProcessor` / `DerivativeModel`; §10.7 reuses `volts_to_millivolts` and `first_order_concentration`. Avoid publishing these as exact corresponding GitHub modules without evidence.

**Gate:** Chapter 10 scoped technical validation remains accepted (local 31/31 tests, source-specific CI success, core Word numerical table checked). Final G3 PASS remains HOLD pending a precise standalone/dependent determination for actual code blocks, with expected outputs and earlier definitions carried into their original context. Neither Word manuscript nor executable GitHub code changed.