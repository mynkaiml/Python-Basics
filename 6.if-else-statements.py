# if statements = execute some code only if a condition is True.
#                   they allow for basic decision-making
#                   (if, elif, else)

age = int(input("Enter your age here : "))


if age >= 18:
    print("You are eligible to give vote!")

elif age < 0:
    print("You havent been born yet!")

elif age == 0:
    print("You are a child!")

else:
    print("You are not eligible!")