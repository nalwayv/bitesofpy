""" 
Bite 61. Create a variable size Paw Patrol card deck with random actions
"""
from collections import namedtuple
import random
import string

ACTIONS = [
    'draw_card', 'play_again', 'interchange_cards', 'change_turn_direction'
]

NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def create_paw_deck(n=8):
    if n > 26:
        raise ValueError('n too large')

    actions = ACTIONS * n

    cards = []
    for char in string.ascii_uppercase[:n]:
        for num in NUMBERS:
            cards.append([f'{char}{num}', None])
    random.shuffle(cards)

    for i in range(n):
        cards[i][1] = actions.pop()

    deck = [PawCard(card=name, action=act) for name, act in cards]

    random.shuffle(deck)

    return deck
