# Chapter 5 C2 — Word / Code Scoped Alignment (2026-10-25)

**Decision: Representative C2 concept alignment CONFIRMED. Full 1:1 manuscript fidelity and public rights NOT PROVEN.**

| Word v37 section | GitHub source or test | Finding |
|---|---|---|
| 5.7.1 interval consumption rates | `calculate_interval_rates` | `-ΔC/Δt`; [1.8, 1.5, 1.2, 0.9] agrees |
| 5.7.1 interval midpoint | `analyze_kinetics` | [0.5, 1.5, 2.5, 3.5] agrees |
| 5.7.2 excerpt | `c2_kinetics_pipeline.py` | function name, arrays, outputs agree; excerpt is NOT entire source file |
| 5.7.2 input contract | `validate_kinetic_data` | 1D real numeric finite ndarray, matching lengths, >=2 points, nonnegative times/concentrations, increasing times |
| 5.7.3 first-order model | `make_first_order_model(10, .2)` | C(t)=10 exp(-0.2 t); t=0..4 predicts 10, 8.1873, 6.7032, 5.4881, 4.4933 (4-decimal rounding) |
| 5.7.3 tests | `tests/test_c2.py` | input integrity, output independence, bad inputs and numerical results covered |

The five observations are *synthetic teaching data*, not measured experimental observations. The parameter k=0.2 is selected for demonstration and is not fitted to those observations. The model prediction for t=4 is 4.4933, while the listed observation is 4.6.

**Limits:** No proof of exact manuscript-text historical reconstruction; user-local environment not independently tested; redistribution rights of `ARCHIVED_CHAPTER_REVIEW_COPY` remain UNVERIFIED. G3, G4, G5, G6 remain open. Do not edit Word warnings or source code on the strength of this check.
