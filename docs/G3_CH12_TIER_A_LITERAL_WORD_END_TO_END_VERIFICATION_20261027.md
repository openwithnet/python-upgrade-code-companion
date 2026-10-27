# Chapter 12 G3 — Tier A original Word source runtime verification

Date: 2026-10-27. Read-only canonical source: `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`, direct `word/document.xml` zero-based top-level paragraphs. The prior Tier-A static manifest contains exact paragraph selections and individual source hashes.

This pass combined original Word code statements, using only `import numpy as np` for isolated execution setup. Six scoped runnable contexts compiled and executed:

| Context | Observed result | Verdict |
|---|---|---|
| Euler literal function p7082–7123 and original call p7125–7132 | `[1.      0.8     0.64    0.512   0.4096  0.32768]` | PASS, exact Word output |
| Expression setup, metadata, dimensions | `2`, `(4, 4)`, `16` | PASS, exact Word output |
| Expression sample totals | `[100. 102. 100.  98.]`, `(4,)` | PASS |
| Expression gene means | `[24.5  15.   26.25 34.25]` | PASS |
| Expression row normalization with Word assertion | row-normalized 4×4 output matches Word; `np.testing.assert_allclose` passes | PASS |
| Word wrong-axis educational expression | output shape `(4,4)`; reviewer contract confirms row totals are not 100 | PASS expected scientifically wrong-axis demonstration, NOT proof of valid sample normalization |

These are **six narrow executions** of exact Word-extracted statements, not six entirely novel manuscript examples: they overlap prior reconstructed QA cases and should NOT be added blindly to historical case totals. Exact actual stdout, full-source SHA256, and descriptions are recorded in intermediate `G3_CH12_TierA_Original_Word_EndToEnd_Run_20261027.csv`.

Result: Tier-A selected Euler function + call now has literal-source execution evidence; the selected expression analysis pipeline has literal-source output evidence, including the intentionally incorrect alternative marked as such. This closes an important Tier-A *selected-source identity* concern but **does not certify every statement in §§12.6/12.8 or complete Chapter-12 code block inventory**. Remaining B-tier seven parent contexts and chapter-wide canonical inventory require separate reconciliation.

No Word manuscript, OMML equation, or production GitHub Python edits. G3 FULL HOLD / scoped Tier-A PASS; G4/G5/G6 HOLD. Intermediate audit only: no user download or save needed.