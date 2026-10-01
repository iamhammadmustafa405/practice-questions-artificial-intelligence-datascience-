# 126: Bank Account (Encapsulation + Getter/Setter)
# Create a class BankAccount:

# Requirements:

# Private attribute: __balance
# Constructor to initialize balance
# Getter method using @property → balance
# Setter method to update balance (only if value is positive)
# Methods:
# deposit(amount) → adds money
# withdraw(amount) → subtracts money if enough balance exists

# Tasks:

# Prevent direct access to __balance
# Ensure negative balance is not allowed
# Use @property and @balance.setter

class Bank_Account:
  def __init__(self,balance):
    self.__balance= balance

  
  
  @property
  def name(self):
    return self.__balance
  

  def deposit(self,amt):


    @self.name.setter
    def balance(self):
        if amt <=0:
          print("Invalid Amount!")
          return
        self.__balance +=amt
      

b= Bank_Account(3000)
print(b.balances)
b.deposit(500)
