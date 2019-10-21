"""
Bite 80 check equality of two lists
"""

from enum import Enum
from typing import List


class Equality(Enum):
    """LIST-CHECKS"""
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1: List, list2: List):
    """check_equality - check equality between two lists
    """
    # check id
    if id(list1) == id(list2):
        return Equality.SAME_REFERENCE

    # same ordered
    if list1 == list2:
        return Equality.SAME_ORDERED

    # same unordered
    def counter(lista, listb) -> bool:
        from collections import Counter
        return Counter(lista) == Counter(listb)

    if counter(list1, list2):
        return Equality.SAME_UNORDERED

    # same unordered deduped  - when set they are the same
    if set(list1) == set(list2):
        return Equality.SAME_UNORDERED_DEDUPED

    # not equal
    return Equality.NO_EQUALITY


# - TESTS -


def test_same_reference():
    a = [1, 2, 3, 4]
    b = a
    # shallow copy (do not change original), alternatively use the copy module
    c = a[:]
    v1 = check_equality(a, b) == Equality.SAME_REFERENCE
    v2 = check_equality(a, c) != Equality.SAME_REFERENCE
    print(f"{v1}, {v2}")


def test_same_ordered():
    a = [1, 2, 3, 4]
    b = a[:]
    c = a
    v1 = check_equality(a, b) == Equality.SAME_ORDERED
    v2 = check_equality(a, c) != Equality.SAME_ORDERED  # SAME_REFERENCE
    print(f"{v1}, {v2}")


def test_same_unordered():
    a = [1, 2, 3, 4]
    b = a[::-1]
    c = b[:] + [5]
    v1 = check_equality(a, b) == Equality.SAME_UNORDERED
    v2 = check_equality(a, c) != Equality.SAME_UNORDERED
    print(f"{v1}, {v2}")


def test_same_unordered_deduped():
    a = [1, 2, 2, 3, 4]
    b = a[:] + [1, 3, 4, 4]
    c = b[:] + [5]

    v1 = check_equality(a, b) == Equality.SAME_UNORDERED_DEDUPED
    v2 = check_equality(a, c) != Equality.SAME_UNORDERED_DEDUPED
    print(f"{v1}, {v2}")


def test_not_same():
    a = [1, 2, 3]
    b = [4, 5, 6]
    v1 = check_equality(a, b) == Equality.NO_EQUALITY
    print(f"{v1}")
