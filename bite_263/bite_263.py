"""
Bite 263. Count the number of islands in a grid 
"""
from typing import List
from collections import namedtuple

Point = namedtuple("Point", "x y")

squares = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 0]]

sparse = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

empty = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

bad_map = [[]]

circles = [[1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 0]]


def is_on_grid(point: Point, n: int) -> bool:
    """is_on_grid
    
    check if point is on grid

    Args:
        point (Point): x, y
        n (int): size of grid array
    
    Returns:
        bool: point is on grid
    """
    return (point.x >= 0 and point.x < n) and (point.y >= 0 and point.y < n)


def get_neighbours(point: Point, grid: list, n: int) -> List[Point]:
    """get_neighbours
    
    get points neighbours

    Args:
        point (Point): x, y
        grid (List[List[int]]): 2d array
        n (int): len of grid
    
    Returns:
        List[Point]: points neighbours
    """
    res = []

    for d in [Point(1, 0), Point(-1, 0), Point(0, -1), Point(0, 1)]:

        p2 = Point(point.x + d.x, point.y + d.y)

        if is_on_grid(p2, n):
            if grid[p2.x][p2.y] == 1:
                res.append(p2)

    return res


def count_islands(grid: list) -> int:
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    if not grid:
        return 0
    if not all(g for g in grid):
        return 0

    n = len(grid[0])

    islands = 0

    for x in range(n):
        for y in range(n):

            if grid[x][y] == 1:

                stack: List[Point] = [Point(x, y)]
                explored: List[Point] = []

                while stack:

                    current: Point = stack.pop()

                    if current in explored:
                        continue

                    explored.append(current)
                    for neighbour in get_neighbours(current, grid, n):
                        stack.append(neighbour)
                        mark_islands(neighbour, grid)

                islands += 1

    return islands


def mark_islands(p: Point, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    grid[p.x][p.y] = "#"


if __name__ == "__main__":
    print(count_islands(squares))
    print(count_islands(sparse))
    print(count_islands(empty))
    print(count_islands(bad_map))
    print(count_islands(circles))