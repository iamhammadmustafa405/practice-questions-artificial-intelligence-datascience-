# # Write a program that prints all Armstrong numbers between 1 and 999. An Armstrong number
# equals the sum of its digits each raised to the power of the number of digits. (Example: 153 = 1³ + 5³ + 3³ = 153 ✓)



armstrong_list= []

for i in range(1,1000):
    l = []
    for j in str(i):
        digit = int(i)**3
        l.append(digit)
        

    sum= 0
    for k in l:
        sum+=k

    if i == sum:
        armstrong_list.append(sum)

print(armstrong_list)
