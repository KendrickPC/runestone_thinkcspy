def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)

# Which of the following best reflects the order in which
# these lines of code are processed in Python?

# E. 1, 5, 9, 10, 5, 6, 1, 2, 3, 6, 7, 10, 11

'''
✔️ Python starts at line 1, notices that it is a function definition and skips over all of the lines in the function definition until it finds a line that it no longer included in the function (line 5). It then notices line 5 is also a function definition and again skips over the function body to line 9. On line 10 it notices it has a function to execute, so it goes back and executes that function. Notice that that function includes another function call. It returns from the function call and completes the assignment in line 6. Then it returns the result of line 7 and completes the assignment in line 10. Finally, it will go to line 11 after the function square and the assignment are complete.
'''

