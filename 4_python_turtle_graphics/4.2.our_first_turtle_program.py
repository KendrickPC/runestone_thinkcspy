# 4.2 Our First Turtle Program
'''
Let’s try a couple of lines of Python code to create a new turtle and start drawing a simple figure like a rectangle. We will refer to our first turtle using the variable name alex, but remember that you can choose any name you wish as long as you follow the naming rules from the previous chapter.

The program as shown will only draw the first two sides of the rectangle. After line 4 you will have a straight line going from the center of the drawing canvas towards the right. After line 6, you will have a canvas with a turtle and a half drawn rectangle. Press the run button to try it and see.
'''

'''
import turtle # allows us to use the turtles library

wn = turtle.Screen() # creates a graphics window
alex = turtle.Turtle() # create a turtle named alex


alex.forward(150) # tell alex to move forward by 150 units
alex.left(90) # turn by 90 degrees
alex.forward(150) # complete the second side of a rectangle
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)

wn.exitonclick()
'''


'''
Here are a couple of things you’ll need to understand about this program.

The first line tells Python to load a module named turtle. That module brings us two new types that we can use: the Turtle type, and the Screen type. The dot notation turtle. Turtle means “The Turtle type that is defined within the turtle module”. (Remember that Python is case sensitive, so the module name, turtle, with a lowercase t, is different from the type Turtle because of the uppercase T.)

We then create and open what the turtle module calls a screen (we would prefer to call it a window, or in the case of this web version of Python simply a canvas), which we assign to variable wn. Every window contains a canvas, which is the area inside the window on which we can draw.

In line 3 we create a turtle. The variable alex is made to refer to this turtle. These first three lines set us up so that we are ready to do some drawing.

In lines 4-6, we instruct the object alex to move and to turn. We do this by invoking or activating alex’s methods — these are the instructions that all turtles know how to respond to. Here the dot indicates that the methods invoked belong to and refer to the object alex.
'''

# Complete the rectangle
'''
Modify the program by adding the commands necessary to have alex complete the rectangle.
'''

# Check your understanding
'''
turtle-2-1: Which direction does the Turtle face when it is created?
Answer: East
'''

# turtle-2-2:
'''
The following program uses a turtle to draw a capital L as shown in the picture to the left of this text, but the lines are mixed up. The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle. Remember that the turtle starts off facing east when it is created. The turtle should turn to face south and draw a line that is 150 pixels long and then turn to face east and draw a line that is 75 pixels long. We have added a compass to the picture to indicate the directions north, south, west, and east.

Drag the blocks of statements from the left column to the right column and put them in the right order. Then click on Check Me to see if you are right. You will be told if any of the lines are in the wrong order.
'''

'''
import turtle

window = turtle.Screen()
ella = turtle.Turtle()

ella.right(90)
ella.forward(150)

ella.left(90)
ella.forward(75)

window.exitonclick()
'''


# turtle-2-3:
'''
The following program uses a turtle to draw a checkmark as shown to the left, but the lines are mixed up. The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle. The turtle should turn to face southeast, draw a line that is 75 pixels long, then turn to face northeast, and draw a line that is 150 pixels long. We have added a compass to the picture to indicate the directions north, south, west, and east. Northeast is between north and east. Southeast is between south and east.

Drag the blocks of statements from the left column to the right column and put them in the right order. Then click on Check Me to see if you are right. You will be told if any of the lines are in the wrong order.
'''

'''
import turtle # Import turtle library

window = turtle.Screen() # Creates a graphics window
maria = turtle.Turtle() # Creates a turtle named maria

maria.right(45)
maria.forward(75)

maria.left(90)
maria.forward(150)

window.exitonclick()
'''

# turtle-2-4: 
'''
The following program uses a turtle to draw a single line to the west as shown to the left, but the program lines are mixed up. The program should do all necessary set-up: import the turtle module, get the window to draw on, and create the turtle. The turtle should then turn to face west and draw a line that is 75 pixels long.

Drag the blocks of statements from the left column to the right column and put them in the right order. Then click on Check Me to see if you are right. You will be told if any of the lines are in the wrong order.
'''

'''
import turtle

window = turtle.Screen()
jamal = turtle.Turtle()

jamal.left(180)
jamal.forward(75)

window.exitonclick()
'''


'''
An object can have various methods — things it can do — and it can also have attributes — (sometimes called properties). For example, each turtle has a color attribute. The method invocation alex.color(“red”) will make alex red and the line that it draws will be red too.

The color of the turtle, the width of its pen(tail), the position of the turtle within the window, which way it is facing, and so on are all part of its current state. Similarly, the window object has a background color which is part of its state.

Quite a number of methods exist that allow us to modify the turtle and window objects. In the example below, we show just show a couple and have only commented those lines that are different from the previous example. Note also that we have decided to call our turtle object tess.
'''
'''
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen") # set the window background color

tess = turtle.Turtle()
tess.color("blue") # make tess blue
tess.pensize(3) # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick() # wait for a user click on the canvas
'''

'''
The last line plays a very important role. The wn variable refers to the window shown above. When we invoke its exitonclick method, the program pauses execution and waits for the user to click the mouse somewhere in the window. When this click event occurs, the response is to close the turtle window and exit (stop execution of) the Python program.

Each time we run this program, a new drawing window pops up, and will remain on the screen until we click on it.
'''

# Extend this program
'''
1. Modify this program so that before it creates the window, it prompts the user to enter the desired background color. It should store the user’s responses in a variable, and modify the color of the window according to the user’s wishes. (Hint: you can find a list of permitted color names at https://www.w3schools.com/colors/colors_names.asp. It includes some quite unusual ones, like “PeachPuff” and “HotPink”.)

2. Do similar changes to allow the user, at runtime, to set tess’ color.

3. Do the same for the width of tess’ pen. Hint: your dialog with the user will return a string, but tess’ pensize method expects its argument to be an int. That means you need to convert the string to an int before you pass it to pensize.
'''


background_prompt = input("What is your desired background color? ")
pen_prompt = input("What is your desired pen color? ")
pen_size = input("What is the size (thickness) of pen you want? Please enter an integer: ")
pen_size_int = int(pen_size)

import turtle # import turtle

window = turtle.Screen() # open screen


window.bgcolor(background_prompt) # set the window background color

tess = turtle.Turtle()
tess.color(pen_prompt) # setting pen color
tess.pensize(pen_size_int) # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

window.exitonclick() # wait for a user click on the canvas


# turtle-2-5: Consider the following code:
# What does the line “import turtle” do?
# B. It defines the module turtle which will allow you to create a Turtle object and draw with it.


# turtle-2-6: Why do we type turtle.Turtle() to get a new Turtle object?
# C. The first "turtle" (before the period) tells Python that we are referring to the turtle module, which is where the object "Turtle" is found. Yes, the Turtle type is defined in the module turtle. Remember that Python is case sensitive and Turtle is different from turtle.


# turtle-2-7: True or False: A Turtle object can have any name that follows the naming rules from Chapter 2.
# Answer: <<< True 
# n this chapter you saw one named alex and one named tess, but any legal variable name is allowed.




