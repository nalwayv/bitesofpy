"""
Bite 97: BeautifulSoup II - scrape US holidays

using BeautifulSoup 4.8.1
"""

import os
from collections import defaultdict
from typing import Dict, List

from bs4 import BeautifulSoup

# from urllib.request import urlretrieve

# prep data
holidays_page = os.path.join(os.path.dirname(__file__), 'tmp',
                             'us_holidays.php')
# urlretrieve('https://bit.ly/2LG098I', holidays_page)

# holidays = defaultdict(list)


def open_file() -> str:
    content = None
    with open(holidays_page) as f:
        content = f.read()
    return content


def get_us_bank_holidays(content) -> Dict[str, List[str]]:
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays

    Returns:
        dict(str, list[str]): 
    """
    soup = BeautifulSoup(content, features="html.parser")

    times = [
        time.text
        for time in soup.findAll('time', attrs={'itemprop': 'startDate'})
    ]

    holidays = [
        holiday.text for holiday in soup.findAll('a', attrs={'rel': 'tooltip'})
    ]

    months = {f"0{i}" if i < 10 else f"{i}": [] for i in range(1, 13)}

    for bank_days in zip(holidays, times):
        bh, time = bank_days
        _, month, _ = time.split("-")
        months[month.strip()].append(bh.strip())

    # filter for months with holidays
    return {key: val for key, val in months.items() if val}
