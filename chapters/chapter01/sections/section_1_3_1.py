# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: WORD_EXTRACT_REASSEMBLED
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
# Chapter 1 / section 1.3.1
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.3.1 ---
# manuscript paragraph 97
temperatures = np.array([20.5, 21.0, 20.8, 21.3, 20.9])
print(temperatures[0], temperatures[-1])
measurements = np.array([[1.2, 3.4, 2.1], [1.5, 3.1, 2.4], [1.3, 3.6, 2.2]])
print(measurements[1, 2])
