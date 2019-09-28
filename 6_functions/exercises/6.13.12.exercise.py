'''
Write a function called drawSprite that will draw a sprite.
The function will need parameters for the turtle, the
number of legs, and the length of the legs. Invoke the
function to create a sprite with 15 legs of length 120.
'''

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("hotpink")
kendrick.pensize(2)

def drawSprite(kendrick, n):
    for i in range(n):
        kendrick.forward(30) # Should be 120
        kendrick.left(360 - 360/n)

drawSprite(kendrick, 15)

window.exitonclick()
