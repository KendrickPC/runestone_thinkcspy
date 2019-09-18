'''
# 13 A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360 / n degrees.

Write a program to draw a sprite where the number of legs is provided by the user.

'''

number_of_legs = input("input a number of legs (choose between 0 and 360): ")
number_of_legs_int = int(number_of_legs)

if number_of_legs_int == 0:
    print("\tZero doesn't draw anything. Please try again.")

import turtle

window = turtle.Screen()
ken = turtle.Turtle()
window.bgcolor("lightblue")
ken.color("pink")
ken.pensize(4)

for i in range(number_of_legs_int + 1):
    ken.forward(100)
    ken.backward(100)
    ken.left(360 / number_of_legs_int)

window.exitonclick()
