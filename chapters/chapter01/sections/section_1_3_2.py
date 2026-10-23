# Chapter 1 / section 1.3.2
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.3.2 ---
# manuscript paragraph 105
values = np.array([10, 20, 30, 40, 50, 60])
print(values[1:4])
print(values[::2])
print(values[::-1])

# manuscript paragraph 109
times = np.linspace(0.0, 10.0, 11)
positions = 2.0 * times
print(times[3:7])
print(positions[3:7])
