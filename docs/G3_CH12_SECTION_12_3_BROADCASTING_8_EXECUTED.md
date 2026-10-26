# G3 — Chapter 12.3 Broadcasting Eight Direct Execution Checks (2026-10-26)

**Scope:** Eight representative Word-extracted examples from §§12.3.1–12.3.2 of the v37 G4 QA manuscript. All eight Python subprocesses return zero and their stdout matches explicit Word expected-output paragraphs. No Python source or Word master changed.

| Example | Word code paragraphs (zero-based) | Expected output | Result |
|---|---|---|---|
| scalar addition | 5380,5382,5384,5386 | 5388 | PASS |
| broadcast row vector | 5413–5417,5419,5421,5423 | 5425–5427 | PASS |
| broadcast_shapes | 5436–5441 | 5443 | PASS |
| zero-size array shape | 5454,5456 | 5458 | PASS |
| experiment-wise scaling | 5485–5489,5491,5497–5500,5502 | 5504–5506 | PASS |
| scales[:, np.newaxis] shape | 5491,5508 | 5510 | PASS |
| timewise scaling | 5485–5489,5518–5520,5523–5525,5527 | 5529–5531 | PASS |
| vectorized decay across initial conditions | 5543,5545–5547,5549,5551–5554,5556 | 5558 | PASS |

**Execution method:** The named Word code paragraphs were concatenated in their original order with an explicit `import numpy as np` for isolated examples where needed. Word explanatory text and mathematical displays were excluded; stdout compared with whitespace normalization, preserving all numerical tokens. Evidence table: `G3_Ch12_12_3_Broadcasting_8_Examples_20261026.csv` in the QA workspace.

**Nuance:** `(3,4)` times `(3,)` does NOT broadcast because trailing axis 4 vs 3 fails, while `(3,4)` times `(3,1)` broadcasts as intended for per-experiment scaling. Separately, `(3,4)` times `(4,)` applies timewise scaling. The intentionally invalid shape example in Word p5445–5449 is described rather than executed among these eight; do not claim the failure-path test was performed here.

**Cumulative nonoverlapping scoped examples:** previous 12.1 count 19 and reviewed 12.2 count 10; adding 8 gives **37 executed examples**, of which **35 have matched explicit Word stdout**, two had no printed expected output. This is not full Chapter 12 corpus coverage.

G3 overall and G4/G5/G6 remain HOLD.