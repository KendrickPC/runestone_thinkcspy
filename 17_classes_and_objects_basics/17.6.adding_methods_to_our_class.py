# 17.6. Adding Methods to Our Class

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


print("\nExample #1:")
p = Point(7, 6)
print(p.getX())
print(p.getY())


'''
Note that the getX method simply returns the value of self.x from the
object itself. In other words, the implementation of the method is to go
to the state of the object itself and get the value of x. Likewise, the
getY method looks the same.

Let’s add another method, distanceFromOrigin, to see better how methods
work. This method will again not need any additional information to do
its work. It will perform a more complex task.
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


print("\nExample #2:")
p = Point(7, 6)
print(p.distanceFromOrigin())


