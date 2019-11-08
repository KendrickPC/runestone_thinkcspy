'''
Write a new method called diagonal that will return the length of
the diagonal that runs from the lower left corner to the opposite
corner.
'''

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

    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp


    def contains(self, point):
        x, y = point.getX(), point.getY()
        return 0 <= x < self.width and 0 <= y < self.height

    def diagonal(self):
        d = (self.width ** 2 + self.height ** 2) ** 0.5
        return d


