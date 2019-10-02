'''
Write a function findHypot. The function will be given the length
of two sides of a right-angled triangle and it should return the
length of the hypotenuse. (Hint: x ** 0.5 will return the square
root, or use sqrt from the math module)
'''

import unittest

def findHypot(sideA, sideB):
    result = (sideA**2) + (sideB**2)
    return result ** 0.5


class TestFindHypot(unittest.TestCase):
    def test_findHypot(self):
        self.assertEqual(findHypot(3, 4), (5))
        self.assertEqual(findHypot(9, 7), (11.40175425099138))


if __name__ == '__main__':
    unittest.main()
