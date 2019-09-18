'''
# 11. Write a program to draw some kind of picture.
Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.
    https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/SummaryofTurtleMethods.html#turtle-methods
'''

import turtle

window = turtle.Screen()
ken = turtle.Turtle()


window.bgcolor("lightblue")
ken.color("pink")
ken.pensize(4)
# ken.shape("line")


# Letter 'N'
ken.left(90)
ken.forward(80)
ken.right(155)
ken.forward(90)
ken.left(155)
ken.forward(80)

# Letter 'O'
ken.penup()
ken.backward(75)
ken.right(90)
ken.forward(50)

ken.pendown()
ken.circle(20)
ken.penup()


window.exitonclick()
