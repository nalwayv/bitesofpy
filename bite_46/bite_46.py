""" 
Bite 46
"""
from typing import Tuple


def fizzbuzz(n) -> Tuple[int, str]:
    """fizzbuzz

    Returns
    -------
        tup(int,str)
    """
    promts = []

    if n % 3 == 0:
        promts.append("Fizz")

    if n % 5 == 0:
        promts.append("Buzz")

    if not promts:
        return n, ""

    return n, " ".join(promts)
