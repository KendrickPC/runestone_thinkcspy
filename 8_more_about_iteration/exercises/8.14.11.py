'''
Write a function to uniformly enlarge an image by a factor of 2 (double the size).
'''

import cImage as image

img = image.Image("elmo.gif")
win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)


def double(oldImage):
    oldWidth = oldImage.getWidth()
    oldHeight = oldImage.getHeight()

    newImage = image.EmptyImage(oldWidth*2, oldHeight*2)
    for row in range(oldHeight):
        for col in range(oldWidth):
            oldPixel = oldImage.getPixel(col, row)

            newImage.setPixel(2*col, 2*row, oldPixel)
            newImage.setPixel(2*col+1, 2*row, oldPixel)
            newImage.setPixel(2*col, 2*row+1, oldPixel)
            newImage.setPixel(2*col+1, 2*row+1, oldPixel)

    return newImage

bigImg = double(img)
bigImg.draw(win)

win.exitonclick()
