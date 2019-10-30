""" 
Bite 55:
"""
from collections import namedtuple
from typing import List

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games() -> List[Game]:
    """get_games

    Parses Steam's RSS feed and returns a list of Game namedtuples

    Returns:
    --------
        List[Game]: list of Game namedtules
    """
    raw_data: "FeedParserDict" = feedparser.parse(FEED_URL)
    names = [item['title'] for item in raw_data.entries]
    links = [item['link'] for item in raw_data.entries]
    return [
        Game(title=game_name, link=game_link)
        for game_name, game_link in list(zip(names, links))
    ]


if __name__ == "__main__":
    for game in get_games():
        print(game)
