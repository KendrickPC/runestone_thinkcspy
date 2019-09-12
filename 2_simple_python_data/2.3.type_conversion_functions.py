'''
The int function can take a floating point number or a string, and turn
it into an int. For floating point numbers, it discards the decimal
portion of the number - a process we call truncation towards zero on
the number line. Let us see this in action:
'''

print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
# print(int("\n23bottles"))

print(float("123.45"))
print(type(float("123.45")))

print(str(17))
print(str(123.45))
print(type(str(123.45)))

# data-3-1: What value is printed when the following statement executes?
# print( int(53.785) )
# B. 53



