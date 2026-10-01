# 23: Replace all odd numbers in an array with -1.
import numpy as np
size= int(input("How many numbers you want in array: "))
nums= []

for i in range(size):
    n= int(input("Enter a Number: "))
    nums.append(n)

numbers = np.array(nums)
print(f"The Original Array is: {numbers}")

for i in range(len(numbers)):
    if  numbers[i] %2 != 0:
        numbers[i] = -1

print(f"The Updated Array is: {numbers}")
        
# improve code


import numpy as np

size = int(input("How many numbers? "))
nums = [int(input(f"Enter number {i + 1}: ")) for i in range(size)]

numbers = np.array(nums)
print(f"Original Array : {numbers}")

# ✅ NumPy vectorized boolean masking — no loop needed!
numbers[numbers % 2 != 0] = -1

print(f"Updated Array  : {numbers}")