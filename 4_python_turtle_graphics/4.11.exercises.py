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






