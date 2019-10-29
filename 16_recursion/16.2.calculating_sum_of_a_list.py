# 16.1. Calculating the Sum of a List of Numbers.

def listSum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


print(listSum([1, 3, 5, 7, 9]))


def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

