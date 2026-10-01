# 27: Slice the first two rows and first two columns of a 3D array.
import numpy as np
a= np.arange(27).reshape(3,3,3)
print(a)
print(a[0,0:2,0:2])