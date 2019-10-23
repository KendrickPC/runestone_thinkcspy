# Letter Count Histogram
'''
The previous lab wrote a function to return a dictionary of letter
counts. In an earlier chapter, we wrote a turtle program that could
draw a histogram.

Combine these two ideas together to create a function that will take
a string and create a histogram of the number of times each letter
occurs. Make sure it is in alphabetical order from left to right.

Count the number of times each letter occurs.
Keep the count in a dictionary.

Get the keys from the dictionary, convert them to a list, and sort them.

Iterate through the keys, in alphabetical order, getting the associated
value (count).

Make a histogram bar for each.
'''

from collections import Counter

def countAll(text):
    text = text.upper()
    return (dict(Counter(list(text))))

print(countAll("banana"))
