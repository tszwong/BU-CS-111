#
# ps3pr4.py (Problem Set 3, Problem 4)
#
# Caesar cipher / decipher
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

import random


def first_occur(elem, seq):
    """takes as inputs an element elem and a sequence seq,
    and that uses recursion (i.e., that calls itself recursively)
    to find and return the index of the first occurrence of elem in seq"""

    not_in = -1

    if len(seq) == 0:
        return not_in
    if seq[0] == elem:
        return 0
    else:
        rest_seq = first_occur(elem, seq[1:])
        if rest_seq == not_in:
            return rest_seq
        else:
            return 1 + rest_seq


def rem_first(c, s):
    """takes as inputs a single character c and an
    arbitrary string s and that uses recursion to create
    and return a version of s in which only the first
    occurrence of c (if any) has been removed"""

    if s == "":
        return ""
    else:
        rest_s = rem_first(c, s[1:])
        if first_occur(c, s) != -1:
            index = first_occur(c, s)
            string_rest = s[0:index] + s[index + 1:len(s)]
            return string_rest
        else:
            rest_s = rem_first(c, s[1:])
            return s[0] + rest_s


def jscore(s1, s2):
    """takes two strings s1 and s2 as inputs and that uses
    recursion to compute and return the Jotto score of s1 compared with s2"""

    if not s1 or not s2:
        return 0
    else:
        jscore_rest = jscore(s1[1:], s2)
        if s1[0] in s2:
            current_score = rem_first(s1[0], s2)
            jscore_rest = jscore(s1[1:], current_score)
            return 1 + jscore_rest
        else:
            return jscore_rest


def negate_last(n, values):
    """takes as inputs an integer n and an arbitrary list
    of integers values and that uses recursion to create and
    return a version of values in which only the last
    occurrence of n (if any) has been negated"""

    if not values:      # base case 1
        return []
    if n not in values: # base case 2
        return values
    if n == values[-1]: # base case 3
        values[-1] = -n
        return values
    else:   # recursive case
        rest_values = negate_last(n, values[0:len(values)-1])
        return rest_values + [values[-1]]


def test():
    """testing functions made"""

    #  first_occur()
    print(f"first_occur(5, [4, 10, 5, 3, 7, 5]):  {first_occur(5, [4, 10, 5, 3, 7, 5])}")
    print(f"first_occur('hi', ['well', 'hi', 'there']):  {first_occur('hi', ['well', 'hi', 'there'])}")
    print(f"first_occur('b', 'banana'):  {first_occur('b', 'banana')}")
    print(f"first_occur('a', 'banana'):  {first_occur('a', 'banana')}")
    print(f"first_occur('i', 'team'):  {first_occur('i', 'team')}")
    print(f"first_occur('hi', ['hello', 111, True]):  {first_occur('hi', ['hello', 111, True])}")
    print(f"first_occur('a', ''):  {first_occur('a', '')}")
    print(f"first_occur(42, []):  {first_occur(42, [])}\n")

    # rem_first()
    print(f"rem_first('a', 'bananas'):  {rem_first('a', 'bananas')}")
    print(f"rem_first('n', 'bananas'):  {rem_first('n', 'bananas')}")
    print(f"rem_first('x', 'bananas'):  {rem_first('x', 'bananas')}")
    print(f"rem_first('a', ''):  {rem_first('a', '')}\n")

    # jscore()
    print(f"jscore('diner', 'syrup'):  {jscore('diner', 'syrup')}")
    print(f"jscore('always', 'bananas'):  {jscore('always', 'bananas')}")
    print(f"jscore('always', 'walking'):  {jscore('always', 'walking')}")
    print(f"jscore('recursion', 'excursion'):  {jscore('recurison', 'excursion')}")
    print(f"jscore('recursion', ''):  {jscore('recurison', '')}")
    print(f"jscore('', 'recursion'):  {jscore('', 'recursion')}\n")

    # negate_last(), tests provided in pset
    print(f"negate_last(3, [2, 3, 1, 2, 3, 4]):  {negate_last(3, [2, 3, 1, 2, 3, 4])}")
    print(f"negate_last(2, [2, 3, 1, 2, 3, 4]):  {negate_last(2, [2, 3, 1, 2, 3, 4])}")
    print(f"negate_last(5, [2, 5, 3, 1, 2, 3, 4, 5, 5, 6, 7]):  {negate_last(5, [2, 5, 3, 1, 2, 3, 4, 5, 5, 6, 7])}")
    print(f"negate_last(7, [9, 5, 7, 7, 7]):  {negate_last(7, [9, 5, 7, 7, 7])}")
    print(f"negate_last(2, [1, 3, 5, 7, 9]):  {negate_last(2, [1, 3, 5, 7, 9])}")
    print(f"negate_last(2, []):  {negate_last(2, [])}\n\n")

    # negate_last(), test with random combinations
    random_new_list = []
    for x in range(0, 10):
        random_num = random.randint(0, 10)
        random_new_list.append(random_num)

    random_n = random.randint(0, 10)

    print(f"new_list: {random_new_list}, random: {random_n} ")
    print(f"negate_last({random_n}, {random_new_list}):  {negate_last(random_n, random_new_list)}")


test()
