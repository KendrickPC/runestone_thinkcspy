'''
Rewrite the function sumTo(n) that returns the sum of all
integer numbers up to and including n.
This time use the accumulator pattern.
'''

import unittest


def sumTo(n):
    return (n * (n + 1)) / 2

print(sumTo(3))
print(sumTo(20))

# Wrote a test case for sumTo function.
class TestSumTo(unittest.TestCase):
    def test_sumTo(self):
        self.assertEqual(sumTo(3), (6))
        self.assertEqual(sumTo(20), (210))

if __name__ == '__main__':
    unittest.main()
