""" 
Bite 175. Find missing dates
"""
from datetime import date
from typing import List


def get_missing_dates(dates: List[date]):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    year = dates[0].year
    month = dates[0].month

    day_range = list(range(min(dates).day, max(dates).day))
    days = [d.day for d in dates]

    res = [
        date(year=year, month=month, day=num) for num in day_range
        if num not in days
    ]

    return res


if __name__ == "__main__":
    date_range = [date(year=2019, month=2, day=n) for n in range(1, 11, 2)]
    print(get_missing_dates(date_range))
