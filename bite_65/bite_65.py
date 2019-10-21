"""
Bite 65: Get all valid dictionary words for a draw of letters
"""
import os
from collections import Counter
from itertools import permutations

# CONSTS
DICTIONARY = os.path.join(os.path.dirname(__file__), 'tmp', 'dictionary.txt')
SCRABBLE_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {
    letter: score
    for score, letters in SCRABBLE_SCORES for letter in letters.split()
}


# FUNCS
def load_words():
    """Load the words dictionary (DICTIONARY constant)
    into a list and return it
    """
    words = []
    file_path = os.path.abspath(DICTIONARY)

    try:
        with open(file_path, "r") as file:
            words = set([word.strip().lower() for word in file.read().split()])
    except IOError as err:
        print(f"file not found! - {err}")
        raise IOError()

    return words


def _test_word(draw: list, word: str):
    return all(word.count(c) <= draw.count(c) for c in word)


def _get_permutations_draw(draw, size):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    perm = permutations(draw, size)
    return list(perm)


def get_possible_dict_words(draw: list):
    draw_str = "".join(draw).lower()
    words = [
        word for word in sorted(load_words())
        if len(word) <= len(draw) and word[0] in [c for c in draw_str]
    ]
    return [w for w in words if _test_word(draw_str, w)]

