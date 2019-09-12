print(type("Hello, World!")) # <<< class 'str'
print(type(17)) # <<< class 'int'
print("Hello, World") # <<< Hello, World

print(type(3.2)) # <<< class 'float'
print(type("17")) # <<< 'str'
print(type("3.2")) # <<< 'str'

print(type('This is a string.') ) # <<< class 'str'
print(type("And so is this.") ) # <<< class 'str'
print(type("""and this.""") ) # <<< class 'str'
print(type('''and even this...''') ) # <<< class 'str'

# Triple Quoted Strings
print("""\nThis message will span
several lines
of the text.""")

print(42000)
'''
Well, that’s not what we expected at all! Because of the comma, Python chose
to treat this as a pair of values. In fact, the print function can print any
number of values as long as you separate them by commas. Notice that the
values are separated by spaces when they are displayed.
'''
print(42,000) # Commas don't work here. <<< 42 0

# data-2-1: How can you determine the type of a variable?
# B. Use the type function.

# data-2-2: What is the data type of ‘this is what kind of data’?
# D. String


