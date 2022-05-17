# eight_puzzle.py (Final project)
# driver/test code for state-space search on Eight Puzzles   
#
# name: Tsz Kit Wong
# email: wongt@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: None
# partner's email: None

from searcher import *
from timer import *


def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None

    if algorithm == 'random':
        searcher = Searcher(param)
    ## You will uncommment the following lines as you implement
    ## other algorithms.
    elif algorithm == 'BFS':
       searcher = BFSearcher(param)
    elif algorithm == 'DFS':
       searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
       searcher = GreedySearcher(param)
    elif algorithm == 'A*':
       searcher = AStarSearcher(param)
    else:
        print('unknown algorithm:', algorithm)

    return searcher


def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()

    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


def process_file(filename, algorithm, param):
    """open the file with the specified filename for reading, and
    it should use a loop to process the file one line at a time"""

    file_open = open(filename, "r")

    num_solved = 0
    num_moves = 0
    num_states = 0

    for line in file_open:

        digit_string = line[:-1]
        init_board = Board(digit_string)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)

        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')

        if soln == None:
            print(f"{digit_string}: no solution")
        else:
            num_solved += 1
            num_moves += soln.num_moves
            num_states += searcher.num_tested

            print(f"{digit_string}: {soln.num_moves} moves, {searcher.num_tested} states tested")

    if num_solved != 0:
        print(f"\nsolved: {num_solved} puzzles\naverages: {num_moves/num_solved} "
              f"moves, {num_states/num_solved} states tested")
    else:
        print(f"\nsolved: {num_solved} puzzles")

    file_close = file_open.close()
