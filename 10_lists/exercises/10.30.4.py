'''
Create a list containing 100 random integers between 0 and 1000 (use
iteration, append, and the random module). Write a function called
average that will take the list as a parameter and return the average.
'''

import random


def createRandomList():
    random_num_list = []
    for i in range(100):
        new_int = random.randrange(0, 1000)
        random_num_list.append(new_int)
    return random_num_list


# print(createRandomList())
# print(len(createRandomList()))


def average(aList):
    total_items = 0
    total_value = 0
    for item in aList:
        item_int = int(item)
        total_items = total_items + 1
        total_value = total_value + item_int
    average_value = total_value / total_items
    return average_value


myList = createRandomList()
listAverage = average(myList)

print(myList)
print(listAverage)
