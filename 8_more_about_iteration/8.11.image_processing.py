# 8.11 Image Processing
'''
Note:
One important caveat about using cImage.py is that it will only work with GIF
files unless you also install the Python Image Library. Don’t worry if you
pip install cImage it will automatically take care of this for you. Otherwise,
the easiest version to install is called Pillow. If you have the pip command
installed on your computer this is really easy to install, with pip install
pillow otherwise you will need to follow the instructions on the Python Package
Index page. With Pillow installed you will be able to use almost any kind of
image that you download.
'''

# import cImage as image
# img = image.Image("myfile.gif")

import cImage as image

p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())


'''
iter-9-1: If you have a pixel whose RGB value is (50, 0, 0), what color
will this pixel appear to be?
Answer: Dark Red

✔️ Because all three values are close to 0, the color will be dark.
But because the red value is higher than the other two, the color will appear red.
'''

