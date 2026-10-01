# 14: Find the cube root of elements in an array.
import numpy as np
# a= np.arange(1,11).reshape(5,2)
# cube= a**(1/3)
# print(cube)


# 2nd Method
a= np.arange(1,11).reshape(5,2)
cube= np.cbrt(a)
print(f"The Cube root of Array is: {cube}")