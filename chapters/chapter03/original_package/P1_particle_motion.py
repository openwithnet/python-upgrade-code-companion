# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""P1: Explicit Euler for constant acceleration. Python standard library only."""
import math

# 1. Initial conditions and parameters (SI units)
initial_position = 0.0
initial_velocity = 0.0
acceleration = 2.0
time_step = 0.5
total_time = 2.0

# 2. Validate inputs
for name, value in [('initial_position', initial_position), ('initial_velocity', initial_velocity), ('acceleration', acceleration), ('time_step', time_step), ('total_time', total_time)]:
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be finite')
if time_step <= 0 or total_time < 0:
    raise ValueError('time_step must be positive and total_time nonnegative')
step_ratio = total_time / time_step
if not math.isfinite(step_ratio):
    raise ValueError('invalid step count')
number_of_steps = round(step_ratio)
if not math.isclose(step_ratio, number_of_steps, rel_tol=1e-12, abs_tol=1e-12):
    raise ValueError('total_time must be an integer multiple of time_step')

# 3. Initialize state and history
position = initial_position
velocity = initial_velocity
time = 0.0
times = [time]
positions = [position]
velocities = [velocity]

# 4. Explicit Euler: both next values use the previous state
for step_index in range(number_of_steps):
    next_position = position + velocity * time_step
    next_velocity = velocity + acceleration * time_step
    time = (step_index + 1) * time_step
    position = next_position
    velocity = next_velocity
    times.append(time)
    positions.append(position)
    velocities.append(velocity)

# 5. Output
print('time  position  velocity')
for i in range(len(times)):
    print(f'{times[i]:4.1f}  {positions[i]:8.3f}  {velocities[i]:8.3f}')

# 6. Reference solution
exact_position = initial_position + initial_velocity * total_time + 0.5 * acceleration * total_time**2
exact_velocity = initial_velocity + acceleration * total_time
position_error = abs(positions[-1] - exact_position)
velocity_error = abs(velocities[-1] - exact_velocity)
print()
print(f'Final numerical position: {positions[-1]:.3f}')
print(f'Final exact position:     {exact_position:.3f}')
print(f'Position error:           {position_error:.3f}')
print(f'Final numerical velocity: {velocities[-1]:.3f}')
print(f'Final exact velocity:     {exact_velocity:.3f}')
print(f'Velocity error:           {velocity_error:.3f}')

# 7. Structural and finite-value checks
assert len(times) == number_of_steps + 1
assert len(times) == len(positions) == len(velocities)
assert math.isclose(times[-1], total_time, rel_tol=1e-12, abs_tol=1e-12)
assert all(math.isfinite(x) for x in positions)
assert all(math.isfinite(v) for v in velocities)
