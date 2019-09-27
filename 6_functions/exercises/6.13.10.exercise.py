'''
Extend your program above. Draw five stars, but between
each, pick up the pen, move forward by 350 units, turn
right by 144, put the pen down, and draw the next star.
You’ll get something like this (note that you will need
to move to the left before drawing your first star in
order to fit everything in the window):
'''

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("hotpink")
kendrick.pensize(2)


def relocate_to_begin():
    kendrick.penup()
    kendrick.backward(125)
    kendrick.right(90)
    kendrick.forward(100)
    kendrick.left(90)
    kendrick.pendown()


def draw_one_star():
    for i in range(5):
        kendrick.forward(100)
        kendrick.right(144)


def relocate():
    kendrick.penup()
    kendrick.forward(250)
    kendrick.right(144)
    kendrick.pendown()


def relocate_second_layer_stars():
    kendrick.left(144)
    kendrick.left(90)
    kendrick.penup()
    kendrick.forward(100)
    kendrick.left(90)
    kendrick.forward(300)
    kendrick.right(180)
    kendrick.pendown()


def relocate_second_layer():
    kendrick.penup()
    kendrick.forward(250)
    kendrick.pendown()


def relocate_top_layer():
    kendrick.penup()
    kendrick.left(90)
    kendrick.forward(100)
    kendrick.left(90)
    kendrick.forward(125)
    kendrick.right(180)
    kendrick.pendown()



relocate_to_begin()
draw_one_star()
relocate()
draw_one_star()

relocate_second_layer_stars()
draw_one_star()
relocate_second_layer()
draw_one_star()

relocate_top_layer()
draw_one_star()

window.exitonclick()





