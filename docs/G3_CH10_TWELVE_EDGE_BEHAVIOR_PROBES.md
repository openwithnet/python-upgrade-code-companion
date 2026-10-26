# G3 Chapter 10 — Twelve Edge-Case Behavior Probes (2026-10-26)

**Execution method:** Verified the GitHub contents of `kinetics.py` and `ch10_composition_example.py`, then retyped equivalent function bodies into an isolated Python probe and executed 12 scenarios. **This is not a verbatim GitHub checkout/test run**, and no `ch10_pipeline.py` cases were included. Working evidence: `G3_CH10_Edge_12_Scoped_20261026.csv`.

| Module | Scenario | Observed | Classification |
|---|---|---|---|
| kinetics | NaN dt | ValueError | correct rejection |
| kinetics | negative dt | ValueError | correct rejection |
| kinetics | negative steps | ValueError | correct rejection |
| kinetics | NaN c0 | ValueError | correct rejection |
| kinetics | infinite external model.rate | ValueError | correct rejection |
| kinetics | negative external model.rate | ValueError | correct rejection |
| kinetics | time overflow | ValueError | correct rejection |
| kinetics | k*c rate overflow | ValueError | correct rejection |
| composition | negative dt | returns 1.2 | actual behavior; no validation |
| composition | NaN initial state | returns NaN | actual behavior; no validation |
| composition | solver=None | AttributeError | raw protocol failure |
| composition | negative initial state in midpoint | returns -0.82 | actual behavior; no validation |

**Interpretation:** 8/8 kinetics negative tests passed their explicit rejection expectations. 4/4 composition probes matched current implementation behavior, **not a claim that its validation coverage is adequate**. A new requirement to reject invalid values would require an explicit educational/API decision; don't silently modify the teaching sample. No observed kinetics defect in this scoped run. No Word master or GitHub source changed.

Prior Chapter 10 test-review documentation did not run code and must not be counted as execution. G3/G4/G5/G6 remain HOLD.