# 10.17 Lists and Loops
'''

'''

fruits = ["apple", "orange", "banana", "cherry"]
for afruit in fruits:     # by item
    print(afruit)

'''
In this example, each time through the loop, the variable position
is used as an index into the list, printing the position-eth element.
Note that we used len as the upper bound on the range so that we can
iterate correctly no matter how many items are in the list.
'''

print("\nNew Example:")
fruits = ["apple", "orange", "banana", "cherry"]

for position in range(len(fruits)):     # by index
    print(fruits[position])


'''
Any sequence expression can be used in a for loop. For example,
the range function returns a sequence of integers.

This example prints all the multiples of 3 between 0 and 19.
'''

print("\nNew Example:")
for number in range(20):
    if number % 3 == 0:
        print(number)


'''

'''

print("\nNew Example:")
numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)
