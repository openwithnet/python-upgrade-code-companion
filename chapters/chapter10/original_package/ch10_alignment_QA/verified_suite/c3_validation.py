"""Chapter 9 C3 input-unit boundary; core calibrations remain dimensionless."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from c3_calibration import CalibrationModel, finite_real, analyze_many

SignalUnit = Literal['mV', 'V']

@dataclass(frozen=True)
class SignalMeasurement:
    value: float
    unit: SignalUnit

    def __post_init__(self) -> None:
        value = finite_real(self.value, 'measurement')
        if self.unit not in ('mV', 'V'):
            raise ValueError('unit must be mV or V')
        object.__setattr__(self, 'value', value)

    def as_millivolts(self) -> float:
        factor = 1000.0 if self.unit == 'V' else 1.0
        return finite_real(self.value * factor, 'signal_mV')


def analyze_measurements(
    measurements: list[SignalMeasurement],
    model: CalibrationModel,
) -> list[float]:
    signals_mv = [measurement.as_millivolts() for measurement in measurements]
    return analyze_many(signals_mv, model)
