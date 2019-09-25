# 6.13.2 Exercises
'''
# Write a program to draw this. Assume the innermost square
is 20 units per side, and each successive square is 20 units
bigger, per side, than the one inside it.
'''

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color('hotpink')
kendrick.pensize(3)


for i in range(10, 100, 10):
    kendrick.forward(i)
    kendrick.left(90)

    kendrick.forward(i)
    kendrick.left(90)

    kendrick.forward(i)
    kendrick.left(90)

    kendrick.forward(i)
    kendrick.left(90)

    kendrick.penup()
    kendrick.backward(10)
    kendrick.right(90)
    kendrick.forward(10)
    kendrick.left(90)
    kendrick.pendown()


'''
kendrick.forward(10)
kendrick.left(90)

kendrick.forward(10)
kendrick.left(90)

kendrick.forward(10)
kendrick.left(90)

kendrick.forward(10)
kendrick.left(90)

kendrick.penup()
kendrick.backward(10)
kendrick.right(90)
kendrick.forward(10)
kendrick.left(90)
kendrick.pendown()
'''

window.exitonclick()