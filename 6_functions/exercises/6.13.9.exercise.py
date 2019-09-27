'''
Write a non-fruitful function to draw a five pointed
star, where the length of each side is 100 units.
'''

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("white")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("black")
kendrick.pensize(2)


def draw_one_star():
    for i in range(5):
        kendrick.forward(100)
        kendrick.right(144)


draw_one_star()

window.exitonclick()
