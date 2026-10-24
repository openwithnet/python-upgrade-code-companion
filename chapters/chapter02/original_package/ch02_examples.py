# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 2 illustrative snippets, run sequentially (educational)."""

# --- Example 01 ---
measurements = [10.0, 12.0, 14.0]
total = 0.0
for value in measurements:
    total += value
average = total / len(measurements)
print(average)

# --- Example 02 ---
def calculate_mean(values):
    return sum(values) / len(values)

print(calculate_mean([10.0, 12.0, 14.0]))

# --- Example 03 ---
import numpy as np
print(np.mean(np.array([10.0, 12.0, 14.0])))

# --- Example 04 ---
def process_data(values):
    result = []
    for value in values:
        result.append(value * 2)
    return result

print(process_data([1, 2, 3]))

# --- Example 05 ---
def double(value):
    return value * 2

print(list(map(double, [1, 2, 3])))

# --- Example 06 ---
measurements = [10.0, 12.0, 14.0]
total = 0.0
for value in measurements:
    total += value
print(total)

# --- Example 07 ---
def calculate_total(values):
    total = 0.0
    for value in values:
        total += value
    return total

print(calculate_total([10.0, 12.0, 14.0]))

# --- Example 08 ---
def double(value):
    return value * 2

measurements = [10.0, 12.0, 14.0]
print(list(map(double, measurements)))

# --- Example 09 ---
class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def describe(self):
        return f"{self.value} {self.unit}"

print(Measurement(25.3, "C").describe())

# --- Example 10 ---
def concentration_from_signal(signal, slope):
    return signal / slope

class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def calculate(self, signal):
        return concentration_from_signal(signal, self.slope)

print(Calibration(2.0).calculate(6.0))

# --- Example 11 ---
def on_measurement_received(value):
    print(f"Received: {value}")

# 이벤트 발생을 직접 호출로 모의한다.
on_measurement_received(25.3)

# --- Example 12 ---
def classify_temperature(value):
    if value > 37.0:
        return "HIGH"
    return "NORMAL"

print(classify_temperature(38.2))

# --- Example 13 ---
def calculate_concentration(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def concentration_from_signal(self, signal):
        return calculate_concentration(signal, self.slope)

calibration = Calibration(slope=2.0)
print(calibration.concentration_from_signal(6.0))

# --- Example 14 ---
signals = [2.0, 4.0, 6.0]
slope = 2.0
concentrations = []
for signal in signals:
    concentrations.append(signal / slope)
print(concentrations)

# --- Example 15 ---
def concentration_from_signal(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

signals = [2.0, 4.0, 6.0]
concentrations = [concentration_from_signal(x, 2.0) for x in signals]
print(concentrations)

# --- Example 16 ---
class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def calculate(self, signal):
        return signal / self.slope

calibration = Calibration(2.0)
print([calibration.calculate(x) for x in [2.0, 4.0, 6.0]])

# --- Example 17 ---
import numpy as np
signals = np.array([2.0, 4.0, 6.0], dtype=np.float64)
print(signals / 2.0)

# --- Example 18 ---
import numpy as np

def scale_inplace(values, factor):
    values *= factor

data = np.array([1.0, 2.0, 3.0])
scale_inplace(data, 2.0)
print(data)

# --- Example 19 ---
import numpy as np

def scaled(values, factor):
    return values * factor

data = np.array([1.0, 2.0, 3.0])
result = scaled(data, 2.0)
print(data)
print(result)

# --- Example 20 ---
signals = [2.0, 4.0, 6.0]
slope = 2.0
if slope <= 0:
    raise ValueError("slope must be positive")

concentrations = []
for signal in signals:
    concentration = signal / slope
    concentrations.append(concentration)
print(concentrations)

# --- Example 21 ---
def concentration_from_signal(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

signals = [2.0, 4.0, 6.0]
concentrations = [concentration_from_signal(x, 2.0) for x in signals]
print(concentrations)
print([concentration_from_signal(x, 4.0) for x in signals])

# --- Example 22 ---
import math
assert math.isclose(concentration_from_signal(6.0, 2.0), 3.0)

# --- Example 23 ---
class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def concentration_from_signal(self, signal):
        return signal / self.slope

calibration = Calibration(slope=2.0)
signals = [2.0, 4.0, 6.0]
print([calibration.concentration_from_signal(x) for x in signals])

calibration_a = Calibration(2.0)
calibration_b = Calibration(4.0)
print(calibration_a.concentration_from_signal(8.0))
print(calibration_b.concentration_from_signal(8.0))

# --- Example 24 ---
def calculate_concentration(signal, slope):
    if slope <= 0:
        raise ValueError("slope must be positive")
    return signal / slope

class Calibration:
    def __init__(self, slope):
        if slope <= 0:
            raise ValueError("slope must be positive")
        self.slope = slope

    def calculate(self, signal):
        return calculate_concentration(signal, self.slope)

calibration = Calibration(2.0)
results = []
for signal in [2.0, 4.0, 6.0]:
    results.append(calibration.calculate(signal))
print(results)

# --- Example 25 ---
import numpy as np
expected = np.array([1.0, 2.0, 3.0])
actual = np.array(results)
assert np.allclose(actual, expected)
