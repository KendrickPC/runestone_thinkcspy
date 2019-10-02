# Give the logical opposites of these conditions.
# You are not allowed to use the not operator.

'''
1. a > b
2. a >= b
3. a >= 18  and  day == 3
4. a >= 18  or  day != 3
'''

a = 3
b = 2
day = 2

original_1 = a < b
logical_opposite_1 = a > b

print("\nOriginal Statement 1:")
print(original_1)
print("Logical Opposite Statement 1:")
print(logical_opposite_1)

original_2 = a >= b
logical_opposite_2 = a <= b

print("\nOriginal Statement 2:")
print(original_2)
print("Logical Opposite Statement 2:")
print(logical_opposite_2)

original_3 = a >= 18 and day == 3
logical_opposite_3 = a <= 18 or day ==3
print("\nOriginal Statement 3:")
print(original_3)
print("Logical Opposite Statement 3:")
print(logical_opposite_3)

original_4 = a >= 18 or day !=3
logical_opposite_4 = a <= 18 and day == 3
print("\nOriginal Statement 4:")
print(original_4)
print("Logical Opposite Statement 4:")
print(logical_opposite_4)