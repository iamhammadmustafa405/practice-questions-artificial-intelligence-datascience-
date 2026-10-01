# 5. Column-wise Operation (Broadcasting)
# Add a column vector:
import numpy as np
col = np.array([[1], [2], [3], [4], [5]])
print(f"Column Vector: {col}")
# Add it to matrix using broadcasting.
import numpy as np
matrix= np.arange(1,26).reshape(5,5)
print(f"Matrix: {matrix}")

result = (matrix + col)
print(f"The result using Broadcasting: {result}")