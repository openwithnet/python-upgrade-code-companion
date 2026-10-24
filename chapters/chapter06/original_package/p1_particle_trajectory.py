# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 6, P1: particle trajectory with explicit Euler integration."""
from __future__ import annotations

from dataclasses import dataclass
import math


def finite_real(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return float(value)


@dataclass(frozen=True)
class ParticleState:
    position: float
    velocity: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "position", finite_real(self.position, "position"))
        object.__setattr__(self, "velocity", finite_real(self.velocity, "velocity"))


def euler_step(state: ParticleState, acceleration: float, time_step: float) -> ParticleState:
    if not isinstance(state, ParticleState):
        raise TypeError("state must be a ParticleState")
    a = finite_real(acceleration, "acceleration")
    dt = finite_real(time_step, "time_step")
    if dt <= 0:
        raise ValueError("time_step must be positive")
    return ParticleState(
        position=state.position + state.velocity * dt,
        velocity=state.velocity + a * dt,
    )


class Particle:
    def __init__(self, initial_state: ParticleState) -> None:
        if not isinstance(initial_state, ParticleState):
            raise TypeError("initial_state must be a ParticleState")
        self._state = initial_state

    @property
    def state(self) -> ParticleState:
        return self._state

    def predict(self, acceleration: float, time_step: float) -> ParticleState:
        return euler_step(self._state, acceleration, time_step)

    def advance(self, acceleration: float, time_step: float) -> None:
        next_state = self.predict(acceleration, time_step)
        self._state = next_state


@dataclass(frozen=True)
class TrajectoryRecord:
    time: float
    state: ParticleState

    def __post_init__(self) -> None:
        object.__setattr__(self, "time", finite_real(self.time, "time"))
        if not isinstance(self.state, ParticleState):
            raise TypeError("state must be a ParticleState")


class Trajectory:
    def __init__(self) -> None:
        self._records: list[TrajectoryRecord] = []

    @property
    def records(self) -> tuple[TrajectoryRecord, ...]:
        return tuple(self._records)

    def append(self, time: float, state: ParticleState) -> None:
        record = TrajectoryRecord(time, state)
        if record.time < 0:
            raise ValueError("time must be nonnegative")
        if self._records and record.time <= self._records[-1].time:
            raise ValueError("time must be strictly increasing")
        self._records.append(record)

    def __len__(self) -> int:
        return len(self._records)


def simulate_particle(initial_state: ParticleState, acceleration: float, time_step: float, steps: int) -> Trajectory:
    if not isinstance(steps, int) or isinstance(steps, bool):
        raise TypeError("steps must be an integer")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    # Validate even when steps=0; avoid partial execution for invalid settings.
    a = finite_real(acceleration, "acceleration")
    dt = finite_real(time_step, "time_step")
    if dt <= 0:
        raise ValueError("time_step must be positive")
    particle = Particle(initial_state)
    trajectory = Trajectory()
    trajectory.append(0.0, particle.state)
    for index in range(1, steps + 1):
        particle.advance(a, dt)
        trajectory.append(index * dt, particle.state)
    return trajectory


def main() -> None:
    initial = ParticleState(0.0, 0.0)
    trajectory = simulate_particle(initial, acceleration=2.0, time_step=0.5, steps=4)
    print("time   position   velocity")
    for record in trajectory.records:
        print(f"{record.time:4.1f}   {record.state.position:8.3f}   {record.state.velocity:8.3f}")
    final = trajectory.records[-1]
    exact_position = initial.position + initial.velocity * final.time + 0.5 * 2.0 * final.time**2
    print(f"Euler final position: {final.state.position:.3f}")
    print(f"Exact final position: {exact_position:.3f}")
    print(f"Absolute position error: {abs(final.state.position-exact_position):.3f}")

if __name__ == "__main__":
    main()
