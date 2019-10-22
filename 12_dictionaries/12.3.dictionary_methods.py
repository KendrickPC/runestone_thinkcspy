# 12.3 Dictionary Methods
'''
Dictionaries have a number of useful built-in methods. The following table
provides a summary and more details can be found in the Python Documentation.


    Method      Parameters      Description

    keys        None            Returns a view of the keys in the dictionary

    values      none            Returns a view of the values in the dictionary

    items       none            Returns a view of the key-value pairs in the dictionary

    get         key             Returns the value associated with key; None otherwise

    get         key,alt         Returns the value associated with key; alt otherwise


The keys method returns what Python 3 calls a view of its underlying keys.
We can iterate over the view or turn the view into a list by using the list
conversion function.
'''

print("\nExample 1:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

'''
It is so common to iterate over the keys in a dictionary that you can omit the
keys method call in the for loop — iterating over a dictionary implicitly iterates
over its keys.
'''

print("\nExample 2:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Got key", k)
   # print(inventory[k])

'''
As we saw earlier with strings and lists, dictionary methods use dot notation, which
specifies the name of the method to the right of the dot and the name of the object
on which to apply the method immediately to the left of the dot. The empty parentheses
in the case of keys indicate that this method takes no parameters.

The values and items methods are similar to keys. They return view objects which can be
turned into lists or iterated over directly. Note that the items are shown as tuples
containing the key and the associated value.

'''

print("\nExample 3:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

# There are two ways of mapping the values in key/value pairs.
for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])


'''
Note that tuples are often useful for getting both the key and the value at
the same time while you are looping. The two loops do the same thing.

The in and not in operators can test if a key is in the dictionary:
'''

print("\nExample 4:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'apples' in inventory:
    print(inventory['apples'])
else:
    print("We have no apples")


'''
This operator can be very useful since looking up a non-existent key in a
dictionary causes a runtime error.

The get method allows us to access the value associated with a key, similar
to the [ ] operator. The important difference is that get will not cause a
runtime error if the key is not present. It will instead return None. There
exists a variation of get that allows a second parameter that serves as an
alternative return value in the case where the key is not present. This can
be seen in the final example below. In this case, since “cherries” is not a
key, return 0 (instead of None).
'''


print("\nExample 5:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

