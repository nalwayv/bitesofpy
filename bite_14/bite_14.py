""" 
Bite 14. Generate a table of n sequences 
"""
import random
from typing import Iterator

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*args) -> Iterator[str]:
    are_all_lists = all(isinstance(a, list) for a in args)
    are_all_same_len = all(len(a) == max(len(x) for x in args) for a in args)

    if not args or not are_all_lists or not are_all_same_len:
        raise Exception('error with args passed in')

    for arg in zip(*args):
        yield SEPARATOR.join(str(value) for value in arg)


if __name__ == "__main__":
    for table in generate_table(names, aliases, points, awake):
        print(table)
