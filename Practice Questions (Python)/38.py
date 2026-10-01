# 38: Keep asking for a password until the correct one is entered.
# password= "Hammad@456"
# pass_word= input("Enter Password:")
# while pass_word != password:
#     print("Wrong Password, Try Again, Hint: @456")
#     pass_word= input("Enter Password: ")
# print("Congratulations, You Entered the Correct Password.")

password= "Hammad@456"
while True:
    user_input= input("Enter password: ")
    if user_input == password:
        print("Correct Password!")
        break
    else:
        print("Wrong Password , try again!")