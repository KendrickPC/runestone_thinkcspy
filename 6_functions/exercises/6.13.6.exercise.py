# Write a non-fruitful function drawEquitriangle(someturtle, somesize) which
# calls drawPoly from the previous question to have its turtle draw a
# equilateral triangle.

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("hotpink")
kendrick.pensize(3)


def drawPoly(someturtle, somesides, somesize):
    # kendrick.penup()
    # kendrick.backward(somesize / 2)
    # kendrick.pendown()

    for i in range(3):
        kendrick.forward(somesize)
        kendrick.left(360 / somesides)

drawPoly(kendrick, 3, 100)


window.exitonclick()
