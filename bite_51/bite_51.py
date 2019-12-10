"""
Bite 51. When does Python 2 die on Planet Miller? 
"""
from datetime import datetime, timedelta

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
START_DATE_2 = BITE_CREATED_DT - timedelta(days=1000)

HOUR = 3600
DAY = HOUR * 24
YEAR = DAY * 365
MILLER_HOUR = YEAR * 7
MILLER_MIN = MILLER_HOUR / 60


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)
    """
    t1 = PY2_DEATH_DT - start_date
    return round(t1.total_seconds() / HOUR, 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)
    """
    t1 = PY2_DEATH_DT - start_date
    return round(t1.total_seconds() / MILLER_MIN, 2)


if __name__ == "__main__":
    print(py2_earth_hours_left())
    print(py2_miller_min_left())
    print("-" * 45)
    print(py2_earth_hours_left(START_DATE_2))
    print(py2_miller_min_left(START_DATE_2))
