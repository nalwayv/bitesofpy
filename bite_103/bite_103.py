"""
Bite 103
"""
games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing (print, not return) how many games each person has won,
       pluralize 'game' based on number.

       Expected output (ignore the docstring's indentation):

       sara has won 0 games
       bob has won 1 game
       tim has won 5 games
       julian has won 3 games
       jim has won 1 game

       (Note that as of Python 3.7 - which we're using atm - dict insert order is retained
        so no sorting is required for this Bite.)
    """
    for key,value in games_won.items():
        if value == 1:
            print(f"{key} has won {value} game")
        else:
            print(f"{key} has won {value} games")
