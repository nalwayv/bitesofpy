""" 
Bite 168. Ninja Rankings
"""
from dataclasses import dataclass, field
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]

NAMES: List[Tuple[str, int]] = [(name, bite)
                                for name, bite in zip(names, bites)]


@dataclass(order=True)
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __str__(self):
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    rankings: List[Ninja] = field(init=False, default_factory=list)

    def __len__(self):
        return len(self.rankings)

    def add(self, ninja: "Ninja"):
        self.rankings.append(ninja)
        self.rankings.sort(key=lambda x: x.bites, reverse=True)

    def dump(self):
        last = self.rankings.pop()
        return last

    def highest(self, count: int = 1):
        return self.rankings[:count]

    def lowest(self, count: int = 1):
        return self.rankings[-count:][::-1]

    def pair_up(self, count: int = 3):
        high = self.highest(count)
        low = self.lowest(count)
        return list(zip(high, low))
