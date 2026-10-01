# 31:Perform element-wise addition, subtraction, multiplication, and division on two arrays.
import numpy as np
a= np.arange(12).reshape(3,4)
b= np.arange(12,24).reshape(3,4)
c= a+b
d= a-b
e= a*b
f= a/b
print(f"Addition: {c}")
print(f"Substraction: {d}")
print(f"Multiplication: {e}")
print(f"Division: {f}")