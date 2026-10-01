# 38: Create a (5, 5) matrix and add:

# row-wise values [1, 2, 3, 4, 5]
# then column-wise values [[1], [2], [3], [4], [5]]
import numpy as np
matrix_01= np.random.randint(1,101,size=(5,5))
vector= np.array([1,2,3,4,5])
matrix_02= np.array([[1],[2],[3],[4],[5]])

# row-wise values
row_wise_values= matrix_01+ vector
print(f"Row-wise Values: {row_wise_values}")

# column-wise values
column_wise_values =  matrix_01 + matrix_02
print(f"Column-wise Values: {column_wise_values}")