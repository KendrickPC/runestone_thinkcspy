# 10.16 Append VS Concatenate
'''
The append method adds a new item to the end of a list. It is also possible to
add a new item to the end of a list by using the concatenation operator.
However, you need to be careful.

Consider the following example. The original list has 3 integers.
We want to add the word “cat” to the end of the list.
'''

origlist = [45, 32, 88]
origlist.append("cat")
print(origlist)

'''
It is also important to realize that with append, the original list is
simply modified. With concatenation, an entirely new list is created.
This is why the assignment operation is necessary as part of the
accumulator pattern.
'''

print("\nNew Reference:")
origlist = [45, 32, 88]

newlist = origlist + ["cat"]
print(newlist)

