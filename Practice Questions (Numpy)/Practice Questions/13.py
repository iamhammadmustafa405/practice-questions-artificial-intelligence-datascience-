# 13: Find the square of every element in an array.
import numpy as np
a= np.arange(1,13).reshape(4,3)
print(a)
sq = a**2
print(f"The Squared Array is: {sq}")