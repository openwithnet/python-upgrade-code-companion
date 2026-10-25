# G3 — Additional Word Code Samples, Chapters 10 and 12 (2026-10-25)

**Status: 5 reconstructed components executed successfully; sample-level evidence only, not G3 PASS.**

| Example | Zero-based Word paragraphs | Execution/context result |
|---|---|---|
| Ch10 `linear_concentration` function definition | 1471–1478 | Compiles and defines function |
| Ch10 dependent list comprehension and print | 1481–1492 | PASS with preceding function definition; prints `[0.0, 1.0, 4.0]` |
| Ch12 Python list repeat | 4523 and 4525 | PASS; prints `[1, 2, 3, 1, 2, 3]`; intervening paragraph 4524 is explanation, NOT code |
| Ch12 NumPy elementwise multiply | 4531–4533 | PASS when earlier `import numpy as np` dependency is supplied; prints `[2 4 6]` |
| Ch12 vectorized first-order kinetics | 4570–4586 | PASS; prints `[1.       0.818731 0.67032  0.548812 0.449329 0.367879]` |

**Important extraction observations:** Blind paragraph-span execution initially caused `SyntaxError` when natural-language paragraphs were included (Ch12). The NumPy elementwise snippet then raised `NameError: np is not defined` when run without its established earlier import. These are **extraction and dependency errors**, not evidence that the textbook's Python computation is incorrect. Corrected selection/import yielded the outputs above.

**Scientific distinction:** Ch12 vectorized `c0*np.exp(-k*times)` evaluates the analytical first-order solution at an array of times. It is not Euler/Midpoint numerical integration. This distinction is explicit in Word.

**Verification status:** Executed under the working Python environment, not independent user Windows/Anaconda; expected outputs match the Word snippets inspected. No exact repository-file identity shown for these five extracted components; no test of all 1,090 candidate groups. Full provenance and rights remain OPEN.

**No Word or Python source files modified.** G3 and G4–G6 HOLD.
