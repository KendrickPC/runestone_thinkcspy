# 16.3 Three Laws of Recursion
'''
16.3. The Three Laws of Recursion
Like the robots of Asimov, all recursive algorithms must obey three important laws:

    1. A recursive algorithm must have a base case.
    2. A recursive algorithm must change its state and move toward the base case.
    3. A recursive algorithm must call itself, recursively.

'''

'''
1. How many recursive calls are made when computing the sum of the list [2,4,6,8,10]?
Answer: 4     
            The first recursive call passes the list [4,6,8,10], the
            second [6,8,10] and so on until [10].

2. Suppose you are going to write a recusive function to calculate the factorial of
a number. fact(n) returns n * n-1 * n-2 * … * 1, and the factorial of zero is definded
to be 1. What would be the most appropriate base case?

Answer: n <= 0
✔️ Good, this is the most efficient, and even keeps your program from crashing if you
try to compute the factorial of a negative number.
'''


