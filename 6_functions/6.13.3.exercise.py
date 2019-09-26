# 6.13.3 Exercise:

# Write a non-fruitful function drawPoly(someturtle, somesides, somesize)
# which makes a turtle draw a regular polygon. When called with
# drawPoly(tess, 8, 50), it will draw a shape like this:

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("hotpink")
kendrick.pensize(3)



def drawPoly(someturtle, somesides, somesize):
    for i in range(somesides):
        kendrick.forward(somesize)
        kendrick.left(360/somesides)
    

drawPoly(kendrick, 8, 50)


window.exitonclick()