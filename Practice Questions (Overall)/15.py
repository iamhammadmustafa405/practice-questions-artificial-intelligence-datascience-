# Write a program that generates the first 20 numbers of the Fibonacci sequence and stores them in
# a list. Then: (a) print all even Fibonacci numbers, (b) print the sum of all Fibonacci numbers in the
# list.

first_num= 0
second_num = 1
fab = []

for i in range(20):
    next_num= first_num + second_num
    fab.append(next_num)
    first_num= second_num
    second_num=next_num

#a print all even Fibonacci numbers,

for num in fab:
    if num % 2 == 0:
        print(num)

# (b) print the sum of all Fibonacci numbers in the
# # list

sum= 0
for num in fab:
    sum+=num

print(f"The sum is: {sum}")
