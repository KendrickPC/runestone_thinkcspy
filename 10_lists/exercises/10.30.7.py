'''
Write a function that counts how many odd numbers are in a list.
'''

import random


def countOdd(lst):
    # your code here
    odd_lst = 0
    for e in lst:
        if e % 2 != 0:
            odd_lst = odd_lst + 1
    return odd_lst


# Generating random list of odd numbers for our test function.
lst = []
for i in range(100):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))

