'''
Modify the recursive tree program using one or all of the following ideas:

    1. Modify the thickness of the branches so that as the branchLen
    gets smaller, the line gets thinner.

    2. Modify the color of the branches so that as the branchLen gets 
    very short it is colored like a leaf.

    3. Modify the angle used in turning the turtle so that at each
    branch point the angle is selected at random in some range.
    For example choose the angle between 15 and 45 degrees. Play
    around to see what looks good.

    4. Modify the branchLen recursively so that instead of always
    subtracting the same amount you subtract a random amount in
    some range.

If you implement all of the above ideas you will have a very
realistic looking tree
'''

#Recursive Tree Challenge - www.101computing.net/recursive-tree-challenge
import turtle

def tree(branchLen,t):
    if branchLen > 2:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        # Modification #3 complete with code below.
        t.left(30)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(60)
    t.up()
    t.backward(50)
    t.down()
    t.color("green")
    # Modification #1 complete with code below.
    t.width(1)
    # Modification #2 complete with code below.
    tree(75, t)
    myWin.exitonclick()

main()
