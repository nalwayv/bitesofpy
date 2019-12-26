"""
Bite 16. PyBites date generator
"""

from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)
ONE_YEAR = timedelta(days=365)
ONE_HUNDRED_DAYS = timedelta(days=100)


def gen_special_pybites_dates():
    pybites_born = PYBITES_BORN
    future_year = pybites_born + ONE_YEAR

    while True:
        pybites_born += ONE_HUNDRED_DAYS
        if pybites_born > future_year:
            yield future_year
            future_year += ONE_YEAR

        yield pybites_born


if __name__ == "__main__":
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))
    expected = [
        datetime(2017, 3, 29, 0, 0),
        datetime(2017, 7, 7, 0, 0),
        datetime(2017, 10, 15, 0, 0),
        datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
        datetime(2018, 1, 23, 0, 0),
        datetime(2018, 5, 3, 0, 0),
        datetime(2018, 8, 11, 0, 0),
        datetime(2018, 11, 19, 0, 0),
        datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
        datetime(2019, 2, 27, 0, 0)
    ]
    print(dates == expected)
