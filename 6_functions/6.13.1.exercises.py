import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

kendrick = turtle.Turtle()
kendrick.color('hotpink')
kendrick.pensize(3)

# Initialize start position from left most point
kendrick.penup()
kendrick.backward(250)
kendrick.pendown()

def draw_one_square():
    for i in range(4):
        kendrick.forward(50)
        kendrick.left(90)

def relocate_to_new_start():
    kendrick.penup()
    kendrick.forward(75)
    kendrick.pendown()


def draw_five_boxes():
    for i in range(5):
        draw_one_square()
        relocate_to_new_start()


draw_five_boxes()


window.exitonclick()