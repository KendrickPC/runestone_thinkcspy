# 17.8 Converting an Object to a String
'''
When we’re working with classes and objects, it is often necessary to
print an object (that is to print the state of an object). Consider
the example below:
'''

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "\tx=" + str(self.x) + ", y=" + str(self.y)


p = Point(7, 6)
print(p)

'''
The print function shown above produces a string representation of the
Point p. The default functionality provided by Python tells you that p
is an object of type Point. However, it does not tell you anything about
the specific state of the point.

We can improve on this representation if we include a special method
call __str__. Notice that this method uses the same naming convention
as the constructor, that is two underscores before and after the name.
It is common that Python uses this naming technique for special methods.

The __str__ method is responsible for returning a string representation
as defined by the class creator. In other words, you as the programmer,
get to choose what a Point should look like when it gets printed. In
this case, we have decided that the string representation will include
the values of x and y as well as some identifying text. It is required
that the __str__ method create and return a string.
'''

