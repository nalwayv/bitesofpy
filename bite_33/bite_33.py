""" 
Bite 33. Transpose a data structure 
"""
from collections import namedtuple
from random import randint
from typing import Any, Iterator, List

POSTS = {
    '2017-8': 19,
    '2017-9': 13,
    '2017-10': 13,
    '2017-11': 12,
    '2017-12': 11,
    '2018-1': 3
}

NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']

Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')


def _gen_community() -> Iterator[Member]:
    for name in NAMES:
        yield Member(name=name,
                     since_days=randint(1, 365),
                     karma_points=randint(1, 100),
                     bitecoin_earned=randint(1, 100))


def transpose(data: Any) -> List[list]:
    """Transpose a data structure
    - 1. dict

        >>> data = {'2017-8': 19, '2017-9': 13}
        >>> transpose(data)
        [['2017-8', '2017-9'], [19, 13]]

    - 2. list of (named)tuples

        >>> data = [
            Member(name='Bob', since_days=60, karma_points=60, bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34, bitecoin_earned=78)
        ]
        >>> transpose(data)
        [['Bob', 'Julian'], [60, 221], [60, 34], [56, 78]]
    """
    if isinstance(data, dict):
        return list(zip(*((key,val) for key,val in data.items())))

    if isinstance(data, list):
        return list(zip(*data))

    raise ValueError("data is not of type list or dict")


if __name__ == "__main__":
    # DICT
    months, posts = transpose(POSTS)
    print(months)
    print(posts)
    print("-" * 45)
    # LIST
    names, days, karma, bitecoin = transpose(list(_gen_community()))
    print(names)
    print(days)
    print(karma)
    print(bitecoin)
