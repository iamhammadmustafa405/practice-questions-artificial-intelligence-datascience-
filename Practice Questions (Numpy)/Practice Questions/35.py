# 35: Subtract the mean of each column from a 2D NumPy array using broadcasting.
import numpy as np
matrix= np.arange(9).reshape(3,3)
mean_vector= np.mean(matrix,axis=0) # axis= 0 for column wise mean
result= matrix - mean_vector
print(f"The Result is: {result}")
