# Extend the star function to draw an n pointed star.
# (Hint: n must be an odd number greater or equal to 3).


# n pointed star
import turtle

# Initializing turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

# Changing colors and pensize for turtle
kendrick = turtle.Turtle()
kendrick.color("hotpink")
kendrick.pensize(2)

def draw_N_Star(kendrick, n):
    # Formula for n star is left(180 - 180/n)
    # In order to close the star, use an odd number.
    for i in range(n):
        kendrick.forward(100)
        kendrick.left(180 - 180/n)

draw_N_Star(kendrick, 8)

window.exitonclick()
