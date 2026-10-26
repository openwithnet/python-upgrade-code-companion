# G3 Chapter 12 — Targeted Word v37 Unmapped Case Execution (2026-10-26)

## Scope
The previous 889 paragraph-candidate triage and documented 126 scoped case checks are retained as-is. This follow-up selected five executable examples from §12.2, §12.3, and §12.8 for which the prior paragraph-to-case crosswalk lacked an exact paragraph-level execution record. It does **not** certify the entire outstanding queue or increase the 126-case count without overlap reconciliation.

The actual Word v37 document `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx` was read from its `word/document.xml`, direct `w:body/w:p` (zero-based). Code paragraphs were concatenated in manuscript order; `import numpy as np` was explicitly supplied as a setup dependency where applicable, and previously defined arrays were reintroduced from their Word paragraph positions. Outputs were compared to printed Word strings without changing numerical values. The two non-printing tests were checked with assertions supplied by the reviewer or printed Word code.

## New targeted cases

| Section | Named check | Word code paragraphs | Printed Word output | Result |
|---|---|---|---|---|
| 12.2 | keepdims along axis 0 | 4980–4984; 5038–5042; 5044–5045 | 5047–5048; `[[2. 4. 6. 8.]]`, `(1, 4)` | PASS |
| 12.2 | keepdims along axis 1 | 4980–4984; 5051–5055; 5057–5058 | 5060–5063; column means, `(3, 1)` | PASS |
| 12.2 | mean_over_replicates 3-D contract | 5318–5327 | no printed output; valid 3-D axis-0 mean and invalid 2-D `ValueError` verified by reviewer-added calls | PASS |
| 12.3 | per-experiment initial conditions and rates | 5572, 5574, 5576–5578, 5583–5588, 5590 | 5592; `(3, 4)` | PASS |
| 12.8 | scalar-loop versus NumPy `log2` | 7591, 7593–7598, 7866, 7868, 7870–7876, 7878, 7880, 7882, 7884–7887 | no printed stdout; actual Word `np.testing.assert_allclose` passed | PASS |

Total: **5/5 executable checks pass; 3/3 explicitly printed output groups match; 2/2 non-printing contracts pass.**

## Important evidence distinctions
- The Word chapter p4451–8621 contains 889 broad syntax-candidate paragraphs; 452 groups from prior proximity analysis are *not* validated executable units.
- The older 126 checks are retained without re-execution. The five new checks may overlap with earlier **semantically similar** cases, even where the old audit did not give an exact line/paragraph mapping; they are **not** added arithmetically to the audited 126 total.
- This round has concrete exact paragraph spans and execution evidence for these five examples. It does not prove every block in §12.2, §12.3, §12.8, nor the whole Chapter 12.
- No Word source, GitHub executable code, or Chapter 6/10 evidence was altered.

## Next step
Classify the remaining unlinked **multi-paragraph** candidates (priority §12.2 shape/reduction examples, §12.3 advanced broadcasting, §12.8 integrated case and contracts). Resolve each block's full Word code span and test provenance; do not re-execute existing verified cases without a concrete evidence gap.

G3 Chapter 12: IN PROGRESS; G4/G5/G6: HOLD.
