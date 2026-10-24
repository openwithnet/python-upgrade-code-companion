# CODE_COMPANION_ROLE: REFERENCE
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 14 §§14.3–14.6: reconstructed, executable educational examples.
Synthetic data only; none of these models is a validated biological predictor.
"""
from typing import Protocol, Self
import numpy as np
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from sklearn.base import clone
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from ch14_examples import sequence_features

class FitPredictProtocol(Protocol):
    def fit(self, X: np.ndarray, y: np.ndarray) -> Self: ...
    def predict(self, X: np.ndarray) -> np.ndarray: ...


def fit_and_predict(model: FitPredictProtocol, X, y, X_new):
    model.fit(X, y)
    return model.predict(X_new)


class MeanRegressor:
    """Simple duck-typed estimator: predicts the training target mean."""
    def fit(self, X, y):
        X = np.asarray(X)
        y = np.asarray(y, dtype=float)
        if X.ndim != 2 or y.ndim != 1 or len(X) != len(y) or len(y) == 0:
            raise ValueError('Invalid training shapes')
        if not np.all(np.isfinite(y)):
            raise ValueError('Targets must be finite')
        self.mean_ = float(y.mean())
        self.n_features_in_ = X.shape[1]
        return self

    def predict(self, X):
        if not hasattr(self, 'mean_'):
            raise RuntimeError('Fit before predict')
        X = np.asarray(X)
        if X.ndim != 2 or X.shape[1] != self.n_features_in_:
            raise ValueError('Feature count mismatch')
        return np.full(len(X), self.mean_)


def compare_estimators():
    X = np.arange(6.0).reshape(-1, 1)
    y = 1 + 2 * X[:, 0]
    return {type(model).__name__: float(fit_and_predict(model, X, y, [[6]])[0])
            for model in (LinearRegression(), Ridge(alpha=1.0))}


def build_pipeline():
    return Pipeline([('scaler', StandardScaler()), ('regressor', Ridge(alpha=1.0))])


def pipeline_without_leakage(X_train, y_train, X_test):
    """Fit scaler on train only; return fitted pipeline and test prediction."""
    model = build_pipeline()
    model.fit(X_train, y_train)
    return model, model.predict(X_test)


RAW_SEQUENCES = [
    ('S01','ATATATAT'), ('S02','ATGCATGC'), ('S03','GCGCGCGC'),
    ('S04','AATTGGCCAA'), ('S05','GGCCGGCCAA'), ('S06','ATATGCATATGC'),
    ('S07','GCGCATGCGCAT'), ('S08','AAAACCCCGGGG'), ('S09','ATGCATGCATGCAT'),
    ('S10','GGGGCCCCAAAATT'), ('S11','ATATATATATATATAT'), ('S12','GCGCGCGCGCGCGCGC')]
NOISE = np.array([.01,-.02,.01,0,-.01,.01,-.01,.02,-.02,.01,-.01,0])


def run_sequence_analysis():
    records = [SeqRecord(Seq(seq), id=rid, description='Synthetic teaching example')
               for rid, seq in RAW_SEQUENCES]
    X = np.vstack([sequence_features(record) for record in records])
    # The manuscript uses GC percentage for targets, not fractional GC ratio.
    X[:, 1] *= 100
    y = .05 * X[:, 0] + .02 * X[:, 1] + NOISE
    model, predictions = pipeline_without_leakage(X[:9], y[:9], X[9:])
    return {'ids': [r.id for r in records[9:]], 'X': X, 'y': y,
            'predictions': predictions, 'y_test': y[9:],
            'rmse': float(np.sqrt(mean_squared_error(y[9:], predictions))),
            'scaler_mean': model.named_steps['scaler'].mean_, 'pipeline': model}
