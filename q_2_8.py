"""
Python Programming in Context
"""

#################################### 2.8 #######################################
# Compute the sum of the first 100 even numbers. Save the sum to the variable
# sum_100_evens.

sum_100_evens = 0
# USE A FOR LOOP TO UPDATE THE VALUE OF sum_100_evens

for num in range(0,101,2):
    sum_100_evens=num+sum_100_evens


# This is an f string. It starts with `f` before the quotation marks. We can use
# that and the curly brackets to print out the name *and* the value of the
# variable sum_100_evens
print(f"{sum_100_evens=}")
