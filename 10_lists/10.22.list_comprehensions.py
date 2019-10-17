# 10.22. List Comprehensions
'''
The previous example creates a list from a sequence of values based on some
selection criteria. An easy way to do this type of processing in Python is
to use a list comprehension. List comprehensions are concise ways to create
lists. The general syntax is:

        [<expression> for <item> in <sequence> if <condition>]

where the if clause is optional. For example:
'''

mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist]

print(yourlist)

'''
The expression describes each element of the list that is being built. The
for clause iterates through each item in a sequence. The items are filtered
by the if clause if there is one. In the example above, the for statement
lets item take on all the values in the list mylist. Each item is then squared
before it is added to the list that is being built. The result is a list of
squares of the values in mylist.

To write the primes_upto function we will use the is_prime function to filter
the sequence of integers coming from the range function. In other words, for
every integer from 2 up to but not including n, if the integer is prime,
keep it in the list.
'''

def primes_upto(n):
    """ Return a list of all prime numbers less than n using a list comprehension. """

    result = [num for num in range(2,n) if is_prime(num)]
    return result

