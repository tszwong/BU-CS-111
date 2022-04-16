#
# Problem Set 2 Problem 3
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def len_diff(s1, s2):
    """takes as inputs two string values s1 and s2,
    and returns the difference between their
    lengths as a non-negative number"""

    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2:
        return len_s1 - len_s2
    elif len_s1 < len_s2:
        return len_s2 - len_s1
    elif len_s1 == len_s2:
        return 0


def combine(s1, s2, n):
    """takes as inputs two strings s1 and s2 and an integer n,
    and returns a new string in which the first n characters
    of s1 are followed by the last n characters of s2"""

    combined_string = s1[0:n:1] + s2[(len(s2)-n):len(s2):1]
    if len(s1) < n:
        combined_string = s1 + s2[(len(s2)-n):len(s2):1]
    elif len(s2) < n:
        combined_string = s1[0:n:1] + s2

    return combined_string


def reverse_last(vals, n):
    """takes as inputs a list vals and an integer n,
    and that constructs and returns a new list in which
    the last n values of vals are reversed and all other
    values from vals remain in their original positions"""

    reversed_list = vals[0:(len(vals)-n):1] + vals[len(vals):(len(vals)-n-1):-1]
    if n >= len(vals):
        reversed_list = vals[::-1]

    return reversed_list


def test():
    """test running previous functions"""

    print(f"len_diff('code, 'program'): {len_diff('code', 'program')}")
    print(f"len_diff('begin', 'again'): {len_diff('begin', 'again')}")
    print(f"len_diff('another', 'one'): {len_diff('another', 'one')}")
    print(f"len_diff('one', 'another'): {len_diff('one', 'another')}\n")

    print(f"combine('computer', 'science', 4): {combine('computer', 'science', 4)}")
    print(f"combine('python', 'code', 2): {combine('python', 'code', 2)}")
    print(f"combine('you', 'program', 4): {combine('you', 'program', 4)}")
    print(f"combine('afternoon', 'fun', 5): {combine('afternoon', 'fun', 5)}\n")

    print(f"reverse_last([1, 2, 3, 4, 5, 6], 3): {reverse_last([1, 2, 3, 4, 5, 6], 3)}")
    print(f"reverse_last([1, 2, 3, 4, 5, 6], 4): {reverse_last([1, 2, 3, 4, 5, 6], 4)}")
    print(f"reverse_last([10, 20, 30, 40], 2): {reverse_last([10, 20, 30, 40], 2)}")
    print(f"reverse_last([10, 20, 30, 40], 6): {reverse_last([10, 20, 30, 40], 6)}\n")


# test()
