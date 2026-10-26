# G3 Chapter 12 — §12.9 exact Word-source position function (2026-10-26)

## Scope
The previous broad-range reconciliation identified Word v37 paragraphs 8081–8100 (function `position_constant_acceleration`) as *not* explicitly documented in the earlier 12-case paragraph-boundary CSV, despite semantic overlap with the already verified analytic-position formula. This follow-up closes that **specific** missing evidence.

Source: Library-backed `Canonical_Word_v37_G4_Ch09_API_Aligned_QA.docx`; `word/document.xml` top-level `w:body/w:p`, zero-based.

## Literal extraction
- Setup: p8026 `import numpy as np`; p8028–8032 `times = np.linspace(0.0, 4.0, 5)`.
- Function body: p8081–8091 `def position_constant_acceleration(times: np.ndarray, x0: float, v0: float, a: float) -> np.ndarray:` and original multi-line return expression.
- Function call: p8093–8098, with `x0=2.0`, `v0=3.0`, `a=-1.0`.
- Output call: p8100 `print(positions)`.
- Reference output text: Word p8062 `[2.  4.5 6.  6.5 6. ]` (this output illustrates the same analytic equation earlier in §12.9).

All code was extracted directly from the Word paragraph text without inserting or changing calculation statements. The selected nonadjacent positions were concatenated in their original order. Generated Python source SHA-256: `ab1c0dd32712034bea72cdafe1209ec8b20500f8d2c97b3a0672c05951372438`.

## Execution evidence
- Runtime: Python with NumPy **2.3.5**.
- Actual stdout: `[2.  4.5 6.  6.5 6. ]`
- Printed reference from Word p8062: `[2.  4.5 6.  6.5 6. ]`
- **PASS, exact stdout match.**

This is **one additional precise Word-source execution** and directly resolves the previously noted §12.9 p8081–8100 gap. It does not imply 7 independent programs (7 of the old 64 candidate paragraph positions occur in this span). The existing 126 case checks were not rerun; do not automatically add one to a unique total until semantic-case overlap is reconciled.

## Overall status
- The 64 old broad-only candidate positions were Word XML role-classified as 54 code/continuation, 9 OMML equations and 1 explanatory paragraph in the prior audit; this additional check resolves the exceptional §12.9 function-source evidence.
- §12.6's 47 code-form candidates remain linked at case-range/behavior level to the previous nine-case audit; no line-by-line literal whole-function execution claim is added.
- The separate **213** previously unclassified candidate positions remain for real block-level triage.
- Word and GitHub executable sources unchanged. G3 Chapter 12 IN PROGRESS. G4/G5/G6 HOLD.
