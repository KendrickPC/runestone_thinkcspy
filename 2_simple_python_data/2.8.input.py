# Input
n = input("Please enter your name: ")
print("\nHello", n)

print("\n--------------------------")
string_seconds = input("Please input the number of seconds you wish to convert: ")
total_seconds = int(string_seconds)
hours = total_seconds // 3600
seconds_still_remaining = total_seconds % 3600
minutes = seconds_still_remaining // 60
seconds_finally_remaining = seconds_still_remaining % 60

print("hours = {}, minutes = {}, seconds = {}".format(hours, minutes, seconds_finally_remaining))


print("\n--------------------------")
# data-8-1: What is printed when the following statements execute?
n = input("Please enter your age: ")
# user types in 18
print ( type(n) )
# <<< class 'str'

print("\n--------------------------")

# data-8-2: Click on all of the variables of type `int` in the code below
# data-8-3: Click on all of the variables of type `str` in the code below



