#
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part II
#
# Your name: Tsz Kit Wong
# Your email: wongt@bu.edu
#

def mirror(s):
    """takes a string s as input and returns a mirrored
    version of s that is twice the length of the original string"""

    reversed_string = s[::-1]
    return s + reversed_string


def ends_match(s):
    """takes a string input s and returns True if the first character
     in s matches the last character in s, and False otherwise"""

    if s[0] == s[-1]:
        return True
    else:
        return False


def replace_end(values, new_end_vals):
    """takes as inputs a list values and another list new_end_vals,
    and returns a new list in which the elements in new_end_vals
    have replaced the last n elements of the list values"""

    new_end_index = (len(values) - len(new_end_vals))
    new_list = values[0:new_end_index:1] + new_end_vals

    if new_end_index <= 0:
        return new_end_vals

    return new_list


def repeat_elem(values, index, num_times):
    """takes as inputs a list values, an integer index, and a positive integer
    num_times, and returns a new list in which the element of values at position
     index has been repeated num_times times."""

    repeat_values = [values[index]]*(num_times-1)
    new_list = []

    if index == 0:
        new_list += repeat_values
        new_list += values[1::1]
    else:
        new_list += values[0:index:1]
        new_list += repeat_values
        new_list += values[index::1]

    return new_list


# test
def test():
    """run tests for functions created
    """
    print(f"mirror(s): \n{mirror('hello')} \n{mirror('bacon')} \n{mirror('XYZ')}\n")
    print(f"ends_match(s): \n'no match':{ends_match('no match')} \n'hah! a match': {ends_match('hah! a match')}"
          f" \n'q': {ends_match('q')}\n")
    print(f"replace_end(values, new_end_vals): \n1,2,3,4,5 and 7,8,9: {replace_end([1, 2, 3, 4, 5], [7, 8, 9])}"
          f" \n1,2,3,4,5 and 10,11: {replace_end([1, 2, 3, 4, 5], [10, 11])} \n1,2,3,4,5 and 12: "
          f"{replace_end([1, 2, 3, 4, 5], [12])}\n")
    print(f"0,2,4,6 and 4,3,2,1: {replace_end([0, 2, 4, 6], [4, 3, 2, 1])}"
          f" \n0,2,4,6 and 4,3,2,1,0: {replace_end([0, 2, 4, 6], [4, 3, 2, 1, 0])}\n")
    print(f"repeat_elem(values, index, num_times): \n[10, 11, 12, 13], 2, 4: {repeat_elem([10, 11, 12, 13], 2, 4)}"
          f" \n[10, 11, 12, 13], 2, 6: {repeat_elem([10, 11, 12, 13], 2, 6)} \n[5, 6, 7], 1, 3: {repeat_elem([5, 6, 7], 1, 3)}")
