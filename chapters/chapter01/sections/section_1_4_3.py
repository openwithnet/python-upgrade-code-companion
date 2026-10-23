# Chapter 1 / section 1.4.3
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.4.3 ---
# manuscript paragraph 166
values = np.array([10., 12., 11., 13., 14.])
print(np.sum(values), np.mean(values))
print(round(np.std(values), 6), round(np.std(values, ddof=1), 6))

# manuscript paragraph 172
expression = np.array([[10., 20., 30.], [12., 18., 33.], [15., 22., 29.]])
print(np.mean(expression, axis=0))
print(np.mean(expression, axis=1))
print(np.mean(expression, axis=1, keepdims=True).shape)
