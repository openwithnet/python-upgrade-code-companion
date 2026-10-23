# Chapter 1 / section 1.4.2
# Prerequisite definitions replayed in the original manuscript order.
# Source: v37 Word, exact original code blocks (comments inserted only).

# Dependencies retained from original manuscript (minimal verified subset).
# prerequisite: 1.1.3 NumPy가 필요한 이유 / p32
import numpy as np
values = [1, 2, 3]
array = np.array(values)
print(values * 2)
print(array * 2)


# --- Current section: 1.4.2 ---
# manuscript paragraph 157
times = np.linspace(0.0, 5.0, 6)
x0 = 2.0; velocity = 3.0
positions = x0 + velocity * times
print(positions)
