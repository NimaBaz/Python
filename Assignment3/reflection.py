"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    # Create new image to contain reflection
    reflected_image = SimpleImage.blank(width, height * 2)

    # TODO: your code here.
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            reflected_image.set_pixel(x, y, pixel)
            reflected_image.set_pixel(x, (height * 2) - (y + 1), pixel)
    return reflected_image


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
