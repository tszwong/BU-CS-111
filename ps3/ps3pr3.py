#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
# Name: Tsz Kit Wong
# Email: wongt@bu.edu

# A template for the first function that you are required to write.
def rotate(c, n):
    """takes as inputs a single character c and a
    non-negative integer n between 0 and 25, and
    that returns a single character that is based on c"""

    # check to ensure that c is a single character
    assert (type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    new_ord = ord(c) + n
    if "a" <= c <= "z":
        if new_ord > ord("z"):
            new_ord = new_ord - 26
    elif "A" <= c <= "Z":
        if new_ord > ord("Z"):
            new_ord = new_ord - 26
    else:
        new_ord = ord(c)
    return chr(new_ord)


# Put your code for the encipher function below. #
def encipher(s, n):
    """takes as inputs an arbitrary string s and a non-negative integer n between 0 and 25,
    and that uses recursion to create and return a new string in which the letters in s have
    been “rotated” by n characters forward in the alphabet, wrapping around as needed. Upper-case
    letters should be rotated to upper-case letters, lower-case letters should be rotated
    to lower-case letters, and non-alphabetic characters should be left unchanged"""

    if s == "":
        return ""
    else:
        word_rest = encipher(s[1:], n)
        rotated_letter = rotate(s[0], n)
        return rotated_letter + word_rest



# A helper function that you will use in implementing your 
# string_score function.
# You should *NOT* modify this function.

def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        https://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """

    # check to ensure that c is a single character
    assert (type(c) == str and len(c) == 1)

    if c == ' ':
        return 0.1904
    elif c == 'e' or c == 'E':
        return 0.1017
    elif c == 't' or c == 'T':
        return 0.0737
    elif c == 'a' or c == 'A':
        return 0.0661
    elif c == 'o' or c == 'O':
        return 0.0610
    elif c == 'i' or c == 'I':
        return 0.0562
    elif c == 'n' or c == 'N':
        return 0.0557
    elif c == 'h' or c == 'H':
        return 0.0542
    elif c == 's' or c == 'S':
        return 0.0508
    elif c == 'r' or c == 'R':
        return 0.0458
    elif c == 'd' or c == 'D':
        return 0.0369
    elif c == 'l' or c == 'L':
        return 0.0325
    elif c == 'u' or c == 'U':
        return 0.0228
    elif c == 'm' or c == 'M':
        return 0.0205
    elif c == 'c' or c == 'C':
        return 0.0192
    elif c == 'w' or c == 'W':
        return 0.0190
    elif c == 'f' or c == 'F':
        return 0.0175
    elif c == 'y' or c == 'Y':
        return 0.0165
    elif c == 'g' or c == 'G':
        return 0.0161
    elif c == 'p' or c == 'P':
        return 0.0131
    elif c == 'b' or c == 'B':
        return 0.0115
    elif c == 'v' or c == 'V':
        return 0.0088
    elif c == 'k' or c == 'K':
        return 0.0066
    elif c == 'x' or c == 'X':
        return 0.0014
    elif c == 'j' or c == 'J':
        return 0.0008
    elif c == 'q' or c == 'Q':
        return 0.0008
    elif c == 'z' or c == 'Z':
        return 0.0005
    else:
        return 0.0


# Put your code for string_score and decipher below. #
def string_score(s):
    """takes an arbitrary string s and that uses either recursion
    OR a list comprehension to compute and return the sum of the
    letter-score values of the characters in s. Your function must
    call the provided letter_score function as a helper function
    to determine the score of a given letter"""

    if s == "":
        return ""
    else:
        score_s = [letter_score(letter) for letter in s]
        sum_score = sum(score_s)
        return sum_score


def decipher(s):
    """takes as input an arbitrary string s that has already been
    enciphered by having its characters “rotated” by some amount (possibly 0).
    The function should return, to the best of its ability, the original
    English string, which will be some rotation (possibly 0) of the input string s"""

    options = [encipher(s, n) for n in range(0, 26)]
    options_scores = [[string_score(options[i]), options[i]] for i in range(0, 26)]

    best_option = max(options_scores)
    return best_option[1]


def test():
    """testing functions made"""

    #  rotate()
    print(f"rotate('a', 1):  {rotate('a', 1)}")
    print(f"rotate('B', 3):  {rotate('B', 3)}")
    print(f"rotate('Y', 3):  {rotate('Y', 3)}")
    print(f"rotate('y', 5):  {rotate('y', 5)}")
    print(f"rotate('!', 4):  {rotate('!', 4)}\n")

    # encipher()
    print(f"encipher('hello', 1):  {encipher('hello', 1)}")
    print(f"encipher('hello', 2):  {encipher('hello', 2)}")
    print(f"encipher('ABCXYZ', 3):  {encipher('ABCXYZ', 3)}")
    print(f"encipher('xyzabc', 4):  {encipher('xyzabc', 4)}")
    print(f"encipher('#caesar!', 2):  {encipher('#caesar!', 2)}\n")

    # string_score()
    print(f"string_score('t'):  {string_score('t')}")
    print(f"string_score('m'):  {string_score('m')}")
    print(f"string_score('caesar'):  {string_score('caesar')}")
    print(f"string_score('brutus'):  {string_score('brutus')}\n")

    # decipher()
    print(f"decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'):  {decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.')}")
    print(f"decipher('Kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj.'):  "
          f"{decipher('Kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj.')}")
    print(f"decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'):  "
          f"{decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.')}")
    print(f"decipher('python'):  {decipher('python')}\n")


# test()
