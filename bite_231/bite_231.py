"""
Bite 231. Where are the emojis?
"""
import string
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib

EMOJIS = [
    ('We 💜 Python 🐍', [3, 12]),
    ('We are so happy 😊😍 seeing you all coding', [16, 17]),
    ('😂 ROFL that is funny 😂', [0, 21]),
    ('No way 😭, that is not cool 🤔', [7, 27]),
    ('Great job 👌 hitting that Ninja 💪 belt', [10, 31]),
    ('Good luck with your 100 days of code 💯', [37]),
    ('Our 🥋 ninjas are on fire 🔥', [4, 25]),
    ('Happy Valentine 💕, buy some gifts 🎁', [16, 34]),
    ('pytest is so cool 😎, after grasping it 🤯', [18, 39]),
    ('Books can be boring 😴, better to code 💪❗', [20, 38, 39]),
]


def get_emoji_indices(text: str) -> List[int]:
    """get_emoji_indices

    Given a text return indices of emoji characters

    Paramiters:
    -----------
        text (str): 
            text to check for emojis
        
    Returns:
    --------
        List[int]: 
            list with indexes of emojis
    """
    vals = [
        ord(char) for char in f"{string.ascii_letters}{string.punctuation}"
    ]
    _max = max(vals)

    res = []
    for idx, char in enumerate([c for c in text]):
        ok = ord(char) <= _max
        if not ok:
            res.append(idx)
    return res


if __name__ == "__main__":
    for text, result in EMOJIS:
        ok = get_emoji_indices(text)
        print(ok == result)
