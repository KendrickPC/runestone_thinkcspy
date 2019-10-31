'''
Using the turtle graphics module, write a recursive program
to display a Koch snowflake.

Reference:
https://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html
https://trinket.io/python/8c8b7f567e


'''


import turtle
import math

# Get the screen size and set some scaling
window = turtle.Screen()
window_x = window.window_width() * 0.5
window_y = window.window_height() * 0.5

base_triange_length = 2 / math.sqrt(3) * window_y

# Parameters of the Koch Triangle
depth = 2

# Set up the turtle
Koch = turtle.Turtle()
Koch.speed(50 * (depth + 1))
Koch.penup()
Koch.setposition((-window_x / 2, -window_y / 2))
Koch.pendown()
Koch.left(60)


def drawKochSegment(t, run, mydepth, depth):
    if mydepth == depth:
        # Draw a segment
        t.fd(run)
    else:
        myrun = run / 3.0
        # Making each straight bit into a smaller version of ourselves
        drawKochSegment(t, myrun, mydepth + 1, depth)
        t.left(60)
        drawKochSegment(t, myrun, mydepth + 1, depth)
        t.right(120)
        drawKochSegment(t, myrun, mydepth + 1, depth)
        t.left(60)
        drawKochSegment(t, myrun, mydepth + 1, depth)


# Drawing a basic triangle outline
for i in range(3):
    drawKochSegment(Koch, base_triange_length, 0, depth)
    Koch.right(120)


window.exitonclick()



