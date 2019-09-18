# 4.11 Exercises
'''
1. Write a program that prints We like Python's turtles! 100 times.
'''


def print_100_times():

    for i in range(1, 101, 1):
        print(str(i) + ". We like Python's turtles!")

print_100_times()

print("\n-----------------------------------")

'''
2. Short Answer
turtle-8-4: Turtle objects have methods and attributes. For example, a turtle has a position and when you move the turtle forward, the position changes. Think about the other methods shown in the summary above. Which attibutes, if any, does each method relate to? Does the method change the attribute?

#### method
A function that is attached to an object. Invoking or activating the method causes the object to respond in some way, e.g. forward is the method when we say tess.forward(100).

#### attribute
Some state or value that belongs to a particular object. For example, tess has a color.

The method does not change the attribute. For instance, if the turtle moves forward 100 units, the color of the turtle
will not be changed by moving the turtle forward 100 units.

'''

'''
3. Write a program that uses a for loop to print

        One of the months of the year is January
        One of the months of the year is February
        One of the months of the year is March
        etc …
'''


month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for i in month_list:
    print("One of the months of the year is " + i + ".")

print("\n-----------------------------------")

'''
4. Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20

Write a loop that prints each of the numbers on a new line.

Write a loop that prints each number and its square on a new line.
'''

num_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print("\nnum_list:")
for i in num_list:
    print(i)

print("\n------------------------")

print("num_list squared:")
for i in num_list:
    print(i ** 2)

print("\n-----------------------------------")


'''
5. Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

    * An equilateral triangle
    * A square
    * A hexagon (six sides)
    * An octagon (eight sides)
'''

'''
# An Equilateral Triangle
import turtle

window = turtle.Screen()
ken = turtle.Turtle()

for i in range(2):
    ken.forward(100) # draws base
    ken.left(120)

ken.forward(100)
window.exitonclick()
'''

'''
# A square

import turtle

window = turtle.Screen()
ken = turtle.Turtle()

for i in range(4):
    ken.forward(200)
    ken.left(90)

window.exitonclick()
'''

'''
# A Hexigon (six sides)

import turtle

window = turtle.Screen()
ken = turtle.Turtle()

for i in range(6):
    ken.forward(100)
    ken.left(60)

window.exitonclick()
'''

'''
# An octagon (eight sides)

import turtle

window = turtle.Screen()
ken = turtle.Turtle()

for i in range(8):
    ken.forward(100)
    ken.left(45)

window.exitonclick()
'''

'''
#6. Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon. The program should draw the polygon and then fill it in.
'''

'''
import turtle

window = turtle.Screen()
ken = turtle.Turtle()

number_of_sides = input("How many sides do you want for your polygon? (choose between 3, 4, 6, and 8): ")

number_of_sides_int = int(number_of_sides)

color_choice = input("What do you want the color of your ploygon to be? ")

fill_color_choice = input("What do you want your fill color to be? ")

ken.color(color_choice)
ken.fillcolor(fill_color_choice)

if number_of_sides_int == 3:
    for i in range(2):
        ken.forward(100) # draws base
        ken.left(120)

    ken.forward(100)

elif number_of_sides_int == 4:
    for i in range(4):
        ken.forward(200)
        ken.left(90)

elif number_of_sides_int == 6:
    for i in range(6):
        ken.forward(100)
        ken.left(60)

elif number_of_sides_int == 8:
    for i in range(8):
        ken.forward(100)
        ken.left(45)

else:
    print("Please choose a number from 3, 4, 6, and 8 ONLY. Try Again.")

window.exitonclick()
'''

'''
# 7 A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading.
'''

'''
# Positive angles are counter-clockwise
import turtle

window = turtle.Screen()
ken = turtle.Turtle()
ken.color("blue")
ken.fillcolor("pink")

drunk_turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in drunk_turns:
    ken.left(i)
    ken.forward(100)
    

print("\nThe final heading is: " + str(ken.heading()))

window.exitonclick()
'''

'''
# 6. Write a program that has a shape of a star.
# Each angle within a star is 36 degrees from the inside.
# 36 * 5 = 180

import turtle

window = turtle.Screen()
ken = turtle.Turtle()
ken.color("blue")
ken.fillcolor("pink")   

ken.penup()
ken.backward(75)
ken.pendown()

for i in range(5):
    ken.forward(150)
    ken.right(144)


window.exitonclick()
'''








