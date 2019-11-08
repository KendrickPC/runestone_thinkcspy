'''
In games, we often put a rectangular “bounding box” around our
sprites in the game. We can then do collision detection between,
say, bombs and spaceships, by comparing whether their rectangles
overlap anywhere.

Write a function to determine whether two rectangles collide.
Hint: this might be quite a tough exercise! Think carefully about
all the cases before you code.
'''

# Reference:
# https://stackoverflow.com/questions/40795709/checking-whether-two-rectangles-overlap-in-python-using-two-bottom-left-corners

from collections import namedtuple

RECT_NAMEDTUPLE = namedtuple('RECT_NAMEDTUPLE', 'x1 x2 y1 y2')

Rect1 = RECT_NAMEDTUPLE(10,100,40,80)
Rect2 = RECT_NAMEDTUPLE(20,210,10,60)

def overlap(rec1, rec2):
    if (Rect2.x2 > Rect1.x1 and Rect2.x2 < Rect1.x2) or \
       (Rect2.x1 > Rect1.x1 and Rect2.x1 < Rect1.x2):
        x_match = True
    else:
        x_match = False
    if (Rect2.y2 > Rect1.y1 and Rect2.y2 < Rect1.y2) or \
       (Rect2.y1 > Rect1.y1 and Rect2.y1 < Rect1.y2):
        y_match = True
    else:
        y_match = False
    if x_match and y_match:
        return True
    else:
        return False

print ("Overlap found?", overlap(Rect1, Rect2))
