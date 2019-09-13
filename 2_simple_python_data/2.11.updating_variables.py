# 2.11 Updating Variables

x = 6
print(x) # <<< 6
x = x + 1
print(x) # <<< 7

'''
If you try to update a variable that doesn’t exist, you get an error because
Python evaluates the expression on the right side of the assignment operator
before it assigns the resulting value to the name on the left. Before you can
update a variable, you have to initialize it, usually with a simple assignment.
In the above example, x was initialized to 6.

Updating a variable by adding 1 is called an increment; subtracting 1 is called
a decrement. Sometimes programmers also talk about bumping a variable, which
means the same as incrementing it by 1.
'''

print("\ndata-11-1: What is printed when the following statements execute?")
x = 12
x = x - 1
print(x) # <<< 11

print("\ndata-11-2: What is printed when the following statements execute?")
x = 12
x = x - 3
x = x + 5
x = x + 1
print(x) # <<< 15

print("\ndata-11-3: Construct the code that will result in the value 134 being printed.")
bank_balance = 100
bank_balance += 34
print(bank_balance)

