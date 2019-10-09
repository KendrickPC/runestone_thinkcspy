'''
Write a general pixel mapper function that will take an image and
a pixel mapping function as parameters. The pixel mapping
function should perform a manipulation on a single pixel and
return a new pixel.
'''

import cImage as image


def pixelMapper(oldimage, rbgFunction):
    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = image.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            originalpixel = oldimage.getPixel(col, row)
            newpixel = rbgFunction(originalpixel)
            newim.setPixel(col, row, newpixel)

    return newim


def grayPixel(oldpixel):
    intensitysum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    aveRGB = intensitysum // 3
    newPixel = image.Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel


win = image.ImageWin()
img = image.Image("elmo.gif")

newim = pixelMapper(img, grayPixel)
newim.draw(win)

win.exitonclick()
