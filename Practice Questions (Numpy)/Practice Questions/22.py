# 22: Extract only even numbers from an array.
# import numpy as np
# l= []
# for i in range(5):
#     n= int(input("Enter a Number: "))
    
#     l.append(n)

# a= np.array(l)

# even_list= []
# for i in a:
#     if i%2 ==0:
#         even_list.append(i)


# even_array= np.array(even_list)
# print(f"The Array of Even Numbers is: {even_array}")


# By using Boolean Indexing

import numpy as np
a= np.array([3,4,5,6,7,8,9])
even= a[a%2==0]
print(even)