# 18.2 Objects are Mutable
'''
There are two important things to note about this implementation.
First, the gcd function is not a method of the class. It does not
belong to Fraction. Instead it is a function that is used by Fraction
to assist in a task that needs to be performed. This type of function
is often called a helper function. Second, the simplify method does
not return anything. Its job is to modify the object itself. This
type of method is known as a mutator method because it mutates or
changes the internal state of the object.
'''

# Helper function - used to assist Fraction class.
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # Mutator - changes the internal state of the object.
    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common


myfraction = Fraction(12, 16)

print(myfraction)
myfraction.simplify()
print(myfraction)
