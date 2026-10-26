# G3 Chapter 12 — §§12.4–12.5 Twelve Word-Native Block Executions (2026-10-26)

## Scope and actual execution
Read `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` from Library, parsed `word/document.xml` direct `w:body/w:p` (zero-based), preserving Word text/control breaks. Starting from the previously classified 52 broad-span positions (44 code-like, four prose and four OMML), manually reconstructed **12 runnable demonstration contexts** from relevant Word paragraph groups. `import numpy as np` was added as explicit isolated execution setup. Python source was compiled and executed locally with captured stdout; literal expected Word output paragraphs were compared without numeric tolerance or whitespace alteration. These are additional *paragraph-specific* checks, not proof of 12 semantically unique examples absent from the historical 126 scoped cases.

| Case | Word code paragraph indices | Expected Word output indices | Result |
|---|---|---|---|
| 3D indexing | 6081–6084, 6087, 6089–6090, 6095, 6097 | 6092,6093,6099 | PASS EXACT |
| repeated integer indices | 6107,6109 | no separate printed output paragraph | PASS execution-only |
| reshape base | 6139,6141,6145,6147 | 6143,6149–6151 | PASS EXACT |
| reshape inferred dimension | 6159,6161,6163,6167,6169 | 6165,6171 | PASS EXACT |
| transpose | 6185–6188,6191,6193–6194 | 6196–6199 | PASS EXACT |
| reshape vs transpose definitions | 6207,6209,6211 | no print | PASS execution-only |
| transpose axis order | 6230–6232,6238–6240,6242 | 6244 | PASS EXACT |
| moveaxis | 6253,6255–6259,6261 | 6263 | PASS EXACT |
| swapaxes | 6253,6266–6270,6272 | 6274 | PASS EXACT |
| view vs copy definitions | 6327,6328,6332 | no print | PASS execution-only |
| ndarray shape/dtype | 6349,6351–6354,6356–6357 | no distinct printed output, prose says integer dtype environment dependent | PASS execution-only |
| view slice | 6363,6365,6367 | 6369 | PASS EXACT |

**12/12 clean executions. Eight explicit Word output groups match exactly (8/8). Four execution-only cases have no separate printed-result block.** The ndarray dtype displayed as `int64` under the current NumPy environment, not a portable dtype guarantee.

Original 126 scoped cases were not deliberately rerun. No Chapter 6/10 tests; no change to Word manuscript or GitHub production Python source. The results do not establish a complete code boundary audit of all 44 candidate paragraphs: many are continuation lines within the named contexts and neighboring §12.5 examples still require explicit mapping. New local CSV: `G3_CH12_S12_4_5_12_Word_Block_Execution_20261026.csv`.

Chapter 12 G3 IN PROGRESS; G4/G5/G6 HOLD.
