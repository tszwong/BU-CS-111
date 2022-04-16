#
# ps4pr2.py (Problem Set 4, Problem 2)
#
# Using your conversion functions
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin


def mul_bin(b1, b2):
    """takes as inputs two strings b1 and b2 that represent binary
    numbers. The function should multiply the numbers and return the
    result in the form of a string that represents a binary number"""

    # converting b1 and b2 to decimal
    b1_dec = bin_to_dec(b1)
    b2_dec = bin_to_dec(b2)

    # product of decimal form b1 and b2
    dec_product = b1_dec * b2_dec

    # convert decimal form product back to binary and return
    bin_product = dec_to_bin(dec_product)
    return bin_product


def largest_bin(binvals):
    """takes a list binvals of 1 or more strings – each of which
    represents a binary number – and that finds and returns the
    string in binvals that represents the largest binary number"""

    list_vals = [(bin_to_dec(i), i) for i in binvals]
    max_pair = max(list_vals)
    return max_pair[1]


def test():
    """testing functions made"""

    # mul_bin()
    print(f"mul_bin('11', '10'):  {mul_bin('11', '10')}")  # 3 * 2 = 6
    print(f"mul_bin('1001', '101'):  {mul_bin('1001', '101')}")  # 9 * 5 = 45

    # largest_bin()
    print(f"largest_bin(['1100', '10011', '101', '10000']):  {largest_bin(['1100', '10011', '101', '10000'])}")  # 10011
    print(f"largest_bin(['0', '10', '10000', '1010']):  {largest_bin(['0', '10', '10000', '1010'])}")  # 10000


test()
