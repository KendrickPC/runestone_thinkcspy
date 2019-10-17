# 10.19 Pure Functions
'''
A pure function does not produce side effects. It communicates with the calling
program only through parameters (which it does not modify) and a return value.
Here is the doubleStuff function from the previous section written as a pure
function. To use the pure function version of double_stuff to modify things,
you would assign the return value back to things.
'''

def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
