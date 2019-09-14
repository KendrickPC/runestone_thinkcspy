# 3.2. How to Avoid Debugging

'''
Perhaps the most important lesson in debugging is that it is largely avoidable – if you work carefully.

1. Understand the Problem:
    You must have a firm grasp on what you are trying to accomplish but not necessarily how to do it. You do not need to understand the entire problem. But you must understand at least a portion of it and what the program should do in a specific circumstance – what output should be produced for some given input. This will allow you to test your progress. You can then identify if a solution is correct or whether there remains work to do or bugs to fix. This is probably the single biggest piece of advice for programmers at every level.

2. Start Small:
    It is tempting to sit down and crank out an entire program at once. But, when the program – inevitably – does not work, you have a myriad of options for things that might be wrong. Where to start? Where to look first? How to figure out what went wrong? I’ll get to that in the next section. So, start with something really small. Maybe just two lines and then make sure that runs. Hitting the run button is quick and easy. It gives you immediate feedback about whether what you have just done works or not. Another immediate benefit of having something small working is that you have something to turn in. Turning in a small, incomplete program, is almost always better than nothing.

3. Keep Improving It
    Once you have a small part of your program working, the next step is to figure out something small to add to it – how can you move closer to a correct solution. As you add to your program, you gain greater insight into the underlying problem you are trying to solve.

If you keep adding small pieces of the program one at a time, it is much easier to figure out what went wrong. (This of course means you must be able to recognize if there is an error. And that is done through testing.)

As long as you always test each new bit of code, it is most likely that any error is in the new code you have just added. Less new code means its easier to figure out where the problem is.

This notion of Get something working and keep improving it is a mantra that you can repeat throughout your career as a programmer. It’s a great way to avoid the frustrations mentioned above. Think of it this way. Every time you have a little success, your brain releases a tiny bit of chemical that makes you happy. So, you can keep yourself happy and make programming more enjoyable by creating lots of small victories for yourself.

# Note
The technique of start small and keep improving is the basis of Agile software development. This practice is used widely in the industry.

Ok, let’s look at an example. Let’s solve the problem posed in question 3 at the end of the Simple Python Data chapter. Ask the user for the time now (in hours 0 - 23), and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off. For example, if current_time is 8 and wait_time is 5, final_time should be 13 (1 pm).

So, where to start? The problem requires two pieces of input from the user, so let’s start there and make sure we can get the data we need.
'''

current_time_str = input("What is the current time (in hours 0-23)? ")
wait_time_str = input("How many hours do you want to wait: ")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int

final_answer = final_time_int % 24

print("The time after waiting is: ", final_answer)
