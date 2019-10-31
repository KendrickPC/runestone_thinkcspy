'''
Generalize the problem above so that the parameters to your solution
include the sizes of each jug and the final amount of water to be left
in the larger jug.
'''

from collections import defaultdict

# jug1 and jug2 contain the value for max capacity in respective jugs
# and aim is the amount of water to be measured.
jug1, jug2, aim = 20, 15, 8

# Initialize dictionary with default value as false.
visited = defaultdict(lambda: False)


def waterJugSolver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True

    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)

        visited[(amt1, amt2)] = True

        return (waterJugSolver(0, amt2) or 
                waterJugSolver(amt1, 0) or
                waterJugSolver(jug1, amt2) or
                waterJugSolver(amt1, jug2) or
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
                amt2 - min(amt2, (jug1 - amt1))) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
                amt2 + min(amt1, (jug2 - amt2))))
    
    else:
        return False

print("\nSteps: ")

waterJugSolver(0, 0)