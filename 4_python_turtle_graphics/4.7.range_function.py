# 4.7 The Range Function
'''
In our simple example from the last section (shown again below), we used a list of four integers to cause the iteration to happen four times. We said that we could have used any four values. In fact, we even used four colors.
'''

'''
import turtle # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]: # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
'''

'''
It turns out that generating lists with a specific number of integers is a very common thing to do, especially when you want to write simple for loop controlled iteration. Even though you can use any four items, or any four integers for that matter, the conventional thing to do is to use a list of integers starting with 0. In fact, these lists are so popular that Python gives us special built-in range objects that can deliver a sequence of values to the for loop. When called with one parameter, the sequence provided by range always starts with 0. If you ask for range(4), then you will get 4 values starting with 0. In other words, 0, 1, 2, and finally 3. Notice that 4 is not included since we started with 0. Likewise, range(10) provides 10 values, 0 through 9.
'''

'''
for i in range(4):
    # Executes the body with i = 0, then 1, then 2, then 3
    print(i)

for x in range(10):
    # sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(x)
'''

# Note: Computer scientists like to count from 0!

# So to repeat something four times, a good Python programmer would do this:

'''
for i in range(4):
    alex.forward(50)
    alex.left(90)
'''

'''
The range function is actually a very powerful function when it comes to creating sequences of integers. It can take one, two, or three parameters. We have seen the simplest case of one parameter such as range(4) which creates [0, 1, 2, 3]. But what if we really want to have the sequence [1, 2, 3, 4]? We can do this by using a two parameter version of range where the first parameter is the starting point and the second parameter is the ending point. The evaluation of range(1,5) produces the desired sequence. What happened to the 5? In this case we interpret the parameters of the range function to mean range(start,beyondLast), where beyondLast means an index past the last index we want. In the 2-parameter version of range, that is the last index included + 1.

Note:
Why in the world would range not just work like range(start, stop)? Think about it like this. Because computer scientists like to start counting at 0 instead of 1, range(N) produces a sequence of things that is N long, but the consequence of this is that the final number of the sequence is N-1. In the case of start, stop it helps to simply think that the sequence begins with start and continues as long as the number is less than stop.

Note:
The range function is lazy: It produces the next element only when needed. With a regular Python 3 interpreter, printing a range does not calculate all the elements. To immediately calculate all the elements in a range, wrap the range in a list, like list(range(4)). Activecode is not designed to work on very long sequences, and it may allow you to be sloppy, avoiding the list function, and see the elements in the range with print(range(4)).

Here are a two examples for you to run. Try them and then add another line below to create a sequence starting at 10 and going up to 20 (including 20).
'''

print(list(range(4)))
print(list(range(1, 5)))

print(list(range(10, 21, 1)))

'''
Finally, suppose we want to have a sequence of even numbers. How would we do that? Easy, we add another parameter, a step, that tells range what to count by. For even numbers we want to start at 0 and count by 2’s. So if we wanted the first 10 even numbers we would use range(0,19,2). The most general form of the range is range(start, beyondLast, step). You can also create a sequence of numbers that starts big and gets smaller by using a negative value for the step parameter.
'''

print("\n-----------------------------")
print(list(range(0, 19, 2)))
print(list(range(0, 20, 2)))
print(list(range(10, 0, -1)))


# turtle-8-1: 
'''
In the command range(3, 10, 2), what does the second argument (10) specify?
Answer: A. Range should generate a sequence that stops before 10 (including 9). ✔️ Range will generate the sequence 3, 5, 7, 9.
'''

# turtle-8-2:
'''
What command correctly generates the sequence 2, 5, 8?
    Answer: print(list(range(2, 10, 3)))
✔️ The first number is the starting point, the second is past the last allowed, and the third is the amount to increment by.
'''

# turtle-8-3:
'''
What happens if you give range only one argument? For example: range(4)
A. It will generate a sequence starting at 0, with every number included up to but not including the argument it was passed. ✔️ Yes, if you only give one number to range it starts with 0 and ends before the number specified incrementing by 1.
'''

# turtle-8-4:
'''
Which range function call will produce the sequence 20, 15, 10, 5?
    Answer: print(list(range(20, 3, -5)))
✔️ Yes: If we take steps of -5, not worrying about the ending, we get 20, 15, 10, 5, 0, .... The limit 3 is past the 5, so the range sequence stops with the 5.
'''

# turtle-8-5:
'''
What could the second parameter (12) in range(2, 12, 4) be replaced with and generate exactly the same sequence?
    Answer: C. 11, 13, or 14
✔️ Yes, any integer past 10, and not past the next step at 14 would work.
'''
