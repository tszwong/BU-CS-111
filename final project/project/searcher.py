# searcher.py (Final project)
# classes for objects that perform state-space search on Eight Puzzles
#
# name: Tsz Kit Wong
# email: wongt@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: None
# partner's email: None

import random
from state import *


class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """

    ### Add your Searcher method definitions here. ###

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


    def __init__(self, depth_limit):
        """constructs a new Searcher object by initializing the following
        states: Searcher‘s list of untested states; initialized to an empty list
        num_tested: keep track of how many states the Searcher tests; initialized to 0
        depth_limit: specifies how deep in the state-space search tree the Searcher will go"""

        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def add_state(self, new_state):
        """takes a single State object called new_state and
        adds it to the Searcher‘s list of untested states"""

        self.states.append(new_state)


    def should_add(self, state):
        """takes a State object called state and returns True if the called Searcher
        should add state to its list of untested states, and False otherwise"""

        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle():
            return False
        else:
            return True


    def add_states(self, new_states):
        """takes a list State objects called new_states, and
        that processes the elements of new_states one at a time"""

        for s in new_states:
            if self.should_add(s):
                self.add_state(s)


    def next_state(self):
        """ chooses the next state to be tested from the list of
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)

        return s


    def find_solution(self, init_state):
        """performs a full state-space search that begins at the
        specified initial state init_state and ends when the goal state
        is found or when the Searcher runs out of untested states"""

        self.add_state(init_state)

        while self.states != []:
            s = self.next_state()
            self.num_tested += 1

            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())

        return None  # failure


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    #  for searcher objects that perform breadth-first search (BFS) instead of random search

    def next_state(self):
        """overrides (i.e., replaces) the next_state method that is
        inherited from Searcher using FIFO(First In First Out)"""

        longest_state = self.states[0]
        self.states.remove(longest_state)

        return longest_state


class DFSearcher(Searcher):
    #  for searcher objects that perform depth-first search (DFS) instead of random search

    def next_state(self):
        """overrides (i.e., replaces) the next_state method that is
        inherited from Searcher using LIFO(Last In First Out)"""

        recent_state = self.states[-1]
        self.states.remove(recent_state)

        return recent_state


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """computes and returns an estimate of how many additional
    moves are needed to get from state to the goal state"""

    additional_moves = state.board.num_misplaced()
    return additional_moves


def h2(state):
    """alternate heuristic"""

    additional_moves = state.board.num_misplaced()
    spot = state.board.misplaced_spot()
    moves = additional_moves + spot

    return moves


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """

    ### Add your GreedySearcher method definitions here. ###

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


    def __init__(self, heuristic):
        """constructs a new GreedySearcher object"""
        
        super(GreedySearcher, self).__init__(-1)
        self.heuristic = heuristic


    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """

        return -1 * self.heuristic(state)


    def add_state(self, state):
        """verrides (i.e., replaces) the add_state method that is inherited from Searcher
        """

        self.states.append([self.priority(state), state])


    def next_state(self):
        """overrides (i.e., replaces) the next_state method that is
        inherited from Searcher. This version of next_state should
        choose one of the states with the highest priority"""

        highest_priority = max(self.states)
        self.states.remove(highest_priority)

        return highest_priority[-1]


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """A* is an informed search algorithm that assigns a priority to
    each state based on a heuristic function, and that selects the next state based on
    those priorities. However, when A* assigns a priority to a state, it also takes
    into account the cost that has already been expended to get to that state
    """

    def priority_search(self, state):
        """computation of the priority of a state"""

        priority = -1 * (self.heuristic(state) + state.num_moves)
        return priority
