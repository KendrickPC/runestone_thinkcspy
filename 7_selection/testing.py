import unittest

def isDivisible(x, y):
    '''is x evenly divisible by y?'''
    return x % y == 0


class TestIsDivisible(unittest.TestCase):
    def test_isDivisible(self):
        self.assertEqual(isDivisible(10, 5), (True))
        self.assertEqual(isDivisible(-15, 5), (True))

if __name__ == '__main__':
    unittest.main()
