# 10.25. list Type Conversion Function
'''
Python has a built-in type conversion function called list that
tries to turn whatever you give it into a list.
For example, try the following:
'''

xs = list("Crunchy Frog")
print(xs)

'''
The string “Crunchy Frog” is turned into a list by taking each character
in the string and placing it in a list. In general, any sequence can be
turned into a list using this function. The result will be a list
containing the elements in the original sequence. It is not legal to
use the list conversion function on any argument that is not a sequence.

It is also important to point out that the list conversion function will
place each element of the original sequence in the new list. When working
with strings, this is very different than the result of the split method.

* Whereas split will break a string into a list of “words”, list will
  always break it into a list of characters.
'''

