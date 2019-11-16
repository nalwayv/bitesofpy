import calendar
from datetime import date
from typing import Optional

def weekday_of_birth_date(date: date) -> Optional[str]:
    """Takes a date object and returns the corresponding weekday string"""
    for idx, day in [(idx, day) for idx, day in enumerate(list(calendar.day_name))]:
        if idx == date.weekday():
            return day
    return None


if __name__ == "__main__":
    leonardo_dicaprio = weekday_of_birth_date(date(1974, 11, 11))
    print(leonardo_dicaprio)

    will_smith = weekday_of_birth_date(date(1968, 9, 25))
    print(will_smith)

    robert_downey = weekday_of_birth_date(date(1965, 4, 4))
    print(robert_downey)