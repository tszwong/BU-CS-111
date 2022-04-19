# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
#
# Partner: None

from ps9pr1 import Board

# write your class below.
class Player:

    def __init__(self, checker):
        """constructs a new Player object by initializing the
        following two attributes: checker, num_moves"""

        assert (checker == 'X' or checker == 'O')

        self.checker = checker
        self.num_moves = 0


    def __repr__(self):
        """returns a string representing a Player object. The string
        returned should indicate which checker the Player object is using"""

        if self.checker == "X":
            return "Player X"

        if self.checker == "O":
            return "Player O"


    def opponent_checker(self):
        """returns a one-character string representing the
        checker of the Player object’s opponent"""

        op_ch = ""

        if self.checker == "X":
            op_ch = "O"
            return op_ch

        if self.checker == "O":
            op_ch = "X"
            return op_ch


    def next_move(self, b):
        """accepts a Board object b as a parameter and returns
        the column where the player wants to make the next move"""

        while True:
            col_num = int(input("Enter a column: "))
            validity = b.can_add_to(col_num)

            if validity:
                self.num_moves += 1
                return col_num
