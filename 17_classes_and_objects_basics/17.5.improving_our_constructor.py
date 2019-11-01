# 17.5 Improving Our Constructor
'''
Our constructor so far can only create points at location (0,0). To create a point at position (7, 6) requires that we provide some additional capability for the user to pass information to the constructor. Since constructors are simply specially named functions, we can use parameters (as we’ve seen before) to provide the specific information.

We can make our class constructor more general by putting extra parameters into the __init__ method, as shown in this codelens example.
'''

class Point:
    ''' Point class for representing and manipulating x, y coordinates'''

    def __init__(self, initX, initY):
        ''' Create a new point at the given coordinates.'''
        self.x = initX
        self.y = initY

p = Point(7, 6)

print(p)
print(type(p)) # Class data structures
