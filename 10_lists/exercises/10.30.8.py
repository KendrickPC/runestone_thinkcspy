'''
Sum up all the even numbers in a list.
'''

import random

def sumEven(lst):
    # your code here
    return sum(i for i in lst if not i % 2)

# Generating random numbers lists.

print(sumEven([3, 2, 1]))
print(sumEven([10, 2, 20]))

