"""
Bite 147. 100 WEEKDays of Code Date Range
"""

from datetime import date
from dateutil.rrule import rrule, MO, TU, WE, TH, FR, DAILY
from typing import List

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY) -> List[date]:
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays
    """

    data = list(
        rrule(DAILY,
              count=100,
              byweekday=(MO, TU, WE, TH, FR),
              dtstart=start_date))

    return [d.date() for d in data]


if __name__ == '__main__':
    days = get_hundred_weekdays(TODAY)
    print(TODAY)
    print(days[0] == TODAY)
    print(days[-1] == date(2019, 4, 17))
    print(days[1] == date(2018, 11, 30))
    print(days[2] == date(2018, 12, 3))
    fri_index = days.index(date(2019, 1, 18))
    print(days[fri_index + 1] == date(2019, 1, 21))
