""" 
Bite 142. Exception Handling: Calculate the Winning Player
"""
from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores) -> int:
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    ok = all(isinstance(i, int) for i in scores)
    if not ok:
        raise ValueError('not all scores are of type int')

    ok = all(i >= min(DICE_VALUES) and i <= max(DICE_VALUES) for i in scores)
    if not ok:
        raise ValueError('score is not valid')

    return sum([i for i in scores if i >= MIN_SCORE])


def get_winner(players) -> Player:
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    max_len = max(len(p.scores) for p in players)
    ok = all(len(p.scores) == max_len for p in players)

    if not ok:
        raise ValueError('players dont all have the same amount of score values!')

    return max(players, key=lambda player: player.scores)


if __name__ == "__main__":
    tests = [([1, 3, 2, 5], 5), 
             ([1, 4, 2, 5], 9), 
             ([1, 1, 1, 1], 0),
             ([4, 5, 1, 2], 9), 
             ([6, 6, 5, 5], 22)]
    for scores, result in tests:
        try:
            print(calculate_score(scores) == result)
        except ValueError as err:
            print(err)

    players = [
        Player(name='player 1', scores=[1, 3, 2, 5]),
        Player(name='player 2', scores=[4, 4, 6, 1]),
        Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
    ]
    try:
        print(get_winner(players))
    except ValueError as err:
        print(err)