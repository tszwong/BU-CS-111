# board.py (Final project)
# A Board class for the Eight Puzzle
#
# name: Tsz Kit Wong
# email: wongt@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: None
# partner's email: None

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]


class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """

    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert (len(digitstr) == 9)
        for x in range(9):
            assert (str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.

        for row in range(3):
            for col in range(3):

                self.tiles[row][col] = digitstr[3 * row + col]  # sets the tiles

                if self.tiles[row][col] == "0":  # checks if blank
                    self.blank_r = row
                    self.blank_c = col

    ### Add your other method definitions below. ###

    def __repr__(self):
        """returns a string representation of a Board object"""

        output = ""

        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == "0":
                    output += "_ " # the blank space will be replaced by an underscore
                else:
                    output += self.tiles[row][col]
                    output += " "  # spacing for display

            output += "\n"

        return output


    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction in which
        the blank should move, and that attempts to modify the contents of the called
        Board object accordingly"""

        possible_moves = ["up", "down", "left", "right"]

        if direction not in possible_moves:
            return False  # early return if move is illegal

        temp_r = self.blank_r
        temp_c = self.blank_c

        if direction == "up":
            if temp_r in range(1,3) and temp_c in range(3):
                temp_r = self.blank_r - 1
                holder = self.tiles[temp_r][temp_c]

                self.tiles[temp_r][temp_c] = "0"
                self.tiles[self.blank_r][self.blank_c] = holder

                self.blank_r = temp_r
                self.blank_c = temp_c

                return True

            else:
                return False

        elif direction == "down":
            if temp_r in range(2) and temp_c in range(3):
                temp_r = self.blank_r + 1
                holder = self.tiles[temp_r][temp_c]

                self.tiles[temp_r][temp_c] = "0"
                self.tiles[self.blank_r][self.blank_c] = holder

                self.blank_r = temp_r
                self.blank_c = temp_c

                return True

            else:
                return False

        elif direction == "left":
            if temp_r in range(3) and temp_c in range(1,3):
                temp_c = self.blank_c - 1
                holder = self.tiles[temp_r][temp_c]

                self.tiles[temp_r][temp_c] = "0"
                self.tiles[self.blank_r][self.blank_c] = holder

                self.blank_r = temp_r
                self.blank_c = temp_c

                return True

            else:
                return False

        elif direction == "right":
            if temp_r in range(3) and temp_c in range(2):
                temp_c = self.blank_c + 1
                holder = self.tiles[temp_r][temp_c]

                self.tiles[temp_r][temp_c] = "0"
                self.tiles[self.blank_r][self.blank_c] = holder

                self.blank_r = temp_r
                self.blank_c = temp_c

                return True

            else:
                return False


    def digit_string(self):
        """creates and returns a string of digits that corresponds to the
        current contents of the called Board object’s tiles attribute"""

        out_put = ""

        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == "_":
                    out_put += "0"
                else:
                    out_put += self.tiles[row][col]

        return out_put


    def copy(self):
        """returns a newly-constructed Board object
        that is a deep copy of the called object"""

        dig_str = self.digit_string()
        copy_board = Board(dig_str)

        return copy_board


    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board
        object that are not where they should be in the goal state.
        Does not count blank."""

        count = 0
        order = "0123456789"
        curr = self.digit_string()

        for i in range(len(curr) - 1):
            if curr[i] != 0 and curr[i] != order[i]:
                count += 1

        return count


    def misplaced_spot(self):
        """count number of misplaced in each role"""

        count = 0

        for i in range(len(self.tiles)):
            if self.tiles[0][i] in "012":
                pass
            if self.tiles[1][i] in "0345":
                pass
            if self.tiles[2][i] in "0678":
                pass
            else:
                count += 1

        return count


    def __eq__(self, other):
        """can be called when the == operator is used to compare two Board objects.
        The method should return True if the called object (self) and the argument
        (other) have the same values for the tiles attribute, and False otherwise"""

        if self.tiles == other.tiles:
            return True
        else:
            return False
