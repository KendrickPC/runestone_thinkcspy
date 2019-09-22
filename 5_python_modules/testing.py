# 4. Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic. Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.

# https://www.youtube.com/watch?v=JjfrNc-G-zA

'''
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
'''

import matplotlib
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000 # Darts thrown
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


