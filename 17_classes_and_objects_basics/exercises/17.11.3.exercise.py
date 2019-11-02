'''
Add a method slope_from_origin which returns the slope of the
line joining the origin to the point. For example:

>>> Point(4, 10).slope_from_origin()
    2.5
'''


class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y / self.x  

print("\nExample 1:")
print(Point(4, 10).slope_from_origin()) # <<< 2.5

print("\nExample 2:")
print(Point(0, 10).slope_from_origin()) # <<< None

print("\nExample 3:")
print(Point(-5, 20).slope_from_origin()) # <<< -4.0
