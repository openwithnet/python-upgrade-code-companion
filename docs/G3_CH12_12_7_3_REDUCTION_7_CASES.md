# G3 — Chapter 12.7.3 Reduction numerical verification

Date: 2026-10-26. Source: current G4 v37 QA Word manuscript.

**Seven selected reconstructed examples executed successfully. Five matched explicit Word output exactly; one calculated a mean without printing and one executed `np.testing.assert_allclose()` without assertion failure.**

| Case | Zero-based Word code positions | Expected result | Result |
|---|---|---|---|
| Addition order | 7453–7458, skipping explanatory paragraphs | `1.0`, `0.0` | PASS |
| np.sum original order | 7465, 7467–7471, 7473 | `0.0` | PASS |
| np.sum reordered | 7465, 7476–7480, 7482 | `1.0` | PASS |
| float32 sum | 7465, 7490–7493, 7496 | `0.0` | PASS |
| float64 accumulation | 7465, 7490–7493, 7499–7504 | `1.0` | PASS |
| float64 mean | 7465, 7490–7493, 7515–7518 | no printed output | PASS, execution only |
| assert_allclose | 7524, 7526–7529, 7531–7534, 7536–7541 | no printed output | PASS, assertions evaluated |

Exact source statements were selected from Word paragraphs. Subprocesses returned exit code 0; explicit outputs matched without numeric rounding or tolerance changes. The execution context uses the installed current Python/NumPy runtime, and `np.sum()` output for this specific example is not promised to be identical across all NumPy implementations, input shapes or future versions. Evidence CSV: `G3_Ch12_12_7_3_Reduction_7_Cases_20261026.csv`.

Prior Chapter 12 subtotal was 95; the new nonoverlapping scope brings it to **102 reviewed case checks**, not 102 distinct scripts or full manuscript coverage. No Word or GitHub source changed. G3/G4/G5/G6 remain HOLD.