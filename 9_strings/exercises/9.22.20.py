'''
Write a function called remove_dups that takes a string and creates a new
string by only adding those characters that are not already present. In
other words, there will never be a duplicate letter added to the new string.
'''

# Reference Source: 
# https://www.geeksforgeeks.org/remove-duplicates-given-string-python/


from collections import OrderedDict


def remove_dups(astring):
    # return ''.join(set(astring)) # <<< smpi
    '''
    Having the input string converted to a dictionary will automatically
    remove duplicates becasue dictionaries remove duplicates as a feature
    of being part of a dictionary.
    '''
    return ''.join(OrderedDict.fromkeys(astring)) # <<< misp


print(remove_dups("mississippi")) # <<< misp

