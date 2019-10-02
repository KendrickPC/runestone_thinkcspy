# 7.8 Now write the function is_odd(n) that returns True
# when n is odd and False otherwise.


import unittest

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

# print(is_odd(5))


class Test_is_odd(unittest.TestCase):
    def test_is_odd(self):
        self.assertEqual(is_odd(5), True)
        self.assertEqual(is_odd(4), False)


if __name__ == '__main__':
    unittest.main()
