# 16: Find the index of the maximum element.
# import numpy as np
# a= np.array([23,42,456,85,90])
# max_idx = np.argmax(a)
# print(f"The Maximum element is: {a[max_idx]} & its index is: {max_idx}")

#                       2nd Method...

import numpy as np
a= np.arange(1,20,2)
max_element= a[0]
idx = 0
for i in range(len(a)):
    if a[i]>max_element:
        max_element= a[i]
        idx= i

print(f"The Maximum element is: {max_element} & its index is: {idx}")