# 10: Change the datatype of an array from integer to float.
import numpy as np
a= np.arange(1,6)
a= a.astype(np.float64)
print(a.dtype)