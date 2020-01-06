"""  
Bite 197. What date is Mother's Day celebrated?
"""
from datetime import date
import calendar


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""

    may = calendar.monthcalendar(year, 5)
    return date(year=year, month=5, day=may[1][calendar.SUNDAY])


if __name__ == "__main__":
    tests = [(2014, date(2014, 5, 11)), (2015, date(2015, 5, 10)),
             (2016, date(2016, 5, 8)), (2017, date(2017, 5, 14)),
             (2018, date(2018, 5, 13)), (2019, date(2019, 5, 12)),
             (2020, date(2020, 5, 10)), (2021, date(2021, 5, 9)),
             (2022, date(2022, 5, 8)), (2023, date(2023, 5, 14)),
             (2024, date(2024, 5, 12))]

    for year, expected in tests:
        print(get_mothers_day_date(year) == expected)