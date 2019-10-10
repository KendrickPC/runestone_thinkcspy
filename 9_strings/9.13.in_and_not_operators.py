# 9.13 The in and not operators

# The in operator tests if one string is a substring of another:
print('p' in 'apple') # <<< True
print('i' in 'apple') # <<< False
print('ap' in 'apple') # <<< True
print('pa' in 'apple') # <<< False

'''
Note that a string is a substring of itself, and the empty string
is a substring of any other string. (Also note that computer
scientists like to think about these edge cases quite carefully!)
'''
print("\nTesting Edge Cases:")
print('a' in 'a') # <<< True
print('apple' in 'apple') # <<< True
print('' in 'a') # <<< True
print('' in 'apple') # <<< True

