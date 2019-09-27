import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("blue")
kendrick.pensize(2)

for j in range(20):
    for i in range(4):
        kendrick.forward(50)
        kendrick.left(90)

    # rotate square
    kendrick.left(18)

window.exitonclick()