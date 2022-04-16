#
# Problem Set 3 Problem 2
# Algorithm Design
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#

def cube_all_lc(values):
    """takes as input a list of numbers called values,
    and that uses a list comprehension to create and
    return a list containing the cubes of the numbers in values"""

    return [x**3 for x in values]


def cube_all_rec(values):
    """ takes as input a list of numbers called values,
    and that uses recursion to create and return a list
    containing the cubes of the numbers in values"""

    if not values:  # base case
        return []
    
    else:           # recursive case
        rest_values = cube_all_lc(values[1:])
        cubed_valued = [values[0]**3]

        return cubed_valued + rest_values


def consonants(s):
    """takes as input a string s and uses a
    list comprehension to create and return a
    list containing the consonants (if any) in s"""

    consonant_letters = "bcdfghjklmnpqrstvwxyz"
    s_consonants = [x for x in s if x in consonant_letters]
    return s_consonants


def num_consonants(s):
    """takes as input a string s and
    returns the number of consonants in s"""

    list_consonants = consonants(s)
    len_list = len(list_consonants)
    return len_list


def most_consonants(wordlist):
    """takes a list of lowercase words called
    wordlist and returns the word in the list
    with the most consonants"""

    words_with_num_consonants = [[num_consonants(x), x] for x in wordlist]
    highest_pair = max(words_with_num_consonants)

    return highest_pair[1]


def test():
    """test functions made"""

    #  cube_all_lc()
    print(f"cube_all_lc([-2, 5, 4, -3]):  {cube_all_lc([-2, 5, 4, -3])}")
    print(f"cube_all_lc([1, 2, 3]):  {cube_all_lc([1, 2, 3])}\n")

    #  cube_all_rec()
    print(f"cube_all_rec([-2, 5, 4, -3]):  {cube_all_rec([-2, 5, 4, -3])}")
    print(f"cube_all_rec([1, 2, 3]):  {cube_all_rec([1, 2, 3])}\n")

    # consonants()
    print(f"consonants('computer'):  {consonants('computer')}")
    print(f"consonants('science'):  {consonants('science')}")
    print(f"consonants('aeiou'):  {consonants('aeiou')}\n")

    # num_consonants()
    print(f"num_consonants('computer'): {num_consonants('computer')}\n")

    # most_consonants()
    print(f"most_consonants(['computer', 'science']):  {most_consonants(['computer', 'science'])}")
    print(f"most_consonants(['obama', 'bush', 'clinton']):  {most_consonants(['obama', 'bush', 'clinton'])}")


test()
