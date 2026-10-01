# 6. Advanced Indexing (fancy indexing)
import numpy as np

# Extract elements from matrix using coordinates:

# My Logic
# matrix= np.arange(1,26).reshape(5,5)
# matrix= np.flip(matrix,axis= 0)
# print(matrix)
# rows = np.array([0, 1, 2, 3, 4])
# cols = np.array([4, 3, 2, 1, 0])

# Return selected diagonal-like elements.
# result= np.diagonal(matrix)
# print(result)

# Main Method by using Fancy Indexing ( i also do it without any help)

matrix= np.arange(1,26).reshape(5,5)
print(matrix)

rows = np.array([0, 1, 2, 3, 4])
cols = np.array([4, 3, 2, 1, 0])
# result= matrix[[0,1,2,3,4],[4,3,2,1,0]] # fancy indexing in 2d array
result= matrix[[rows],[cols]]
print(result)