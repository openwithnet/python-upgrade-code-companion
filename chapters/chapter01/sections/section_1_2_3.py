# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: WORD_EXTRACT_REASSEMBLED
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
# Chapter 1 / section 1.2.3
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.2.3 ---
# manuscript paragraph 66 (v37 G4 QA; zero-based)
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print(zeros.shape, ones.shape)

# manuscript paragraph 71 (v37 G4 QA; zero-based)
times1 = np.arange(0, 5, 1)
times2 = np.linspace(0.0, 10.0, 101)
print(times1)
print(times2.shape, times2[0], times2[-1])

# manuscript paragraph 76 (v37 G4 QA; zero-based)
values = np.array([1.9, 2.7, 3.2])
print(values.astype(np.int64))
print(np.array([1, 2, 3], dtype=np.float64).dtype)

# manuscript paragraph 86 (v37 G4 QA; zero-based)
single = np.array([1.25, 2.50], dtype=np.float32)
double = np.array([1.25, 2.50], dtype=np.float64)
print(single.dtype, single.itemsize)
print(double.dtype, double.itemsize)

# manuscript paragraph 90 (v37 G4 QA; zero-based)
ragged = [[1, 2, 3], [4, 5]]
try:
    np.array(ragged)
except ValueError:
    print('ValueError: 행의 길이가 일정하지 않음')
