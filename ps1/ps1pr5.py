#
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#
# Your name: Tsz Kit Wong
# Your email: wongt@bu.edu
#

def first_and_last(values):
    """ returns the first and last value of values in a list """

    first = values[0]
    last = values[-1]

    return [first, last]


def longer_len(s1, s2):
    """takes two string values for inputs s1 and s2,
    and that returns the length of the longer string"""

    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2:
        return len_s1
    else:
        return len_s2


def move_to_end(s, n):
    """takes a string value s and an integer n as inputs
    , and that returns a new string in which the first n characters of
    s have been moved to the end of the string"""

    new_string = s[n::1] + s[0:n:1]
    if n > len(s):
        return s

    return new_string


# tests
def test():
    """run tests for functions created
    """
    print(f"first_and_last(values):\n[1,2,3,4]: {first_and_last([1, 2, 3, 4])}\n")
    print(f"longer_len(s1, s2): \n'computer','compute': {longer_len('computer', 'compute')}\n")
    print(f"move_to_end(s, n): \n'computer',3: {move_to_end('computer', 3)} \n'computer',3: {move_to_end('computer', 5)}"
          f" \n'hi',5: {move_to_end('hi', 5)}")
