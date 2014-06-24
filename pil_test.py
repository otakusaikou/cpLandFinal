# This program shows how to resize an image and save the result to
# a file of different format, for example, from 'PNG' to 'JPG'.

from PIL import Image

img = Image.open('baboon.png')

# find the image size
width, height = img.size

# display the image
img.show()

# change the size of image, and store the result as a new image
new_size = 200, 180
new_img = img.resize(new_size)

# save the new image in a different format
new_img.save('new_200x180.jpg')

# rotate the image 90 degrees (counter clockwise)
rot_90 = new_img.rotate(90)
rot_90.save('new_rot_90.tif')
rot_90.show()
