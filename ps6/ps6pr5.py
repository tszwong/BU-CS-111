# ps6pr5.py (Problem Set 6, Problem 5)
#
# 2-D Lists
# Computer Science 111
#
# Name: Tsz Kit Wong
# Email: wongt@bu.edu
# Partner: None

import random


def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []

    for r in range(num_rows):
        row = [0] * num_cols  # a row containing width 0s
        grid += [row]

    return grid


def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')


def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))

    return grid


def col_index_grid(num_rows, num_cols):
    """creates and returns a 2-D list with the specified dimensions in which
    each cell has as its value the index of the column to which the cell belongs"""

    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = c

    return grid


def num_between(grid, n1, n2):
    """takes a 2-D list of integers grid and two integers n1 and n2, and
    that returns the number of values in grid that are between n1 and n2"""

    count = 0

    for x in grid:
        for y in x:
            if y >= n1 and y <= n2:
                count += 1

    return count


def copy(grid):
    """creates and returns a deep copy of grid–a new, separate
    2-D list that has the same dimensions and cell values as grid"""

    copy_list = [[i for i in row] for row in grid]

    return copy_list


def double_with_cap(grid, cap):
    """takes a 2-D list of integers grid and a single integer cap, and that modifies
    the internals of grid. Specifically, the function should double the value of each
    element unless doing so would cause the value of the element to be greater than
    cap. If doubling the element produces a value that is greater than cap, the element
    should be replaced with the value of cap instead"""

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] * 2 < cap:
                grid[x][y] *=2
            else:
                grid[x][y] = cap


def sum_evens_in_col(grid, colnum):
    """takes a 2-D list of integers grid and an integer colnum, and that computes and
    returns the sum of the even values in the column of grid whose index is colnum"""

    sum_evens = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if y == colnum:
                if grid[x][y] % 2 == 0:
                    sum_evens += grid[x][y]

    return sum_evens


def test():
    """test functions made"""

    # random_grid()
    grid = col_index_grid(5, 4)
    print_grid(grid)
    print()

    grid2 = col_index_grid(7, 3)
    print_grid(grid2)
    print()

    grid3 = [[0, 4, 8], [6, 10, 5]]
    print(f"num_between(grid, 4, 6):  {num_between(grid3, 4, 6)}")
    print(f"num_between(grid, 7, 11):  {num_between(grid3, 7, 11)}")
    print(f"num_between(grid, 1, 3):  {num_between(grid3, 1, 3)}")
    print(f"num_between(grid, 11, 7):  {num_between(grid3, 11, 7)}\n")

    grid4 = col_index_grid(3, 4)
    print_grid(grid4)
    print()

    grid5 = copy(grid4)
    print_grid(grid5)
    print()

    grid4[0][1] = 7
    print_grid(grid4)
    print()
    print_grid(grid5)
    print()

    grid7 = [[1, 3, 4], [6, 0, 5]]
    print_grid(grid7)
    print()

    double_with_cap(grid7, 9)
    print_grid(grid7)

    grid8 = [[1, 3, 4], [4, 5, 6], [8, 9, 10]]
    print_grid(grid8)
    print()

    print(sum_evens_in_col(grid8, 0))
    print(sum_evens_in_col(grid8, 1))
    print(sum_evens_in_col(grid8, 2))


# test()
