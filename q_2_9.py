"""
Python Programming in Context
"""


#################################### 2.9 #######################################
# Compute the sum of the first 50 odd numbers. Save the sum to the variable
# sum_50_odds

sum_50_odds = 0
# USE A FOR LOOP TO UPDATE THE VALUE OF sum_50_odds

"""
The loop starts at 1 and has a step of 2 to 51 therefore adding all numbers
0-50 that are odd. The step by 2 ensures they are odd and counting to 51
ensures that all numbers are counted. 
"""

for num in range(1,51,2):
    sum_50_odds=num+sum_50_odds


# Write an f string to print out the name *and* value of sum_50_odds
print(f"{sum_50_odds=}")