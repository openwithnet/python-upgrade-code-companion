# G3 Chapter 10 — Solver, Rate-Law and Analysis-Pipeline Interface Audit

Date: 2026-10-26. Scope: direct examination of three repository files, alongside previously checked Word Chapter 10 examples. **Source API comparison, not a new independently executed test run.**

| Source | Chapter teaching role | Essential interface | Relation to Word |
|---|---|---|---|
| `ch10_composition_example.py` | §§10.3–10.4 one-step composition | `DerivativeModel.derivative(c)` is signed dc/dt; `StepSolver.step(c,model,dt)`; `EulerStep`, `MidpointStep`, `Simulation.advance` | Direct semantic comparison with Word Euler/Midpoint step examples. Prints Euler 0.8, Midpoint 0.82 for c=1,k=.2,dt=1 |
| `kinetics.py` | §10.5 first-order kinetics | `RateLaw.rate(c)` is nonnegative **consumption** rate; `simulate_euler` updates c as c - dt*rate(c) | Word §§10.5: `RateLaw`, `FirstOrderRate`, `Trajectory`, `simulate_euler`. Numerical and validation semantics align in scoped prior verification |
| `ch10_pipeline.py` | §10.6 C3 orchestration | `CalibrationModel.predict_concentration`, `SignalMeasurement`, `analyze_measurements`, `run_analysis` | Calibration/units/report workflow, NOT an alternative kinetics integrator |

## Critical conceptual/API boundary
For first-order decay, `dc/dt=-k*c` and positive consumption rate `r(c)=k*c` are mathematically compatible **only if the sign convention is handled correctly**. The two source modules should not be merged by simple function renaming; passing the positive rate directly to a signed-derivative Euler step would make concentration increase incorrectly.

## Concrete source contracts
- `ch10_composition_example.py`: validates `FirstOrderModel.k` (finite, nonnegative); minimal `EulerStep`/`MidpointStep` do **not** apply all of `kinetics.py`'s input checks. This is a pedagogical one-step example.
- `kinetics.py`: `nonnegative_finite` rejects bool, nonfinite and negative inputs, `simulate_euler` rejects invalid step count, nonpositive dt, and Euler steps producing negative concentration. `exact_first_order` computes analytic comparison.
- `ch10_pipeline.py`: validates measurements list, mapping of named calibration models, and callable `predict_concentration`; supports linear and quadratic calibration reports. No solver-step API. Includes its own unit conversion path through C3 modules.

## Provenance, verification and release
All three paths are `ARCHIVED_CHAPTER_REVIEW_COPY` and remain candidate/not frozen. Prior Word-based six checks used a reviewer-provided helper for an omitted `nonnegative_finite`; they are not proof of all GitHub modules passing every edge case. Existing CI results must be cited with their earlier commit scope. This audit is a source inspection and semantic mapping only, no Python source modification or new execution PASS.

**Next:** use the existing test modules `test_kinetics.py`, `test_ch10_composition_example.py`, `test_ch10_pipeline.py` to compare their specific contracts, and check their corresponding Word source spans. G3/G4/G5/G6 remain HOLD.
