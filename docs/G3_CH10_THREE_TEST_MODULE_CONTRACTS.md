# G3 — Chapter 10 Three Test-Module Contract Review (2026-10-26)

**Evidence**: Directly inspected the current contents of `test_kinetics.py`, `test_ch10_composition_example.py`, and `test_ch10_pipeline.py` under `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite`. This audit reviews test assertions and intended contracts; it is **not a new local test execution**.

## Distinct test contract coverage

| Code module | Checked tests / intended behavior | Main caution |
|---|---|---|
| `kinetics.py` | positive consumption rate `r(3)=.6` at k=.2; `steps=0` retains initial data; 3-step Euler values (1,.8,.64,.512); exact exp(-1); k=0 keeps concentration 3; invalid negative/NaN/Inf/bool k rejected; too-large dt raises ValueError; boolean steps rejected; smaller step gives smaller error at t=5 | `rate(c)` is positive **consumption rate**; do not pass it as a signed derivative |
| `ch10_composition_example.py` | signed derivative `-.6`; Euler .8; Midpoint .82; injected `RecordingSolver` receives model, dt, state and returns 7.5 as controlled | A tiny educational solver without `kinetics.py`'s full validation; `RecordingSolver` is a double, not a physical model |
| `ch10_pipeline.py` | linear concentrations (0,1,4), quadratic (0,1,2); empty samples produce empty result; empty models, invalid names, wrong measurement elements and containers, bad models rejected; errors propagated; frozen report; input unchanged; V/mV conversion and insertion-order model outputs | This is a C3 calibration report pipeline, **not** numerical integration |

### Word alignment and residual questions

Word §§10.3–10.5: rate-law, solver steps and Euler trajectory relate to the composition and kinetics modules; Chapter 10 §10.6 relates to C3 calibration orchestration. Previous six Word-derived behavior checks used reviewer-provided helper definitions, so those checks do not certify a fully independently executable Word program. Current test assertions were examined as repository evidence; exact current Word section-to-test traceability and full corpus coverage remain unfinished.

### CI context

GitHub Actions workflow run [40182527282](https://github.com/openwithnet/python-upgrade-code-companion/actions/runs/40182527282) now reads `completed / success` at source/hash commit `dc450b87727f8618e91f9b0fdf5510ed71969a6a`. This clears **that earlier Linux-head pending status**, not a new Windows CI result and not a promise of any later changes. Repo test files still have `ARCHIVED_CHAPTER_REVIEW_COPY` provenance / `EXCLUDE_FROM_PRODUCTION` role. Exclusion from production does not imply tests are unneeded in a private QA repository.

**No source or Word edits.** G3 overall, G4, G5 and G6 remain HOLD.
