# Write a function that will return the number of digits in an integer.


def numDigits(n):
    # your code here
    numberString = str(n)
    return len(numberString)


print(numDigits(1000))
print(numDigits(1000000))
print(numDigits(1000000000))