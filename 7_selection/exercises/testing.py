def getGrade(grade):
    #your code here
    if grade >= 90:
        return ("A")
    elif grade < 90 and grade >= 80:
        return ("B")
    elif grade < 80 and grade >= 70:
        return ("C")
    elif grade < 70 and grade >= 60:
        return ("D")
    else:
        return ("F")


