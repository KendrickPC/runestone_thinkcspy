# 17.4. User Definied Classes

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)

'''
The combined process of “make me a new object” and “get its settings
initialized to the factory default settings” is called instantiation.
'''
