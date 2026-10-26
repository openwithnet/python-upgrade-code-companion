# G3 Chapter 10 — Ten Focused Word–GitHub API Contract Spotchecks

Date: 2026-10-26. Source: Word v37 G4 QA top-level paragraph excerpts and eight GitHub blob-verified modules already fetched into the exact-source local directory.

**Executed 10 selected assertions; 10/10 PASS**, using exact original GitHub module code in the verified directory. Reviewer harness: `check_ch10_contracts.py`. Results CSV: `G3_CH10_Contract_Spotchecks_20261026.csv`.

Representative pairs and adjudication:

- Word 1471–1492 procedural/function linear calibration vs `LinearCalibration(2,1)`: same formula/result 4, distinct API.
- Word 1504–1525 `LinearModel` vs `LinearCalibration`: same ordinary result 4; GitHub implementation explicitly rejects zero slope (`ValueError`), unlike plain illustrative Word class, so **not equivalent full contract**.
- Word 1611–1625 quadratic class vs `QuadraticCalibration`: same output 2 but different class name and validation.
- Word 1595–1602 volts helper vs `SignalMeasurement.as_millivolts()`: same 9mV nominal result, but GitHub requires a value/unit object.
- Word 2055–2067 measurement analysis vs `c3_validation.analyze_measurements`: matches both V/mV conversion and linear calibration resulting [4,4].
- Word 2252–2266 derivative and 2379–2413 Euler/Midpoint vs `ch10_composition_example`: -0.6, 0.8, 0.82, scoped semantic agreement.
- Word 3181–3303 positive consumption-rate kinetics via `kinetics.simulate_euler`: after 3 steps 0.512. The derivative-style solver uses a negative signed derivative, not positive consumption rate.

**Limit**: The 10 assertions run the GitHub modules with selected values and reviewer-specified expected results; they do not execute literal extracted Word code in this new pass. Word spans were read and compared by mathematical/API inspection. The results establish scoped agreement and explicit contract differences, not exact text equivalence of 59 units. `ch10_pipeline.py` remains C3-related, not a direct implementation of Word §10.6 (design/over-abstraction).

No source or Word edits. G3 Chapter 10 NOT APPROVED; G4/G5/G6 HOLD. Remaining: missed-code completeness check, explicit classification of teaching snippets vs runnable repository candidates, and publication/provenance decision.