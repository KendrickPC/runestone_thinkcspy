# 6.9. Program Development
'''
At this point, you should be able to look at complete functions and tell what they do. Also, if you have been doing the exercises, you have written some small functions. As you write larger functions, you might start to have more difficulty, especially with runtime and semantic errors.

To deal with increasingly complex programs, we are going to suggest a technique called incremental development. The goal of incremental development is to avoid long debugging sessions by adding and testing only a small amount of code at a time.

As an example, suppose you want to find the distance between two points, given by the coordinates (x1, y1) and (x2, y2). By the Pythagorean theorem, the distance is

distance = square_root( (x2 - y2)^2 + (x1 - y1)^2 )

'''

"""
def distance(x1, y1, x2, y2):
    pass
"""

'''
Extend the program …

[x] On line 6, write another unit test. Use (1,2, 4,6) as the parameters to the distance function. How far apart are these two points? Use that value (instead of 0) as the correct answer for this unit test.

On line 7, write another unit test. Use (0,0, 1,1) as the parameters to the distance function. How far apart are these two points? Use that value as the correct answer for this unit test.

The first test passes but the others fail since the distance function does not yet contain all the necessary steps.
'''

# Testing Tutorial
# https://www.youtube.com/watch?v=6tNS--WetLI

# Unit Test Documentation
# https://docs.python.org/3/library/unittest.html


import unittest

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d_squared = dx ** 2 + dy ** 2
    result = d_squared ** 0.5    
    return result

'''
print("\nDistance between two points:")
print(distance(1,2,1,2))
print(distance(1, 2, 4, 6))
print(distance(0, 0, 1, 1))
'''


class TestDistance(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(distance(1, 2, 1, 2), (0.0))
        self.assertEqual(distance(1, 2, 4, 6), (5.0))
        self.assertEqual(distance(0, 0, 1, 1), (1.4142135623730951))

if __name__ == '__main__':
    unittest.main()


'''
The key aspects of the process are:

1. Make sure you know what you are trying to accomplish.
   Then you can write appropriate unit tests.

2. Start with a working skeleton program and make small
   incremental changes. At any point, if there is an error,
   you will know exactly where it is.

3. Use temporary variables to hold intermediate values so
   that you can easily inspect and check them.

4. Once the program is working, you might want to consolidate
   multiple statements into compound expressions, but only do
   this if it does not make the program more difficult to read.
'''
