'''
Add a method reflect_x to Point which returns a new Point, one which is
the reflection of the point about the x-axis.
For example, Point(3, 5).reflect_x() is (3, -5)
'''


import math

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def reflect_x(self):
        return self.x * -1, self.y


print("\nExample 1:")
print(Point(3, 5).reflect_x()) # <<< (-3, 5)

print("\nExample 2:")
print(Point(-5, 10).reflect_x()) # <<< (5, 10)

print("\nExample 3:")
print(Point(0, 0).reflect_x()) # <<< (0, 0)