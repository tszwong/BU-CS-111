#
# ps4pr3.py (Problem Set 4, Problem 3)
#
# Functions that process binary numberss
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def count_evens_rec(binvals):
    """takes a list binvals of 0 or more strings – each of which represents
    a binary number – and that uses recursion to compute and return the
    number of the bitstrings in the list that represent an even number"""

    if not binvals:
        return 0
    else:
        rest_count = count_evens_rec(binvals[1:])
        curr_val = binvals[0]
        last_bit = curr_val[-1]
        if last_bit == "0":
            return 1 + rest_count
        else:
            return rest_count


def count_evens_lc(binvals):
    """takes a list binvals of 0 or more strings – each of which represents
    a binary number – and that uses a list comprehension to compute and return
    the number of bitstrings in the list that represent an even number"""

    even_occur = [i for i in binvals if i[-1] == "0"]
    num_times = len(even_occur)
    return num_times


def add_bitwise(b1, b2):
    """adds two binary numbers using recursion to perform
    the bitwise, “elementary-school” addition algorithm,
    and return the result"""

    if not b1:
        return b2
    if not b2:
        return b1
    else:
        rest_add = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == "0" and b2[-1] == "0":
            return rest_add + "0"
        elif b1[-1] == "0" or b2[-1] == "0":
            return rest_add + "1"
        else:
            return add_bitwise(rest_add, "1") + "0"


def test():
    """testing functions made"""

    # count_evens_rec()
    print(f"count_evens_rec(['1100', '10011', '101', '010']):  {count_evens_rec(['1100', '10011', '101', '010'])}")
    print(f"count_evens_rec(['1', '10', '101', '010','1010']):  {count_evens_rec(['1', '10', '101', '010', '1010'])}\n")

    # count_evens_lc()
    print(f"count_evens_lc(['1100', '10011', '101', '010']):  {count_evens_lc(['1100', '10011', '101', '010'])}")
    print(f"count_evens_lc(['1', '10', '101', '010', '1010']):  {count_evens_lc(['1', '10', '101', '010', '1010'])}\n")

    # add_bitwise()
    print(f"add_bitwise('11', '100'):  {add_bitwise('11', '100')}")
    print(f"add_bitwise('11', '1'):  {add_bitwise('11', '1')}")
    print(f"add_bitwise('', '101'):  {add_bitwise('', '101')}")
    print(f"add_bitwise('11100', '11110'):  {add_bitwise('11100', '11110')}")


# test()
