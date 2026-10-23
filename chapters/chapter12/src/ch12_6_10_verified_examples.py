"""Chapter 12 sections 12.6–12.9: manuscript-grounded standalone examples.
Educational reconstruction, not verbatim complete extraction.
"""
import math
import numpy as np

def concentration(times, c0=1.0, k=0.2):
    return c0 * np.exp(-k * np.asarray(times, dtype=float))

def expression_analysis():
    expression = np.array([[10.,20.,30.,40.], [12.,18.,33.,39.],
                           [40.,10.,20.,30.], [36.,12.,22.,28.]])
    groups = np.array(['A','A','B','B'])
    a = expression[groups == 'A'].mean(axis=0)
    b = expression[groups == 'B'].mean(axis=0)
    return expression.sum(axis=1), expression.mean(axis=0), a, b, b/a

def exact_positions(times, x0=2.0, v0=3.0, a=-1.0):
    t = np.asarray(times, dtype=float)
    return x0 + v0*t + .5*a*t*t

def simulate_euler_motion(x0: float, v0: float, a: float, dt: float, steps: int):
    if not np.all(np.isfinite([x0,v0,a,dt])): raise ValueError('all parameters must be finite')
    if dt <= 0: raise ValueError('dt must be positive')
    if isinstance(steps,bool) or not isinstance(steps,int) or steps < 0:
        raise ValueError('steps must be a nonnegative integer')
    ts = np.arange(steps + 1, dtype=np.float64)*dt
    xs = np.empty(steps+1, dtype=np.float64); vs = np.empty(steps+1, dtype=np.float64)
    xs[0]=x0; vs[0]=v0
    for i in range(steps):
        xs[i+1] = xs[i]+dt*vs[i]
        vs[i+1] = vs[i]+dt*a
    return ts,xs,vs
