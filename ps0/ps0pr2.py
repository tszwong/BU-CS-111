#
# ps0pr2.py - Problem Set 0, Problem 2
#
# Computes the integers 0 through 4 using exactly four fours.
#
# name: Tsz Kit Wong
# email: wongt@bu.edu
#

zero = 4 + 4 - 4 - 4


# Put your definitions of the remaining variables below.
one = 4 * 4 // 4 // 4
two = 4 // 4 + 4 // 4
three = (4 + 4 + 4) // 4
four = 4 * (4 - 4) + 4

# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':
    for x in ['zero', 'one', 'two', 'three', 'four']:
        if x in dir():
            print(x, '=', eval(x))
