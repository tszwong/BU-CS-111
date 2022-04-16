# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name: n/a
# partner's email: n/a
#

# function 0
def opposite(x):
    """ returns the opposite of its input,
        input x: any number (int or float)
    """
    return -1 * x


# put your definitions for the remaining functions below
def cube(x):
    """takes a number x as its input and
     returns the cube of its input"""

    x = x ** 3
    return x


def convert_to_inches(yards, feet):
    """takes two numeric inputs yards and feet that together
    represent a single length broken up into yards and feet,
    and that returns the corresponding length in inches"""

    yards_to_inches = yards * 36
    feet_to_inches = feet * 12

    if yards < 0:
        yards_to_inches = 0
    elif feet < 0:
        feet_to_inches = 0

    return yards_to_inches + feet_to_inches


def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """returns the area of the rectangle in
     square inches based on the height and width"""

    height = convert_to_inches(height_yds, height_ft)
    width = convert_to_inches(width_yds, width_ft)

    area = height * width
    return area


def median(a, b, c):
    """takes three numeric inputs a, b, and c,
    and that returns the median of the three inputs"""

    median_num = [0, 0, 0]

    if a <= b and a <= c:
        median_num[0] = a
        if b <= c:
            median_num[1] = b
            median_num[2] = c
        else:
            median_num[1] = c
            median_num[2] = b
    elif a >= b and a >= c:
        median_num[2] = a
        if b <= c:
            median_num[0] = b
            median_num[1] = c
        else:
            median_num[0] = c
            median_num[1] = b
    elif b <= a <= c:
        median_num[0] = b
        median_num[1] = a
        median_num[2] = c
    else:
        median_num[0] = a
        median_num[1] = b
        median_num[2] = c

    return median_num[1]


# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
    print(f"cube(x) tests: \n2: {cube(2)} \n-5: {cube(-5)}\n")
    print(f"convert_to_inches(yards, feet) tests: \n{convert_to_inches(4, 2)} \n{convert_to_inches(1, 1)} \n"
          f"{convert_to_inches(-4, 2)} \n{convert_to_inches(3, -5)}\n")
    print(f"area_sq_inches(height_yds, height_ft, width_yds, width_ft) tests: \n{area_sq_inches(1, 2, 3, 1)} "
          f"\n{area_sq_inches(2, 0, 1, 2)}\n")
    print(f"median(a, b, c) tests: \n10,2,7: {median(10, 2, 7)} \n7,2,10: {median(7, 2, 10)}"
          f" \n8,6,4: {median(8, 6, 4)} \n10,2,2: {median(10, 2, 2)}\n")
