# ps7pr2.py - Problem Set 7, Problem 2
#
# Our Rectangle class revisited
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#
# Partner Name: N/A

import math


class Rectangle:
    def __init__(self, init_width, init_height, init_unit):
        """ constructor for a Rectangle object with the specified dimensions 
            init_width and init_height, and initial x and y coordinates of 0
        """
        self.x = 0
        self.y = 0
        self.width = init_width
        self.height = init_height
        self.unit = init_unit


    def grow(self, dwidth, dheight):
        """ modifies the dimensions of the called Rectangle object
            (the one given by self) by adding dwidth to the current width
            and dheight to the current height.
            Note that nothing needs to be returned. The changes are
            made to the internals of the called object, and thus they 
            will still be there after the method returns!
        """
        self.width += dwidth
        self.height += dheight


    def area(self):
        """ computes and returns the area of the called Rectangle object
        """
        return self.width * self.height


    def perimeter(self):
        """ computes and returns the perimeter of the called Rectangle object
        """
        return 2 * self.width + 2 * self.height


    def scale(self, factor):
        """ modifies the dimensions of the called Rectangle object
            by multiplying them by the specified factor.
        """
        self.width *= factor
        self.height *= factor


    def diagonal(self):
        """akes no inputs and computes and returns the length
        of the called Rectangle object’s diagonal"""

        add_part = self.width**2 + self.height**2
        sqrt_add = math.sqrt(add_part)

        return sqrt_add


    def larger_than(self, other):
        """takes another Rectangle other as a parameter and that returns True if
        the called Rectangle object (the object given by self) has a larger area
        than the area of the Rectangle passed in for other, and False otherwise"""

        area_self = self.area()
        area_other = other.area()

        if area_self > area_other:
            return False
        elif self.unit == other.unit:
            return False
        else:
            return True


    def __eq__(self, other):
        """ determines if the called Rectangle object (self) is 
            equivalent to the Rectangle object given by other
            note: the \ symbol at the end of the first line below 
            allows us to continue that line onto the next line of the file.
        """
        if self.width == other.width and self.height == other.height \
                and self.unit == other.unit:
            return True
        else:
            return False


    def __repr__(self):
        """ creates and returns a string representation of the 
            called Rectangle object
        """
        return str(self.width) + ' x ' + str(self.height) + " " + str(self.unit)
