# Write a perimeter method in the Rectangle class so that we can
# find the perimeter of any rectangle instance:


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

    def perimeter(self):
        return str(self.width * 2 + self.height * 2)

r = Rectangle(Point(0, 0), 10, 5)
print(r.perimeter())

# All tests have passed.
