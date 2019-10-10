# 9.9 Strings Are Immutable
'''
One final thing that makes strings different from some other Python collection
types is that you are not allowed to modify the individual characters in the
collection. It is tempting to use the [] operator on the left side of an
assignment, with the intention of changing a character in a string. For
example, in the following code, we would like to change the first letter
of greeting.
'''


greeting = "Hello, world!"
# greeting[0] = 'J' # <<< ERROR!
print(greeting)

'''
Instead of producing the output Jello, world!, this code produces the
runtime error TypeError: 'str' object does not support item assignment.

Strings are immutable, which means you cannot change an existing string.
The best you can do is create a new string that is a variation on
the original.
'''

print("\n")
greeting = "Hello, world!"
newgreeting = "J" + greeting[1:]
print(newgreeting)

