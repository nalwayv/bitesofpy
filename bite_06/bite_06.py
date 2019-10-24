"""
Bite 6. PyBites Die Hard 

Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs
"""
from collections import Counter, namedtuple
import os
from typing import List, Iterator, Tuple
import re
# import urllib.request

# prep

tempfile = os.path.join(os.path.dirname(__file__), 'tmp', 'dirnames')
# urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code
def open_file() -> List[str]:
    """open_file
    
    Returns:
        list(str): file contents
    """
    content = None
    try:
        with open(os.path.abspath(tempfile)) as file:
            content = file.readlines()
    except FileNotFoundError as err:
        print("ERROR: {err}")
        return None
    return content


def gen_files() -> Iterator[Tuple[str, str, bool]]:
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """

    pattern = r"[/,]"
    check = re.compile(pattern)

    file_data = open_file()

    if file_data is None:
        raise Exception("error with file data 'dirnames'")

    d1 = []
    for data in file_data:
        dirnames_data = check.split(data)
        a, b, c = dirnames_data
        if c.strip() == 'True':
            d1.append((a, b, True))

    # generator
    n = len(d1)
    idx = 0
    while idx < n:
        yield d1[idx]
        idx += 1


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))

    Returns:
        Status (namedtuple): Status.user, Status.challenge
    """

    names = []
    challenges = []
    for gen in gen_files():
        a, b, _ = gen
        if b in IGNORE:
            continue
        names.append(b)
        challenges.append(a)

    # count
    users = Counter(names)
    popular_challenges = Counter(challenges)

    # data tuple
    most_user = users.most_common(1)[0]
    most_challenge = popular_challenges.most_common(1)[0]

    most_user_name = most_user[0]  # just the name not the count

    return Stats(user=most_user_name, challenge=most_challenge)
