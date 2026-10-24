# CODE_COMPANION_ROLE: REFERENCE
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 15.2–15.4 and 15.6: CPU, educational examples.
These are checked companion reconstructions, not verbatim complete manuscript exports.
"""
import numpy as np

def torch_backward_example(x_value=3.0):
    import torch
    x = torch.tensor(float(x_value), dtype=torch.float64, requires_grad=True)
    y = x**2 + 2*x
    y.backward()
    first = x.grad.item()
    (x**2 + 2*x).backward()  # rebuild graph; .grad accumulates
    accumulated = x.grad.item()
    x.grad.zero_()
    (x**2 + 2*x).backward()
    reset = x.grad.item()
    return y.item(), first, accumulated, reset

def torch_tensor_numpy_copy():
    import torch
    x = np.array([1.0, 2.0], dtype=np.float64)
    t = torch.from_numpy(x)
    t[0] = 7.0
    shared = x[0] == 7.0
    isolated = torch.tensor(x)
    isolated[0] = 8.0
    return bool(shared), bool(x[0] == 7.0)

def jax_functional_grad(x_value=3.0):
    import jax
    import jax.numpy as jnp
    f = lambda x: x*x + 2*x
    x = jnp.asarray(x_value, dtype=jnp.float32)
    eager = jax.grad(f)(x)
    compiled = jax.jit(jax.grad(f))(x)
    return float(eager), float(compiled)

def jax_array_update():
    import jax.numpy as jnp
    a = jnp.array([1,2,3])
    b = a.at[0].set(7)
    return np.asarray(a), np.asarray(b)

def derivative_comparison(x=3.0, h=1e-5):
    if not np.isfinite(h) or h <= 0:
        raise ValueError('h must be finite and positive')
    f = lambda v: v*v + 2*v
    analytic = 2*x + 2
    central = (f(x+h)-f(x-h))/(2*h)
    return float(analytic), float(central)

def three_library_decay(times, c0=1.0, k=0.2):
    import torch
    import jax.numpy as jnp
    t = np.asarray(times, dtype=np.float64)
    n = c0*np.exp(-k*t)
    p = (c0*torch.exp(-k*torch.as_tensor(t, dtype=torch.float64))).numpy()
    j = np.asarray(c0*jnp.exp(-k*jnp.asarray(t, dtype=jnp.float32)))
    return n, p, j
