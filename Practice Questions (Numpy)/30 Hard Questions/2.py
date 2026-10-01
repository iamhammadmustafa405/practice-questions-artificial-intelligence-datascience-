# Dataset
import numpy as np
sales= np.array([120,340,560, 230, 890, 410, 670, 150, 980, 300])
profit = np.array([20, 50, 80, 30, 120, 60, 90, 25, 140, 45])
region = np.array(['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'])

matrix= np.arange(1,26).reshape(5,5)
print(f"Sales: {sales}")
print(f"Profit: {profit}")
print(f"Region: {region}")
print(f"Matrix: {matrix}")
print("--------------------------------------------------")

# 2. Multi-condition Filtering (AND / OR)

# From sales, return values where:

# (value < 200 OR value > 800)
# AND
# corresponding region is not 'B'

# Return filtered sales array.

# My logic

# result =sales[(sales<200) | (sales>800)]
# print(result)


# l1=[]
# l2= []
# for i in range(len(sales)):
#     l2.insert(0,sales[i])
#     l2.insert(1,region[i])
#     l1.append(l2)

# l1= np.array(l1)
# print(l1)

# real solution by boolean masking
result = sales[((sales<200)  | (sales>800))  & (region != "B")] # Boolean Masking
print(result)