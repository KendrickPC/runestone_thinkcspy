# 12.1 Dictionaries
'''
All of the compound data types we have studied in detail so far — strings, lists, and tuples — are sequential collections. This means that the items in the collection are ordered from left to right and they use integers as indices to access the values they contain.

Dictionaries are a different kind of collection. They are Python’s built-in mapping type. A map is an unordered, associative collection. The association, or mapping, is from a key, which can be any immutable type, to a value, which can be any Python data object.

As an example, we will create a dictionary to translate English words into Spanish. For this dictionary, the keys are strings and the values will also be strings.

One way to create a dictionary is to start with the empty dictionary and add key-value pairs. The empty dictionary is denoted {}

'''

print("\nExample 1:")
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)

'''
The first assignment creates an empty dictionary named eng2sp. The other assignments add new key-value pairs to the dictionary. The left hand side gives the dictionary and the key being associated. The right hand side gives the value being associated with that key. We can print the current value of the dictionary in the usual way. The key-value pairs of the dictionary are separated by commas. Each pair contains a key and a value separated by a colon.

The order of the pairs may not be what you expected. Python uses complex algorithms, designed for very fast access, to determine where the key-value pairs are stored in a dictionary. For our purposes we can think of this ordering as unpredictable.

Another way to create a dictionary is to provide a list of key-value pairs using the same syntax as the previous output.

'''

print("\nExample 2:")
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)

'''
It doesn’t matter what order we write the pairs. The values in a dictionary are accessed with keys, not with indices, so there is no need to care about ordering.

Here is how we use a key to look up the corresponding value.
'''

print("\nExample 3:")
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
value = eng2sp['two']
print(value)

