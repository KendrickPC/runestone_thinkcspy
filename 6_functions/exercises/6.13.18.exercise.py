'''
There was a whole program in A Turtle Bar Chart to create
a bar chart with specific data. Creating a bar chart is a
useful idea in general. Write a non-fruitful function
called barChart, that takes the numeric list of data as
a parameter, and draws the bar chart.
Write a full program calling this function.
The current version of the drawBar function unfortuately
draws the top of the bar through the bottom of the label.
A nice elaboration is to make the label appear completely
above the top line. To keep the spacing consistent you
might pass an extra parameter to drawBar for the distance
to move up.
For the barChart function make that parameter be some
small fraction of maxheight+border. The fill action makes
this modification particularly tricky: You will want to
move past the top of the bar and write before or after
drawing and filling the bar.
'''


import turtle

xs = [33, 27, 8, 99, 34, 23, 18] # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10


window = turtle.Screen() # Setting up window attributes
window.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
window.bgcolor('lightgreen')

kendrick = turtle.Turtle()
kendrick.color('blue')
kendrick.fillcolor('yellow')
kendrick.pensize(2)


def labeling(t, height):
    # Attacking labeling issue in barchart
    kendrick.penup()
    kendrick.forward(3)
    kendrick.right(90)
    kendrick.forward(18)
    kendrick.pendown()

    kendrick.write(height)
    kendrick.penup()
    kendrick.backward(18)
    kendrick.left(90)
    kendrick.backward(3)
    kendrick.pendown()


def drawBar(t, height):
    # Turtle kendrick draws one bar with height
    kendrick.begin_fill()
    kendrick.left(90)
    kendrick.forward(height)
    
    labeling(t, height)

    kendrick.right(90)
    kendrick.forward(40)
    kendrick.right(90)
    kendrick.forward(height)
    kendrick.left(90)
    kendrick.end_fill() # Stop filling the shape.


for a in xs:
    drawBar(kendrick, a)


window.exitonclick()


