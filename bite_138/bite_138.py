"""
Bite 138 oop at the zoo.
"""
from typing import List


class Animal:
    """Animal
    """
    __animals: List[str] = []

    def __init__(self, name: str = ""):
        self.name = name
        if name:
            Animal.__animals.append(name)

    def __str__(self):
        idx = Animal.__animals.index(self.name) + 1
        total = 10000 + idx
        return f"{total}. {self.name.title()}"

    def __iter__(self):
        num = 10001
        for animal in self.__animals:
            yield f"{num}. {animal.title()}"
            num += 1

    @classmethod
    def zoo(cls):
        """zoo
        """
        return "\n".join(list(cls()))
