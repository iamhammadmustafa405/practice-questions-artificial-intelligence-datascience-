# Print the following number pyramid for n = 5 (ask n from the user):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Each row should be centred. The numbers inside each row should be separated by a space

def num_pattern(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j ,end= " ")
        
        print(" ")

num_pattern(4)
num_pattern(10)