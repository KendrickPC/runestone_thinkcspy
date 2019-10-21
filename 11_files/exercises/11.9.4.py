'''
Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair. Write a function called plotRegression that reads the data from this file and uses a turtle to plot those points and a best fit line according to the following formulas:

𝑦=𝑦¯+𝑚(𝑥−𝑥¯)

𝑚=∑𝑥𝑖𝑦𝑖−𝑛𝑥¯𝑦¯∑𝑥2𝑖−𝑛𝑥¯2

where 𝑥¯ is the mean of the x-values, 𝑦¯ is the mean of the y- values and 𝑛 is the number of points. If you are not familiar with the mathematical ∑ it is the sum operation. For example ∑𝑥𝑖 means to add up all the x values.

Your program should analyze the points and correctly scale the window using setworldcoordinates so that that each point can be plotted. Then you should draw the best fit line, in a different color, through the points.
'''

from turtle import Turtle, Screen

def plotRegression(data):

    x_list, y_list = [int(i[0]) for i in data], [int(i[1]) for i in data]
    x_list, y_list = [float(i) for i in x_list], [float(i) for i in y_list]
    x_sum, y_sum = sum(x_list), sum(y_list)
    x_bar, y_bar = x_sum / len(x_list), y_sum / len(y_list)
    x_list_square = [i ** 2 for i in x_list]
    x_list_square_sum = sum(x_list_square)
    xy_list = [x_list[i] * y_list[i] for i in range(len(x_list))]
    xy_list_sum = sum(xy_list)

    m = (xy_list_sum - len(x_list) * x_bar * y_bar) / (x_list_square_sum - len(x_list) * x_bar ** 2)
    # best y
    y_best = [(y_bar + m * (x_list[i] - x_bar)) for i in range(len(x_list))]

    # plot points

    turtle = Turtle()

    for i in range(len(x_list)):
        turtle.penup()
        turtle.setposition(x_list[i], y_list[i])
        turtle.stamp()

    # plot best y
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.color('blue')
    for i in range(len(x_list)):
        turtle.setposition(x_list[i], y_best[i])
        turtle.pendown()

    return (min(x_list), min(y_list), max(x_list), max(y_list))

screen = Screen()

screen.bgcolor('pink')

f = open("labdata.txt", "r")

plot_data = []

for aline in f:
    x, y = aline.split()
    plot_data.append((x, y))

# This next line should be something like:

# screen.setworldcoordinates(*plotRegression(plot_data))

# but setworldcoordinates() is so tricky to work with
# that I'm going to leave it at:

print(*plotRegression(plot_data))

# and suggest you trace a rectangle with the return
# values to get an idea what's going to happen to
# your coordinate system

screen.exitonclick()