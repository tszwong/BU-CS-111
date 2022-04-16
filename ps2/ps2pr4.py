#
# Problem Set 2 Problem 4
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def total_len(words):
    """takes as input a list of 0 or more strings words and uses recursion
    to compute and return the value obtained by adding together the lengths
    of all of the strings in the list"""

    if words == []:  # base case
        return 0
    else:
        remaining_words = total_len(words[1:])

        return remaining_words + len(words[0])


def exclaim(s):
    """takes an arbitrary string s as input and uses recursion
    to form and return the string formed by adding an exclamation
    point (i.e., the character '!') after each characters in the string"""

    if s == "":
        return ""
    else:
        remaining_letters = exclaim(s[1:])
        new_string = s[0] + "!"

        return new_string + remaining_letters


def test():
    """test running previous functions"""

    print(f"total_len(['hi', 'there']):  {total_len(['hi', 'there'])}")
    print(f"total_len(['recursion', 'is', 'fun']):  {total_len(['recursion', 'is', 'fun'])}")
    print(f"total_len(['bye']):  {total_len(['bye'])}")
    print(f"total_len([]):  {total_len([])}\n")

    print(f"exclaim('hello'):  {exclaim('hello')}")
    print(f"exclaim('wow'):  {exclaim('wow')}")
    print(f"exclaim('o'):  {exclaim('o')}")
    print(f"exclaim(''):  {exclaim('')}\n")

# test()
