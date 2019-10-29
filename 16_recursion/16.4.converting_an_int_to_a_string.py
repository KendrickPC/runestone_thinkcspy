# 16.4. Converting an Integer to a String in Any Base
'''
Knowing what our base is suggests that the overall algorithm will involve
three components:

Reduce the original number to a series of single-digit numbers.

Convert the single digit-number to a string using a lookup.

Concatenate the single-digit strings together to form the final result.
'''

print("\nExample 1:")


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]


print(toStr(1453, 16)) # <<< 5AD


'''
Self Check

Write a function that takes a string as a parameter and returns a
new string that is the reverse of the old string.
'''
print("\nExample 2:")


def reverse(s):
    return s[::-1]

print(reverse("abc"))


'''
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward. for example: radar is a palindrome. for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking. for example: madam i’m adam is a palindrome. Other fun palindromes include:

    kayak
    aibohphobia
    Live not on evil
    Reviled did I live, said I, as evil I did deliver
    Go hang a salami; I’m a lasagna hog.
    Able was I ere I saw Elba
    Kanakanak – a town in Alaska
    Wassamassaw – a town in South Dakota

'''


print("\nExample 3:")


# from test import testEqual
def removeWhite(s):
    removed_white_space = s.strip()
    return removed_white_space

def isPal(s):
    reverse_string = s[::-1]
    if s == reverse_string:
        return True
    else:
        return False

# testEqual(isPal(removeWhite("x")),True)
# testEqual(isPal(removeWhite("radar")),True)
# testEqual(isPal(removeWhite("hello")),False)
# testEqual(isPal(removeWhite("")),True)
# testEqual(isPal(removeWhite("hannah")),True)
# testEqual(isPal(removeWhite("madam i'm adam")),True)


print("\nRemove White Space Test:")
print(removeWhite("      abc    ")) # Pass

print("\nTesting for Palindrome:")
print(isPal("racecar"))



