# 33: Multiply a 1D array [1, 2, 3] with a 2D array:

# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# using broadcasting.
import numpy as np
a= np.arange(1,4)
b= np.arange(1,10).reshape(3,3)
result= a*b
print(result)