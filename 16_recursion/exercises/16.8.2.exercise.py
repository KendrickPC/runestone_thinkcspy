# Write a recursive function to reverse a list.


def reverseList(lst):
    #your code here
    if not lst:
        return []
    return [lst[-1]] + reverseList(lst[:-1])

print(reverseList([1, 2, 3, 4, 5]))
