'''
Write a function that counts how many non-overlapping occurences
of a substring appear in a string.
'''

# https://stackoverflow.com/questions/8899905/count-number-of-occurrences-of-a-given-substring-in-a-string


import string


def count(substr, theStr):
    return theStr.count(substr)


print(count("ken", "kenkenken"))
print(count("ken", "charles"))
