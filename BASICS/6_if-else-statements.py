# if statements = execute some code only if a condition is True.
#                   they allow for basic decision-making
#                   (if, elif, else)

age = int(input("Enter your age here : "))
has_ticket = True
price = 10.0


if age >= 65:
    print("You are an senior")
    print(f"The ticket price for a senior is ${price * 0.75}")

if age >= 18:
    print("You are an adult")
    print(f"The ticket price for an adult is ${price}")

else:
    print("You are a child")
    print(f"The ticket price for an child is ${price * 0.5}")

if has_ticket:
    print("you may enter, you have a ticket")
else:
    print("You need to buy a ticket")