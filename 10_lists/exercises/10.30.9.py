# Sum up all the negative numbers in a list.

def sumNegatives(lst):
    # your code here
    return sum(i for i in lst if i < 0)


print(sumNegatives([-1, -5, 10]))
print(sumNegatives([1, 5, 10]))
