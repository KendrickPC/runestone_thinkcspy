'''
Add a distanceFromPoint method that works similar to
distanceFromOrigin except that it takes a Point as a
parameter and computes the distance between that point
and self.
'''

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
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def distanceFromPoint(self, other_point):
        dx = (other_point.getX() - self.x)
        dy = (other_point.getY() - self.y)
        return math.sqrt(dy ** 2 + dx ** 2)



print("\nExample 1:")
p = Point(3, 3)
q = Point(6, 7)
print(p.distanceFromPoint(q))


print("\nExample 2:")
p = Point(3, 4)
q = Point(5, 12)
print(p.distanceFromPoint(q))
