# Print out a neatly formatted multiplication table, up to 12 x 12.

# Research Reference:
# https://stackoverflow.com/questions/20415384/properly-formatted-multiplication-table


def multiplcationTable():
    for x in range(1, 13):
        for y in range(1, 13):
            z = x * y
            print(z, end="\t")
        print() #creates the space after the loop


multiplcationTable()
