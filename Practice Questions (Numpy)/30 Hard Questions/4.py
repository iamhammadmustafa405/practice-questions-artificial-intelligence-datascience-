import numpy as np
# 4. Broadcasting (Row Scaling)
# Divide each row of matrix by scale using broadcasting.

# matrix
matrix= np.arange(1,26).reshape(5,5)

print(f"Matrix: {matrix}")

scale = np.array([1, 2, 3, 4, 5])
print(f"Scale: {scale}")
result= (matrix/scale)
print(f"The Result (by Broadcasting): {result}")