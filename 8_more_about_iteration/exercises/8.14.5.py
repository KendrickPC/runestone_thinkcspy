'''
Modify the turtle walk program so that you have two turtles each with
a random starting location. Keep the turtles moving until one of them
leaves the screen.
'''

import random
import turtle

# Initializing boht turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
window = turtle.Screen()

# Initializing shape of turtles
t1.shape('square')
t2.shape('circle')

# Boundaries of window.
leftBound = -window.window_width() / 2
rightBound= window.window_width() / 2
topBound = window.window_height() / 2
bottomBound = -window.window_height() / 2


# Random movement of turtle
def moveRandom(window, t):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)


# Collision Detection
def collision_detection(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False


# Check to see if both turtles are on the screen/window
def check_on_screen(w, t):
    # Boundaries of window.
    leftBound = -window.window_width() / 2
    rightBound= window.window_width() / 2
    topBound = window.window_height() / 2
    bottomBound = -window.window_height() / 2    

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX < leftBound or turtleX > rightBound:
        stillIn = False
    if turtleY < bottomBound or turtleY > topBound:
        stillIn = False
    return stillIn


# t1 random movements
t1.up()
# random.uniform vs random.randrange
# https://stackoverflow.com/questions/26784252/non-integer-arg-1-for-randrange-in-python-libary
t1.goto(random.uniform(leftBound, rightBound),
        random.uniform(bottomBound, topBound))
t1.setheading(random.randrange(0, 360))
t1.down()

#t2 random movements
# random.uniform vs random.randrange
# https://stackoverflow.com/questions/26784252/non-integer-arg-1-for-randrange-in-python-libary
t2.up()
t2.goto(random.uniform(leftBound, rightBound),
        random.uniform(bottomBound, topBound))
t2.setheading(random.randrange(0, 360))
t2.down()


while check_on_screen(window, t1) and check_on_screen(window, t2):
    moveRandom(window, t1)
    moveRandom(window, t2)


window.exitonclick()
