# 10.27 Tuple Assignment
'''
Python has a very powerful tuple assignment feature that allows a tuple of
variables on the left of an assignment to be assigned values from a tuple
on the right of the assignment.

    (name, surname, birth_year, movie, movie_year, profession, birth_place) = julia

This does the equivalent of seven assignment statements, all on one easy line.
One requirement is that the number of variables on the left must match the
number of elements in the tuple.

Once in a while, it is useful to swap the values of two variables.
With conventional assignment statements, we have to use a temporary variable.
For example, to swap a and b:

    temp = a
    a = b
    b = temp

Tuple assignment solves this problem neatly.

    (a, b) = (b, a)

The left side is a tuple of variables; the right side is a tuple of values.
Each value is assigned to its respective variable. All the expressions on
the right side are evaluated before any of the assignments. This feature
makes tuple assignment quite versatile.

Naturally, the number of variables on the left and the number of values
on the right have to be the same.

    >>> (a, b, c, d) = (1, 2, 3)
    ValueError: need more than 3 values to unpack

'''

