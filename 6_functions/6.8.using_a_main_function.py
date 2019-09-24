# 6.8 Using a Main Function
'''
These final five statements perform the main processing that the program will do. Notice that much of the detail has been pushed inside the drawSquare function. However, there are still these five lines of code that are needed to get things done.

In many programming languages (e.g. Java and C++), it is not possible to simply have statements sitting alone like this at the bottom of the program. They are required to be part of a special function that is automatically invoked by the operating system when the program is executed. This special function is called main. Although this is not required by the Python programming language, it is actually a good idea that we can incorporate into the logical structure of our program. In other words, these five lines are logically related to one another in that they provide the main tasks that the program will perform. Since functions are designed to allow us to break up a program into logical pieces, it makes sense to call this piece main.
'''

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


def main(): # Define the main function
    window = turtle.Screen() # Set up window and its attributes
    window.bgcolor("lightblue")

    kendrick = turtle.Turtle()
    drawSquare(kendrick, 75)

    window.exitonclick()

main() # Invoke the main function


'''
Note:
In Python there is nothing special about the name main. We could have called this function anything we wanted. We chose main just to be consistent with some of the other languages.
'''

# Advanced Topics
