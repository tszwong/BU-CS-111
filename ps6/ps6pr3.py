# PS5 Problem 8
#
# Processing Sequences With Loops
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
# Partner: None

def repeat(s, n):
    """takes a string s and an integer n, and that uses
    a loop to create and return a string in which n copies
    of s have been concatenated together"""

    new_str = ""

    for i in range(n):
        new_str += s

    return new_str


def contains(s, c):
    """takes an arbitrary string s and a single-character c as
    inputs and uses a loop to determine if s contains the character c,
    returning True if it does and False if it does not"""

    for i in s:
        if i == c:
            return True

    return False


def add(vals1, vals2):
    """takes as inputs two lists of numbers, vals1 and vals2, and that uses
    a loop to construct and return a new list in which each element is the sum
    of the elements at the corresponding positions in the original lists"""

    len_vals1 = len(vals1)
    len_vals2 = len(vals2)
    output_lst = []

    if len_vals1 < len_vals2:
        len_diff = len_vals2 - len_vals1
        for i in range(len_diff):
            vals1 = [0] + vals1
    elif len_vals2 < len_vals1:
        len_diff = len_vals1 - len_vals2
        for i in range(len_diff):
            vals2 = [0] + vals2

    for i in range(len_vals1):
        add_sum = vals1[i] + vals2[i]
        output_lst += [add_sum]

    return output_lst


def negate_odds(values):
    """takes a list of integers called values, and that modifies the
    list so that all of its odd-valued elements are replaced with their
    negated values, but all of its even-valued elements are left unchanged"""

    for i in range(len(values)):
        if values[i] % 2 != 0:
            values[i] = -values[i]


def test():
    """tests functions made"""

    # repeat()
    print(f"repeat('da', 2):  {repeat('da', 2)}")
    print(f"repeat('Go BU!', 4):  {repeat('Go BU!', 4)}")
    print(f"repeat('hello', 1):  {repeat('hello', 1)}")
    print(f"repeat('hello', 0):  {repeat('hello', 0)}\n")

    # contains()
    print(f"contains('hello', 'e'):  {contains('hello', 'e')}")
    print(f"contains('hello', 'l'):  {contains('hello', 'l')}")
    print(f"contains('hello', 'x'):  {contains('hello', 'x')}")
    print(f"contains('', 'x'):  {contains('', 'x')}\n")

    # add()
    print(f"add([1, 2, 3], [4, 5, 6]):  {add([1, 2, 3], [4, 5, 6])}")
    print(f"add([5, 3], [6, 4]):  {add([5, 3], [6, 4])}")
    print(f"add([1, 2, 3, 4], [20, 30, 50, 80]):  {add([1, 2, 3, 4], [20, 30, 50, 80])}")
    print(f"add([7, 5, 3], [6]):  {add([7, 5, 3], [6])}")
    print(f"add([7, 5, 3, 6, 2, 1], [6]):  {add([7, 5, 3, 6, 2, 1], [6])}\n")


# test()
#
# vals1 = [1, 2, 3, 4, 5, 6]
# print(vals1)
# print(negate_odds(vals1))
# print(vals1)
# print()
#
# vals2 = [7, -3, 10, 8, -1]
# print(vals2)
# print(negate_odds(vals2))
# print(vals2)
