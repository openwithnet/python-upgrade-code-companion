# G3 — Chapter 12.8 Integrated Expression Matrix Audit (2026-10-26)

**Current-turn execution:** Twelve ordered cases reconstructed from Word v37 G4 QA §§12.8.1–12.8.3. All twelve execute after full prior setup; ten matched explicit Word printed outputs, and two cases were nonprinting contracts (normalization assertion and deliberately wrong-axis computation). No Word or GitHub source changed.

| Case | Word zero-based code positions | Result |
|---|---|---|
| Matrix dimensions | 7620–7622 | 2, (4,4), 16 |
| Sample totals | 7670–7672 | [100,102,100,98] |
| Gene means | 7687–7689 | [24.5,15,26.25,34.25] |
| Group A selection | 7700–7704 | two rows |
| Group B selection | 7709–7713 | two rows |
| Group means A/B | 7722–7726 | expected means |
| B/A mean ratio | 7736–7738 | [3.455,.579,.667,.734] |
| keepdims totals | 7774–7780 | shape (4,1) |
| Relative normalization | 7789–7798 | 4x4 expected output |
| Per-row sum contract | 7811–7820 | np.testing.assert_allclose succeeded |
| Wrong axis sample-normalization demonstration | 7826–7833 | executes but uses gene axis, scientifically wrong target |
| log2 transform | 7845–7854 | 4x4 Word output |

**Important caution:** The sum across *only four illustrated genes* is not a transcriptome-scale sequencing library size. Relative row percentages here are a didactic ratio, not a standard RNA-seq normalization method. Mean differences here do not establish differential expression statistical significance; replicate design and variance/multiplicity matter. Because shape is (4,4), an erroneous gene-axis divisor also broadcasts and returns the same shape, illustrating the need for semantic contracts.

**Extraction QA:** Initial attempts to execute the assertion and wrong-axis examples omitted the closing parenthesis from multi-paragraph Word code, causing a Python SyntaxError. Corrected paragraph boundaries (7811–7813, 7826–7829) were subsequently executed successfully. This was extraction error, not a textbook algorithm error.

Detailed CSV: `G3_Ch12_12_8_Integrated_12_Cases_20261026.csv`. Prior cumulative scoped cases: 102; these twelve bring it to **114 scoped checks**, not 114 independent source files nor full Chapter 12 coverage. G3/G4/G5/G6 remain HOLD.