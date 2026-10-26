# G3 — Chapter 10.1/10.2 Three Remaining Scoped Checks

2026-10-26. Word v37, zero-based top-level paragraph positions.

- Word §10.2 p1842–1855: `analyze_fixed_model(9.0)` returns 4.0 — PASS.
- Word §10.2 p2055–2067: `analyze_measurements` with 9mV and .009V using `LinearCalibration(2,1)` returns [4.0,4.0] — PASS.
- Word §10.1 p1698–1707: `run_analysis` delegates to real `analyze_measurements` and produces [4.0] for .009V input — PASS.

Executed the reconstructed Word functions with the prior local C3 source-copy environment, not reviewer synthetic `Demo` objects. These are three scoped behavior checks **with reviewer-selected inputs**; no direct Word printed-output claim for these calls. Local dependency files were previously proven not byte-identical to GitHub blobs. Working evidence: `G3_CH10_10_1_10_2_Three_Gap_Checks_20261026.csv` and `G3_CH10_10_1_10_2_three_gap_checks.py`.

These results address previously registered execution gaps; they do not establish Chapter 10 whole-manuscript G3 acceptance, exact GitHub-source parity, or rights clearance. Word and GitHub calculation sources unchanged. G3/G4/G5/G6 HOLD.