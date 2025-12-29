# While Loop = used to repeat a block of code as long as the given condition is true.
#              we-recheck the condition at the end of the loop


number = 1 

print("Counting from 1 to 5")

while number <=5:
    print(number)
    number+=1



name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age here: "))

while age < 0:
    print("Please enter an valid age here please: ")
    age = int(input("Enter your age here: "))


print(f"Hello {name}")
print(f"You are {age} years old")