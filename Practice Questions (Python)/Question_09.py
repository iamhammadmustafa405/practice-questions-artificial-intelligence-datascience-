# Question - 09: Write a program to print the first & last Character of the string.
str= input("Enter your name: ")
if len(str) == 0:
    print("The string is empty.")
else:   
    print(f"the first character {str[0]}")
    print(f"the last character {str[len(str)-1]}")
