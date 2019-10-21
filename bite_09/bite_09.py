"""
Bite 9: Palindromes
Write a function to determine if a word (or phrase) is a palindrome.

Then write a second function to receive a word (or phrase) list and determine
which word is the longest palindrome.

See the template code / docstrings below for further requirements as well as
the tests.

A palindrome is a word, phrase, number, or other sequence
of characters which reads the same backward as forward
"""

import os

DICTIONARY = os.path.join('tmp', 'dictionary_m_words.txt')


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word: str) -> str:
    """is_palindrome - checks if a wors is a palindrome

    Args:
        word (str): a word

    Returns:
        bool: is a palindrome or not
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    abc = f"{letters}{letters.upper()}"
    word_cleanup = ''.join(
        [c.lower() for c in word if (abc.index(c) if c in abc else -1) != -1])

    def inner_palindrome(w: str):
        if len(w) <= 0:
            return True
        return w[0] == w[-1] and inner_palindrome(w[1:-1])

    return inner_palindrome(word_cleanup)


def get_longest_palindrome(words=None) -> str:
    """get_longest_palindrome

    Args
        words (list[str], optional): if none open load_dictionary.txt, by default None

    Returns
        str: longest palindrome
    """
    if words is None:
        words = load_dictionary()

    current_top = ""
    for word in words:
        ok = is_palindrome(word)
        if ok:
            if len(word) > len(current_top):
                current_top = word

    return current_top
