"""Chapter 15.5: first-order decay Jacobians. Educational CPU example."""
import numpy as np

def numpy_concentration(times, theta):
    times = np.asarray(times, dtype=np.float64)
    c0, k = np.asarray(theta, dtype=np.float64)
    return c0 * np.exp(-k * times)

def analytical_jacobian(times, theta):
    times = np.asarray(times, dtype=np.float64)
    c0, k = np.asarray(theta, dtype=np.float64)
    term = np.exp(-k * times)
    return np.column_stack((term, -times * c0 * term))

def torch_jacobian(times, theta):
    import torch
    t = torch.as_tensor(np.asarray(times), dtype=torch.float64, device="cpu")
    th = torch.as_tensor(np.asarray(theta), dtype=torch.float64, device="cpu")
    def model(p):
        c0, k = p
        return c0 * torch.exp(-k * t)
    return torch.func.jacrev(model)(th).detach().cpu().numpy()

def jax_jacobian(times, theta, compile=False):
    import jax
    jax.config.update("jax_enable_x64", True)
    import jax.numpy as jnp
    t = jnp.asarray(times, dtype=jnp.float64)
    th = jnp.asarray(theta, dtype=jnp.float64)
    def model(p, ts):
        c0, k = p
        return c0 * jnp.exp(-k * ts)
    fun = jax.jacrev(model, argnums=0)
    if compile:
        fun = jax.jit(fun)
    return np.asarray(fun(th, t))

def default_example():
    times = np.array([0., 1., 2., 3., 5.])
    theta = np.array([1., 0.2])
    return times, theta
