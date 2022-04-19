# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
# Computer Science 111
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu

import random  
from ps9pr3 import *

class AIPlayer(Player):
    #  will look ahead some number of moves into the future to assess the impact of each possible move
    #  that it could make for its next move, and it will assign a score to each possible move. And since
    #  each move corresponds to a column number, it will effectively assign a score to each column

    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object. Begin the method
        with assert statements that validate the inputs"""

        assert (checker == 'X' or checker == 'O')
        assert (tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert (lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead


    def __repr__(self):
        """returns a string representing an AIPlayer object"""

        output = "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"
        return  output


    def max_score_column(self, scores):
        """makes a list scores containing a score for each column of the board,
        and that returns the index of the column with the maximum score"""

        highest_score = max(scores)
        num_lst = []

        for i in scores:
            if i == highest_score:
                num_lst += [scores.index(i)]

        if self.tiebreak == "RIGHT":
            return num_lst[-1]
        elif self.tiebreak == "LEFT":
            return num_lst[0]
        else:
            return random.choice(num_lst)


    def scores_for(self, b):
        """takes a Board object b and determines the called AIPlayer‘s scores for the columns in b.
        Each column should be assigned one of the four possible scores discussed in the Overview at
        the start of this problem, based on the called AIPlayer‘s lookahead value.
        The method should return a list containing one score for each column"""

        scores = [' ' for col in range(b.width)]

        for i in range(b.width):

            if not b.can_add_to(i):
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50

            else:
                b.add_checker(self.checker, i)

                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)  #  creates an opponent

                scores_opponent = opponent.scores_for(b)  # recursive call
                scores[i] = 100 - max(scores_opponent)

                b.remove_checker(i)  #  restore the board b to its prior state

        return scores



    def next_move(self, b):
        """overrides (i.e., replaces) the next_move method that is inherited from Player.
        Rather than asking the user for the next move, this version of next_move should return
        the called AIPlayer‘s judgment of its best possible move"""

        self.num_moves += 1
        move = self.max_score_column(self.scores_for(b))

        return move
