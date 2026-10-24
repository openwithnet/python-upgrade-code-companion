# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: WORD_EXTRACT_REASSEMBLED
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
# Chapter 1 / section 1.2.1
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).

# --- Current section: 1.2.1 ---
# manuscript paragraph 41
import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(type(a))
print(a + b)
print(a * b)
print(a @ b)
