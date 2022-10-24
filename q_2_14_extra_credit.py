"""
Python Programming in Context
"""

#################################### 2.14 ######################################
#                 _                                 _ _ _   
#         _____  _| |_ _ __ __ _    ___ _ __ ___  __| (_) |_ 
#         / _ \ \/ / __| '__/ _` |  / __| '__/ _ \/ _` | | __|
#         |  __/>  <| |_| | | (_| | | (__| | |  __/ (_| | | |_ 
#         \___/_/\_\\__|_|  \__,_|  \___|_|  \___|\__,_|_|\__|
# .
# This question is optional. Make sure to complete 2.13 first, as this question
# builds on that one. Write a function to compute the Nth Fibonacci number,
# where n is a parameter. You may assume that n will be greater than or equal to
# 3.


"""
Intialize variables. Then repeat n-2 amounts which is set to 10-2 currently.
We need the minus two because num_1 and num_2 are two of the numbers in the 
sequence. Then return the total and print the value.

"""
def fibbonacci(n):
    num_1=1
    num_2=1
    total=0
    for _ in range(n-2):
        total=num_1+num_2
        num_2=num_1
        num_1=total
    return total
pass

#replace 5 with any number that you want and it will show that position in the sequence

print(f"{fibbonacci(5)=}")
