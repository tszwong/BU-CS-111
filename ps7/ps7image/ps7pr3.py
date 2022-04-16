# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# Name: Tsz Kit Wong
# Email: wongt@bu.edu

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images


def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels


def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21 * red + 72 * green + 7 * blue) // 100

## put your functions below
def grayscale(pixels):
    """takes the 2-D list pixels containing pixels for an image,
    and that creates and returns a new 2-D list of pixels for an image
    that is a grayscale version of the original image"""

    height = len(pixels)
    width = len(pixels[0])

    new_pixels = create_green_image(height, width)

    for x in range(height):
        for y in range(width):
            pixel = pixels[x][y]
            brightness_pixels = brightness(pixels[x][y])
            pixel[0] = brightness_pixels
            pixel[1] = brightness_pixels
            pixel[2] = brightness_pixels

            new_pixels[x][y] = [pixel[0], pixel[1], pixel[2]]

    return new_pixels


def mirror_vert(pixels):
    """takes the 2-D list pixels containing pixels for an image,
    and that creates and returns a new 2-D list of pixels for an
    image in which the original image is “mirrored” vertically"""

    height = len(pixels)
    width = len(pixels[0])

    new_pixels = create_green_image(height, width)

    for x in range(height//2):
        for y in range(width):
            new_pixels[x][y] = pixels[x][y]
            new_pixels[height-1-x][y] = pixels[x][y]

    return new_pixels


def flip_horiz(pixels):
    """takes the 2-D list pixels containing pixels for an image, and that creates and returns a
    new 2-D list of pixels for an image in which the original image is “flipped” horizontally"""

    height = len(pixels)
    width = len(pixels[0])

    new_pixels = create_green_image(height,width)

    for x in range(height):
        for y in range(width):
            new_pixels[x][width-1-y] = pixels[x][y]

    return new_pixels


def extract(pixels, rmin, rmax, cmin, cmax):
    """takes the 2-D list pixels containing pixels for an image, and
    that creates and returns a new 2-D list that represents the portion
    of the original image that is specified by the other four parameters"""

    height = rmax - rmin
    width = cmax - cmin

    new_pixels = create_green_image(height,width)

    for x in range(height):
        for y in range(width):
            new_pixels[x][y] = pixels[rmin+x][cmin+y]

    return new_pixels
