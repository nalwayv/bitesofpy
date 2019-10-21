"""
Bite 05
"""
from typing import List, Tuple

NAMES = [
    'arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
    'julian sequeira', 'sandra bullock', 'keanu reeves', 'julbob pybites',
    'bob belderbos', 'julian sequeira', 'al pacino', 'brad pitt', 'matt damon',
    'brad pitt'
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    titles = {name.title() for name in names}
    return list(titles)


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # ...
    data: List[Tuple[str, str]] = [tuple(name.split(" ")) for name in names]
    data.sort(key=lambda x: x[1], reverse=True)

    return [f"{f} {s}" for f, s in data]


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    data: List[Tuple[str, str]] = [tuple(name.split(" ")) for name in names]
    data.sort(key=lambda x: len(x[0]))

    return data[0][0]
