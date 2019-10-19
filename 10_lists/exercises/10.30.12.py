'''
Count how many words occur in a list up to and including the
first occurrence of the word “sam”.
'''

def count(lst):
    # your code here
    count = 0
    index = 0
    while index < len(lst) and lst[index] != 'sam':
        count = count + 1
        index = index + 1
    return count


print(count(['hello', 'my', 'name','is', 'sam', '.', 'what', 'is']))