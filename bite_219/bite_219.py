""" 
Bite 219. Bite notification planner
"""
from datetime import date, timedelta
from itertools import islice

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    while True:
        start_date = start_date + timedelta(days=num_days)
        for _ in range(num_bites):
            yield start_date


if __name__ == "__main__":
    for v in list(islice(gen_bite_planning(num_days=2), 10)):
        print(v)