# Chapter 9 C3 — Word v37 / GitHub Scoped Alignment (2026-10-25)

**Decision: Numerical calculations and boundary-validation structure aligned in Word §§9.4–9.5; one API-name editorial inconsistency identified. Chapter-wide 1:1 and third-party rights NOT PROVEN.**

## Verified correspondence

| Word paragraph/section | GitHub source | Evidence |
|---|---|---|
| §9.4.2 tolerance example | `test_c3_pytest.py` | `math.isclose(..., rel_tol=1e-12, abs_tol=1e-12)` and `pytest.approx` appropriate for numerical tests |
| §9.4.3 verification vs scientific validation | calibration equations | Example c=3 -> s=19 for quadratic; linear inverse gives c=9: computational correctness does not guarantee model suitability |
| §9.5.1 units | `c3_validation.SignalMeasurement.as_millivolts` | 0.009 V -> 9.0 mV; only V/mV accepted, nonfinite or overflow rejected |
| §9.5.2 batch calculation | `analyze_measurements`, `analyze_many` | [0.001 V, 3 mV, 0.009 V] -> [1,3,9] mV; linear [0,1,4], quadratic [0,1,2] |
| §9.5.3 equivalent units | `test_c3_validation.py` | 0.009 V and 9 mV both yield 4 under LinearCalibration(2,1) |
| §9.5.3 additional boundaries | `test_ch09_additional.py` | empty batch, changed intercept, just-below boundary, negative coefficients, input order, immutability |

## Editorial issue discovered

In Word paragraph 1349 (§9.5.2), the text says a model object provides `predict()`, but the actual `CalibrationModel` Protocol and both implementations define **`predict_concentration(signal)`**. Correct the explanation to the actual API name in the next controlled Word revision; do not change source method names.

## Test count caution

Word §9.5.3 states a historic 32 baseline plus 10 additional (42 total) passing tests. Those are **historical claims**, not equivalent to the 30 chapter-entry CI checks reported by Run `40140880013`. Pytest parametrization yields a different granularity from raw test function counts. The present examination verifies source assertions and cross-consistency, **not a freshly executed 42-case standalone pytest run**. Keep historical wording attributed until a matching test report is produced.

## Scope and release

- Chapter 8 and Chapter 9 both contain C3 calibration files; their source identity/duplication is not an approval to merge directories without checking test imports.
- `SignalMeasurement` checks numeric units and finite values; it does **not** establish the physical units or experimental validity of calibration coefficients, experimental uncertainty, or limit of detection.
- Source provenance: `ARCHIVED_CHAPTER_REVIEW_COPY`; redistribution rights **UNVERIFIED**.
- Retain G3/G4/G5/G6 HOLD outside this scoped finding. No Python files changed.

Source files: `chapters/chapter09/original_package/{c3_calibration.py,c3_validation.py,test_c3_pytest.py,test_c3_validation.py,test_ch09_additional.py}`.
