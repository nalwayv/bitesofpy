""" 
Bite 61. Create a variable size Paw Patrol card deck with random actions
"""
import random
import string
from collections import namedtuple
from itertools import zip_longest

ACTIONS = [
    'draw_card', 'play_again', 'interchange_cards', 'change_turn_direction'
]

NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def create_paw_deck(n=8):
    if n > 26:
        raise ValueError('n too large')

    cards = [
        f'{char}{num}' for char in string.ascii_uppercase[:n]
        for num in NUMBERS
    ]

    random.shuffle(cards)
    actions = random.choices(ACTIONS * n, k=n)

    return [PawCard(card=c, action=a) for c, a in zip_longest(cards, actions)]
