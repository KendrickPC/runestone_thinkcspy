# Write a function to convert the image to grayscale.

'''
For example, you can create a gray scale pixel by averaging the red, green and blue intensities and then using that value for all intensities.
'''


import cImage as image


img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        newred = 174
        newgreen = 174
        newblue = 174

        newpixel = image.Pixel(newred, newgreen, newblue)

        newimg.setPixel(col, row, newpixel)


# print(p.getRed(), p.getGreen(), p.getBlue())
# <<< (194, 173, 156)
# print("\nThe average values for grayscale")
# print((194+173+156)/3)
# <<< 174
newimg.draw(win)
win.exitonclick()



