'''
The following sample file called studentdata.txt contains one line
for each student in an imaginary class. The student’s name is the
first thing on each line, followed by some exam scores.
The number of scores might be different for each student.

Using the text file studentdata.txt write a program that prints out
the names of students that have more than six quiz scores.

'''

# [7:]

f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])

f.close()

