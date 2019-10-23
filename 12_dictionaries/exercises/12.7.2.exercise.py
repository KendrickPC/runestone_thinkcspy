'''
Give the Python interpreter’s response to each of the following from a
continuous interpreter session:
'''

print("\nProblem 1:")
d = {'apples': 15, 'bananas': 35, 'grapes': 12}
# d['banana']
# print(d) # <<< KeyError: 'banana'

print("\nProblem 2:")
d['oranges'] = 20
print(len(d)) # <<< 4

print("\nProblem 3:")
print('grapes' in d) # <<< True

print("\nProblem 4:")
d['pears'] = 5
print(d) # <<< {'apples': 15, 'bananas': 35, 'grapes': 12, 'oranges': 20, 'pears': 5}

print("\nProblem 5:")
print(d.get('pears', 0)) # <<< 5

print("\nProblem 6:")
# Python3 Implementation
fruits = sorted(d.keys())
print(fruits)

print("\nProblem 7:")
del(d['apples'])
print('apples' in d) # <<< False


def add_fruit(inventory, fruit, quantity=0):
    """
    Adds quantity of fruit to inventory.

      >>> new_inventory = {}
      >>> add_fruit(new_inventory, 'strawberries', 10)
      >>> new_inventory.has_key('strawberries')
      True
      >>> new_inventory['strawberries']
      10
      >>> add_fruit(new_inventory, 'strawberries', 25)
      >>> new_inventory['strawberries']
      35
    """
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity


print("\nFruit Function:")
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
# print(new_inventory.has_key('strawberries'))

print('strawberries' in new_inventory)
print(new_inventory['strawberries'])
add_fruit(new_inventory, 'strawberries', 25)
print(new_inventory['strawberries'])
