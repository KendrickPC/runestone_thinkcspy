'''
Write a function is_rightangled which, given the length of three
sides of a triangle, will determine whether the triangle is
right-angled. Assume that the third argument to the function is
always the longest side. It will return True if the triangle
is right-angled, or False otherwise.

Hint: floating point arithmetic is not always exactly accurate,
so it is not safe to test floating point numbers for equality.
If a good programmer wants to know whether x is equal or close
enough to y, they would probably code it up as:
    
    # if x is approximately equal to y
    if abs(x - y) < 0.001: 

'''

import unittest

def is_rightangled(a, b, c):
    # your code here
    result = a**2 + b**2
    hypot = result ** 0.5

    if abs(c - hypot) < 0.0001:
        return True
    else:
        return False


class TestIsRightAngled(unittest.TestCase):
    def test_is_rightangled(self):
        # Common Right Triangle Testing
        self.assertEqual(is_rightangled(3, 4, 5), True)
        self.assertEqual(is_rightangled(5, 12, 13), True)
        self.assertEqual(is_rightangled(6, 8, 10), True)
        
    def test_floatingPointArithmetic(self):
        # Floating Point Arithmetic Test
        self.assertEqual(is_rightangled(1.5, 2.0, 2.5), True)
        self.assertEqual(is_rightangled(4.0, 8.0, 16.0), False)
        self.assertEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
        self.assertEqual(is_rightangled(4.1, 8.2, 9.16787), True)
        self.assertEqual(is_rightangled(4.1, 8.2, 9.168), False)
        self.assertEqual(is_rightangled(0.5, 0.4, 0.64031), True)


if __name__ == '__main__':
    unittest.main()

