# 10.14 List Methods
'''
The dot operator can also be used to access built-in methods of list objects.
append is a list method which adds the argument passed to it to the end of the
list. Continuing with this example, we show several other list methods.
Many of them are easy to understand.
'''

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist) # <<< [5, 27, 3, 12]

mylist.insert(1, 12)
print(mylist) # <<< [5, 12, 27, 3, 12]
print(mylist.count(12)) # <<< 2

print(mylist.index(3)) # <<< 3
print(mylist.count(5)) # <<< 1

mylist.reverse()
print(mylist) # <<< [12, 3, 27, 12, 5]

mylist.sort()
print(mylist) # <<< [3, 5, 12, 12, 27]

mylist.remove(5)
print(mylist) # <<< [3, 12, 12, 27]

lastitem = mylist.pop()
print(lastitem) # <<< 27
print(mylist) # [3, 12, 12]

'''
There are two ways to use the pop method. The first, with no parameter, will
remove and return the last item of the list. If you provide a parameter for
the position, pop will remove and return the item at that position.
Either way the list is changed.

The following table provides a summary of the list methods shown above. The
column labeled result gives an explanation as to what the return value is as
it relates to the new value of the list. The word mutator means that the list
is changed by the method but nothing is returned (actually None is returned).
A hybrid method is one that not only changes the list but also returns a value
as its result. Finally, if the result is simply a return, then the list is
unchanged by the method.

Be sure to experiment with these methods to gain a better understanding
of what they do.
'''

'''
It is important to remember that methods like append, sort, and reverse all
return None. This means that re-assigning mylist to the result of sorting
mylist will result in losing the entire list. Calls like these will likely
never appear as part of an assignment statement (see line 8 below).
'''

# Python Documentation: 
# https://docs.python.org/3/library/stdtypes.html#sequence-types-str-bytes-bytearray-list-tuple-range

print("\nNew Reference:")
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()   #probably an error
print(mylist)

