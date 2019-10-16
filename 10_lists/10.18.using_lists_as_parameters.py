# 10.18. Using Lists as Parameters
'''
Functions which take lists as arguments and change them during execution are
called modifiers and the changes they make are called side effects. Passing
a list as an argument actually passes a reference to the list, not a copy of
the list. Since lists are mutable, changes made to the elements referenced by
the parameter change the same list that the argument is referencing.
For example, the function below takes a list as an argument and multiplies
each element in the list by 2:
'''

def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things) # <<< [2, 5, 9]
doubleStuff(things)
print(things) # <<< [4, 10, 18]

'''
The parameter aList and the variable things are aliases for the same object.

Since the list object is shared by two references, there is only one copy.
If a function modifies the elements of a list parameter, the caller sees the
change since the change is occurring to the original.

This can be easily seen in codelens. Note that after the call to doubleStuff,
the formal parameter aList refers to the same object as the actual parameter
things. There is only one copy of the list object itself.
'''

