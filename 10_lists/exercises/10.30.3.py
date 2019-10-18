'''
Starting with the list of the previous exercise, write Python
statements to do the following:

    a. Append “apple” and 76 to the list.
    b. Insert the value “cat” at position 3.
    c. Insert the value 99 at the start of the list.
    d. Find the index of “hello”.
    e. Count the number of 76s in the list.
    f. Remove the first occurrence of 76 from the list.
    g. Remove True from the list using pop and index.

'''

# Starting with list from previous exercise
myList = [76, 92.3, 'hello', True, 4, 76]


myList.append("apple")
myList.append(76)
myList.insert(3, 'cat')
myList.insert(0, 99)

print("\nFinding index of 'hello'.")
print(myList.index('hello'))

print("\nCounting the number of 76s in the list.")
print(myList.count(76))

myList.remove(76)
myList.pop(myList.index(True))

print("\nEnding List:")
print(myList)
