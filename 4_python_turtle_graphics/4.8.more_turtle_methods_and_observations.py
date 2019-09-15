# 4.8. 
# A Few More turtle Methods and Observations

'''
Here are a few more things that you might find useful as you write programs that use turtles.

    1. Turtle methods can use negative angles or distances. So tess.forward(-100) will move tess backwards, and tess.left(-30) turns her to the right. Additionally, because there are 360 degrees in a circle, turning 30 to the left will leave you facing in the same direction as turning 330 to the right! (The on-screen animation will differ, though — you will be able to tell if tess is turning clockwise or counter-clockwise!)

    This suggests that we don’t need both a left and a right turn method — we could be minimalists, and just have one method. There is also a backward method. (If you are very nerdy, you might enjoy saying alex.backward(-100) to move alex forward!)

    Part of thinking like a scientist is to understand more of the structure and rich relationships in your field. So reviewing a few basic facts about geometry and number lines, like we’ve done here is a good start if we’re going to play with turtles.

    2. A turtle’s pen can be picked up or put down. This allows us to move a turtle to a different place without drawing a line. The methods are up and down. Note that the methods penup and pendown do the same thing.

        alex.up()
        alex.forward(100)     # this moves alex, but no line is drawn
        alex.down()

    3. Every turtle can have its own shape. The ones available “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.
        Example: alex.shape("turtle")

    4. You can speed up or slow down the turtle’s animation speed. (Animation controls how quickly the turtle turns and moves forward). Speed settings can be set between 1 (slowest) to 10 (fastest). But if you set the speed to 0, it has a special meaning — turn off animation and go as fast as possible.
        Example: alex.speed(10)

    5. A turtle can “stamp” its footprint onto the canvas, and this will remain after the turtle has moved somewhere else. Stamping works even when the pen is up.

Let’s do an example that shows off some of these new features.
'''

'''
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

ken = turtle.Turtle()
ken.color("blue")
ken.shape("turtle")

print(list(range(5, 60, 2)))
ken.up()
for size in range(5, 60, 2): # start with size = 5 and grow by 2
    ken.stamp() # leave an impression on the canvas
    ken.forward(size) # move ken along
    ken.right(24) # turn ken right

window.exitonclick()
'''

'''
import turtle
window = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

# jose.forward(50)

for size in range(10):
    jose.right(36)
    jose.forward(-50)
    jose.stamp()
    jose.forward(50)
    

window.exitonclick()
'''

import turtle
wn = turtle.Screen()
nikea = turtle.Turtle()
nikea.shape("turtle")
nikea.penup()

for size in range(3):
    nikea.forward(50)
    nikea.stamp()

wn.exitonclick()


