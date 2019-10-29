# 16.6. Sierpinski Triangle
'''
Another fractal that exhibits the property of self-similarity is the Sierpinski
triangle. An example is shown in Figure 3. The Sierpinski triangle illustrates
a three-way recursive algorithm.

The procedure for drawing a Sierpinski triangle by hand is simple.
Start with a single large triangle. Divide this large triangle into four new
triangles by connecting the midpoint of each side. Ignoring the middle triangle
that you just created, apply the same procedure to each of the three corner
triangles. Each time you create a new set of triangles, you recursively apply
this procedure to the three smaller corner triangles. You can continue to apply
this procedure indefinitely if you have a sharp enough pencil. Before you
continue reading, you may want to try drawing the Sierpinski triangle yourself,
using the method described.

Since we can continue to apply the algorithm indefinitely, what is the base case?
We will see that the base case is set arbitrarily as the number of times we want
to divide the triangle into pieces. Sometimes we call this number the “degree” of
the fractal. Each time we make a recursive call, we subtract 1 from the degree
until we reach 0. When we reach a degree of 0, we stop making recursive calls.
The code that generated this Sierpinski Triangle is shown below.
'''


# PEP8 Verified
'''
The sierpinski function relies heavily on the getMid function. getMid takes
as arguments two endpoints and returns the point halfway between them. In
addition, this program has a function that draws a filled triangle using
the begin_fill and end_fill turtle methods.
'''


import turtle


def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

main()
