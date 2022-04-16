# PS5 Problem 8
#
# Processing Sequences With Loops
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
# Partner: None

def total_len(words):
    """takes as input a list of 0 or more strings words
    and uses a loop to compute and return the value obtained
    by adding together the lengths of all the strings in the list"""

    len_words = 0

    for word in words:
        len_words += len(word)

    return len_words


def exclaim(s):
    """takes an arbitrary string s as input and uses a loop to form
    and return the string formed by adding an exclamation point
    (i.e., the character '!') after each character in the string s"""

    output_str = ""

    for letter in s:
        letter_exc = letter + "!"
        output_str += letter_exc

    return output_str


def consonants(s):
    """takes as input a string s and uses a loop to create
    and return a list containing the consonants (if any) in s"""

    vowels = "aeiou"
    output_lst = []

    for letter in s:
        if letter not in vowels:
            output_lst += letter

    return output_lst


def smaller_of(vals1, vals2):
    """takes as inputs two lists vals1 and vals2 and uses a loop
    to construct and return a new list in which each element is the
    the smaller of the corresponding elements from the original lists"""

    output_lst = []
    shorter_len = min(len(vals1), len(vals2))
    index = 0

    for i in range(shorter_len):
        if vals1[index] < vals2[index] or vals1[index] == vals2[index]:
            output_lst += [vals1[index]]
        else:
            output_lst += [vals2[index]]
        index += 1

    return output_lst


def test():
    """tests functions made"""

    # total_len()
    print(f"total_len(['hi', 'there']):  {total_len(['hi', 'there'])}")
    print(f"total_len(['looping', 'is', 'fun']):  {total_len(['looping', 'is', 'fun'])}")
    print(f"total_len(['bye']):  {total_len(['bye'])}")
    print(f"total_len([]):  {total_len([])}\n")

    # exclaim()
    print(f"exclaim('hello'):  {exclaim('hello')}")
    print(f"exclaim('wow'):  {exclaim('wow')}")
    print(f"exclaim('o'):  {exclaim('o')}")
    print(f"exclaim(''):  {exclaim('')}\n")

    # consonants()
    print(f"consonants('computer'):  {consonants('computer')}")
    print(f"consonants('science'):  {consonants('science')}")
    print(f"consonants('aeiou'):  {consonants('aeiou')}\n")

    # smaller_of()
    print(f"smaller_of([3, 4, 9, 5], [7, 2, 0, 5]):  {smaller_of([3, 4, 9, 5], [7, 2, 0, 5])}")
    print(f"smaller_of([5, 7, 2], [1, 9, 15]):  {smaller_of([5, 7, 2], [1, 9, 15])}")
    print(f"smaller_of([], []):  {smaller_of([], [])}")
    print(f"smaller_of([0, 3, 6, 9], [1, 1]):  {smaller_of([0, 3, 6, 9], [1, 1])}")
    print(f"smaller_of([3, 1, 0], [2, 4, 5, 6]):  {smaller_of([3, 1, 0], [2, 4, 5, 6])}\n")

# test()
