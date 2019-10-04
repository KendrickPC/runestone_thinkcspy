# 8.5 The 3n+1 Sequence

'''
As another example of indefinite iteration, let’s look at a sequence that has fascinated mathematicians for many years. The rule for creating the sequence is to start from some positive integer, call it n, and to generate the next term of the sequence from n, either by halving n, whenever n is even, or else by multiplying it by three and adding 1 when it is odd. The sequence terminates when n reaches 1.

This Python function captures that algorithm. Try running this program several times supplying different values for n.
'''

# Collatz Conjecture
# https://www.youtube.com/watch?v=K0yMyUn--0s

def collatzConjecture(n):
    # Terminate once n = 1
    count = 0
    while n != 1:
        count += 1
        print(n)
        if n % 2 == 0: # n is Even
            n = n // 2
        else: # n is odd
            n = 3*n + 1
    print(n) # This is to get n to print 1
    print("The number of iterations is: " + str(count))

collatzConjecture(1)
collatzConjecture(2)
collatzConjecture(3)
collatzConjecture(6)
collatzConjecture(7)

'''
# Choosing Between for and while

Use a for loop if you know the maximum number of times that you’ll need to execute the body. For example, if you’re traversing a list of elements, or can formulate a suitable call to range, then choose the for loop.

So any problem like “iterate this weather model run for 1000 cycles”, or “search this list of words”, “check all integers up to 10000 to see which are prime” suggest that a for loop is best.

By contrast, if you are required to repeat some computation until some condition is met, as we did in this 3n + 1 problem, you’ll need a while loop.

As we noted before, the first case is called definite iteration — we have some definite bounds for what is needed. The latter case is called indefinite iteration — we are not sure how many iterations we’ll need — we cannot even establish an upper bound!
'''

