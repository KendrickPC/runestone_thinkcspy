# Count how many words in a list have length 5.

def countWords(lst):
    # your code here
    count = 0
    for i in lst:
        if len(i) == 5:
            count = count + 1
    return count


print(countWords(['hello', 'no', 'fiveO']))

