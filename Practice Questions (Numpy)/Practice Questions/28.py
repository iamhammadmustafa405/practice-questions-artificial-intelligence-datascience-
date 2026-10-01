# 28: Slice the first two rows and first two columns of a 3 x 3 array.
import numpy as np
a = np.arange(9).reshape(3,3)
print(a[0:2,0:2])