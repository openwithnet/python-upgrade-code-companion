# G3 Chapter 13–17 — Numerical and Contract Test Evidence (2026-10-25)

**Verdict: SOURCE-TEST ASSERTIONS REVIEWED; CI PASS already recorded; NOT full Word block 1:1, not fresh local test execution, not public release clearance.**

| Chapter | Test file | Concrete expected contract | Scope limitation |
|---|---|---|---|
| 13 | `test_ch13_examples.py` | exponential decay c(1)=exp(-.2); fitted noiseless c0=1.02, k=.21 within 1e-6; `solve_ivp` 6 points vs analytic solution within 1e-8; pandas residual/RMSE; CSV SHA256 matches | Synthetic fit not experimental validation; no guarantee all Word snippets reproduced |
| 14 | `test_ch14_examples.py` | DNA 'ATGAAATTTTAA' -> RNA 'AUGAAAUUUUAA', protein 'MKF*'; reverse complement 'TTAAAATTTCAT'; linear regression slope 2 predicts 13 at x=6; 4bp sequence GC=.5 | Educational sequences, no predictive biological validation |
| 15 | `test_ch15_core_concepts.py` | Torch f(3)=15 and df/dx=8; accumulated gradient 16 before reset, reset 8; JAX grad/JIT near 8; array update retains original; NumPy/PyTorch/JAX decay nearly equal | CPU torch/JAX Windows job PASS run 40140880013, not every manuscript snippet; nondeterminism/backend tolerances |
| 16 | `test_ch16_validation.py` | intentional bug coerces bool/string to numeric; `validated_decay` rejects invalid scalar/vector inputs; c(2)=exp(-.4); empty vector and k=0 boundary tests | Intentional defect is *pedagogical*, should not be portrayed as endorsed implementation; AST parsing not code security verification |
| 17 | `test_core.py` | harmonic oscillator m=1,k=4, initial [1,0]; Euler/RK4/SciPy provide 11x2 for 10 steps; accuracy SciPy<RK4<Euler error at t=1; energy initially 2; defensive copy; DOP853 and RK45 constructor contracts | `RECONSTRUCTED_NOT_ORIGINAL`: mathematically aligned candidate, not historical recovered code |

### Tested source vs manuscript provenance
All test files were read and their assertions examined; each is an educational or reconstructed Code Companion. Actual CI evidence is **Linux run 40062492646** and **Windows/Miniconda run 40140880013**, not a newly executed test suite during this audit. No whole-chapter Word code extraction/coverage audit was established by this check.

### Follow-up acceptance
1. For each Ch13–17 source entrypoint, attach precise Word section or paragraph anchor and mark either DIRECT_SEMANTIC, RELATED_IMPLEMENTATION, TEXTBOOK_ONLY or intentionally defective.
2. Distinguish examples with numeric output from explanatory fragments and explicit pseudocode.
3. Confirm permitted redistribution by origin; keep archived/reconstructed provenance distinct.
4. Maintain G3/G4/G5/G6 hold pending complete scoped decisions. No code or Word edits in this audit.
