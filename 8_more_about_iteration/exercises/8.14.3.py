# 8.14.3
'''
Write a function, is_prime, that takes a single integer argument and returns
True when the argument is a prime number and False otherwise.
'''


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(13))
print(is_prime(10))
print(is_prime(1))
print(is_prime(2))