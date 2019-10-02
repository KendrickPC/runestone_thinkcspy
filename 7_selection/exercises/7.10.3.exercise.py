'''
# 7.10.3 Write a function which is given an exam mark, and it
returns a string — the grade for that mark — according to
this scheme:

Mark:           Grade:

>= 90           A
[80-90)         B
[70-80)         C
[60-70)         D
<60             F


The square and round brackets denote closed and open intervals.
A closed interval includes the number, and open interval excludes it.
So 79.99999 gets grade C , but 80 gets grade B.

Test your function by printing the mark and the grade for a number of
different marks.
'''


import unittest

def examLetterGrades(mark):
    if mark >= 90:
        return ("A")
    elif mark < 90 and mark >= 80:
        return ("B")
    elif mark < 80 and mark >= 70:
        return ("C")
    elif mark < 70 and mark >= 60:
        return ("D")
    else:
        return ("F")


class TestingExamLetterGrades(unittest.TestCase):
    def test_examLetterGrades(self):
        self.assertTrue(examLetterGrades(90), ("A"))
        self.assertTrue(examLetterGrades(80), ("B"))
        self.assertTrue(examLetterGrades(70), ("C"))
        self.assertTrue(examLetterGrades(60), ("D"))
        self.assertTrue(examLetterGrades(59), ("E"))

if __name__ == '__main__':
    unittest.main()
