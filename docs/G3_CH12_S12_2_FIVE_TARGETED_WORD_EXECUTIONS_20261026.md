# G3 Chapter 12 — §12.2 Five Targeted Word-Native Execution Checks (2026-10-26)

## Inputs and method
Actual Word v37 file `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` recovered from Library. Extracted `word/document.xml` direct `w:body/w:p`, zero-based; preserved individual `w:t` text and newline/control nodes. Reassembled complete code from exact Word paragraph IDs listed below. Only `import numpy as np` was added as a standalone setup for isolated runs. Captured actual stdout and compared to Word's literal displayed output after terminal-newline/whitespace-token normalization. No existing Chapter 6/10 or existing 126 Chapter 12 case tests were rerun.

## Targeted checks

| Name | Word code paragraph IDs | Word expected paragraphs | Execution result |
|---|---|---|---|
| Negative axis sum | 4932–4935, 4963–4964 | None; prose explains axis equivalence | PASS: `[ 60 150]` twice |
| Centering with keepdims | 4980–4984, 5072–5076, 5078, 5080 | 5082–5084 | PASS: exact 3×4 printed array |
| Mean over axes (0, 2) | 5098–5101, 5104–5106, 5108–5109 | 5111–5112 | PASS: `[ 7.5 11.5 15.5]`, `(3,)` |
| std default vs ddof=1 | 5121–5123, 5125, 5127–5130 | None | PASS: `0.816496580927726`, `1.0` |
| mean vs nanmean | 5140–5144, 5146, 5150 | 5148, 5152 | PASS: `nan`, `2.0` |

**Result:** 5/5 checks executed cleanly; 3/3 cases with explicit printed outputs matched Word; two additional examples had no distinct expected-output block.

## Evidence limits
The checks supply exact Word code span and current execution evidence for blocks lacking itemized references in the prior paragraph crosswalk. Some overlap semantically with preexisting 126 scoped audits; do not present 131 as a certified disjoint total. The cases depend on local NumPy behavior; no independent Windows/Conda or fresh GitHub checkout has been re-tested. Word and canonical source files were not modified. Chapter 12 G3 remains IN PROGRESS; G4/G5/G6 HOLD.

Attached working record: `G3_CH12_12_2_Targeted_5_Cases_20261026.csv`.
