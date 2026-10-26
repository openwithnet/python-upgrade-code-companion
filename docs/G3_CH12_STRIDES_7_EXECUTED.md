# G3 Chapter 12.5.2 — Strides and Memory Layout

Date: 2026-10-26. Source: current Word v37 G4 QA manuscript.

Seven independent checks reconstructed from Word paragraphs were executed in the QA Python environment. All exited with code 0 and matched their stated Word results. For the final reshape example, the Word prose states the expected result False rather than providing a separate output block.

| Example | Word code locations | Verified output |
|---|---|---|
| C-order strides and itemsize | 6471–6478 | shape (3,4), itemsize 8, strides (32,8) |
| C versus Fortran order | 6507–6520 | strides (24,8) and (8,16) |
| Contiguity flags | 6531–6534 | True, False |
| Every-other-column slice | 6544–6555 | shape (3,2), strides (32,16) |
| Transpose | 6568–6576 | (3,4) (32,8); (4,3) (8,32) |
| Negative stride | 6587–6595 | [40 30 20 10], (-8,) |
| Transposed reshape | 6615–6619 | shares_memory=False |

Reconstruction included explicit NumPy import. Output checks used whitespace normalization only and did not modify numeric values. Evidence CSV: `G3_Ch12_Strides_7_Executed_20261026.csv` in working QA folder.

Prior scoped Chapter 12 total: 63. Current total: 70 checks (68 normal executions; 66 with stated output or prose result, 2 without expected print; 2 expected exceptions). These counts do not establish full chapter coverage, and scripts may share prerequisite setup. No Word or source modification. G3/G4/G5/G6 remain HOLD.