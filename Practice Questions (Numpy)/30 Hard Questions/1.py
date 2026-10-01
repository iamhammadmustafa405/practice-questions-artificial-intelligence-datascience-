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

# 1. Boolean Masking + Condition Filtering

# From sales, extract all values:

# greater than 400
# and less than 900

# Return as a 1D array.

# less_900= sales[sales<900] # condition in the array
# print(less_900[less_900>400]) # Chained Filtering


# single filtering
result= sales[(sales>400) & (sales<900)]
print(f"Extracted data is: {result}")