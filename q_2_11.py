"""
Python Programming in Context
"""

#################################### 2.11 ######################################
# Write a function that returns the average of the first n numbers, starting at
# 1, including n.
"""
First, intialize variable average. Next add numbers to the value average.
After, divide by the number of numbers and return the value of average.

"""
def average_up_to(n):
    #intialize variable
    average=0
    for num in range(n):
        average=average+(num+1)
    #loop adding numbers to variable average
    average=average/n
    #dividing the sum by the number of numbers to make it the average
    return average
    pass

# This code will compare your answers to the correct ones:
print(f"{average_up_to(1)=}  <-- this should be 1.0")
print(f"{average_up_to(3)=}  <-- this should be 2.0")
print(f"{average_up_to(10)=}  <-- this should be 5.5")
print(f"{average_up_to(100)=}  <-- this should be 50.5")
