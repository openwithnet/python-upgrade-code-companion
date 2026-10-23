"""Chapter 12 sections 12.1–12.3: manuscript-aligned canonical teaching examples.
Reassembled from code statements in the manuscript; this is NOT an original release source.
"""
import numpy as np

def decay_vectorized():
    # 12.1.1, original manuscript paragraphs 123–139
    c0 = 1.0
    k = 0.2
    times = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    concentrations = c0 * np.exp(-k * times)
    return concentrations

def axis_means():
    # 12.1.2, original manuscript paragraphs 244–266
    concentrations = np.array([
        [1.0, 0.8, 0.6, 0.5],
        [1.1, 0.9, 0.7, 0.6],
        [0.9, 0.7, 0.5, 0.4],
    ])
    mean_by_time = np.mean(concentrations, axis=0)
    mean_by_experiment = np.mean(concentrations, axis=1)
    return mean_by_time, mean_by_experiment

def broadcasting():
    # 12.3.1, original manuscript paragraphs 966–980
    a = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ])
    b = np.array([10, 20, 30, 40])
    result = a + b
    return result

if __name__ == '__main__':
    print('12.1 decay:', np.round(decay_vectorized(), 6))
    print('12.1 by time:', axis_means()[0])
    print('12.1 by experiment:', axis_means()[1])
    print('12.3 broadcast:\n', broadcasting())
