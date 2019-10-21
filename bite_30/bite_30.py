"""
Bite 30 Movie data analysis:
    get movie info from csv file and filter it for key info
"""
import os
import csv
from collections import namedtuple
from math import floor
from typing import List, Dict, Tuple

# CONSTS
FILE_PATH = os.path.join(os.path.dirname(__file__), "tmp", "movie_metadata.csv")
MIN_YEAR = 1960  # only movies made after
MIN_MOVIES = 4  # if director has more then min amount of movies in list

# TUPLES
Movie = namedtuple('Movie', 'title year score')


# FUNCS
def get_movies_by_director() -> Dict[str, List[Movie]]:
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple
    """
    movie_data = {}
    with open(os.path.abspath(FILE_PATH), newline='', encoding='utf-8') as in_file:
        for row in csv.DictReader(in_file):
            # keys
            name = row.get("director_name")
            title = row.get("movie_title")
            year = row.get("title_year")
            score = row.get("imdb_score")

            # convert
            int_year = 0
            if year:
                try:
                    int_year = int(year)
                except ValueError:
                    int_year = 0

            float_score = 0.0
            if score:
                try:
                    float_score = float(score)
                except ValueError:
                    float_score = 0.0

            # filter
            if int_year > MIN_YEAR:
                if name in movie_data:
                    movie = Movie(title=title,
                                  year=int_year,
                                  score=float_score)
                    movie_data[name].append(movie)

                else:
                    movie_data[name] = []
                    movie = Movie(title=title,
                                  year=int_year,
                                  score=float_score)
                    movie_data[name].append(movie)

    return movie_data


def calc_mean_score(movies: List[Movie]) -> float:
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place
    """
    return round(sum([m.score for m in movies]) / len(movies), 1)


def get_average_scores(directors: Dict[str, List[Movie]]) -> List[Tuple[str, float]]:
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES
    """
    res = []
    for director_name, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg_score = calc_mean_score(movies)
            info = (director_name, avg_score)
            res.append(info)

    return sorted(res, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    for movie in get_average_scores(get_movies_by_director())[:5]:
        print(movie)