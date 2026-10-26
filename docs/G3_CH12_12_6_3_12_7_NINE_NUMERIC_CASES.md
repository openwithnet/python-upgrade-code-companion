# G3: Chapter 12.6.3 and 12.7.1–12.7.2 — Nine verified numerical cases

Date: 2026-10-26. Source is current Word v37 G4 QA manuscript.

Nine scoped scenarios were reconstructed from Word paragraphs and executed in Python. All nine met their expected checks. The reconstruction reassembled multi-paragraph function indentation; the cases are not claimed to be nine independently runnable Word blocks.

| Case | Word paragraph range | Result |
|---|---|---|
| Euler sequential time integration | 7080–7134 | `[1. 0.8 0.64 0.512 0.4096 0.32768]` as Word output, PASS |
| Euler nonnegative contract | 7082–7123 | `ValueError` for `dt*k>1`, PASS |
| Euler rejects boolean step count | 7098–7102 | `TypeError`, PASS |
| Independent initial states, sequential time loop | 7146–7156 | `[0.817073 1.634146 2.451218]`; independently checked against closed-form recurrence, PASS |
| Conditional `np.where` values | 7167–7179 | `[2. 1. 0. 4.]`, PASS |
| Eager invalid logarithm evaluation | 7184–7192 | Expected runtime warning from `np.log` on negative input, PASS |
| `np.vectorize` function application | 7200–7213 | `[2. 5. 10.]`, PASS |
| Explicit `float32` dtype | 7282–7289 | `float32`, PASS |
| Floating-point cancellation | 7391–7399 | `0.0` vs mathematical expectation 1.0, PASS |

**Validation scope:** 9/9 means each selected behavioral contract passed, including 2 expected exceptions and 1 expected warning. Not every case has literal Word stdout. The warning and negative-input cases are intentionally nonstandard behavior tests; they should not be counted as clean arithmetic output matches.

One case adds a reviewer assertion comparing the three-initial-state Euler loop against the recurrence `(1-dt*k)**10` for each initial concentration; this assertion was not part of the printed Word sample. Numerical library version/runtime details remain in the working QA execution environment, and these are not universal timing or accuracy guarantees.

CSV evidence: `G3_Ch12_12_6_3_12_7_Nine_Cases_20261026.csv`. Previous Chapter 12 scoped total was 86 cases; with these nine it is **95 case checks**, not 95 separate programs or whole-chapter coverage. No Word master or GitHub Python code changed. G3/G4/G5/G6 stay HOLD.