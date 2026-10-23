# Chapter 10 — Code Companion

**Executable release-candidate entry point:** `original_package/ch10_alignment_QA/verified_suite/ch10_pipeline.py`.

Word v37 section **10.1.3** uses `run_analysis(measurements, model)` to teach the orchestration idea with a single model. The runnable companion uses a **mapping of named calibration models** and returns an `AnalysisReport`; it is not a literal copy of that introductory snippet. Keep both at their distinct teaching levels.

Other executable files in `verified_suite/` include `ch10_composition_example.py` (derivative `dc/dt`) and `kinetics.py` (consumption rate `-dc/dt`). Their signs and contracts differ intentionally.

**Test from `verified_suite` directory:**

```sh
python -m pytest -q --import-mode=importlib
```

See `../../docs/CH10_CANONICAL_CONTRACT_DECISION.md` for the full decision, Chapter 13 name distinction, provenance, and remaining validation gates.
