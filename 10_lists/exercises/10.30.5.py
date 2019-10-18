'''
Write a Python function that will take a the list of 100 random
integers between 0 and 1000 and return the maximum value.
(Note: there is a builtin function named max but pretend you
cannot use it.)
'''

import random

# Global Scope List of Random Number List
random_num_list = []

def createRandomList():
    for i in range(100):
        new_int = random.randrange(0, 1000)
        random_num_list.append(new_int)
    return random_num_list

createRandomList()


def max(random_num_list):
    max = 0
    for e in random_num_list:
        if e > max:
            max = e
    return max


print("\nMaximum Number in List:")
print(max(random_num_list))    

print("\nRandom Number List:")
print(createRandomList())
