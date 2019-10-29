""" 
Bite 118. List exercise: return first occurrence indices of duplicated words
"""
from typing import List

WORDS_A = ['is', 'it', 'true', 'or', 'is', 'it', 'not']

WORDS_B = [
    'this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this', 'bite', 'will',
    'teach', 'you', 'something', 'new'
]

WORDS_C = ('List comprehensions provide a concise way to create '
           'lists. Common applications are to make new lists where '
           'each element is the result of some operations applied '
           'to each member of another sequence or iterable, or to '
           'create a subsequence of those elements that satisfy a '
           'certain condition').split()


def get_duplicate_indices(words: List[str]) -> List[int]:
    """get_duplicate_indices
    
    Given a list of words, loop through the words and check for each
    word if it occurs more than once.
    If so return the index of its first ocurrence.
    For example in the following list 'is' and 'it'
    occurr more than once, and they are at indices 0 and 1 so you would
    return [0, 1]:
    ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
    Make sure the returning list is unique and sorted in ascending order.
    
    Paramiters:
    -----------
        words (List[str]):
            list of words
    Returns:
    --------
        List[int]:
            duplicate idx's
    """

    data = {key: [] for key in words}
    for idx, word in enumerate(words):
        data[word].append(idx)
    return [idx[0] for idx in data.values() if len(idx) > 1]
