# 6.2. Functions that Return Values

'''
Most functions require arguments, values that control how the function does its job. For example, if you want to find the absolute value of a number, you have to indicate what the number is. Python has a built-in function for computing the absolute value:
'''

print(abs(5))
print(abs(-5))

print("\n--------------------")

# Power function
import math

print(math.pow(2, 3))
print(math.pow(7, 4))

'''
Note: 
Of course, we have already seen that raising a base to an
exponent can be done with the ** operator.
'''

print("\n--------------------")
print(max(7, 11))
print(max(4, 1, 17, 2, 12))
print(max(3 * 11, 5 ** 3, 512 - 9, 1024 ** 0))


print("\n--------------------")
def square(x):
    y = x * x
    return y

to_square = input("Enter an integer: ")
to_square_int = int(to_square)
result = square(to_square_int)
print("The result of", to_square_int, "squared is", result)

print("\n--------------------")


