"""
Python Programming in Context
"""

#################################### 2.10 ######################################
# Compute the average of the first 100 odd numbers. Save the sum to a variable
# and print its name and value using an f string

sum_100_odds_average=0

"""
The loop starts at 1 and has a step of 2 to 101 therefore adding all numbers
0-101 that are odd. The step by 2 ensures they are odd and counting to 101
ensures that all numbers are counted. After it is averaged by dividing by the
number of terms, 50.
"""

for num in range(1,101,2):
    sum_100_odds_average=num+sum_100_odds_average

sum_100_odds_average=sum_100_odds_average/50

# f string to printout the name of the variable and the value

print(f"{sum_100_odds_average=}")