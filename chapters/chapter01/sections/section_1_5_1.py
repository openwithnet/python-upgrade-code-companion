# Chapter 1 / section 1.5.1
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).

# --- Current section: 1.5.1 ---
# manuscript paragraph 187
import numpy as np
expression = np.array([[10,20,30,40],[12,18,33,39],[15,22,29,45]], dtype=np.float64)
sample_names = ["Sample 1", "Sample 2", "Sample 3"]
gene_names = ["Gene A", "Gene B", "Gene C", "Gene D"]
print(expression.shape, expression.dtype)
