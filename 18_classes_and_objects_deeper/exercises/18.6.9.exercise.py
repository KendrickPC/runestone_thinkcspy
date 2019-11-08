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

    def area(self):
        return str(self.width * self.height)

r = Rectangle(Point(0, 0), 10, 5)
print(r.area())
