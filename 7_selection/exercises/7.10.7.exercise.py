'''
Write a function called is_even(n) that takes an integer as
an argument and returns True if the argument is an even number
and False if it is odd.
'''


import unittest


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


# print(is_even(10))
# print(is_even(11))

class TestIs_Even(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(is_even(10), True)
        self.assertEqual(is_even(11), False)

if __name__ == '__main__':
    unittest.main()
