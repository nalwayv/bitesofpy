from datetime import datetime, timedelta, date
import re
from typing import List, Tuple

TODAY = date(2018, 11, 12)

DATA = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
"""


def extract_dates(data) -> List[date]:
    """Extract unique dates from DB table representation as shown in Bite"""
    pattern = re.compile('\d+-\d+-\d+', re.MULTILINE)
    dates = pattern.findall(data)

    if dates:
        result = []
        for da in dates:
            y, m, d = da.split("-")
            new_date = date(year=int(y), month=int(m), day=int(d))
            if new_date not in result:
                result.append(new_date)

        return result
    return []


def calculate_streak(dates: List[date]) -> int:
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    if not dates:
        return 0

    sorted_dates = sorted(dates, reverse=True)
    current = TODAY
    streak = 0
    for date in sorted_dates:
        if date == current or current - date == timedelta(days=1):
            streak += 1
            current = date
        else:
            break

    return streak


if __name__ == "__main__":
    dates = extract_dates(DATA)
    streak = calculate_streak(dates)
    print(f"STREAK: {streak}")