# Using the turtle graphics module, write a recursive program to
# display a Hilbert curve.

# Reference:
# https://stackoverflow.com/questions/53243985/hilbert-curve-using-turtle-graphics-and-recursion

from turtle import Screen, Turtle


def hilbertCurve(turtle, A, parity, n):
    # Base Case
    if n < 1:
        return

    # Hilbert Curbe
    turtle.left(parity * 90)
    hilbertCurve(turtle, A, -parity, n-1)
    turtle.forward(A)
    turtle.right(parity * 90)
    hilbertCurve(turtle, A, parity, n-1)
    turtle.forward(A)
    hilbertCurve(turtle, A, parity, n-1)
    turtle.right(parity * 90)
    turtle.forward(A)
    hilbertCurve(turtle, A, -parity, n-1)
    turtle.left(parity * 90)


def __main__():
    screen = Screen()
    turtle = Turtle()
    turtle.speed('fastest')
    hilbertCurve(turtle, 10, 1, 4)
    screen.exitonclick()


__main__()
