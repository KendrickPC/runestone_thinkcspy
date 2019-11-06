# 18.3 Sameness
'''
The meaning of the word same seems perfectly clear until you give it
some thought and then you realize there is more to it than you
expected.

For example, if you say, Chris and I have the same car, you mean that
his car and yours are the same make and model, but that they are two
different cars. If you say, Chris and I have the same mother, you
mean that his mother and yours are the same person.

When you talk about objects, there is a similar ambiguity. For
example, if two Fractions are the same, does that mean they represent
the same rational number or that they are actually the same object?

We’ve already seen the is operator in the chapter on lists, where we
talked about aliases. It allows us to find out if two references
refer to the same object.
'''


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


print("\nExample 1:")
myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)


print("\nExample 2:")
ourfraction = myfraction
print(myfraction is ourfraction)