"""
Bite 178. Parse PyBites blog git commit log
"""
import os
import re
from collections import Counter, defaultdict
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.path.dirname(__file__), 'tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    data = defaultdict(int)
    commit_file = None

    # file
    with open(commit_log) as file:
        commit_file = file.read()

    for line in commit_file.splitlines():

        ok_date = re.findall(r'^Date:\s+([^+-]+)', line)
        ok_num = re.findall(
            r'\d+.insertions|\d+.deletions|\d+.insertion|\d+.deletion', line)

        if ok_date and ok_num:
            date = parse(ok_date[0].strip())
            date_str = YEAR_MONTH.format(y=date.year, m=date.month)
            v1 = sum([int(v.split(" ")[0].strip()) for v in ok_num])

            data[date_str] += v1

    if year is None:
        res = Counter(data).most_common()
        return (res[-1][0], res[0][0])

    res = Counter({k: v
                   for k, v in data.items() if str(year) in k}).most_common()
    return (res[-1][0], res[0][0])
