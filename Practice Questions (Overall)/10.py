# Write a program that converts a temperature given by the user. Ask whether the input is in Celsius
# or Fahrenheit, then convert it to the other unit. Formulas: C = (F − 32) × 5/9 and F = C × 9/5 + 32.


def temp_converter(scale,temp):

    if scale.lower() == "celsius" or scale.lower() == "centigrade" or scale.lower() == "degree centigrade" or scale.lower() =="degree"  or scale.lower() =="c":
        F= temp * (9/5) +32
        print(f"Temperature in Fahrenhiet is : {round(F,2)} degrees fahrenhiet.")
    elif scale.lower() == "fahrenhiet" or scale.lower() == "degree fahrenhiet" or scale.lower() =="f":
        C = (temp-32) * (5/9)
        print(f"Temperature in Centigrade/Celsius is: {round(C,2)} degrees centigrade.")

for i in range(5):
    scale= input("In which scale you want to enter: ")
    temp= float(input("Enter the temperature:"))
    temp_converter(scale=scale,temp=temp)