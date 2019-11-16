""" 
Bite 33. Transpose a data structure 
"""
from collections import namedtuple
from random import randint
from typing import List, Any, Iterator

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
        keys = list(data.keys())
        values = list(data.values())
        return [keys, values]

    if isinstance(data, list):
        try:
            names = [user.name for user in data]
            since_days = [user.since_days for user in data]
            karma_points = [user.karma_points for user in data]
            bitecoin_earned = [user.bitecoin_earned for user in data]
        except AttributeError:
            raise AttributeError(
                "data within list is not of a Member namedtuple")

        return [names, since_days, karma_points, bitecoin_earned]

    raise ValueError("data is not of type list or dict")


if __name__ == "__main__":
    print("-" * 45)
    # DICT
    months, posts = transpose(POSTS)
    print(months)
    print(posts)

    print("-" * 45)
    # LIST
    community = [
        Member(name='Bob', 
                since_days=145, 
                karma_points=69,
                bitecoin_earned=67),

        Member(name='Julian',
                since_days=157,
                karma_points=52,
                bitecoin_earned=14),

        Member(name='Tim', 
                since_days=9,
                karma_points=100,
                bitecoin_earned=10),

        Member(name='Carmen',
               since_days=155,
               karma_points=1,
               bitecoin_earned=49),

        Member(name='Henk',
               since_days=302,
               karma_points=91,
               bitecoin_earned=81),

        Member(name='Sofia',
               since_days=279,
               karma_points=52,
               bitecoin_earned=76),

        Member(name='Bernard',
               since_days=72,
               karma_points=96,
               bitecoin_earned=69)]

    names, days, karma, bitecoin = transpose(community)
    print(names)
    print(days)
    print(karma)
    print(bitecoin)

    print("-" * 45)
