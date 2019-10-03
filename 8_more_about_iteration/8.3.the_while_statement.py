# 8.3 The While Statement

# Here is a new version of the summation program that uses a while statement.

def sumTo(aBound):
    ''' Return the sum of 1+2+3 ... n '''
    theSum = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4)) # <<< 10
print(sumTo(1000)) # <<< 500500

'''
More formally, here is the flow of execution for a while statement:

    1. Evaluate the condition, yielding False or True.
    2. If the condition is False, exit the while statement and continue execution at the next statement.
    3. If the condition is True, execute each of the statements in the body and then go back to step 1.

The body consists of all of the statements below the header with the same indentation.

This type of flow is called a loop because the third step loops back around to the top. Notice that if the condition is False the first time through the loop, the statements inside the loop are never executed.

    Warning:
    Though Python’s while is very close to the English “while”, there is an important difference: In English “while X, do Y”, we usually assume that immediately after X becomes false, we stop with Y. In Python there is not an immediate stop: After the initial test, any following tests come only after the execution of the whole body, even if the condition becomes false in the middle of the loop body.

The body of the loop should change the value of one or more variables so that eventually the condition becomes False and the loop terminates. Otherwise the loop will repeat forever. This is called an infinite loop. An endless source of amusement for computer scientists is the observation that the directions written on the back of the shampoo bottle (lather, rinse, repeat) create an infinite loop.

In the case shown above, we can prove that the loop terminates because we know that the value of aBound is finite, and we can see that the value of aNumber increments each time through the loop, so eventually it will have to exceed aBound. In other cases, it is not so easy to tell.

    Note:
    Introduction of the while statement causes us to think about the types of iteration we have seen. The for statement will always iterate through a sequence of values like the list of names for the party or the list of numbers created by range. Since we know that it will iterate once for each value in the collection, it is often said that a for loop creates a definite iteration because we definitely know how many times we are going to iterate. On the other hand, the while statement is dependent on a condition that needs to evaluate to False in order for the loop to terminate. Since we do not necessarily know when this will happen, it creates what we call indefinite iteration. Indefinite iteration simply means that we don’t know how many times we will repeat but eventually the condition controlling the iteration will fail and the iteration will stop. (Unless we have an infinite loop which is of course a problem.)

What you will notice here is that the while loop is more work for you — the programmer — than the equivalent for loop. When using a while loop you have to control the loop variable yourself. You give it an initial value, test for completion, and then make sure you change something in the body so that the loop terminates.

So why have two kinds of loop if for looks easier? The next section, Randomly Walking Turtles, shows an indefinite iteration where we need the extra power that we get from the while loop.

# Randomly Walking Turtles
# https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/RandomlyWalkingTurtles.html#randomly-walking-turtles

'''

# What is printed by this code?
n = 1
x = 2

while n < 5:
    n = n + 1
    x = x + 1
    n = n + 2
    x = x + n

print(n, x) # <<< (7, 15)


