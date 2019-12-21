"""
Bite 61. Create a variable size Paw Patrol card deck with random actions
"""
import random
from collections import namedtuple
from itertools import zip_longest
from string import ascii_uppercase
from typing import List

ACTIONS = [
    'draw_card', 'play_again', 'interchange_cards', 'change_turn_direction'
]

NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


def create_paw_deck(n: int = 8) -> List[PawCard]:
    """create_paw_deck

    Args:
        n (int): Defaults to 8

    Raises:
        ValueError: if n > 26

    Returns:
        List[PawCard]
    """
    if n > 26:
        raise ValueError('n too large')

    cards = [f'{char}{num}' for char in ascii_uppercase[:n] for num in NUMBERS]

    random.shuffle(cards)
    actions = random.choices(ACTIONS * n, k=n)

    return [PawCard(card=c, action=a) for c, a in zip_longest(cards, actions)]


if __name__ == "__main__":
    small_deck = create_paw_deck(4)
    for card in small_deck:
        print(card.card)
