""" 
Bite 144. Calculate the Number of Months Passed 
"""
from datetime import date

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def calc_months_passed(year, month, day):
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    _date = date(year, month, day)

    if _date < START_DATE:
        raise ValueError("date too low")

    if START_DATE == _date:
        return 0

    rd = relativedelta(_date, START_DATE)

    _d = 1 if rd.days % MIN_DAYS_TO_COUNT_AS_MONTH == 0 else 0

    return _d + rd.months + rd.years * MONTHS_PER_YEAR


if __name__ == "__main__":
    print(calc_months_passed(2018, 11, 1) == 0)
    print(calc_months_passed(2018, 11, 10) == 0)
    print(calc_months_passed(2018, 11, 11) == 1)
    print(calc_months_passed(2018, 12, 10) == 1)
    print(calc_months_passed(2018, 12, 11) == 2)
    print(calc_months_passed(2019, 12, 10) == 13)
    print(calc_months_passed(2019, 12, 11) == 14)

    try:
        calc_months_passed('a',10,1)
    except TypeError:
        print('type error')

    try:
        calc_months_passed(2018, 10, 1)
    except ValueError:
        print('value error')
