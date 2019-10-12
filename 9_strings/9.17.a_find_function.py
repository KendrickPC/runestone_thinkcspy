# 9.17 A Find Function

def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find("Compsci", "p")) # <<< 3
print(find("Compsci", "C")) # <<< 0
print(find("Compsci", "i")) # <<< 6
print(find("Compsci", "x")) # <<< -1

'''
In a sense, find is the opposite of the indexing operator. Instead of taking an index and extracting the corresponding character, it takes a character and finds the index where that character appears for the first time. If the character is not found, the function returns -1.

The while loop in this example uses a slightly more complex condition than we have seen in previous programs. Here there are two parts to the condition. We want to keep going if there are more characters to look through and we want to keep going if we have not found what we are looking for. The variable found is a boolean variable that keeps track of whether we have found the character we are searching for. It is initialized to False. If we find the character, we reassign found to True.

The other part of the condition is the same as we used previously to traverse the characters of the string. Since we have now combined these two parts with a logical and, it is necessary for them both to be True to continue iterating. If one part fails, the condition fails and the iteration stops.

When the iteration stops, we must ask a question to find out the individual condition that caused the termination, and then return the proper value. This is a pattern for dealing with while loops with compound conditions.

Note:
This pattern of computation is sometimes called a eureka traversal because as soon as we find what we are looking for, we can cry Eureka! and stop looking. The way we stop looking is by setting found to True which causes the condition to fail.
'''

