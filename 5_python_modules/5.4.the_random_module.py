# 5.4 The Random Module
'''
We often want to use random numbers in programs. Here are a few typical uses:

    * To play a game of chance where the computer needs to throw some dice, pick a number, or flip a coin,

    * To shuffle a deck of playing cards randomly,

    * To randomly allow a new enemy spaceship to appear and shoot at you,

    * To simulate possible rainfall when we make a computerized model for estimating the environmental impact of building a dam,

    * For encrypting your banking session on the Internet.

Python provides a module random that helps with tasks like this. You can take a look at it in the documentation. Here are the key things we can do with it.
'''

import random

 # Chooses a number between 0 and 1
probability = random.random()
print(probability)

# Returns int of [1, 2, 3, 4, 5, 6]
dice_throw = random.randrange(1, 7)
print(dice_throw)

# Change random range from 0 to 5 (not including 5)
random_from_0_to_5 = random.random()
result = random_from_0_to_5 * 5
print(result)


'''
It is important to note that random number generators are based on a deterministic algorithm — repeatable and predictable. So they’re called pseudo-random generators — they are not genuinely random. They start with a seed value. Each time you ask for another random number, you’ll get one based on the current seed attribute, and the state of the seed (which is one of the attributes of the generator) will be updated. The good news is that each time you run your program, the seed value is likely to be different meaning that even though the random numbers are being created algorithmically, you will likely get random behavior each time you execute.
'''

print("\nPlotting a sine wave")
# https://runestone.academy/runestone/books/published/thinkcspy/Labs/sinlab.html


'''
For this lab, we will use the math library to generate the values that we need. To help you understand the sine function, consider the following Python program. As you can see, the sin function from the math library takes a single parameter. This parameter must be a value in “radians” (you may remember this from trigonometry class). Since most of us are used to stating the size of an angle in “degrees”, the math module provides a function, radians that will convert from degrees to radians for us.
'''

import math

y = math.sin(math.radians(90)) # <<< 1
print(y)


for angle in range(0, 360):
    y = math.sin(math.radians(angle))
    print("angle in degrees: " + str(angle) + " radians: " + str(y))


# Making the Plot
'''
In order to plot a smooth line, we will use the turtle’s goto method. goto takes two parameters, x and y, and moves the turtle to that location. If the tail is down, a line will be drawn from the previous location to the new location.

Let’s try the goto method. Experiment with the method to make sure you understand the coordinate system of the screen. Try both positive and negative number
'''

"""
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

ken = turtle.Turtle()
ken.goto(50, 60)
ken.goto(-200, -159)

wn.exitonclick()
"""

'''
Now we can put the two previous programs together to complete our plot. Here is our sequence of steps.

Create and set up the turtle and the screen.

Iterate the angle from 0 to 360.

Generate the sine value for each angle.

Move the turtle to that position (leave a line behind).

Here is a partial program for you to complete.
'''

import math
import turtle


wn = turtle.Screen()
wn.bgcolor('lightblue')

TMNT = turtle.Turtle()

for angle in range(0, 360):
    y = math.sin(math.radians(angle)) * 100
    TMNT.goto(angle - 180, y)

wn.exitonclick()

# Making the Plot Better
'''
You probably think that the program has errors since it does not draw the picture we expect. Maybe you think it looks a bit like a line? What do you think the problem is? Here is a hint…go back and take a look at the values for the sine function as they were calculated and printed in the earlier example.

Now can you see the problem? The value of sin always stays between -1 and 1. This does not give our turtle much room to run.

In order to fix this problem, we need to redesign our “graph paper” so that the coordinates give us more room to plot the values of the sine function. To do this, we will use a method of the Screen class called setworldcoordinates. This method allows us to change the range of values on the x and y coordinate system for our turtle. Take a look at the documentation for the turtle module to see how to use this method (Global Module Index). Once you have an understanding of the parameters required to use the method, choose an appropriate coordinate system and retry your solution.
'''

# Global Module Index:
    # https://docs.python.org/3/py-modindex.html

'''
Now try this…

Now that you can plot a sine function, how about trying a different function, such as cosine or log?
'''

# Cosine function
'''
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

TMNT = turtle.Turtle()

for angle in range(0, 360):
    y = math.cos(math.radians(angle)) * 100
    TMNT.goto(angle - 180, y)

wn.exitonclick()
'''

# Logarithmic Function


'''
✔️ Computers generate random numbers using a deterministic algorithm. This means that if anyone ever found out the algorithm they could accurately predict the next value to be generated and would always win the lottery.
'''





