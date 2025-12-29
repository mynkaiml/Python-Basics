# logical operators = evaluate multiple conditions (or, and , not)
#                      or = atleast one condition must be true
#                      and = both conditions must be true
#                      not = inverts the condition (not False, not True)

temp = 25

is_raining = False

if temp > 35 or temp < 0  or is_raining:  # True if any one statement is true.
    print("Outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")




tmp = 25

is_sunny = True

if tmp >= 28 and is_sunny: # False if any one statement is False.
    print("It is Hot outside")
    print("It is Sunny")
else:
    print("It is not Hot outside")