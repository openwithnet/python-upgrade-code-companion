# G3 — Chapter 12.9 Particle Motion Verification (2026-10-26)

**12/12 scoped behavioral checks PASS.** These were executed in the current Python environment by reconstructing Word v37 G4 QA examples from paragraph positions 8026–8328. The nine positive checks comprise time grid, velocity, analytic position, loop computation, loop vs NumPy equality, Euler positions, Euler velocities, reduced-step error and multi-initial-condition array shape. Three additional reviewer-generated tests confirm that invalid `steps` values True, -1 and 1.5 raise `ValueError` per the Word input contract.

Results: analytic position `[2,4.5,6,6.5,6]`; Euler positions `[2,5,7,8,8]`; refined Euler maximum absolute position error `0.2`; multi-initial array shape `(3,5)`.

**Scientific distinction:** Analytic constant-acceleration evaluation and explicit Euler step integration implement distinct numerical algorithms. Their different results are not proof of a NumPy vectorization error. The Word §12.9.3 timing discussion compares loop and NumPy evaluation of the **same analytic formula**, not Euler against the analytic expression. Benchmark times are not asserted here.

**Method and scope:** Working CSV `G3_Ch12_12_9_Particle_Motion_12_Cases_20261026.csv` records individual Word paragraph ranges, expected values, computed outputs, and pass flags. These are reconstructed, reviewer-executed components, **not 12 independently exact Word-extracted full scripts**. The Chapter 12 source candidate `ch12_6_10_verified_examples.py` contains `exact_positions` and `simulate_euler_motion`, while `ch12_remaining_examples.py` implements loop/vectorized positions and a performance comparator: **DIRECT_SEMANTIC / representative**, not byte-identical program matches.

Previous Chapter 12 114 scoped cases plus 12 = **126 case checks**, not full chapter verification. No Word or GitHub Python source changes. G3/G4/G5/G6 remain HOLD.