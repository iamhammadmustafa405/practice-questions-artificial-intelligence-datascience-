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



# 3. Indexing + Region Mapping

# Return all profit values where region is 'A', but output them in reverse order.
result= profit[region == "A"]
result= result[::-1]
print(f"The Result is: {result}")