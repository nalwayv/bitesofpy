""" 
Bite 73. Organize a meeting between timezones (pytz)
"""
import pytz
from datetime import datetime, timedelta
from typing import List

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)



def within_schedule(utc: datetime, *timezones: List[str]) -> bool:
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)
    """
    if not all([t in TIMEZONES for t in timezones]):
        raise ValueError

    seconds_in_hour = 60 * 60
    results = []

    utc_tz = pytz.timezone('UTC')
    for timezone in timezones:
        current_tz = pytz.timezone(timezone)

        v1 = utc_tz.localize(utc)

        v2 = current_tz.localize(utc)

        hours = abs((v1 - v2).total_seconds()) / seconds_in_hour

        # NOTE: update time and check if hour is within MEETING_HOURS
        if v1 > v2:
            diff = v1 + timedelta(hours=hours)

            if diff.hour in MEETING_HOURS:
                results.append(True)
            else:
                results.append(False)
        else:
            diff = v1 - timedelta(hours=hours)

            if diff.hour in MEETING_HOURS:
                results.append(True)
            else:
                results.append(False)

    return all(results)

if __name__ == "__main__":

    tests = [(datetime(2018, 4, 18, 13, 28),
              ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago'], False),
             (datetime(2018, 4, 18, 12, 28),
              ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago'], True),
             (datetime(2018, 10, 18, 12, 28),
              ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago'], False),
             (datetime(2018, 4, 18, 6, 45),
              ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago'], False)]
    for dt, tz, expected in tests:
        print(within_schedule(dt, *tz) == expected)

    try:
        dt = datetime(2018, 4, 18, 12, 28)
        timezones = ['Europe/Madrid', 'bogus']
        within_schedule(dt, *timezones)
    except ValueError:
        print('caught value_error')