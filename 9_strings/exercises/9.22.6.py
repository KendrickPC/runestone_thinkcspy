# Write a function that reverses its string argument.

# Reference Source:
# https://stackoverflow.com/questions/3901340/python-write-a-function-that-takes-a-string-as-an-argument-and-displays-the-le

def reverse(astring):
    # your code here
    return ''.join(reversed(astring))

print(reverse('abc'))
