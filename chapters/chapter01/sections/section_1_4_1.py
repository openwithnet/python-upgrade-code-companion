# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: WORD_EXTRACT_REASSEMBLED
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
# Chapter 1 / section 1.4.1
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.4.1 ---
# manuscript paragraph 144
concentrations = np.array([1.2, 1.5, 1.3, 1.8, 1.6])
print(concentrations * 2.0)
a = np.array([1, 2, 3]); b = np.array([4, 5, 6])
print(a * b, a @ b)
print(np.sqrt(np.array([1., 4., 9., 16.])))
