"""
Bite 153
"""
from math import ceil, floor


def floor_it(num: float):
    return floor(num)


def ceil_it(num: float):
    return ceil(num)


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        return [ceil(x) for x in transactions]
    return [floor(x) for x in transactions]
