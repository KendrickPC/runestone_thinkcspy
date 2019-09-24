# 6.5 The Accumulator Pattern


def square(x):
    '''raise x to the second power'''
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal * x
        runningtotal += 1
    return runningtotal

toSquare = 10
absolute_value_to_square = abs(toSquare)
squareResult = square(absolute_value_to_square)

print("\nThe result of", toSquare, "squared is", squareResult)


# 6.5.1. The General Accumulator Pattern
'''
Initialize the accumulator variable
repeat:
    modify the accumulator variable

# when the loop terminates the accumulator has the correct value
'''


'''
print("\nAdding odd numbers together: ")
n = int(input('How many odd numbers would you like to add together?'))
thesum = 0
oddnumber = 1

for counter in range(n):
    thesum = thesum + oddnumber
    oddnumber = oddnumber + 2

print(thesum)
'''


# Additive vs Multiplicative Identity
# https://byjus.com/maths/additive-identity-vs-multiplicative-identity/

