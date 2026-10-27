# Chapter 12 G3 — Tier B vectorize extra print and motion dependent expression follow-up (2026-10-27)

Source: authoritative Word v37 direct OOXML body paragraphs (zero-based). No production source changes.

## Newly verified missing printed expression
Word p7200–7209 defines custom_function, np.vectorize, x and its first print. Word p7213 adds `print(x**2 + 1)` but does not print a second expected output directly afterward. Literal Word code p7200,7201,7203–7205,7207,7209,7213 was compiled and executed in one isolated context (with `import numpy as np` only). Both actual stdout lines were identical: `[ 2.  5. 10.]`. **PASS (one new exact Word source context with an additional print, not two independent novel programs).** Source SHA256 `474452319b64dd3266b2b39f38c682d9c9417f196493dfbb3dcb782888da4036`.

## Motion expressions §12.9
Word p8395–8397 (vector expression) and p8404,p8406–8408 (loop with same constant-acceleration polynomial) were re-extracted and AST parsed: **STATIC PASS**. Both require previously defined `times`, `x0`, `v0`, `a` and are dependent educational presentations, not complete standalone programs. The earlier audit already covered loop vs NumPy analytic-position equivalence under scoped inputs; this follow-up did not rerun the computation or claim source-byte identity to that historical run. These snippets should be attached to their analytic-position parent context in the final manifest.

Detailed local evidence file: `G3_CH12_TierB_Vectorize_Print_and_Motion_Context_20261027.csv` (source hashes and observed outputs).

Gate: Tier B printed-output omission is resolved. This does not itself complete the full Chapter 12 executable block manifest or the GitHub 21-function source-provenance review; **G3 FULL HOLD**, G4/G5/G6 HOLD. No user archive requested; intermediate audit record.