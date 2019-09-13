# Operators and Operands

print("\n----------------------------")
print(2 + 3) # <<< 5
print(2 - 3) # <<< -1
print(2 * 3) # <<< 6
print(2 ** 3) # <<< 8
print(3 ** 2) # <<< 9

print("\n----------------------------")
minutes = 645
hours = minutes / 60
print(hours) # <<< 10.75

print("\n----------------------------")
print(7 / 4) # <<< 1.75
print(7 // 4) # <<< 1
minutes = 645
hours = minutes // 60
print(hours) # <<< 10

print("\nThis is the integer division operator:")
# This is the integer division operator
quotient = 7 // 3     
print(quotient) # <<< 2
remainder = 7 % 3
print(remainder) # <<< 1

print("\nTime Example:")
total_seconds = 7684
hours = total_seconds // 3600 # 1 hour holds 3600 seconds
seconds_remaining = total_seconds % 3600 # Modulo returns the remainder
minutes = seconds_remaining // 60 # Integer division operator
seconds_finally_remaining = seconds_remaining % 60
print("\ntotal_seconds:")
print(total_seconds)
print("hours:")
print(hours)
print("minutes:")
print(minutes)
print("seconds")
print(seconds_finally_remaining)

print("\nChecking answer:")
print((3600*2) + (8 * 60) + 4 )

print("\ndata-7-1: What value is printed when the following statement executes?")
print(18 / 4)
# Answer: <<< 4.5

print("\ndata-7-2: What value is printed when the following statement executes?") 
print(18 // 4)
# Answer: <<< 4

print("\ndata-7-3: What value is printed when the following statement executes?")
print(18 % 4)
# Answer: <<< 2



