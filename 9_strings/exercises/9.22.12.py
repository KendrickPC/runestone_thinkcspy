'''
Write a function that removes all occurrences of a string from
another string.
'''

def remove_all(substr, theStr):
    # your code here
    new_string = theStr.replace(substr, "")
    return new_string

print(remove_all('ken', 'ken ken ken michael jordan ken ken ken'))