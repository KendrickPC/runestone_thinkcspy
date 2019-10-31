'''
Write a recursive function to compute the Fibonacci sequence.
How does the performance of the recursive function compare to
that of an iterative version?
'''

def fibonacciRecursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

print("\nFibonacci Recursive Algorithm:")
print(fibonacciRecursive(1))
print(fibonacciRecursive(2))
print(fibonacciRecursive(3))
print(fibonacciRecursive(4))
print(fibonacciRecursive(5))


def fibonacciIterative(n):
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i -2]
    return fib[n]

print("\nFibonacci Interative Algorithm:")
print(fibonacciIterative(1))
print(fibonacciIterative(2))
print(fibonacciIterative(3))
print(fibonacciIterative(4))
print(fibonacciIterative(5))
