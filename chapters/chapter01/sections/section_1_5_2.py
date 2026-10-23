# Chapter 1 / section 1.5.2
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.5.1 행렬의 데이터 표현 / p187
import numpy as np
expression = np.array([[10,20,30,40],[12,18,33,39],[15,22,29,45]], dtype=np.float64)
sample_names = ["Sample 1", "Sample 2", "Sample 3"]
gene_names = ["Gene A", "Gene B", "Gene C", "Gene D"]
print(expression.shape, expression.dtype)


# --- Current section: 1.5.2 ---
# manuscript paragraph 196
gene_means = np.mean(expression, axis=0)
sample_means = np.mean(expression, axis=1)
gene_c = expression[:, 2]
difference = expression[1, :] - expression[0, :]
ratio = expression[1, :] / expression[0, :]
print(np.round(gene_means, 3))
print(sample_means)
print(gene_c)
print(difference)
print(np.round(ratio, 3))

# manuscript paragraph 207
sample1 = expression[0, :]
sample2 = expression[1, :]
print(sample2 - sample1)
print(np.round(sample2 / sample1, 3))

# manuscript paragraph 212
sample_names = ['Sample 1', 'Sample 2', 'Sample 3']
gene_names = ['Gene A', 'Gene B', 'Gene C', 'Gene D']
assert expression.shape == (len(sample_names), len(gene_names))
for gene, mean_value in zip(gene_names, np.mean(expression, axis=0)):
    print(f'{gene}: {mean_value:.2f}')

# manuscript paragraph 216
assert expression.shape == (3, 4)
assert len(sample_names) == expression.shape[0]
assert len(gene_names) == expression.shape[1]
print(np.mean(expression, axis=1))
