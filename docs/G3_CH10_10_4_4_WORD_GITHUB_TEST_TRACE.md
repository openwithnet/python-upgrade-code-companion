# G3 — Word §10.4.4 to GitHub tests trace

2026-10-26; source Word v37 G4 QA, zero-based top-level paragraph indexes.

Five Word test examples (p2970–3071) restored as executable pytest code. All five passed. Alongside the existing four tests in `test_ch10_composition_example.py` from the previously reconstructed local GitHub-content copy, **9/9 passed** (Python pytest, local run).

| Word test | Paragraph anchors | Existing GitHub test | Result |
|---|---|---|---|
| first order derivative | 2970–2978 | test_derivative | PASS |
| ConstantDerivative(-0.5) Euler at c=2 dt=1 -> 1.5 | 2982–3006 | **NOT PRESENT** | PASS (Word reconstruction) |
| RecordingSolver injection | 3011–3044 | test_solver_injection | PASS |
| integrated Euler 0.8 | 3050–3059 | test_euler | PASS |
| integrated midpoint 0.82 | 3062–3071 | test_midpoint | PASS |

**Finding:** ConstantDerivative isolates the Euler algorithm from the physical model and is present in Word but not in the GitHub test file. This is a **test-coverage gap**, not a demonstrated implementation defect. Recommended next change subject to QA decision: add the independent test to the repository test file, keep production source unchanged.

Evidence files: `G3_CH10_10_4_4_Word_GitHub_Test_Trace_20261026.csv`, `G3_CH10_10_4_4_Word_And_Repo_9_Tests_20261026.txt`, local test `ch10_source_run/test_word_10_4_4_trace.py`. Existing GitHub-content copy has not been byte-hash-matched to a Git checkout. Word indentation reconstructed. No Word or GitHub source edits in this pass. G3/G4/G5/G6 HOLD.