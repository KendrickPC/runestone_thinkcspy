# 6.6. Functions can Call Other Functions

def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c


a = -5 # <<< 25 when squared
b = 2 # <<< 4 when squared
c = 10 # <<< 100 when squared
result = sum_of_squares(a, b, c)
print(result) # <<< 129


print("\nDrawing a square in turtle:")


import turtle


window = turtle.Screen()
window.bgcolor("lightblue")
kendrick = turtle.Turtle()


def drawRectangle(t, w, h):
    # drawing rectangle with width(w), height(h), with turtle(t)
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

# drawSquare function calling the above drawRectangle function above.
def drawSquare(tx, sz):
    drawRectangle(tx, sz, sz)


drawSquare(kendrick, 75)
window.exitonclick()


# Drawing a circle in turtle program
'''
def drawPolygon(t, sideLength, numSides):
    # your code here.
    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)

wn = turtle.Screen()
geo = turtle.Turtle()

drawPolygon(geo,30,10)  # draw a decagon

wn.exitonclick()
'''


import turtle

window = turtle.Screen()
wheel = turtle.Turtle()

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

drawCircle(wheel, 20)
window.exitonclick()
