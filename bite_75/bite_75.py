"""
Bite 75. Parse Unix cal to a weekday mapping 
"""
from typing import Dict

april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

jan_1956 = """    January 1956
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""


def get_weekdays(calendar_output: str) -> Dict[int, str]:
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)
    """
    days = "Su Mo Tu We Th Fr Sa".split(" ")
    data = dict()

    for line in calendar_output.splitlines()[2:]:
        vals = [x for x in line.split(" ") if x != '']
        for week_day, month_day in zip(days, vals):
            data[int(month_day)] = week_day

    return data
