"""
Bite 28. Converting date strings to datetimes
"""
import collections
from datetime import datetime
import os
import re
from typing import List

RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = 'tmp'


def _get_dates() -> List[str]:
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""

    local = os.path.join(os.path.dirname(__file__), TMP, RSS_FEED)
    data = None
    with open(local) as f:
        data = PUB_DATE.findall(f.read())
    return data


def convert_to_datetime(date_str: str) -> datetime:
    """Receives a date str and convert it into a datetime object
    """
    # 'Sun, 07 Jan 2018 12:00:00 +0100'
    # year=2018, day=1, month=1, hour=12, min=0
    months_str = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ")
    months = [(idx + 1, month) for idx, month in enumerate(months_str)]

    data = date_str.replace(",", "").split(" ")

    # Year
    year = int(data[3])
    # Day
    day_of_month = int(data[1])

    # Month
    month_of_year = -1
    for idx, month_name in months:
        if month_name == data[2]:
            month_of_year = idx
            break
    # Time
    time = data[4].split(":")
    time_hour = int(time[0])
    time_min = int(time[1])

    return datetime(year=year,
                    month=month_of_year,
                    day=day_of_month,
                    hour=time_hour,
                    minute=time_min)


def get_month_most_posts(dates: List[datetime]) -> str:
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most
    """
    date_fmt = "%Y-%m"
    count = collections.Counter([date.strftime(date_fmt) for date in dates])
    return count.most_common()[0][0]
