# A function in Python is a named, reusable block of code that performs a specific, related action or task when it is called

def greet(name):
    print(f"Hello {name}")

name = input("Enter your name here: ")

# greet(name)  # Function Call


if name == "Mayank":
    greet(name) # Function Call
else:
    print("Enter correct name")



def add(a ,b): # Parameterized Function
    return a + b

# print(add(100,1000)) # Function Call


num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

print(add(num1, num2))




def find_max(a, b):
    if a > b:
        return a
    else:
        return b
    
a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))

print("The Max Number is : ",find_max(a,b))



# We can make As many function we want.
