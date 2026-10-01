# 29: How do you reshape a 1D array of 12 elements into a 3×4 matrix?
import numpy as np
a= np.arange(12)
a= a.reshape(3,4)
print(a)