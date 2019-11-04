'''
Write a program that prints out Pascal’s triangle.
Your program should accept a parameter that tells how many
rows of the triangle to print.
'''


def pascal(n):
    if n == 0:
        return [1]
    else:
        N = pascal(n - 1)
        return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]


def pascal_triangle(n):
    for i in range(n):
        print(pascal(i))


print("\nPascal's Triangle Testing n = 3")
pascal_triangle(3)

print("\nPascal's Triangle Testing n = 4")
pascal_triangle(4)

print("\nPascal's Triangle Testing n = 5")
pascal_triangle(5)

print("\nPascal's Triangle Testing n = 6")
pascal_triangle(6)

print("\nPascal's Triangle Testing n = 7")
pascal_triangle(7)
