from abc import ABC, abstractmethod
from dataclasses import dataclass
import math
import numbers

import numpy as np


def real_array(value, name):
    def has_boolean(item):
        if isinstance(item, (bool, np.bool_)):
            return True
        if isinstance(item, (list, tuple)):
            return any(has_boolean(x) for x in item)
        if isinstance(item, np.ndarray):
            if item.dtype.kind == "b":
                return True
            if item.dtype.kind == "O":
                return any(has_boolean(x) for x in item.flat)
        return False

    if has_boolean(value):
        raise ValueError(f"{name} must not contain booleans")
    try:
        raw = np.asarray(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a real array") from exc
    if raw.dtype.kind not in "iuf":
        raise ValueError(f"{name} must contain real numbers")
    try:
        data = np.array(raw, dtype=np.float64, copy=True)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} cannot be converted to float64") from exc
    if not np.all(np.isfinite(data)):
        raise ValueError(f"{name} must contain finite values")
    return data


def positive_scalar(value, name):
    data = real_array(value, name)

    if data.ndim != 0:
        raise ValueError(
            f"{name} must be a scalar"
        )

    result = float(data)

    if result <= 0.0:
        raise ValueError(
            f"{name} must be positive"
        )

    return result


def validate_state(value):
    state = real_array(value, "state")

    if state.shape != (2,):
        raise ValueError(
            "state must have shape (2,)"
        )

    return state


def validate_steps(value):
    if (
        isinstance(value, (bool, np.bool_))
        or not isinstance(value, numbers.Integral)
    ):
        raise ValueError(
            "steps must be an integer"
        )

    steps = int(value)

    if steps < 0:
        raise ValueError(
            "steps must be nonnegative"
        )

    return steps


@dataclass(frozen=True)
class OscillatorModel:
    m: float
    k: float

    def __post_init__(self):
        object.__setattr__(
            self,
            "m",
            positive_scalar(self.m, "m"),
        )
        object.__setattr__(
            self,
            "k",
            positive_scalar(self.k, "k"),
        )

        ratio = self.k / self.m

        if not math.isfinite(ratio) or ratio <= 0:
            raise ValueError(
                "k / m must be finite and positive"
            )

    def rhs(self, t, state):
        data = validate_state(state)

        x, v = data

        result = np.array(
            [v, -(self.k / self.m) * x],
            dtype=np.float64,
        )

        if not np.all(np.isfinite(result)):
            raise ValueError(
                "non-finite state derivative"
            )

        return result


class Trajectory:
    def __init__(self, times, states):
        t = real_array(times, "times")
        y = real_array(states, "states")

        if t.ndim != 1:
            raise ValueError(
                "times must be one-dimensional"
            )

        if y.ndim != 2 or y.shape[1] != 2:
            raise ValueError(
                "states must have shape (N, 2)"
            )

        if len(t) != len(y) or len(t) == 0:
            raise ValueError(
                "invalid trajectory length"
            )

        if np.any(t < 0.0):
            raise ValueError(
                "times must be nonnegative"
            )

        if np.any(np.diff(t) <= 0.0):
            raise ValueError(
                "times must be strictly increasing"
            )

        self._times = t
        self._states = y

    @property
    def times(self):
        return self._times.copy()

    @property
    def states(self):
        return self._states.copy()

    @property
    def positions(self):
        return self._states[:, 0].copy()

    @property
    def velocities(self):
        return self._states[:, 1].copy()

    def __len__(self):
        return len(self._times)


def validate_solver_inputs(initial_state, dt, steps):
    state = validate_state(initial_state)
    dt = positive_scalar(dt, "dt")
    steps = validate_steps(steps)

    end_time = dt * steps

    if not math.isfinite(end_time):
        raise ValueError(
            "integration interval must be finite"
        )

    if steps > 0 and end_time <= 0.0:
        raise ValueError(
            "integration interval must be positive"
        )

    return state, dt, steps


class Solver(ABC):
    @abstractmethod
    def solve(self, model, initial_state, dt, steps):
        ...


class EulerSolver(Solver):
    def solve(self, model, initial_state, dt, steps):
        state, dt, steps = validate_solver_inputs(
            initial_state, dt, steps
        )

        times = np.arange(
            steps + 1,
            dtype=np.float64,
        ) * dt

        states = np.empty(
            (steps + 1, 2),
            dtype=np.float64,
        )

        states[0] = state

        for n in range(steps):
            derivative = model.rhs(times[n], state)

            state = state + dt * derivative

            if not np.all(np.isfinite(state)):
                raise ValueError(
                    "non-finite integration state"
                )

            states[n + 1] = state

        return Trajectory(times, states)


def rk4_step(model, t, state, dt):
    k1 = model.rhs(t, state)

    k2 = model.rhs(
        t + dt / 2.0,
        state + dt * k1 / 2.0,
    )

    k3 = model.rhs(
        t + dt / 2.0,
        state + dt * k2 / 2.0,
    )

    k4 = model.rhs(
        t + dt,
        state + dt * k3,
    )

    return state + dt / 6.0 * (
        k1 + 2.0 * k2 + 2.0 * k3 + k4
    )


class RK4Solver(Solver):
    def solve(self, model, initial_state, dt, steps):
        state, dt, steps = validate_solver_inputs(
            initial_state, dt, steps
        )

        times = np.arange(
            steps + 1,
            dtype=np.float64,
        ) * dt

        states = np.empty(
            (steps + 1, 2),
            dtype=np.float64,
        )

        states[0] = state

        for n in range(steps):
            state = rk4_step(
                model,
                times[n],
                state,
                dt,
            )

            if not np.all(np.isfinite(state)):
                raise ValueError(
                    "non-finite integration state"
                )

            states[n + 1] = state

        return Trajectory(times, states)


def exact_state(t, model, initial_state):
    x0, v0 = validate_state(initial_state)
    omega = math.sqrt(model.k / model.m)

    x = (
        x0 * math.cos(omega * t)
        + (v0 / omega) * math.sin(omega * t)
    )

    v = (
        -omega * x0 * math.sin(omega * t)
        + v0 * math.cos(omega * t)
    )

    return np.array([x, v], dtype=np.float64)



def energy(model, state):
    values = real_array(state, "state")
    if values.shape[-1] != 2 or values.ndim not in (1, 2):
        raise ValueError("state must have shape (2,) or (N, 2)")
    x = values[..., 0]
    v = values[..., 1]
    result = 0.5 * model.k * x*x + 0.5 * model.m * v*v
    if not np.all(np.isfinite(result)):
        raise ValueError("non-finite energy")
    return result


class SciPySolver(Solver):
    """Adaptive SciPy integrator; dt sets output sampling, not solver step size."""

    def __init__(self, method="RK45", rtol=1e-9, atol=1e-11):
        self.method = method
        self.rtol = rtol
        self.atol = atol

    def solve(self, model, initial_state, dt, steps):
        from scipy.integrate import solve_ivp

        state, dt, steps = validate_solver_inputs(initial_state, dt, steps)
        if steps == 0:
            return Trajectory([0.0], state.reshape(1, 2))
        times = np.arange(steps + 1, dtype=np.float64) * dt
        result = solve_ivp(
            model.rhs, (0.0, float(times[-1])), state,
            method=self.method, t_eval=times,
            rtol=self.rtol, atol=self.atol,
        )
        if not result.success or result.y.shape != (2, len(times)):
            raise RuntimeError("SciPy integration failed")
        return Trajectory(result.t, result.y.T)
