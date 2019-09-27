# Draw both Squares

import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("blue")
kendrick.pensize(1)

'''
kendrick.right(90)
kendrick.forward(10)
kendrick.right(90)
kendrick.forward(10)

# Second loop
kendrick.right(90)
kendrick.forward(20)
kendrick.right(90)
kendrick.forward(20)

# Third loop
kendrick.right(90)
kendrick.forward(30)
kendrick.right(90)
kendrick.forward(30)
'''

def drawSquares():
    for i in range(5, 200, 5):
        kendrick.right(90)
        kendrick.forward(i)
        kendrick.right(90)
        kendrick.forward(i)

# drawSquares()


def drawRotatedSquare():
    kendrick.right(90)
    for i in range(10, 100, 10):
        kendrick.forward(i)
        kendrick.right(90)
        kendrick.forward(i)
        kendrick.right(90)

        kendrick.forward(i * 3)
        kendrick.right(90)
        kendrick.forward(i * 3)
        kendrick.right(90)
        kendrick.forward(i * 3)

        kendrick.right(65)



    # Working Code
    '''
    kendrick.right(90)
    kendrick.forward(10)
    kendrick.right(90)
    kendrick.forward(10)
    kendrick.right(90)

    kendrick.forward(20)
    kendrick.right(90)
    kendrick.forward(20)
    kendrick.right(90)
    kendrick.forward(20)

    kendrick.right(65)

    kendrick.forward(30)
    kendrick.right(90)
    kendrick.forward(30)
    kendrick.right(90)
    kendrick.forward(50)
    kendrick.right(90)
    kendrick.forward(50)
    '''
drawRotatedSquare()

window.exitonclick()





