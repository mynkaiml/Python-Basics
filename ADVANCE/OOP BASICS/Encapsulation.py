# Creating a class named BankAccount
# This class demonstrates encapsulation
class BankAccount:

    # Constructor to initialize account details
    def __init__(self, name, balance):

        # Public variable (can be accessed directly)
        self.name = name

        # Private variable (cannot be accessed directly outside the class)
        self.__balance = balance

    # Public method to display account holder name
    def show_name(self):
        print("Account Holder:", self.name)

    # Public method to access private balance safely
    def get_balance(self):
        return self.__balance

    # Public method to update private balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # Public method to withdraw money safely
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount


# Creating an object of the BankAccount class
account = BankAccount("Mayank", 1000)

# Accessing public variable
print(account.name)   # Output: Mayank

# Accessing private variable using public method
print(account.get_balance())   # Output: 1000

# Modifying private data using methods
account.deposit(500)
account.withdraw(200)

# Checking updated balance
print(account.get_balance())   # Output: 1300
