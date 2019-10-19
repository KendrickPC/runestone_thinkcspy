'''
Sum all the elements in a list up to but not including
the first even number.
'''

def sumUntilEven(lst):
    # your code here
    sum_lst = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum_lst = sum_lst + lst[index]
        index = index + 1
    return sum_lst


print(sumUntilEven([1, 3, 5, 7, 9, 2, 13, 11, 15]))
