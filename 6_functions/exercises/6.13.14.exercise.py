'''
Write a function called mySqrt that will approximate the square root
of a number, call it n, by using Newton’s algorithm. Newton’s approach
is an iterative guessing algorithm where the initial guess is n/2 and
each subsequent guess is computed using the
formula: newguess = (1/2) * (oldguess + (n/oldguess)).
'''

# Newton's Algorithm.
'''
Youtube Explanation of Newton's Algorithm:
https://www.youtube.com/watch?v=FMCOebUGG94

Reference to coding the algorithm:
https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

Xsub(n + 1) = Xsub(n) - (f(Xsubn) / f'(Xsubn))
'''

import unittest


def mySqrt(n, number_iters = 500):
    a = float(n) # number to get the square root of 
    for i in range(number_iters): #iternation number
        # update the following:
        # x_(n+1) = 0.5 * (x_n +a / x_n)
        n = (1/2) * (n + a / n) 
    return n

print(mySqrt(9)) # <<< 3
print(mySqrt(16)) # <<< 4


class Test_newtonSqrt(unittest.TestCase):
    def test_newtonSqrt(self):
        self.assertEqual(mySqrt(9), (3))
        self.assertEqual(mySqrt(16), (4))

if __name__ == "__main__":
    unittest.main()
