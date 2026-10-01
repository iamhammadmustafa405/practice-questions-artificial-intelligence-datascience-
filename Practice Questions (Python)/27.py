# 27: Use a while loop to find the Fibonacci series upto n terms.
n= int(input("Enter Number of Terms: "))
first_term = 0
second_term = 1
print(first_term)
print(second_term)
count = 2

while count <=n:
    next_term = second_term + first_term
    print(next_term)
    first_term = second_term
    second_term = next_term
    count+=1