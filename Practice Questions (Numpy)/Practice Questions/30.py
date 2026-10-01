# 30: How do you flatten a multidimensional array into 1D?
import numpy as np
a= np.arange(27).reshape(3,3,3)
a= np.ravel(a)
print(a)