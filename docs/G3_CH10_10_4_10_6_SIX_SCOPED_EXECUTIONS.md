# G3 Chapter 10.4–10.6 Six Scoped Word-Derived Executions

Date 2026-10-26. Current Word: v37 G4 Ch09 API Aligned QA. Word positions zero-based top-level paragraphs. Python script `G3_CH10_10_4_10_6_Five_Targets_20261026.py` ran in the local QA environment and produced six passing results in `G3_CH10_10_4_10_6_Six_Scoped_Results_20261026.csv`.

- §10.4.1 pp2680–2731 `FirstOrderModel` + `EulerSolver` + `Simulation`: 0.8, matches printed output.
- §10.4.2 pp2745–2757 `FixedSimulation`: 0.8, reviewer-added expectation (Word does not print this value).
- §10.4.2 pp2765–2789 `ConfigurableSimulation` with injected step dt=0.5: 0.9, reviewer-added expectation (Word does not print this value).
- §10.5.4 pp3340–3370 Euler vs analytic reference: all six formatted stdout lines exactly match the Word display, including t=0..5.
- §10.6.2 pp3571–3605 functional derivative callback Euler: 0.8, matches Word output.
- §10.6.2 pp3613–3634 model bound-method callback: 0.8, reviewer-added expected output; Word code does not print a value.

**Scope**: six *scoped behavioral* checks, not six independently self-contained verbatim Word programs. Class method indentation was reconstructed and shared model/integrator definitions supplied from preceding Word context. The 10.5.4 demonstration used a local semantically equivalent first-order trajectory implementation, not an independently imported verified exact GitHub module. It is a printed-output equivalence check, not whole-source parity. Prior tests in these sections are not recounted here. No Word or repository Python source was changed. G3/G4/G5/G6 HOLD.