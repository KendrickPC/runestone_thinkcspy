# 9.14. The Accumulator Pattern with Strings¶
'''
Combining the in operator with string concatenation using + and the accumulator
pattern, we can write a function that removes all the vowels from a string.
The idea is to start with a string and iterate over each character, checking
to see if the character is a vowel. As we process the characters, we will build
up a new string consisting of only the nonvowel characters.
To do this, we use the accumulator pattern.

Remember that the accumulator pattern allows us to keep a “running total”.
With strings, we are not accumulating a numeric total.
Instead we are accumulating characters onto a string.
'''

def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels

print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))

