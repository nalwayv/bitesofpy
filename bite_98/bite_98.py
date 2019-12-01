""" 
Bite 98. Code your way out of a grid
"""
import re
from typing import List, Tuple

DOWN, UP, LEFT, RIGHT = 'DOWN', 'UP', 'LEFT', 'RIGHT'

START_VALUE = 1

SMALL_GRID = """
21 - 22 - 23 - 24 - 25
 |
20    7 -  8 -  9 - 10
 |    |              |
19    6    1 -  2   11
 |    |         |    |
18    5 -  4 -  3   12
 |                   |
17 - 16 - 15 - 14 - 13
"""

INTERMEDIATE_GRID = """
43 - 44 - 45 - 46 - 47 - 48 - 49
 |
42   21 - 22 - 23 - 24 - 25 - 26
 |    |                        |
41   20    7 -  8 -  9 - 10   27
 |    |    |              |    |
40   19    6    1 -  2   11   28
 |    |    |         |    |    |
39   18    5 -  4 -  3   12   29
 |    |                   |    |
38   17 - 16 - 15 - 14 - 13   30
 |                             |
37 - 36 - 35 - 34 - 33 - 32 - 31
"""

BIG_GRID = """
73 - 74 - 75 - 76 - 77 - 78 - 79 - 80 - 81
 |
72   43 - 44 - 45 - 46 - 47 - 48 - 49 - 50
 |    |                                  |
71   42   21 - 22 - 23 - 24 - 25 - 26   51
 |    |    |                        |    |
70   41   20    7 -  8 -  9 - 10   27   52
 |    |    |    |              |    |    |
69   40   19    6    1 -  2   11   28   53
 |    |    |    |         |    |    |    |
68   39   18    5 -  4 -  3   12   29   54
 |    |    |                   |    |    |
67   38   17 - 16 - 15 - 14 - 13   30   55
 |    |                             |    |
66   37 - 36 - 35 - 34 - 33 - 32 - 31   56
 |                                       |
65 - 64 - 63 - 62 - 61 - 60 - 59 - 58 - 57
"""


def str_grid_to_int_grid(grid: str) -> List[List[int]]:
    """str_grid_to_int_grid

    convert str grid to int grid
    
    Parameters
    ----------
    grid : str
        string 
    
    Returns
    -------
    List[List[int]]
        example -> [[1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4],
                    [1,2,3,4]]
    """
    grid_int = []
    for line in grid.splitlines()[1:]:
        line_nums = re.findall(r'\d+', line)
        if line_nums:
            grid_int.append([int(x) for x in line_nums])
    return grid_int


def get_grid_size(grid: List[List[int]]) -> int:
    """get_grid_size
    """
    return max([len(line) for line in grid])


def grid_max_value(grid: List[List[int]]) -> int:
    """ grid_max_value

    get max int value on grid
    """
    return max([max(line) for line in grid])


def is_on_grid(x: int, y: int, _size: int) -> bool:
    """ is_on_grid
    
    check x,y is on grid
    """
    return x >= 0 and x < _size and y >= 0 and y < _size


def get_start_coords(grid: List[List[int]], target: int,
                     _size: int) -> Tuple[int, int]:
    """ get_start_coords
    
    get x,y coords for start position
    """
    for y in range(_size):
        for x in range(_size):
            if grid[y][x] == target:
                return (x, y)

    return (0, 0)


def sort_path(arr: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """sort_path

    sort a list of tuples based on direction taken

    Example
    -------
    >>> sort_path([('down',1),('left',2),('left',3),('right',4)])
    [
        [('down',1)],
        [('left',2), ('left',3)],
        [('right',4)],
    ]
    """

    start = 0
    end = 0
    n = len(arr)
    point = 0
    path = []

    while start < n:
        p = point

        if p + 1 >= n:
            break

        current_dir, _ = arr[p]

        while p < n:
            other_dir, _ = arr[p]
            if current_dir != other_dir:
                break
            p += 1

        start = point
        end = p
        path.append((arr[start:end]))
        point = p

    return path


def print_sequence_route(grid: str, start_coordinates=None) -> None:
    """print_sequence_route
    
    Parameters
    ----------
    grid : str
        string grid
    start_coordinates : int, optional
        position to start at, by default None
    """
    # Setup
    if start_coordinates is None:
        start_coordinates = START_VALUE

    grid2D = str_grid_to_int_grid(grid)

    grid_size = get_grid_size(grid2D)
    x, y = get_start_coords(grid2D, start_coordinates, grid_size)
    start = start_coordinates
    end = grid_max_value(grid2D)

    # Path
    path = [(DOWN, start)]
    while start != end:
        
        next_value = start + 1

        if is_on_grid(x + 1, y, grid_size):
            if grid2D[x + 1][y] == next_value:
                path.append((LEFT, grid2D[x + 1][y]))
                x += 1

        if is_on_grid(x - 1, y, grid_size):
            if grid2D[x - 1][y] == next_value:
                path.append((RIGHT, grid2D[x - 1][y]))
                x -= 1

        if is_on_grid(x, y + 1, grid_size):
            if grid2D[x][y + 1] == next_value:
                path.append((DOWN, grid2D[x][y + 1]))
                y += 1

        if is_on_grid(x, y - 1, grid_size):
            if grid2D[x][y - 1] == next_value:
                path.append((UP, grid2D[x][y - 1]))
                y -= 1

        start += 1

    # Result
    path_taken = sort_path(path)

    for values in path_taken[:-1]:
        _n = ' '.join([str(v[1]) for v in values])
        _d = {v[0] for v in values}.pop()
        print(f"{_n} {_d}")

    # last line does not have a direction at the end
    for values in path_taken[-1:]:
        _n = ' '.join([str(v[1]) for v in values])
        print(_n)


if __name__ == "__main__":
    print_sequence_route(SMALL_GRID)
