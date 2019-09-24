# Variables and parameters are local
# Local scope variables and parameters

'''
An assignment statement in a function creates a local variable for the variable on the left hand side of the assignment operator. It is called local because this variable only exists inside the function and you cannot use it outside. For example, consider again the square function:
'''

'''
def square(x):
    y = x * x
    return y

z = square(10)
# NameError: name 'y' is not defined
print(y) 
'''

'''
The variable y only exists while the function is being executed — we call this its lifetime. When the execution of the function terminates (returns), the local variables are destroyed. 

On the other hand, it is legal for a function to access a global variable. However, this is considered bad form by nearly all programmers and should be avoided. Look at the following, nonsensical variation of the square function.
'''

def badsquare(x):
    y = x ** power
    return y

power = 2
result = badsquare(10)
print(result) # <<< 100


print("\nRewrite of the power function: ")
def power(x, p=3):
    y = x ** p
    return y

print(power(2))


print("\nExample of local versus global scope: ")
def square(x):
    y = x * x
    x = 0 # Assign a new value to the x parameter.
    return y

x = 2
z = square(x)
print(z)



