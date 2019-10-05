'''
Modify the walking turtle program so that rather than a 90 degree
left or right turn the angle of the turn is determined randomly
at each step.
'''

import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    random_angle = random.randrange(0, 91)
    if coin == 0:
        t.left(random_angle)
    else:
        t.right(random_angle)

    t.forward(10)

wn.exitonclick()
