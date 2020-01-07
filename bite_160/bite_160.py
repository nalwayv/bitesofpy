""" 
Bite 160. 15-way Rock Paper Scissors 
"""
import csv
import os
from urllib.request import urlretrieve
from collections import defaultdict
from typing import Dict

DATA = 'battle-table.csv'
BATTLE_DATA_2 = os.path.join(os.path.dirname(__file__), 'tmp', DATA)

PLAYERS = ("Rock Gun Lightning Devil Dragon Water Air Paper Sponge "
           "Wolf Tree Human Snake Scissors Fire").split()


def _create_defeat_mapping() -> Dict[str, Dict[str, str]]:
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    dt = defaultdict(dict)
    with open(BATTLE_DATA_2) as csv_data:
        reader = csv.DictReader(csv_data)
        for row in reader:
            for p in PLAYERS:
                # NOTE: example {'Rock': {'Scissors':'lose'}}
                dt[row['Attacker']][p] = row[p]
        return dt


def get_winner(player1: str, player2: str, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    if not isinstance(player1, str) or not isinstance(player2, str):
        raise ValueError
    if player1 not in PLAYERS or player2 not in PLAYERS:
        raise ValueError

    defeat_mapping = _create_defeat_mapping()

    result: str = defeat_mapping.get(player1).get(player2)

    if result == 'win':
        return player1

    if result == 'lose':
        return player2

    return 'Tie'


if __name__ == "__main__":
    for t in ['Scissors', 'Snake', 'Human', 'Wolf', 'Sponge']:
        print(get_winner('Rock', t))