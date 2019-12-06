import csv
import re
from collections import Counter, defaultdict

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_words(msg: str) -> list:
    ok = re.findall(r"[^\n ]+", msg)
    if ok:
        return ok
    return []


def cleanup_csv_text(content: str) -> list:
    lines = content.splitlines()
    start = 1
    n = len(lines)
    p1 = 1
    clusters = [lines[0]]

    while start < n:
        p2 = p1
        ll = []
        while p2 < n:
            if len(lines[p2]) == 1:  # line with single "
                break
            ll.append(lines[p2])
            p2 += 1

        start = p1
        if ll:
            if start == 0:
                clusters.append(''.join(ll))
            clusters.append(''.join(ll) + '"')
        p1 = p2 + 1

    return clusters


def get_num_words_spoken_by_character_per_episode(content: str) -> dict:
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken
    """
    clusters = cleanup_csv_text(content)

    data = defaultdict(Counter)

    for row in csv.DictReader(clusters, delimiter=',', quotechar='"'):
        character = row['Character']
        episode = row['Episode']
        text = row['Line']
        words = get_words(text)

        data[character][episode] += len(words)

    return data
