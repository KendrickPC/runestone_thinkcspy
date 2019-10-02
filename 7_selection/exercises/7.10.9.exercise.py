# Modify is_odd so that it uses a call to is_even to determine
# if its argument is an odd integer.

import unittest


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if is_even(n) == True:
        return False
    else:
        return True


# print(is_odd(5))


class TestOddOrEven(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(is_even(10), True)
        self.assertEqual(is_even(11), False)

# class TestIs_Odd(unittest.TestCase):
    def test_is_odd(self):
        self.assertEqual(is_odd(11), True)
        self.assertEqual(is_odd(10), False)

if __name__ == '__main__':
    unittest.main()