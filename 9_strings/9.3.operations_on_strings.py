# 9.3 Operations on Strings
'''
In general, you cannot perform mathematical operations on strings,
even if the strings look like numbers. The following are illegal
(assuming that message has type string):

Interestingly, the + operator does work with strings, but for
strings, the + operator represents concatenation, not addition.
Concatenation means joining the two operands by linking them
end-to-end. For example:
'''


fruit = "banana"
bakedGood = " nut bread"
print(fruit + bakedGood)


print("Go" * 6)
name = "Packers"
print(name * 3)
print(name + "Go" * 3)
print((name + "Go") * 3)


