'''
Find or invent an algorithm for drawing a fractal mountain.
Hint: One approach to this uses triangles again.
'''
# Reference
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

def koch_0(t, size):
    t.forward(size)

def koch_1(t, size):
    for angle in [60, -120, 60, 0]:
       koch_0(t, size/3)
       t.left(angle)

def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
       koch_1(t, size/3)
       t.left(angle)

def koch_3(t, size):
    for angle in [60, -120, 60, 0]:
       koch_2(t, size/3)
       t.left(angle)
