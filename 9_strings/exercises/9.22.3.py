'''
Assign to a variable in your program a triple-quoted string that contains
your favorite paragraph of text - perhaps a poem, a speech, instructions
to bake a cake, some inspirational verses, etc.

Write a function that counts the number of alphabetic characters
(a through z, or A through Z) in your text and then keeps track of how many
are the letter ‘e’. Your function should print an analysis of the
text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.
'''

import string


quote_1 = "The grass is greener where you water it."


def count_e(quote_1):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    count_e = 0
    totalChars = 0

    for achar in quote_1:
        if achar in alphabet_lower or achar in alphabet_upper:
            totalChars = totalChars + 1
            if achar == 'e':
                count_e = count_e + 1

    percent_with_e = (count_e / totalChars) * 100
    print("Your text contains", totalChars, "alphabetic characters of which", count_e, "(", percent_with_e, "%)", "are 'e'.")


count_e(quote_1)
