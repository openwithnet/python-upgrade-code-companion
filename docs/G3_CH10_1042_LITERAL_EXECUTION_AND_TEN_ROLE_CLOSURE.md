# G3 Chapter 10 — Word §10.4.2 literal execution and remaining ten snippet roles (2026-10-26)

## New execution: the one previously semantic-only dependent unit

Read Word v37 from document.xml, extracting §10.4.2 paragraphs 2799–2807, 2809–2816 and 2818–2832; excluded intervening Korean explanatory prose. Only added `from dataclasses import dataclass`, since Word's `@dataclass` depends on a preceding import. Compiled and executed the **literal extracted** `DerivativeModel`, `StepSolver`, and `Simulation` definitions, then supplied small compliant first-order derivative and Euler/Midpoint test doubles. Verified `Simulation.advance(1.0)` returns **0.8 with Euler** and **0.82 with Midpoint** (k=0.2, dt=1.0). All assertions PASS. This establishes **context-completed Word block runtime behavior**, not independence without prerequisite import or parity with every GitHub source line.

Reproducible local scripts: `check_ch10_1042_literal.py`, extracted source `G3_CH10_1042_WORD_EXTRACT_20261026.py`.

## Ten explanatory/dependent/reuse units

Completed row-level editorial-role audit in `G3_CH10_TEN_ILLUSTRATIVE_REUSE_FINAL_REVIEW_20261026.csv`. Distinctions:
- §10.5.6 abbreviated signed derivative: incomplete pseudocode, intentionally not executable.
- §10.6.1 volts-to-mV: full simple function definition.
- §10.6.2 analytic concentration: full sample with math.exp and expected value.
- §10.6.2 functional derivative/Euler: callback example with import and shown 0.8 output.
- §10.6.2 object-derived Euler: requires the prior `euler_step` definition.
- §10.6.3 wrapper: dependent over-abstraction illustration, not a separate implementation requirement.
- §10.6.3 UniversalProcessor vs DerivativeModel: illustrative interface sketch; the latter requires Protocol import.
- §10.6.4 decay_step: before/after same-name redefinition is intentional, includes pytest example.
- §10.7 two function summaries: reused snippets, no new source file needed.

**Decision:** The last specifically recorded `SEMANTIC_ONLY` unit is now directly executed in context. All ten previously pooled illustrative/reuse rows have precise publication roles. No new independently missing Python program was discovered. This improves the Chapter 10 G3 evidence but **does not prove exhaustive all-format Word block capture or the exact execution of every printed example**; Chapter 10 G3 remains scope-accepted / final HOLD pending editorial signoff. Neither master Word nor source repository calculations were changed.