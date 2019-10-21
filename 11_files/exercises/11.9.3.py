'''
Using the text file studentdata.txt (shown in exercise 1) write a
program that calculates the minimum and maximum score for each
student. Print out their name as well.
'''

def min_and_max():
    f = open('studentdata.txt', 'r')

    for i in f:
        items = i.split()
        # print(items[1:])
        minimum = float(min(items[1:]))
        maximum = float(max(items[1:]))
        print("Name: %s, Min: %.2f, Max: %.2f" % (items[0], minimum, maximum))

min_and_max()
