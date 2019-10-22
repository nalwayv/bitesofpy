"""
Bite 38: Parse xml movie data
"""
import xml.etree.ElementTree as ET
from typing import List

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree() -> ET:
    """You probably want to use ET.fromstring

    Returns:
        xml.etree.ElementTree: xml tree
    """
    tree = ET.ElementTree(ET.fromstring(xmlstring))
    return tree


def get_movies() -> List[str]:
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    tree = get_tree()
    return [movie.get(key='title').strip() for movie in tree.findall('movie')]


def parse_time(time_string: str) -> int:
    """parse_time - parse time for this xml form's runtime key

    Args:
        time_string (str): string with digits
    
    Example:
        >>> parse_time('130 min')
        130

    Returns:
        int: min
    """
    start = 0
    end = 0
    n = len(time_string)
    p = 0
    while p < n:
        if not time_string[p].isdigit():
            break
        p += 1
    end = p
    return int(time_string[start:end])


def get_movie_longest_runtime() -> str:
    """Call get_tree again and return the movie title for the movie with the longest
       runtime in minutes, for latter consider adding a _get_runtime helper"""
    tree = get_tree()

    max_time = -1
    max_title = ""

    for movie in tree.findall('movie'):
        run_time = movie.get(key='runtime')
        movie_title = movie.get(key='title')
        int_time = parse_time(run_time)

        if int_time > max_time:
            max_time = int_time
            max_title = movie_title

    return max_title
