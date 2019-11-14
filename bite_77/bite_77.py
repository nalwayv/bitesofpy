"""
Bite 77. New places to travel to 
"""
from typing import List


def uncommon_cities(my_cities: List[str], other_cities: List[str]) -> int:
    """Compare my_cities and other_cities and return the number of different
       cities between the two
    
    Parameters
    ----------
    - my_cities : List[str]
        list of my cities

    - other_cities : List[str]
        list of other cities
    
    Returns
    -------
    int :
        len of difference between two cities
    """
    v1 = set(my_cities)
    v2 = set(other_cities)
    return len(v1 ^ v2)
