'''
Common Mistake!

There is a very common mistake that occurs when programmers
try to write boolean expressions. For example, what if we
have a variable number and we want to check to see if its
value is 5,6, or 7. In words we might say: “number equal to
5 or 6 or 7”. However, if we translate this into Python,
number == 5 or 6 or 7, it will not be correct. The or
operator must join the results of three equality checks.
The correct way to write this is
number == 5 or number == 6 or number == 7. This may seem
like a lot of typing but it is absolutely necessary.
You cannot take a shortcut.
'''

# Relational Operators Precendence
# https://docs.python.org/3/reference/expressions.html#operator-precedence
