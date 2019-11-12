"""
Bite 130. Analyze some basic Car Data
"""
from collections import Counter
import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'tmp', 'data.json')


def open_file() -> json:
    data = None
    with open(os.path.abspath(FILE_PATH)) as file:
        data = json.load(file)
    return data


# your turn:
def most_prolific_automaker(year) -> str:
    """Given year 'year' return the automaker that released
       the highest number of new car models
    """
    automaker = Counter([
        y['automaker'] for y in open_file() if y['year'] == year
    ]).most_common()[0][0]

    return automaker


def get_models(automaker, year) -> set:
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)
    """
    models = {
        d['model']
        for d in open_file()
        if d['automaker'] == automaker and d['year'] == year
    }

    return models
