# 8.14.2.py
'''
Write a function print_triangular_numbers(n) that prints out the
first n triangular numbers. A call to print_triangular_numbers(5)
would produce the following output:

(hint: use a web search to find out what a triangular number is.)
# http://mathworld.wolfram.com/TriangularNumber.html
# Answer: n(n+1)/2
'''

def print_rectangular_functions(n):
    for i in range(1, n+1):
        print(i, i * (i + 1) // 2)

print_rectangular_functions(5)
