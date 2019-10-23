'''
Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample run of the program might look this this:

Please enter a sentence: ThiS is String with Upper and lower case Letters.
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2

'''


def letterCountSort(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    # Empty dictionary
    letter_count = {}
    for char in text:
        if char in alphabet:
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1
    
    # Below will return a counted dictionary
    # return letter_count

    # Sorting the alphabet of the dictionary printed.
    keys = letter_count.keys()
    for char in sorted(keys):
        print(char, letter_count[char])

letterCountSort("How are you?")

