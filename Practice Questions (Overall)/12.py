# Write a program that keeps a running total. The user enters numbers one by one (type 'done' to
# stop). After stopping, print the total, how many numbers were entered, and the average.
num= input("Enter a Number: ")

sum= 0
count= 0
while True:
    if num.isdigit():
        sum+=int(num)
        count+=1
    if (num.lower() == "done") or (not num.isdigit()):
        break
    else:
        num= input("Enter a Number: ")

print(f"Total is: {sum}")
print(f"Total Numbers you entered:  {count}")
print(f"The avg is: {round(sum/count,2)}")
