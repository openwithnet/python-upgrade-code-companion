# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: ARCHIVED_CHAPTER_REVIEW_COPY
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""C3: interchangeable calibration models (educational, dimensionless)."""
from __future__ import annotations
from dataclasses import dataclass
from math import isfinite, sqrt
from typing import Protocol


def finite_real(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f'{name} must be a real number')
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f'{name} must be finite') from exc
    if not isfinite(result):
        raise ValueError(f'{name} must be finite')
    return result


class CalibrationModel(Protocol):
    def predict_concentration(self, signal: float) -> float: ...


@dataclass(frozen=True)
class LinearCalibration:
    slope: float
    intercept: float

    def __post_init__(self) -> None:
        slope = finite_real(self.slope, 'slope')
        intercept = finite_real(self.intercept, 'intercept')
        if slope <= 0:
            raise ValueError('slope must be positive')
        object.__setattr__(self, 'slope', slope)
        object.__setattr__(self, 'intercept', intercept)

    def predict_concentration(self, signal: float) -> float:
        signal = finite_real(signal, 'signal')
        if signal < self.intercept:
            raise ValueError('signal is below the zero-concentration response')
        result = (signal - self.intercept) / self.slope
        return finite_real(result, 'concentration')


@dataclass(frozen=True)
class QuadraticCalibration:
    coefficient: float
    intercept: float

    def __post_init__(self) -> None:
        coefficient = finite_real(self.coefficient, 'coefficient')
        intercept = finite_real(self.intercept, 'intercept')
        if coefficient <= 0:
            raise ValueError('coefficient must be positive')
        object.__setattr__(self, 'coefficient', coefficient)
        object.__setattr__(self, 'intercept', intercept)

    def predict_concentration(self, signal: float) -> float:
        signal = finite_real(signal, 'signal')
        if signal < self.intercept:
            raise ValueError('signal is below the zero-concentration response')
        adjusted = (signal - self.intercept) / self.coefficient
        return finite_real(sqrt(adjusted), 'concentration')


def analyze_signal(signal: float, model: CalibrationModel) -> float:
    return model.predict_concentration(signal)


def analyze_many(signals: list[float], model: CalibrationModel) -> list[float]:
    return [analyze_signal(signal, model) for signal in signals]


if __name__ == '__main__':
    for model in (LinearCalibration(2, 1), QuadraticCalibration(2, 1)):
        print(type(model).__name__, analyze_many([1.0, 3.0, 9.0], model))
