"""
Bite 72 belts
"""

from collections import OrderedDict
from typing import Optional

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score) -> Optional[str]:
    """get_belt - get belt based on score
    """
    #
    if user_score >= MAX_SCORE:
        return HONORS[MAX_SCORE]
    if user_score < MIN_SCORE:
        return None

    for low, high in list(zip(scores, scores[1:])):
        if user_score >= low and user_score < high:
            return HONORS[low]
    return None


if __name__ == "__main__":
    tests = [(0, None), (9, None), (10, 'white'), (48, 'white'),
             (50, 'yellow'), (101, 'orange'), (249, 'green'), (250, 'blue'),
             (251, 'blue'), (400, 'brown'), (599, 'brown'), (600, 'black'),
             (788, 'black'), (800, 'paneled'), (999, 'paneled'), (1000, 'red'),
             (1200, 'red')]

    for score, belt in tests:
        print(get_belt(score) == belt)
