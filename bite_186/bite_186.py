"""
Bite 186. Calculate number of books to have read at date ...
"""
from datetime import datetime
from math import floor
from dateutil.parser import parse

# work with a static date for tests, real use = datetime.now()
NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52


def get_number_books_read(books_per_year_goal: int,
                          at_date: str = None) -> int:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    at_date = at_date or str(NOW)
    # TODOs

    # 1. use dateutil's parse to convert at_date into a
    # datetime object
    current_date = parse(at_date)

    # 2. check books_per_year_goal and at_date and raise
    # a ValueError if goal <= 0 or at_date in the past (< NOW)
    if books_per_year_goal <= 0:
        raise ValueError('books_per_year_goal cant be a negative number')

    if current_date < NOW:
        raise ValueError('at_date cant be less then current NOW date')

    # 3. check the offset of at_date in the year ("week of the
    # year" - e.g. whatweekisit.com) and based on the books_per_year_goal,
    # calculate the number of books that should have been read / completed

    iso_month = current_date.isocalendar()[1]
    cal = (iso_month / WEEKS_PER_YEAR) * books_per_year_goal

    return floor(cal)


if __name__ == "__main__":
    tests = [
        (52, 'Sunday, March 18th, 2019', 12),
        (52, 'Sunday, March 25th, 2019', 13),
        (52, 'April 2nd, 2019', 14),
        (100, 'Sunday, March 18th, 2019', 23),
        (100, 'Sunday, March 25th, 2019', 25),
        (100, '2019-04-02', 26),
        (52, None, 11),
        (100, None, 21),
        (100, '11-20-2019', 90),
        (100, '5/20/2019', 40)
    ]

    for goal, date_str, expected in tests:
        result = (get_number_books_read(goal, date_str) == expected)
        print(result)
