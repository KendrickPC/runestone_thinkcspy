# Counting Letters

# Example 1:

print("\nExample 1:")
def countA(text):
    count = 0
    for c in text:
        if c == 'a':
            count = count + 1
    return count

print(countA("banana"))


print("\nExample 2:")
def countA(text):

    return text.count("a")

print(countA("banana"))


'''
General Solution: Counting All Letters¶
Now we will generalize the counting problem and consider how to count the number of times each letter appears in a given string. In order to do this we need to realize that writing a function that returns a single integer will no longer work. Instead we will need to return some kind of collection that holds the counts for each character.

Although there may be many possible ways to do this, we suggest a dictionary where the keys of the dictionary will be the letters in the string and the associated values for each key will be the number of times that the letter appeared.

What about a letter that does not appear in the string? It will never be placed in the dictionary. By assumption, any key that is not in the dictionary has a count of 0.

If we call the function countAll, then a call to countAll would return the dictionary. For example,
'''

'''
1. Here is a start to the development of the function.
2. Define the function to require one parameter, the string.
3. Create an empty dictionary of counts.
4. Iterate through the characters of the string, one character at a time.

print(countAll("banana"))
# <<< {"a":3, "b":1, "n":2}
'''

# Reference:
# https://stackoverflow.com/questions/46787687/count-bases-return-as-dictionary

print("\nExample 3:")

from collections import Counter

def countAll(text):
    text = text.lower()
    return dict(Counter(list(text)))

print(countAll("banana"))



