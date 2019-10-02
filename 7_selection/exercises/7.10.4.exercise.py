'''
Modify the turtle bar chart program from the previous chapter
so that the bar for any value of 200 or more is filled with
red, values between [100 and 200) are filled yellow, and bars
representing values less than 100 are filled green.
'''


import turtle

xs = [250, 150, 75, 200, 101, 50] # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10


window = turtle.Screen() # Setting up window attributes
window.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
window.bgcolor('lightgreen')

kendrick = turtle.Turtle()
kendrick.color('blue')
# kendrick.fillcolor('yellow')
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
    if a >= 200:
        kendrick.fillcolor("red")
    elif a < 200 and a > 100:
        kendrick.fillcolor("yellow")
    else:
        kendrick.fillcolor("green")
    
    drawBar(kendrick, a)



window.exitonclick()


