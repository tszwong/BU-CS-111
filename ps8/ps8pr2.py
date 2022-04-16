# ps8pr2.py  (Problem Set 8, Problem 2)
# Markov Test Generation
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#
# Partner Name: None

import random


def create_dictionary(filename):
    """takes a string representing the name of a text file,
    and that returns a dictionary of key-value pairs"""

    dictionary = {}
    current_word = "$"
    sentence_end = ["!", "?", "."]

    opened_file = open(filename)
    txt = opened_file.read()
    lines_split = txt.split()

    for word in lines_split:
        if current_word not in dictionary:  # check for new entries of dictionary
            dictionary[current_word] = []
        dictionary[current_word] += [word]

        if word[-1] in sentence_end:  # check if last letter is sentence ending
            current_word = "$"
        else:
            current_word = word

    opened_file.close()

    return dictionary


def generate_text(word_dict, num_words):
    """akes as parameters a dictionary of word transitions (generated
    by the create_dictionary function) named word_dict and a positive
    integer named num_words"""

    current_word = "$"
    sentence_end = ["!", "?", "."]

    for i in range(num_words):
        wordlist = random.choice(word_dict[current_word])
        print(wordlist, end=" ")

        if wordlist[-1] in sentence_end:
            current_word = "$"
        else:
            current_word = wordlist
