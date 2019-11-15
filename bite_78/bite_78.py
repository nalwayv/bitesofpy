"""
Bite 78. Find programmers with common languages
"""
from typing import List, Dict


def common_languages(programmers: Dict[str, List[str]]) -> List[str]:
    """Receive a dict of keys -> names and values -> a sequence of
    of programming languages, return the common languages

    Parameters
    ----------
    programmers : Dict[str, List[str]]
        
    Returns
    -------
    List[str]
        
    """
    values = [val for val in programmers.values()]

    res = set(values[0])

    for val in values[1:]:
        res &= set(val)

    return list(res)
