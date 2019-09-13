# 2.10 Reassignment

a = 5
b = a    # after executing this line, a and b are now equal
print(a, b)
a = 3    # after executing this line, a and b are no longer equal
print(a, b)


# 2.10.1. Developing your mental model of How Python Evaluates
print("\nDeveloping your mental model of How Python Evaluates:")

'''
Note:

In some programming languages, a different symbol is used for
assignment, such as <- or :=. The intent is that this will help
to avoid confusion. Python chose to use the tokens = for assignment,
and == for equality. This is a popular choice also found in
languages like C, C++, Java, and C#.
'''

# data-10-1: After the following statements, what are the values of x and y?
x = 15
y = x
x = 22

# <<< 22, 15 == (x, y)