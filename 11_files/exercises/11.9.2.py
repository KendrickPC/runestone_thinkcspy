'''
Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for each student, and print out the student’s name along with their average grade.
'''

def average_test_scores():
    f = open("studentdata.txt", "r")

    for i in f:
        line = i.split()
        # print(line)
        total_test_scores = sum(float(i) for i in line[1:])
        tests_taken = len(line)
        average = total_test_scores / tests_taken
        # print(total_test_scores / tests_taken)
        print("Name: %s, Avg: %.2f" % (line[0], average))

    f.close()

average_test_scores()
