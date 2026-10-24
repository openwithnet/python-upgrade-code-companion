# CODE_COMPANION_ROLE: REFERENCE
# CODE_COMPANION_PROVENANCE: WORD_BASED_REPRESENTATIVE_RECONSTRUCTION
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
"""Chapter 12 §12.4–12.5: self-contained reconstructed teaching examples.
Not a verbatim extraction of every Word code block.
"""
import numpy as np

def boolean_indexing():
    measurements = np.array([1.2, 3.5, 2.8, 5.1, 4.2])
    mask = measurements > 3.0
    selected = measurements[mask]
    between = measurements[(measurements >= 2.0) & (measurements < 5.0)]
    outside = measurements[(measurements < 2.0) | (measurements >= 5.0)]
    return mask, selected, between, outside

def advanced_indexing():
    values = np.array([10, 20, 30, 40, 50]); selected = values[[1, 4]]
    a = np.arange(10); basic = a[2:6]; advanced = a[[2,3,4,5]]
    return selected, np.shares_memory(a,basic), np.shares_memory(a,advanced)

def reshape_transpose():
    a = np.arange(12); b = a.reshape(3,4)
    matrix = np.array([[1,2,3],[4,5,6]])
    return b.shape, a.reshape(3,-1).shape, a.reshape(-1,6).shape, matrix.T.shape

def view_copy():
    a = np.array([10,20,30,40,50]); b = a[1:4]; b[0] = 200
    raw = np.array([10.,20.,30.,40.]); work = raw[1:3].copy(); work *= 2
    return a, raw, work

def strides():
    a=np.arange(12,dtype=np.float64).reshape(3,4)
    return a.shape,a.itemsize,a.strides,a[1,2]

def in_place_contract():
    raw=np.array([10.,20.,30.,40.]); working=raw[1:3];working*=2
    bad_dtype=False
    try: np.array([1,2,3])*1.5  # out-of-place valid
    except Exception: raise
    try: x=np.array([1,2,3]);x*=1.5
    except (TypeError,ValueError):bad_dtype=True
    return raw,bad_dtype
