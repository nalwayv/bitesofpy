"""
Bite 263. Count the number of islands in a grid 
"""
from typing import List, Tuple
from collections import namedtuple

Point = namedtuple("Point", "x y")

grid = [[1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]]

squares = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 0]]


def is_on_grid(x, y, n):
    return (x >= 0 and x < n) and (y >= 0 and y < n)


def get_neighbours(vec: Tuple[int, int], grid, n) -> List[Tuple[int, int]]:

    res = []

    left = [1, 0]
    right = [-1, 0]
    down = [0, 1]
    up = [0, -1]

    for d in [left, right, up, down]:
        dx = vec[0] + d[0]
        dy = vec[1] + d[1]

        if is_on_grid(dx, dy, n):
            if grid[dx][dy] == 1:
                res.append((dx, dy))
                grid[dx][dy] = "#"

    return res


def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    # grid[i][j] = '#'      # one way to mark visited ones - suggestion.


if __name__ == "__main__":

    n = len(squares[0])

    count = 0

    for x in range(n):
        for y in range(n):

            if squares[x][y] == 1:

                stack = [(x, y)]
                explored = []

                while stack:

                    current = stack.pop()

                    if current in explored:
                        continue

                    explored.append(current)
                    for nei in get_neighbours(current, squares, n):
                        stack.append(nei)

                count += 1

    print(count)
    p = Point(0, 0)
    print(p.x)