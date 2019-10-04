# 8.6 Newton's Method

'''
Loops are often used in programs that compute numerical results
by starting with an approximate answer and iteratively improving
it.

For example, one way of computing square roots is Newton’s
method. Suppose that you want to know the square root of n.
If you start with almost any approximation, you can compute a
better approximation with the following formula:

        better =  1/2 * (approx + n/approx)

Execute this algorithm a few times using your calculator. Can
you see why each iteration brings your estimate a little closer?
One of the amazing properties of this particular algorithm is
how quickly it converges to an accurate answer.

The following implementation of Newton’s method requires two
parameters. The first is the value whose square root will be
approximated. The second is the number of times to iterate the
calculation yielding a better result.
'''


def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(100, 10))
print(newtonSqrt(4, 10))
print(newtonSqrt(1, 10))


# Modify the program …
'''
All three of the calls to newtonSqrt in the previous example
produce the correct square root for the first parameter.
However, were 10 iterations required to get the correct answer?
Experiment with different values for the number of repetitions
(the 10 on lines 8, 9, and 10). For each of these calls, find
the smallest value for the number of repetitions that will
produce the correct result.
'''

# Answer: The smallest # of iterations to produce correct results
# are 3
print("\nModifying the Program:")
print(newtonSqrt(100, 3))
print(newtonSqrt(4, 3))
print(newtonSqrt(1, 3))


