# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: WORD_EXTRACT_REASSEMBLED
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
# Chapter 1 / section 1.2.2
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.2.2 ---
# manuscript paragraph 52 (v37 G4 QA; zero-based)
vector = np.array([10, 20, 30, 40], dtype=np.int64)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(vector.ndim, vector.shape, vector.size, vector.dtype)
print(matrix.ndim, matrix.shape, matrix.size)

# manuscript paragraph 56 (v37 G4 QA; zero-based)
data = np.zeros((2, 3, 4))
scalar_array = np.array(3.14)
print(data.shape, data.size)
print(scalar_array.ndim, scalar_array.shape)
