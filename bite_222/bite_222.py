"""
Bite.222: slice list based on n size
"""
from typing import List


def group(iterable: List[int], n: int) -> List[List[int]]:
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    size = len(iterable)
    return [list(iterable[i:i + n]) for i in range(0, size, n)]

