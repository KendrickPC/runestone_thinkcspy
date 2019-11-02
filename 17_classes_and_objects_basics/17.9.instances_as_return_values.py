# Instances as Return Values
'''
Functions and methods can return objects. This is actually nothing new
since everything in Python is an object and we have been returning
values for quite some time. The difference here is that we want to have
the method create an object using the constructor and then return it as
the value of the method.

Suppose you have a point object and wish to find the midpoint halfway
between it and some other target point. We would like to write a method,
call it halfway that takes another Point as a parameter and returns the
Point that is halfway between the point and the target
'''

# Used for square root function
import math


class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        # Same as setting the power of this equation to ^ 0.5 or ** 0.5
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)

# These print statements below add extra lines of work for codeLens to process
print("\nMidpoint values of both (x and y) for both (p and q).")
print(mid)
print("\nMidpoint values of X for both (p and q).")
print(mid.getX())
print("\nMidpoint values of Y for both (p and q).")
print(mid.getY())

'''
The resulting Point, mid, has an x value of 4 and a y value of 8.
We can also use any other methods since mid is a Point object.

In the definition of the method halfway see how the requirement to
always use dot notation with attributes disambiguates the meaning of
the attributes x and y: We can always see whether the coordinates of
Point self or target are being referred to.
'''



