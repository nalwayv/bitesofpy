"""
Bite 63: Use an infinite iterator to simulate a traffic light
"""
from collections import namedtuple
from itertools import cycle, islice
from time import sleep
from typing import Iterator

# __NAMEDTUPLES__

State = namedtuple('State', 'color command timeout')

# __FUNCS__

def traffic_light() -> Iterator[State]:
    """traffic_light

    Returns an itertools.cycle iterator that
    when iterated over returns State namedtuples
    as shown in the Bite's description

    Returns (Iterator[State]): 
        a cycle iterator that loops over States
    """
    red = State(color='red', command='Stop', timeout=2)
    green = State(color='green', command='Go', timeout=2)
    amber = State(color='amber', command='Caution', timeout=0.5)

    return cycle([red, green, amber])
