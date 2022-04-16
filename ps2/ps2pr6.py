#
# PS2 Part 2 Problem 6
# Fun with recursion Part 3
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def letter_score(letter):
    """takes a lowercase letter as input and returns
    the value of that letter as a scrabble tile.
    If letter is not a lowercase letter from ‘a’
    to ‘z’, the function should return 0"""

    assert (len(letter) == 1)

    # possible scores
    one = ["a", "e", "i", "l", "n", "o", "r", "s", "t", "u"]
    two = ["d", "g"]
    three = ["b", "c", "m", "p"]
    four = ["f", "h", "v", "w", "y"]
    five = ["k"]
    eight = ["j", "x"]
    ten = ["q", "z"]

    if letter in one:
        return 1
    elif letter in two:
        return 2
    elif letter in three:
        return 3
    elif letter in four:
        return 4
    elif letter in five:
        return 5
    elif letter in eight:
        return 8
    elif letter in ten:
        return 10
    else:
        return 0


def scrabble_score(word):
    """takes as input a string word containing
    only lowercase letters, and that uses recursion
    to compute and return the scrabble score of that string"""

    if word == "":
        return 0
    else:
        rest_word = scrabble_score(word[1:])
        scrabble = letter_score(word[0])
        return scrabble + rest_word


def smaller_of(vals1, vals2):
    """takes as inputs two lists vals1 and vals2
    and uses recursion to construct and return a
    new list in which each element is the the smaller
    of the corresponding elements from the original lists"""

    if not vals1 or not vals2:
        return []
    else:
        rest_vals = smaller_of(vals1[1:], vals2[1:])
        if vals1[0] < vals2[0]:
            insert = [vals1[0]]
            return insert + rest_vals
        else:
            insert = [vals2[0]]
            return insert + rest_vals


def merge(s1, s2):
    """takes as inputs two strings s1 and s2
    and uses recursion to determine and return
    a new string that is formed by “merging” together
    the characters in the strings s1 and s2 to create a single string"""

    new_string = ""  # string returned by function

    if s1 == "" or s2 == "":  # base cases

        if len(s1) < len(s2):  # adds remaining letters of longer string to new_string
            remaining_letters = s2[len(s1):(len(s2)-len(s1)):1]
            return new_string + remaining_letters

        if len(s1) > len(s2):  # adds remaining letters of longer string to new_string
            remaining_letters = s1[len(s2):(len(s1)-len(s2)):1]
            return new_string + remaining_letters

        return new_string

    else:
        rest_s = merge(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            new_string += s1[0]
            return new_string + rest_s

        elif s1[0] != s2[0]:  # adds both letters one after another
            new_string += s1[0]
            new_string += s2[0]
            return new_string + rest_s


def test():
    """test running previous functions"""

    # letter_score()
    print(f"letter_score('a'):  {letter_score('a')}")
    print(f"letter_score('q'):  {letter_score('q')}")
    print(f"letter_score('%'):  {letter_score('%')}")
    print(f"letter_score('A'):  {letter_score('A')}\n")

    # scrabble_score()
    print(f"scrabble_score('python'):  {scrabble_score('python')}")
    print(f"scrabble_score('a'):  {scrabble_score('a')}")
    print(f"scrabble_score('quetzal'):  {scrabble_score('quetzal')}\n")

    # smaller_of()
    print(f"smaller_of([3, 4, 9, 5], [7, 2, 0, 5]):  {smaller_of([3, 4, 9, 5], [7, 2, 0, 5])}")
    print(f"smaller_of([5, 7, 2], [1, 9, 15]):  {smaller_of([5, 7, 2], [1, 9, 15])}")
    print(f"smaller_of([], []):  {smaller_of([], [])}")
    print(f"smaller_of([0, 3, 6, 9], [1, 1]):  {smaller_of([0, 3, 6, 9], [1, 1])}")
    print(f"smaller_of([3, 1, 0], [2, 4, 5, 6]):  {smaller_of([3, 1, 0], [2, 4, 5, 6])}")
    print(f"smaller_of([1, 2], []):  {smaller_of([1, 2], [])}")
    print(f"smaller_of([], [3, 4, 5]):  {smaller_of([], [3, 4, 5])}\n")

    # merge()
    print(f"merge('abcde', 'abghe'):  {merge('abcde', 'abghe')}")
    print(f"merge('string', 'sprung'):  {merge('string', 'sprung')}")
    print(f"merge('same', 'same'):  {merge('same', 'same')}")
    print(f"merge('abc', 'efg'):  {merge('abc', 'efg')}")
    print(f"merge('', ''):  {merge('', '')}\n")

    # merger() part II
    print(f"merge('loudest', 'song'):  {merge('loudest', 'song')}")
    print(f"merge('abc', 'aaadd'):  {merge('abc', 'aaadd')}")
    print(f"merge('abc', ''):  {merge('abc', '')}")
    print(f"merge('', 'de'):  {merge('', 'de')}\n")


test()
