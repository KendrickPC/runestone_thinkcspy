# 4.1 Hello Little Turtles
'''
There are many modules in Python that provide very powerful features that we can use in our own programs. Some of these can send email or fetch web pages. Others allow us to perform complex mathematical calculations. In this chapter we will introduce a module that allows us to create a data object called a turtle that can be used to draw pictures.

Turtle graphics, as it is known, is based on a very simple metaphor. Imagine that you have a turtle that understands English. You can tell your turtle to do simple commands such as go forward and turn right. As the turtle moves around, if its tail is down touching the ground, it will draw a line (leave a trail behind) as it moves. If you tell your turtle to lift up its tail it can still move around but will not leave a trail. As you will see, you can make some pretty amazing drawings with this simple capability.
'''

# Note
'''
The turtles are fun, but the real purpose of the chapter is to teach ourselves a little more Python and to develop our theme of computational thinking, or thinking like a computer scientist. Most of the Python covered here will be explored in more depth later.
'''


import turtle

wn = turtle.Screen() # creates a graphic window
alex = turtle.Turtle() # Create a turtle named Alex.
alex.color("green")
alex.pensize(5)

alex.forward(150) # Tell alex to move foward 150 units
alex.left(90) # Turn by 90 degrees
alex.forward(150) # Tell alex to move forward 150 units

wn.exitonclick() # wait for a user click on the canvas
