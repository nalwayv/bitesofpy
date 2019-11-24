""" 
Bite 34. Building a Karma app - implement the User class 
"""

from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(), )  # http://bit.ly/2rmiUrL


class User:
    def __init__(self, name: str):
        self._name = name
        self._transactions = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def fans(self) -> int:
        return len({x.giver for x in self._transactions})

    @property
    def karma(self) -> int:
        return sum(self.points)

    @property
    def points(self) -> list:
        return [x.points for x in self._transactions]

    def __str__(self):
        str_fans = 'fan'
        if self.fans > 1:
            str_fans = 'fans'

        return f"{self.name} has a karma of {self.karma} and {self.fans} {str_fans}"

    def __add__(self, other):
        if not isinstance(other, Transaction):
            raise ValueError('not a transaction')

        self._transactions.append(other)
