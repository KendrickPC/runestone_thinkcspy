# 1. Use a for statement to print 10 random numbers.

import math
import random

random_numbers_needed = 10

for i in range(random_numbers_needed):
    random_generator = random.random()
    print(random_generator)


# 2. Repeat the above exercise but this time print 10 random numbers between 25 and 35, inclusive.

import math
import random

random_numbers_needed = 10

for i in range(random_numbers_needed):
    random_generator = random.randrange(25, 36, 1)
    print(random_generator)

# 3. The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths of the other two sides. Look through the math module and see if you can find a function that will compute this relationship for you. Once you find it, write a short program to try it out.

import math

x = input("\nWhat is the length of the triangle? ")
x_integer = int(x)
x_int_squared = x_integer ** 2

y = input("\nWhat is the height of the triangle? ")
y_integer = int(y)
y_int_squared = y_integer ** 2

hypotenuse = math.sqrt(x_int_squared + y_int_squared)
print("\nThe hypotenuse of the triangle is " + str(hypotenuse))

# 4. Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.


import matplotlib
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000 # Darts thrown
circle_x = []
circle_y = []

square_x = []
square_y = []

count = 1

while count <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x ** 2 + y ** 2 <= 1):
        circle_x.append(x)
        circle_y.append(y)
    else:
        square_x.append(x)
        square_y.append(y)
    
    count += 1    

pi = 4 * len(circle_x) / float(N)

print("Pi is approximately: " + str(pi))
print("Pi is actually: " + str(np.pi))


plt.plot(circle_x, circle_y, 'b.')
plt.plot(square_x, square_y, 'r.')
print(plt.show())


