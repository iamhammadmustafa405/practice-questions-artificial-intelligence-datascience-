# 36: Create a (4, 3) array of random integers and divide each row by:

# [1, 2, 3]

# using broadcasting.
import numpy as np
matrix= np.random.random(12)
matrix= np.round(matrix*100).reshape(4,3)

vector= np.array([1,2,3])

result= matrix/vector
print(f"The Result is: {result}")