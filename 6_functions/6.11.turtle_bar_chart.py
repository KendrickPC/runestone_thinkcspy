# 6.11 Turtle Bar Chart
'''
We can quickly see that drawing a bar will be similar to
drawing a rectangle or a square. Since we will need to do it
a number of times, it makes sense to create a function,
drawBar, that will need a turtle and the height of the bar.
We will assume that the width of the bar will be 40 units.
Once we have the function, we can use a basic for loop to
process the list of data values.
'''
import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill() # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() # stop filling this shape


xs = [33, 27, 8, 99, 34, 23, 18] # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen() # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)


for a in xs:
    drawBar(tess, a)

wn.exitonclick()