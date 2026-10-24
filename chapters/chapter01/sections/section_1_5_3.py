# CODE_COMPANION_ROLE: EXECUTABLE
# CODE_COMPANION_PROVENANCE: WORD_EXTRACT_REASSEMBLED
# CODE_COMPANION_RELEASE: RETAIN_AS_CANDIDATE_NOT_FROZEN
# Chapter 1 / section 1.5.3
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.5.3 ---
# manuscript paragraph 221
expression_list = [[10,20,30,40],[12,18,33,39],[15,22,29,45]]
n_samples = len(expression_list); n_genes = len(expression_list[0])
means_list = []
for j in range(n_genes):
    total = 0.0
    for i in range(n_samples):
        total += expression_list[i][j]
    means_list.append(total / n_samples)
means_numpy = np.mean(np.array(expression_list, dtype=float), axis=0)
print(np.allclose(means_list, means_numpy))

# manuscript paragraph 223
True
