'''
Write a function that mirrors its string argument, generating a
string containing the original string and the string backwards.
'''

import string


def mirror(mystr):
    # print(mystr)
    reverse_string = ''.join(reversed(mystr))
    return mystr + reverse_string

# mystr = "The grass is greener where you water it."

print(mirror('good'))
print(mirror('Python'))
print(mirror(''))
print(mirror('aa'))
