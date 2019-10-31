#6.Implement a solution to the Tower of Hanoi using three stacks to
# keep track of the disks.

# Reference:
# https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/

# Recursive Python function to solve tower of hanoi 

def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod,", from_rod, "to rod", to_rod)
        return
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

print("\n1 Disk:")
towerOfHanoi(1, 'A', 'C', 'B')
print("\n2 Disks:")
towerOfHanoi(2, 'A', 'C', 'B')
print("\n3 Disks:")
towerOfHanoi(3, 'A', 'C', 'B')
print("\n4 Disks:")
towerOfHanoi(4, 'A', 'C', 'B')
print("\n5 Disks:")
towerOfHanoi(5, 'A', 'C', 'B')