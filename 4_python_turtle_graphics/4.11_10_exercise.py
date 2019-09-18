# 6. Write a program that has a shape of a star.
# Each angle within a star is 36 degrees from the inside.
# 36 * 5 = 180


import turtle

window = turtle.Screen()
ken = turtle.Turtle()


window.bgcolor("lightgreen")
ken.color("blue")
# ken.shape("line")

# Draws initial first line.
ken.penup()

for i in range(12):
    ken.forward(100)
    ken.pendown()
    ken.forward(20)

    # Reset the pen the second time.
    ken.penup()
    ken.backward(120)
    ken.left(30)


ken.shape("turtle")
ken.penup()


for i in range(12):
    ken.forward(150)
    ken.pendown()
    ken.stamp()
    ken.penup()
    ken.backward(150)
    ken.left(30)


window.exitonclick()
