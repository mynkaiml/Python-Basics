# Creating a class named Calculator
# This class contains utility methods for calculations
class Calculator:

    # Static method
    # It does not use self or class variables
    # It performs addition of two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Another static method
    # It performs multiplication of two numbers
    @staticmethod
    def multiply(a, b):
        return a * b


# Calling static methods using the class name
# No object creation is needed
result1 = Calculator.add(10, 5)
result2 = Calculator.multiply(4, 3)

# Printing the results
print("Addition:", result1)        # Output: 15
print("Multiplication:", result2)  # Output: 12
