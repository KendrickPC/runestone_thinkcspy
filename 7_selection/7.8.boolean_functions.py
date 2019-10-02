# 7.8. Boolean Functions

'''
def isDivisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False

    return result

print(isDivisible(10, 5)) # <<< True
'''

def isDivisible(x, y):
    return x % y == 0

if isDivisible(10, 5):
    print("That works")
else:
    print("Those values are no good")


# select-8-2: Is the following statement legal in a Python
# function (assuming x, y and z are defined to be numbers)?

# return x + y < z 
# ✔️ It is perfectly valid to return the result of evaluating
# a Boolean expression.


'''
7.8.1. More Unit Testing
When we write unit tests, we should also consider output
equivalence classes that result in significantly different
results.

The isDivisible function can return either True or False.
These two different outputs give us two equivalence classes.
We then choose inputs that should give each of the different
results. It is important to have at least one test for each
output equivalence class.
'''

