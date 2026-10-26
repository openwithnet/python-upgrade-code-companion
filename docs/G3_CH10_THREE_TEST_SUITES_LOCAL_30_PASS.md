# G3 Chapter 10 — Reconstructed Repository-Content Pytest Run

Date: 2026-10-26.

## Method and environment

Source code and three original test definitions were read from GitHub connector paths beneath `chapters/chapter10/original_package/ch10_alignment_QA/verified_suite/`. A **manually transcribed execution copy** of five Python modules and three test modules was written under `/mnt/data/python_upgrade_qa/ch10_source_run/`. This is NOT an authenticated Git checkout or verified byte-for-byte mirror; formatting and module-only boilerplate could differ. Network checkout of the private GitHub repo was unavailable in the container. Existing GitHub original tests were replicated into this isolated execution directory.

Runtime: Python 3.13.5, pytest 9.0.2. Command: `python -m pytest -q -rA test_kinetics.py test_ch10_composition_example.py test_ch10_pipeline.py`

## Results

- `test_kinetics.py`: 12/12 parametrized cases PASS
- `test_ch10_composition_example.py`: 4/4 PASS
- `test_ch10_pipeline.py`: 14/14 PASS
- **Total 30/30 PASS, 0 failures, 0 errors** (0.16 s pytest reported)
- Working output: `G3_CH10_RepoContent_ThreeTests_20261026.txt`

The three components are distinct: derivative-based solver, positive-consumption-rate kinetics, and C3 calibration pipeline. The last is NOT proved to correspond to Word §10.6; that previously incorrect mapping remains explicitly corrected. Test success does not imply total Chapter 10 manuscript G3 coverage, unused error paths correctness, scientific validity or rights clearance.

## Remaining gating work

1. Compare transcribed files with official GitHub bytes (checksum or verified checkout) before declaring original-file test PASS at this source revision.
2. Classify remaining Word §§10.1–10.3 and §10.7 dependent fragments; map true runnable samples and expected outputs.
3. G3 overall / G4 / G5 / G6 remain HOLD. No changes to GitHub executable files or Word master.
