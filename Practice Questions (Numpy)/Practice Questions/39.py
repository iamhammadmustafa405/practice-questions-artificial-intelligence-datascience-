# 39: Normalize a dataset:
# Create a random (4, 3) array.
# Subtract the minimum value of each column from that column using broadcasting.
import numpy as np
matrix= np.random.randint(1,201,size=(4,3))
print(matrix)
# min vector

min_vector= np.min(matrix,axis= 0) # axis = 0 for column-wise
print(min_vector)

# subtracting..
result= matrix-min_vector
print(f"The result is: {result}")