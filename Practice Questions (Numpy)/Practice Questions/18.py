# 18: Find the mean, median, and standard deviation of an array.
import numpy as np
a= np.arange(1,13).reshape(4,3)
print(a)
arr_mean= np.mean(a)
arr_median= np.median(a)
arr_std = np.std(a)
arr_var = np.var(a)
print(f"The Mean of the Array is: {arr_mean}")
print(f"The Median of the Array is: {arr_median}")
print(f"The Standard Deviation of the Array is: {arr_std}")
print(f"The Variance of the Array is: {arr_var}")