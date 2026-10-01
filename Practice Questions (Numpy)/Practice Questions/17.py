# 17: Find the sum of all elements in an array.
import numpy as np
a= np.array([5,4,3,2,67,2,98])
sum= 0
for i in a:
    sum+=i
print(f"The sum of all elements in the array is: {sum}")