# 9.8 String Comparison

word = "banana"
if word == "banana":
    print("Yes, we have bananas!")
else:
    print("Yes, we have NO bananas!")


'''
Other comparison operations are useful for putting words in
lexicographical order. This is similar to the alphabetical order
you would use with a dictionary, except that all the uppercase
letters come before all the lowercase letters.
'''

word = "zebra"

if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")



print("apple" < "banana") # <<< True
print("apple" == "Apple") # <<< False
print("apple" < "Apple") # <<< False

'''
It turns out, as you recall from our discussion of variable names,
that uppercase and lowercase letters are considered to be different
from one another. The way the computer knows they are different is
that each character is assigned a unique integer value.
“A” is 65, “B” is 66, and “5” is 53. The way you can find out the
so-called ordinal value for a given character is to use a character
function called ord.
''' 

print(ord("A")) # <<< 65
print(ord("B")) # <<< 66
print(ord("5")) # <<< 53
print(ord("a")) # <<< 97
print("apple" > "Apple") # <<< True


'''
When you compare characters or strings to one another, Python converts
the characters into their equivalent ordinal values and compares the
integers from left to right. As you can see from the example above,
“a” is greater than “A” so “apple” is greater than “Apple”.

Humans commonly ignore capitalization when comparing two words. However,
computers do not. A common way to address this issue is to convert strings
to a standard format, such as all lowercase, before performing the
comparison.

There is also a similar function called chr that converts integers into
their character equivalent.
'''

print("\nCharacter Equivalent")
print(chr(65)) # <<< A
print(chr(66)) # <<< B
print(chr(49)) # <<< 1
print(chr(53)) # <<< 5
print("The character for 32 is", chr(32), "!!!")
print(ord(" "))


