"""
bite 122 check if two words are anagrams
"""


def is_anagram(word1: str, word2: str) -> bool:
    """is_anagram

    checks if word_2 is an anagram of word_1
    or word_1 is an anagram of word_2 ?

    Args:
        word1 (str): a word that could be an anagram of word_2
        word2 (str): a word that could be an anagram of word_1

    Returns:
        bool: True if ever if an anagram of the other else False
    """
    abc = "abcdefghijklmnopqrstuvwxyz"
    nums = [str(i) for i in range(10)]

    one = sorted([w.strip() for w in word1.lower() if w in abc or w in nums])
    two = sorted([w.strip() for w in word2.lower() if w in abc or w in nums])

    return "".join(one) == "".join(two)
