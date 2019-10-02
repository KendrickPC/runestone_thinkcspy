# 7.10.11 Extend the above program so that the sides can be given
# to the function in any order.

import unittest

def is_rightangled(a, b, c):
    # your code here
    result = a**2 + b**2
    hypot = result ** 0.5


'''
Pseudo-Code:
    if a > c:
        a == c
        c == a
    elif b > c:
        b == c
        c == b
    
'''

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
