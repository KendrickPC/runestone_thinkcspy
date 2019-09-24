# 6.3 Unit Testing
'''
When we write functions that return values, we intend to use them over and over again. However, we want to be certain that they return the correct result. To be more certain these functions work correctly we write unit tests.

To write a unit test, we must know the correct result when calling the function with a specific input.
'''

# Test Module Source Code
# https://runestone.academy/runestone/books/published/thinkcspy/Appendices/testmodule.html#test-module


import unittest

def testEqual(actual,expected,places=5):
    '''
    Does the actual value equal the expected value?
    For floats, places indicates how many places, right of the decimal, must be correct
    '''
    if isinstance(expected,float):
        if abs(actual-expected) < 10**(-places):
            print('\tPass')
            return True
    else:
        if actual == expected:
            print('\tPass')
            return True
    print('\tTest Failed: expected {} but got {}'.format(expected,actual))
    return False


print("\n------Begin Unit Testing------")
import test

def square(x):
    '''raise x to the second power'''
    return x * x

print('testing square function')
test.testEqual(square(10), 100)


def power_of_3(x):
    # To the third power
    return x * x * x

print('\ntesting cube function')
test.testEqual(power_of_3(2), 8)


def doubling(x):
    return x * 2

print('\ntesting doubling function')
test.testEqual(doubling(4), 8)


def subtract_two(x):
    return x - 2

print('\ntesting subtract function')
test.testEqual(subtract_two(-5), -7)
