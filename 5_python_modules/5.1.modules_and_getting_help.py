# 5.1. Modules and Getting Help
'''
A module is a file containing Python definitions and statements intended for
use in other Python programs. There are many Python modules that come with
Python as part of the standard library. We have already used one of these
quite extensively, the turtle module. Recall that once we import the module,
we can use things that are defined inside.
'''

'''
import turtle            # allows us to use the turtles library

wn = turtle.Screen()     # creates a graphics window
alex = turtle.Turtle()   # create a turtle named alex

alex.forward(150)        # tell alex to move forward by 150 units
alex.left(90)            # turn by 90 degrees
alex.forward(75)         # complete the second side of a rectangle
wn.exitonclick()
'''

'''
Here we are using Screen and Turtle, both of which are defined inside the turtle module.

But what if no one had told us about turtle? How would we know that it exists. How would we know what it can do for us? The answer is to ask for help and the best place to get help about the Python programming environment is to consult with the Python Documentation.

The Python Documentation site for Python version 3 (the home page is shown below) is an extremely useful reference for all aspects of Python. The site contains a listing of all the standard modules that are available with Python (see Global Module Index). You will also see that there is a Language Reference and a Tutorial (mostly aimed at people who are already familiar with another programming language), as well as installation instructions, how-tos, and frequently asked questions. We encourage you to become familiar with this site and to use it often.

    Python Global Module Index:
    https://docs.python.org/3/py-modindex.html
    
    Python Documentation:
    https://docs.python.org/3/

    Language Reference:
    https://docs.python.org/3/reference/index.html

    Tutorial:
    https://docs.python.org/3/tutorial/index.html
'''


# Check your understanding
    # modules-1-1: In Python a module is:
    # Answer: A. A file containing Python definitions and statements intended for use in other Python programs.
            # ✔️ A module can be reused in different programs.

    # modules-1-2: To find out information on the standard modules available with Python you should:
    # Answer: A. Go to the Python Documentation site.
            # ✔️ The site contains a listing of all the standard modules that are available with Python.







