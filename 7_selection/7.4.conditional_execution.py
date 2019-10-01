'''
x = input("Please enter an integer: ")
x_int = int(x)

if x_int % 2 == 0:
    print(x_int, "is even")
else:
    print(x_int, "is odd")
'''

# Monte Carlo Simulation of Guessing Pi
# https://gist.github.com/louismullie/3769218

import math as m
import random as r

# Counting number of darts landing inside circle
inside_circle = 0
# Counting total number of darts thrown
total = 1000


# Iterate for the number of darts.
for i in range(0, total):
    # Generate random x, y, in [0, 1]
    x2 = r.random()**2
    y2 = r.random()**2
    # Increment if inside_circle unit circle.
    if m.sqrt(x2 + y2) < 1.0:
        inside_circle += 1

# inside_circle / total = pi / 4
pi = (float(inside_circle) / total) * 4

# Working guess of pi through Monte Carlo simulation
print(pi)

