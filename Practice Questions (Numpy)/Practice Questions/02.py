# 02: Create a NumPy array with values from 1 to 10.
import numpy as np
a= np.array([1,2,3,4,5,6,7,8,9,10])
print(a,type(a))
b= np.arange(1,11,dtype= int)
print(f"Array: {b}")