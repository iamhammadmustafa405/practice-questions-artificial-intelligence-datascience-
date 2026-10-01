# 19: Reverse an array.
# import numpy as np
# a= np.arange(10)
# revr= []
# for i in range(len(a)-1,-1,-1):
#     revr.append(a[i])

# reverse_array= np.array(revr)
# print(f"The Reversed Array is: {reverse_array}")



# shortcuts
import numpy as np
a= np.arange(10)
# reverse_array= a[::-1]
#   OR
reverse_array = np.flip(a)
print(reverse_array)