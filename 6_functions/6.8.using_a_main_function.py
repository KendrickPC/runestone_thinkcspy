# 6.8 Using a Main Function
'''
These final five statements perform the main processing that the program will do. Notice that much of the detail has been pushed inside the drawSquare function. However, there are still these five lines of code that are needed to get things done.

In many programming languages (e.g. Java and C++), it is not possible to simply have statements sitting alone like this at the bottom of the program. They are required to be part of a special function that is automatically invoked by the operating system when the program is executed. This special function is called main. Although this is not required by the Python programming language, it is actually a good idea that we can incorporate into the logical structure of our program. In other words, these five lines are logically related to one another in that they provide the main tasks that the program will perform. Since functions are designed to allow us to break up a program into logical pieces, it makes sense to call this piece main.
'''

'''
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


def main(): # Define the main function
    window = turtle.Screen() # Set up window and its attributes
    window.bgcolor("lightblue")

    kendrick = turtle.Turtle()
    drawSquare(kendrick, 75)

    window.exitonclick()

main() # Invoke the main function
'''

'''
Note:
In Python there is nothing special about the name main. We could have called this function anything we wanted. We chose main just to be consistent with some of the other languages.
'''

# Advanced Topics
def square_it(n):
    return n * n


def cube_it(n):
    return n * n * n

def main():
    prompt = int(input("Please enter an integer: "))
    print(square_it(prompt))
    print(cube_it(prompt))


if __name__ == "__main__":
    main()

'''
An if statement is used to ask about the value of the __name__ variable. If the value is "__main__", then the main function will be called. Otherwise, it can be assumed that the program is being imported into another program and we do not want to call main because that program will invoke the functions as needed. This ability to conditionally execute our main function can be extremely useful when we are writing code that will potentially be used by others. It allows us to include functionality that the user of the code will not need, most often as part of a testing process to be sure that the functions are working correctly.
'''

# Note: 
'''
In order to conditionally execute the main function, we used
a structure called an if statement to create what is known
as selection. This topic will be studied in much more detail
later.
'''
