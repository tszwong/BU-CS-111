#
# Problem Set 2 Part 2 Problem 5
# Fun with recursion
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def add(vals1, vals2):
    """takes as inputs two lists of numbers, vals1 and vals2,
    and that uses recursion to construct and return a new list
    in which each element is the sum of the elements at the
    corresponding positions in the original lists"""

    if len(vals1) == 0 or len(vals2) == 0 or len(vals1) != len(vals2):
        return []
    else:
        add_rest = add(vals1[1:], vals2[1:])
        add_sum = [vals1[0] + vals2[0]]

        return add_sum + add_rest


def contains(s, c):
    """takes an arbitrary string s and a single-character c as inputs
    and uses recursion to determine if s contains the character c,
    returning True if it does and False if it does not"""

    if s == "":
        return False
    if s[0] == c:
        return True
    else:
        rest_string = contains(s[1:], c)
        return rest_string


def process(vals):
    """takes as input a list of 0 or more integers vals
    and uses recursion to create and return a new list in
    which each even element of the original list has been
    tripled and each odd element has been left unchanged"""

    if vals == []:
        return []
    else:
        vals_rest = process(vals[1:])
        if vals[0] % 2 == 0:
            tripled_value = [vals[0] * 3]
            return tripled_value + vals_rest
        else:
            return [vals[0]] + vals_rest


def test():
    """test running previous functions"""

    # add()
    print(f"add([1, 2, 3], [4, 5, 6]):  {add([1, 2, 3], [4, 5, 6])}")
    print(f"add([5, 3], [6, 4]):  {add([5, 3], [6, 4])}")
    print(f"add([1, 2, 3, 4], [20, 30, 50, 80]):  {add([1, 2, 3, 4], [20, 30, 50, 80])}")
    print(f"add([5, 3], [6]):  {add([5, 3], [6])}\n")

    # contains()
    print(f"contains('hello', 'e'):  {contains('hello', 'e')}")
    print(f"contains('hello', 'l'):  {contains('hello', 'l')}")
    print(f"contains('hello', 'x'):  {contains('hello', 'x')}")
    print(f"contains('', 'x'):  {contains('', 'x')}\n")

    # process()
    print(f"process([5, 4, 3, 2]):  {process([5, 4, 3, 2])}")
    print(f"process([6, 3, 10]):  {process([6, 3, 10])}")
    print(f"process([]):  {process([])}\n")


test()
