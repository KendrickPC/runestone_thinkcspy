# 6.10 Composition
'''
The ability to build functions by using other functions is called
composition.

As an example, we’ll write a function that takes two points, the
center of the circle and a point on the perimeter, and computes
the area of the circle.

Assume that the center point is stored in the variables xc and yc,
and the perimeter point is in xp and yp. The first step is to find
the radius of the circle, which is the distance between the two
points. Fortunately, we’ve just written a function, distance, that
does just that, so now all we have to do is use it:
'''

import unittest


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d_squared = dx ** 2 + dy ** 2
    result = d_squared ** 0.5
    return result


def area(r):
    r = 3.1416 * (r**2)
    return r


def area_2_circle(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
    '''
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
    '''

# print(area_2_circle(0, 0, 1, 1))

class TestDistance(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(distance(0, 0, 1, 1), (1.4142135623730951))

    def test_area(self):
        self.assertEqual(area_2_circle(0, 0, 1, 1), (6.283200000000002))

if __name__ == '__main__':
    unittest.main()
