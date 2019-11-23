""" 
Bite 83. At what time does PyBites live?
"""
from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt: datetime):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes
    """
    utc_dt = naive_utc_dt.replace(tzinfo=utc)
    dt_1 = AUSTRALIA.normalize(utc_dt.astimezone(AUSTRALIA))
    dt_2 = SPAIN.normalize(utc_dt.astimezone(SPAIN))
    return (dt_1, dt_2)


if __name__ == "__main__":
    naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)
    aus, spn = what_time_lives_pybites(naive_utc_dt)
    print(aus)
    print(spn)
