# Add the following accessor methods to the Rectangle class:
# getWidth, getHeight, __str__.

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:

    def __init__(self, initP, initW, initH):
        self.location = initP
        self.width = initW
        self.height = initH

    # Implementation of accessor methods for Rectangle class
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __str__(self):
        return "Width is " + str(self.width) + ", height is " + str(self.height)

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)
