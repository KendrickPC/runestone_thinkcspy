'''
Although Python provides us with many list methods, it is
good practice and very instructive to think about how they are
implemented. Implement a Python function that works like
the following:

    a. count
    b. in
    c. reverse
    d. index
    e. insert
'''

lst = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]


def count(obj, lst):
    count = 0
    for e in lst:
        if e == obj:
            count = count + 1
    return count

print("\nCount Function Test:")
print(count(1, lst))
print(count(9, lst))


def is_in(obj, lst):
    for e in lst:
        if e == obj:
            return True
    return False

print("\nis_in Function Test:")
print(is_in(4, lst))
print(is_in(100, lst))


def reverse(lst):
    reversed_lst = []
    # Step through the original list backwards
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print("\nReverse Function Test:")
print(reverse(lst))


def index(obj, lst):
    for i in range(len(lst)):
        if lst[i] == obj:
            return i
    return -1

print("\nIndex Function Test:")
print(index(2, lst))


def insert(obj, index, lst):
    new_lst = []
    for i in range(len(lst)):
        if i == index:
            new_lst.append(obj)
        new_lst.append(lst[i])
    return new_lst

print("\nIndex Function Test:")
print(insert('dog', 4, lst))
