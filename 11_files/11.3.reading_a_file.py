# 11.3 Reading a File
'''
As an example, suppose we have a text file called qbdata.txt that contains 
the following data representing statistics about NFL quarterbacks. Although
it would be possible to consider entering this data by hand each time it
is used, you can imagine that it would be time-consuming and error-prone
to do this. In addition, it is likely that there could be data from more
quarterbacks and other years. The format of the data file is as follows:

First Name, Last Name, Position, Team, Completions, Attempts, Yards, TDs, Ints, Comp%, Rating

To open this file, we would call the open function. The variable,
fileref, now holds a reference to the file object returned by open.
When we are finished with the file, we can close it by using the close
method. After the file is closed any further attempts to use fileref will
result in an error.

    >>>fileref = open("qbdata.txt", "r")
    >>>
    >>>fileref.close()
    >>>

'''

fileref = open("qbdata.txt", "r")
# The code below erases the data in my files..
# fileref = open("qbdata.txt", "w")
# filevariable.close()
fileref.close()
