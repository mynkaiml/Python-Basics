# Recursion is a technique where a function calls itself to solve a problem in smaller steps until a stopping condition is reached.


# Multiplication without using multiply operator By using Recursion.

def mul(a, b):
    if b == 1: # Base case

        return a
    else:
        return a + mul(a, b-1) # Recursion
    
print(mul(2,3)) # Function Call  # Answer will be 6 



# Printing Numbers from 1 to n using Recursion.

def num(n):
    if n == 0: # Base Case
        return
    num(n-1)
    print(n)

num(50) # Function Call


# Factorial of number using Recursion.

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * num(n-1)

print(fact(8))


# Sum of first n natural numbers By recursion.

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))   


# Walking Steps by recursion.

def walk(steps):
    if steps == 0:
        return
    walk(steps-1)

    print(f"You walked {steps} steps")

walk(10)