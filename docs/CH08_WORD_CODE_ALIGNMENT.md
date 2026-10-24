# Chapter 8 C3 — Scoped Word / Code Alignment (2026-10-25)

**Decision:** Representative Chapter 8 §§8.3–8.5 C3 interface/calibration computations agree with the archived source and test code. **Not** whole-chapter 1:1 source reconstruction, user-local validation or rights clearance.

| Word section | Repository implementation / test | Finding |
|---|---|---|
| §8.3.3 runtime contract | `finite_real`, model constructors | rejects booleans, strings, nan/inf, invalid positive-coefficient constraints, and signals below intercept |
| §8.4.1 common operation | `CalibrationModel(Protocol)` | one method `predict_concentration(signal)`; `analyze_signal` delegates |
| §8.4.2 linear | `LinearCalibration(slope=2,intercept=1)` | c=(s−1)/2; signal 9 -> c=4 |
| §8.4.2 quadratic | `QuadraticCalibration(coefficient=2,intercept=1)` | c=sqrt((s−1)/2); signal 9 -> c=2 |
| §8.4.3 batch | `analyze_many([1,3,9],model)` | linear [0,1,4], quadratic [0,1,2] |
| §8.4–8.5 state/abstraction | frozen dataclasses and Protocol | parameter immutability and replaceable implementations verified |
| §8.4.3 error processing | list comprehension over `analyze_signal` | invalid item raises; no partial list returned |
| §8.4.3 tests | `test_c3_calibration.py` | 16 `test_*` methods for numeric, invalid inputs, immutability, structural substitution |

**Scientific scope:** The two models are educational *dimensionless* inverse-response curves and have **not** been fitted to physical calibration measurements. Validity under real concentration units and experimental uncertainty is not established.

**Contract nuance:** The Python `CalibrationModel` Protocol only specifies the method signature. It does **not** enforce a finite nonnegative return for third-party structural implementations; `analyze_signal()` forwards output unchanged. The built-in `LinearCalibration` and `QuadraticCalibration` validate those properties. Word §8.4.1 expresses the intended common *semantic* contract, not a runtime guarantee for arbitrary objects; this distinction should be maintained.

**CI evidence:** Windows/Miniconda Chapter 8 job was included in GitHub Actions run `40140880013` (30/30 overall). Code is currently `ARCHIVED_CHAPTER_REVIEW_COPY` (candidate only). Source rights remain unverified.

**Not proven:** all manuscript paragraphs to code file in byte-perfect 1:1 form, historical original-source provenance, all compatible models meeting semantic contract, third-party redistribution rights. G3 G4 G5 G6 remain open. No source or Word edits performed.

**Files:** `chapters/chapter08/original_package/Chapter_08/c3_calibration.py`, `test_c3_calibration.py`.
