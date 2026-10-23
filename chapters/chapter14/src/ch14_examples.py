"""Chapter 14, representative runnable examples based on textbook §§14.2–14.6.
Reconstructed examples, not a verbatim full-manuscript export.
"""
import numpy as np
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def dna_operations(sequence='ATGAAATTTTAA'):
    dna = Seq(sequence)
    return {'complement':str(dna.complement()), 'reverse_complement':str(dna.reverse_complement()), 'rna':str(dna.transcribe()), 'protein':str(dna.translate())}


def fit_linear_example():
    X=np.arange(6.0).reshape(-1,1)
    y=1+2*X[:,0]
    model=LinearRegression().fit(X,y)
    return model,float(model.predict([[6.]])[0])


def sequence_features(record: SeqRecord):
    sequence=str(record.seq).upper()
    if not sequence or any(base not in 'ACGT' for base in sequence):
        raise ValueError('Expected nonempty unambiguous DNA sequence')
    return np.array([len(sequence), sum(b in 'GC' for b in sequence)/len(sequence)], dtype=float)


def fit_sequence_pipeline(records, y):
    X=np.vstack([sequence_features(r) for r in records])
    y=np.asarray(y,dtype=float)
    if y.ndim!=1 or len(y)!=len(records):
        raise ValueError('Target count must match records')
    pipeline=Pipeline([('scaler',StandardScaler()),('regressor',Ridge(alpha=1.0))])
    pipeline.fit(X,y)
    return pipeline,X
