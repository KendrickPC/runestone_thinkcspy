'''
The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”).
The coefficients a and b completely describe the line. Write a method in the
Point class so that if a point instance is given another point, it will
compute the equation of the straight line joining the two points. It must
return the two coefficients as a tuple of two values.

For example:
    >>> print(Point(4, 11).get_line_to(Point(6, 15)))
    >>> (2, 3)

This tells us that the equation of the line joining the two points
is “y = 2x + 3”. When will your method fail?
'''

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get_line_to(self, other_points):
        dx = (other_points.getX() - self.x)
        dy = (other_points.getY() - self.y)
        return dx, dy


print(Point(4, 11).get_line_to(Point(6, 15))) # <<< (2, 4)

