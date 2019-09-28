'''
Write a function called fancySquare that will draw a square
with fancy corners (sprites on the corners). You should
implement and use the drawSprite function from above. For an
even more interesting look, how about adding small triangles
to the ends of the sprite legs.
'''


import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor('lightgreen')



kendrick = turtle.Turtle()
kendrick.color('blue')
kendrick.pensize(2)

# Start drawing one side of the square


def fancyCorner():
    for i in range(12):
        kendrick.forward(10)
        kendrick.backward(10)
        kendrick.left(30)


def fancySquare():
    for i in range(4):
        kendrick.left(90)
        kendrick.forward(100)
        fancyCorner()


fancySquare()


window.exitonclick()