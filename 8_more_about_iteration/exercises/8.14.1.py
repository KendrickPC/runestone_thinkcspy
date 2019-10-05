# 8.14.1.py

'''
Add a print statement to Newton’s sqrt function that prints out better
each time it is calculated. Call your modified function with 25 as an
argument and record the results.
'''

def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        # Printing out approximation of Newton's Square Root
        print(betterapprox)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(100, 10))
# <<< 26.0
# <<< 14.923076923076923
# <<< 10.812053925455988
# <<< 10.030495203889796
# <<< 10.000046356507898
# <<< 10.000000000107445
# <<< 10.0
# <<< 10.0
# <<< 10.0
# <<< 10.0
# <<< 10.0

# Note: It takes about seven iterations to get to the exact value.
