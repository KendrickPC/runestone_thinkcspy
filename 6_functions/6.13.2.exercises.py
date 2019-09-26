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

# for i in range(10, 30, 10):

def reset():
    kendrick.penup()
    kendrick.backward(length)
    kendrick.right(90)
    kendrick.forward(length)
    kendrick.left(90)
    kendrick.pendown()

# Square 1
length = 10
for j in range(4):
    kendrick.forward(length)
    kendrick.left(90)

reset()

# Square 2
for k in range(4):
    kendrick.forward(length * 3)
    kendrick.left(90)

reset()

# Square 3
for l in range(4):
    kendrick.forward(length * 5)
    kendrick.left(90)

reset()

# Square 4
for m in range(4):
    kendrick.forward(length * 7)
    kendrick.left(90)

reset()

# Square 5
for n in range(4):
    kendrick.forward(length * 9)
    kendrick.left(90)

reset()

# Square 6
for o in range(4):
    kendrick.forward(length * 11)
    kendrick.left(90)

reset()

window.exitonclick()

