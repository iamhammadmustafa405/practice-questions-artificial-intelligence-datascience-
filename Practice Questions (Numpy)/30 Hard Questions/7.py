# Dataset
import numpy as np
sales= np.array([120,340,560, 230, 890, 410, 670, 150, 980, 300])
print(f"Sales: {sales}")
print("--------------------------------------------------")
# 7. Replace Values (in-place modification)

# In sales, replace all values > 500 with -1 using NumPy function (no loops).
# values= np.where(sales>500)
# print(values)
# np.put(sales,values,-1) # changes the original array
# print(f"The Result is : {sales}")


# Easier Method using Boolean Assignment
sales[sales>500] = -1
print(sales)

#  ---------------------------------------------------------------------------------------------------------------------------------
# Important Concept

# This:

# array[condition] = value

# is one of the most used NumPy operations.

# Used constantly in:

# ML preprocessing
# outlier removal
# missing value handling
# feature engineering
# image processing