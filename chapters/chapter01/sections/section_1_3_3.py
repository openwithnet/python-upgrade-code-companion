# Chapter 1 / section 1.3.3
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.3.3 ---
# manuscript paragraph 118
expression = np.array([[10, 20, 30, 40], [12, 18, 33, 39], [15, 22, 29, 45]])
print(expression[1, :])
print(expression[:, 2])
print(expression[1:3, 1:3])
print(expression[1, :].shape, expression[1:2, :].shape)

# manuscript paragraph 122
data = np.arange(24).reshape(2, 3, 4)
print(data[0, :, :].shape)
print(data[..., 2].shape)

# manuscript paragraph 129
import numpy as np
times = np.linspace(0.0, 5.0, 11)
positions = 2.0 + 3.0 * times
print(times[3], positions[3])
print(times[6:9], positions[6:9])

# manuscript paragraph 134
matrix = np.array([[10, 20, 30], [40, 50, 60]])
print(matrix[1, :].shape)   # (3,)
print(matrix[1:2, :].shape) # (1, 3)

# manuscript paragraph 137
data = np.arange(24).reshape(2, 3, 4)
print(data[..., 2].shape)
