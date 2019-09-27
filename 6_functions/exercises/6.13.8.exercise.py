'''
Write a function areaOfCircle(r) which returns the area of a circle
of radius r. Make sure you use the math module in your solution.
'''

import math
import unittest


def areaOfCircle(r):
    # Formula for the area of a circle
    result = math.pi * r ** 2
    return result

print(areaOfCircle(10)) # <<< 314.1592653589793
print(areaOfCircle(5)) # <<< 78.53981633974483


class Test_areaOfCircle(unittest.TestCase):
    def test_areaOfCircle(self):
        self.assertEqual(areaOfCircle(10), (314.1592653589793))
        self.assertEqual(areaOfCircle(5), (78.53981633974483))

if __name__ == '__main__':
    unittest.main()
