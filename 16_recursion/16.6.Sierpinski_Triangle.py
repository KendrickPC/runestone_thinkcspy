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


import turtle

def drawSierpinski(length, depth):
    if depth == 0:
        for i in range(0, 3):
            t.fd(length)
            t.left(120)
    else:
        drawSierpinski(length/2, depth-1)
        t.fd(length/2)
        drawSierpinski(length/2, depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        drawSierpinski(length/2, depth-1)


window = turtle.Screen()
t = turtle.Turtle()
drawSierpinski(250, 2)
window.exitonclick()






