# Write a recursive function to compute the factorial of a number.
# Research reference:
# https://www.programiz.com/python-programming/examples/factorial-recursion


def computeFactorial(number):
    if number < 0:
        return None
    elif number == 0 or number == 1:
        return 1
    else:
        return number * computeFactorial(number-1)

print(computeFactorial(5))

# All test cases passed.
