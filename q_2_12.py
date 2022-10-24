"""
Python Programming in Context
"""

# This module is used to compare your implementation of factorial to a correct
# one.
import math


#################################### 2.12 ######################################
# Write a function called factorial that computes the product of the first n
# numbers, starting at 1, including n.
# Use a for loop and an accumulator variable.

"""
First intialize the value of factorail_total to one because we are using
multiplication. Next multiply factorial total by the number in the sequence
to find the total factorial. Return the value factorial_total.
"""

def factorial(n):
    factorial_total=1
    for num in range(n):
        factorial_total=(num+1)*factorial_total
    return factorial_total
    pass

# This code will compare your answers to the correct ones:
print(f"{factorial(1)=}  <-- this should be {math.factorial(1)}")
print(f"{factorial(3)=}  <-- this should be {math.factorial(3)}")
print(f"{factorial(5)=}  <-- this should be {math.factorial(5)}")
