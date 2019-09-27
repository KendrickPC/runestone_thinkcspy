'''
Write a fruitful function sumTo(n) that returns the sum of all integer
numbers up to and including n. So sumTo(10) would be 1+2+3...+10 which
would return the value 55. Use the equation (n * (n + 1)) / 2.
'''

import unittest

def sumTo(n):
    # result = (n * (n + 1)) / 2
    # return result
    return (n * (n + 1)) / 2

print(sumTo(10))
print(sumTo(20))


# Wrote a test case for sumTo function.
class TestSumTo(unittest.TestCase):
    def test_sumTo(self):
        self.assertEqual(sumTo(10), (55))
        self.assertEqual(sumTo(20), (210))

if __name__ == '__main__':
    unittest.main()