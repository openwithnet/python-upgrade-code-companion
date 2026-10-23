"""Numerical checks for the C1 anchor example."""
import math
import numpy as np

def concentration(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

signals = [2.0, 4.0, 6.0]
expected = [1.0, 2.0, 3.0]
assert np.allclose([concentration(x, 2.0) for x in signals], expected)
assert math.isclose(concentration(6.0, 2.0), 3.0)
for bad in [0, -1]:
    try:
        concentration(6.0, bad)
    except ValueError:
        pass
    else:
        raise AssertionError('invalid slope accepted')
print('C1 checks passed')
