# Functions
'''
def name( parameters ):
    statements
'''

'''
import turtle

def drawSquare(turt, size):
    # Make turtle aka turt draw a square and with size of the side

    for i in range(4):
        turt.forward(size)
        turt.left(90)


# Setting up windows and its attributes
window = turtle.Screen()
window.bgcolor("lightblue")
kendrick = turtle.Turtle() # Create turtle named kendrick
drawSquare(kendrick, 50)

window.exitonclick()
'''

'''
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex
drawSquare(alex, 50)          # Call the function to draw the square

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex,75)           # Draw another square

wn.exitonclick()
'''

import turtle

def drawMulticolorSquare(t, sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['red','green','purple','orange']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightblue")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(4)

size = 20                        # size of the smallest square
for i in range(30):
    drawMulticolorSquare(tess, size)
    size = size + 5             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()



# func-1-1: What is a function in Python?
# Answer: A. A named sequence of statements.

# func-1-2: What is one main purpose of a function?
# Answer: B. To help the programmer organize programs into chunks that match how they think about the solution to the problem.
# ✔️ While functions are not required, they help the programmer better think about the solution by organizing pieces of the solution into logical chunks that can be reused.

# func-1-3: Which of the following is a valid function header (first line of a function definition)?
# Answer: A. def drawCircle(t):
# ✔️ A function may take zero or more parameters. It does not have to have two. In this case the size of the circle might be specified in the body of the function.

# func-1-4: What is the name of the following function?
# Answer: 
