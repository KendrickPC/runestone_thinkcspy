# 7.10.11 Extend the above program so that the sides can be given
# to the function in any order.

# Standardized Method of Swapping Two Variables
# https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python


import unittest

def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
    elif b > a and b > c: 
        is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
    else:
        is_rightangled = abs(a**2 + b**2 - c**2) < 0.001

    return is_rightangled


class TestingIs_RightAngled(unittest.TestCase):
    def test_is_rightangled(self):
        self.assertEqual(is_rightangled(3, 4, 5), True)
        
        self.assertEqual(is_rightangled(1.5, 2.0, 2.5), True)
        self.assertEqual(is_rightangled(4.0, 8.0, 16.0), False)

        self.assertEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
        self.assertEqual(is_rightangled(4.1, 8.2, 9.16787), True)
        
        self.assertEqual(is_rightangled(4.1, 8.2, 9.168), False)
        self.assertEqual(is_rightangled(0.5, 0.4, 0.64031), True)


if __name__ == '__main__':
    unittest.main()
