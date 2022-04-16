# 
# ps1pr2.py - Problem Set 1, Problem 2
#
# Indexing and slicing puzzles
#
#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:]

# Put your solutions to the remaining list puzzles below.
answer1 = e[1:3:1]  # [7, 1]
answer2 = pi[-1:-6:-2]  # [9, 1, 1]
answer3 = [e[-1]] + [e[0]] + pi[0:6:2]  # [1, 2, 3, 4, 5]

#
# String puzzles
#
b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 4)
# Creating the string 'bossy'
answer4 = b[:3] + t[-1] + u[-1]

# Put your solutions to the remaining string puzzles below.
answer5 = b[2::1] + u[4]
answer6 = b[-1:-3:-1] * 5
answer7 = b[0] + u[4::2] + u[-6:-8:-1] + t[5:7]
answer8 = t[-1:-8:-2] + u[1] + u[-3::1]

# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':
    for n in range(0, 9):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))
