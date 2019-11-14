import glob
import json
import os
import re
from typing import List,Optional

# from urllib.request import urlretrieve

# BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = 'tmp'

# little bit of prework (yes working on pip installables ...)
# for movie in MOVIES:
#     fname = f'{movie}.json'
#     remote = os.path.join(BASE_URL, fname)
#     local = os.path.join(TMP, fname)
#     urlretrieve(remote, local)

FILE_PATH = os.path.join(os.path.dirname(__file__), TMP, '*json')
files = glob.glob(os.path.abspath(FILE_PATH))


def get_movie_data(files: List[str]) -> List[dict]:
    """open_files
    
    Returns
    -------
    list : (json_dict)
        list of json_dict objects
    """
    jsons = []
    for file in files:
        with open(file) as _file:
            data = json.load(_file)
        jsons.append(data)
    return jsons


def get_single_comedy(movies:List[dict])->Optional[str]:
    """get_single_comedy
    
    Parameters
    ----------
    movies : List[dict]
        list of movie dict objects
    
    Returns
    -------
    Optional[str]
        ever a string or None
    """
    for movie in movies:
        if 'Comedy' in movie['Genre']:
            return movie['Title']
    return None


def get_movie_most_nominations(movies:List[dict]) -> str:
    """get_movie_most_nominations
    
    Parameters
    ----------
    movies : List[dict]
        list of move dict objects
    
    Returns
    -------
    str
        movies title with most nominations
    """
    pattern = r'\d*\s(?=nominations.)'

    results = []
    for movie in movies:
        title = movie['Title']
        number = int(re.findall(pattern, movie['Awards'])[0].strip())
        results.append((title, number))

    top = max(results, key=lambda movie: movie[1])
    return top[0]


def get_movie_longest_runtime(movies):
    pattern = r'\d*\s(?=min)'
    results = []
    for movie in movies:
        title = movie['Title']
        number = int(re.findall(pattern, movie['Runtime'])[0].strip())
        results.append((title, number))

    top = max(results, key=lambda movie: movie[1])
    return top[0]


if __name__ == "__main__":
    movies = get_movie_data(files)

    print('-' * 45)
    movie_most_awards = get_movie_most_nominations(movies)
    print(movie_most_awards)
    print('-' * 45)
    single_comedy = get_single_comedy(movies)
    print(single_comedy)
    print('-' * 45)
    top_runtime = get_movie_longest_runtime(movies)
    print(top_runtime)
    print('-' * 45)
