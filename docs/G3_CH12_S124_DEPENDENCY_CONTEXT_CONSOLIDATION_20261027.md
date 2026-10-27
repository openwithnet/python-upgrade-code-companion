# Chapter 12 G3 — Section 12.4 source-context consolidation

Date: 2026-10-27. Baseline: authoritative Word v37 and the 249-group provisional source list, unchanged.

All **35 §12.4 provisional source groups** have been uniquely assigned to **16 proposed educational code contexts** using source order and shared definitions. Every original provisional group ID is preserved exactly once; the new CSV contains the selected paragraph IDs and parent boundaries. This is source dependency mapping, not 16 whole-program execution PASS results.

| ID | Word paragraph span | Groups | Context |
|---|---|---:|---|
| S124-01 | 5862–5877 | 2 | Boolean threshold selection |
| S124-02 | 5887–5902 | 3 | Combined Boolean masks |
| S124-03 | 5910–5921 | 1 | Finite/range validity mask |
| S124-04 | 5930–5960 | 3 | 2D row filtering vs element selection sharing data |
| S124-05 | 5972–5987 | 2 | Boolean indexed copy vs assignment |
| S124-06 | 5998–6004 | 1 | Integer selection |
| S124-07 | 6011–6023 | 2 | Basic slice vs advanced index memory sharing |
| S124-08 | 6031–6062 | 4 | 2D indexing and np.ix_ with shared array |
| S124-09 | 6081–6097 | 2 | 3D advanced slicing |
| S124-10 | 6107–6109 | 1 | Repeated integer index reading |
| S124-11 | 6114–6131 | 3 | Repeated increment vs np.add.at |
| S124-12 | 6139–6169 | 2 | Explicit/inferred reshape |
| S124-13 | 6185–6211 | 3 | Transpose vs reshape |
| S124-14 | 6230–6242 | 2 | Transpose axes |
| S124-15 | 6253–6272 | 3 | moveaxis vs swapaxes |
| S124-16 | 6282–6286 | 1 | Transpose view memory check |

Working register: `G3_CH12_S124_35_To_16_Dependency_Context_Proposal_20261027.csv`, with 16 rows, all 35 member IDs exactly once. These inclusive reference spans include explanatory prose/expected output, requiring exact runnable-statement selection and prior QA provenance for canonical release.

Cumulative progress §12.1 29→13; §12.2 31→14; §12.3 35→16; §12.4 35→16. Total **130 provisional groups → 59 proposed instructional contexts**. Not 59 independent scripts.

No computations rerun. Word/GitHub executable source unchanged. Chapter 12 G3 FULL HOLD; G4/G5/G6 HOLD. This is intermediate evidence; the user need not save it.