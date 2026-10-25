# G3 — Chapter 12 §12.1.2–12.1.3 Eight Additional Executed Examples (2026-10-25)

**Status: 8/8 direct Python executions PASS; 8/8 Word expected outputs match.** Word source: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` (zero-based python-docx paragraphs). Extracted full code statements, supplied explicit `import numpy as np` for independent execution, and compared whitespace-normalized stdout to Word. No GitHub Python or Word sources changed.

| Example | Current Word code paragraph indices | Expected output paragraph | Execution |
|---|---|---|---|
| experiment-wise time mean | 4691–4695, 4706–4709, 4711 | 4713 | `[0.725 0.825 0.625]` |
| 2-D shape | 4723–4726, 4728 | 4730 | `(2, 3)` |
| vector / row / column shape | 4735, 4737, 4739–4743, 4745–4747 | 4749–4751 | `(3,)`, `(1, 3)`, `(3, 1)` |
| matrix elementwise multiply | 4760–4763, 4765–4768, 4770 | 4772–4773 | `[[5,12],[21,32]]` NumPy formatting |
| matrix multiplication | 4760–4763, 4765–4768, 4775 | 4777–4778 | `[[19,22],[43,50]]` |
| 3-D tensor shape | 4792, 4794 | 4796 | `(3, 5, 2)` |
| experiment-axis reduction | 4792, 4799, 4801 | 4803 | `(5, 2)` |
| time-axis reduction | 4792, 4806, 4808 | 4810 | `(3, 2)` |

**Provenance of test evidence:** These eight snippets were reconstructed from the actual Word paragraphs and freshly executed in the current container Python environment. A separate working CSV, `G3_Ch12_12_1_Continuation_8_Examples_20261025.csv`, records snippets, output and status. Whitespace normalization does not change numeric values. Earlier §12.1.1–12.1.2 audit reported 11 successful examples, nine with expected outputs, so across these *nonoverlapping* audits there are 19 successful example executions and 17 matches to stated outputs (the other two had no stated print output).

**Limitations:** Not all Word snippets in Chapter 12 have been classified. A set of 19 examples does not represent 19 independent script files. All G3 / G4 / G5 / G6 release gates remain OPEN / HOLD.