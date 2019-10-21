"""
Bite 60 uno cards
"""
from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")

def create_uno_deck() -> list:
    """create_uno_deck - create simple namedtuple uno deck of cards
    """
    pattern = [1] + [2]*12
    cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]

    deck = []

    # - suits
    for suit in SUITS:
        for amount_of, card_type in list(zip(pattern, cards)):
            for _ in range(amount_of):
                deck.append(UnoCard(suit, card_type))

    # - no suit
    for idx in range(8):
        if idx < 4:
            deck.append(UnoCard(None, "Wild"))
        else:
            deck.append(UnoCard(None, "Wild Draw Four"))

    # - result
    return deck


# if __name__ == "__main__":
#     output_deck = create_uno_deck()
#     for card in output_deck:
#         print(card)
