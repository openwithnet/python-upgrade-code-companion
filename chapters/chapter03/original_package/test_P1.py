# CODE_COMPANION_ROLE: TEST
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: EXCLUDE_FROM_PRODUCTION
"""Regression and scientific reference checks for the P1 procedural example."""
import math
import subprocess
import sys
from pathlib import Path

p = Path(__file__).with_name('P1_particle_motion.py')
result = subprocess.run([sys.executable, str(p)], capture_output=True, text=True, check=True)
assert 'Final numerical position: 3.000' in result.stdout
assert 'Final exact position:     4.000' in result.stdout
assert 'Position error:           1.000' in result.stdout
assert 'Velocity error:           0.000' in result.stdout

def evaluate(dt):
    x, v, a, T = 0.0, 0.0, 2.0, 2.0
    n = round(T / dt)
    for _ in range(n):
        nx = x + v * dt
        nv = v + a * dt
        x, v = nx, nv
    return x, v

for dt, expected_position, expected_error in [(1.0,2.0,2.0),(.5,3.0,1.0),(.25,3.5,.5),(.1,3.8,.2)]:
    x,v = evaluate(dt)
    assert math.isclose(x, expected_position, abs_tol=1e-12)
    assert math.isclose(abs(4-x), expected_error, abs_tol=1e-12)
    assert math.isclose(v, 4, abs_tol=1e-12)

# Regression: these two update orders are intentionally different.
x, v, a, dt = 0, 0, 2, 1
explicit_x, explicit_v = x + v*dt, v + a*dt
semi_v = v + a*dt
semi_x = x + semi_v*dt
assert (explicit_x, explicit_v) == (0, 2)
assert (semi_x, semi_v) == (2, 2)
print('PASS: 1 end-to-end script, 4 convergence conditions, 2 update-order checks')
