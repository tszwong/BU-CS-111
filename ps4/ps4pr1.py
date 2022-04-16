#
# ps4pr1.py (Problem Set 4, Problem 1)
#
# From binary to decimal and back!
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def dec_to_bin(n):
    """takes a non-negative integer n and uses recursion to
    convert it from decimal to binary – constructing and returning
    a string version of the binary representation of that number"""

    if n == 0:
        return "0"
    if n == 1:
        return "1"
    else:
        rest_dec_to_bin = dec_to_bin(n >> 1)
        if n % 2 != 0:
            return rest_dec_to_bin + "1"
        else:
            return rest_dec_to_bin + "0"


def bin_to_dec(b):
    """takes a string b that represents a binary number and
    uses recursion to convert the number from binary to decimal,
    returning the resulting integer"""

    if b == "0":
        return 0
    if b == "1":
        return 1
    else:
        rest_binary = bin_to_dec(b[:-1])
        if b[-1] == "0":
            return 2 * rest_binary + 0
        else:
            return 2 * rest_binary + 1


def test():
    """testing functions made"""

    # dec_to_bin()
    print(f"dec_to_bin(5):  {dec_to_bin(5)}")
    print(f"dec_to_bin(12):  {dec_to_bin(12)}")
    print(f"dec_to_bin(0):  {dec_to_bin(0)}")
    print(f"dec_to_bin(3):  {dec_to_bin(3)}")
    print(f"dec_to_bin(1):  {dec_to_bin(1)}\n")

    #bin_to_dec()
    print(f"bin_to_dec('101'):  {bin_to_dec('101')}")
    print(f"bin_to_dec('1100'):  {bin_to_dec('1100')}")
    print(f"bin_to_dec('0'):  {bin_to_dec('0')}")
    print(f"bin_to_dec('1'):  {bin_to_dec('1')}")
    print(f"bin_to_dec('10'):  {bin_to_dec('10')}")
    print(f"bin_to_dec('111101'):  {bin_to_dec('111101')}")


# test()
