'''
Write a function that removes the first occurrence
of a string from another string.
'''

# Reference Source:
# https://stackoverflow.com/questions/6005891/replace-first-occurrence-only-of-a-string

def remove(substr, theStr):
    # your code here
    new_string = theStr.replace(substr, "", 1)
    return new_string

print(remove('ken', 'ken is awesome.'))
