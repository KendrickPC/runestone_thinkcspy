# 12.2 Dictionary Operations
'''
The del statement removes a key-value pair from a dictionary. For example, the
following dictionary contains the names of various fruits and the number of
each fruit in stock. If someone buys all of the pears, we can remove the entry
from the dictionary.
'''

print("\nExample 1:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

del inventory['pears']
print(inventory)

'''
Dictionaries are also mutable. As we’ve seen before with lists, this means that
the dictionary can be modified by referencing an association on the left hand
side of the assignment statement. In the previous example, instead of deleting
the entry for pears, we could have set the inventory to 0.
'''

print("\nExample 2:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['pears'] = 0
print(inventory)


print("\nExample 3:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] = inventory['bananas'] + 200

numItems = len(inventory)
print("Amount of Items in Inventory:", numItems)
print(inventory)


print("\nExample 4:")

