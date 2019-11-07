# Add a method area to the Rectangle class that returns the area
# of any instance:

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

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        return width * height

    def __str__(self):
        return "\nThe area of the rectangle is " + (str(self.width * self.height))

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)
