# 21: Create an array from 1 to 20 and print:
# First 5 elements
# Last 5 elements
# Elements from index 5 to 15
import numpy as np
a= np.arange(1,21)
b= a[:5]
print(b)
c= a[-5:]
print(c)
d= a[5:16]
print(d)