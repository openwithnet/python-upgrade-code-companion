"""Chapter 10.6 educational orchestration; depends on unchanged C3 modules."""
from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Mapping
from c3_calibration import CalibrationModel, LinearCalibration, QuadraticCalibration, finite_real
from c3_validation import SignalMeasurement, analyze_measurements

@dataclass(frozen=True)
class ModelResult:
    model_name: str
    concentrations: tuple[float, ...]

@dataclass(frozen=True)
class AnalysisReport:
    measurements: tuple[SignalMeasurement, ...]
    results: tuple[ModelResult, ...]

def run_analysis(measurements: list[SignalMeasurement], models: Mapping[str, CalibrationModel]) -> AnalysisReport:
    if not isinstance(measurements, list):
        raise TypeError('measurements must be a list')
    if not isinstance(models, Mapping):
        raise TypeError('models must be a mapping')
    if not models:
        raise ValueError('at least one model is required')
    for measurement in measurements:
        if not isinstance(measurement, SignalMeasurement):
            raise TypeError('all measurements must be SignalMeasurement')
    entries = []
    for name, model in models.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError('model names must be nonempty strings')
        if not callable(getattr(model, 'predict_concentration', None)):
            raise TypeError('model must provide predict_concentration')
        values = analyze_measurements(measurements, model)
        entries.append(ModelResult(name, tuple(values)))
    return AnalysisReport(tuple(measurements), tuple(entries))

def make_demo_report() -> AnalysisReport:
    samples = [SignalMeasurement(0.001,'V'), SignalMeasurement(3.,'mV'), SignalMeasurement(0.009,'V')]
    return run_analysis(samples, {'linear': LinearCalibration(2.,1.), 'quadratic': QuadraticCalibration(2.,1.)})

if __name__ == '__main__':
    report = make_demo_report()
    for result in report.results:
        print(result.model_name, list(result.concentrations))
