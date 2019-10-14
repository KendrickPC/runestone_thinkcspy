'''
Write a function that removes all occurrences of a given letter
from a string.
'''

def remove_letter(theLetter, theString):
    
    new_string = ""

    for eachChar in theString:
        if eachChar not in theLetter:
            new_string = new_string + eachChar

    return new_string


print(remove_letter('e', "The grass is greener where you water it."))
