# 32: Add a scalar 5 to every element of a NumPy array [1, 2, 3, 4, 5] using broadcasting.
import numpy as np
a = np.arange(1,6)
rslt= a + 5
print(rslt)