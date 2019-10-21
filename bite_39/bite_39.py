"""
Bite_39
"""

import os
import re
from datetime import datetime, timedelta
from typing import List

FILE_PATH = os.path.join(os.path.dirname(__file__), 'tmp', 'data.txt')


def open_file() -> str:
    """open_file
    
    Returns:
        str: data from course_timings.txt
    """
    lines = None
    abs_path = os.path.abspath(FILE_PATH)

    try:
        with open(abs_path) as file:
            lines = file.read()
    except FileNotFoundError as err:
        raise FileExistsError(err)

    return lines


def get_all_timestamps() -> List[str]:
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

    Returns:
        List[str] - a list of MM:SS timestamps
    """
    data = open_file()
    pattern = r"([0-9]{1,}:[0-9]{1,})"
    check = re.compile(pattern)
    time_stamps: List[str] = check.findall(data)

    return time_stamps


def calc_total_course_duration(timestamps) -> str:
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS
    Args:
        timestamps(List[str])

    Returns:
        str: datetime.time in string format
    
    """
    time_str = "%M:%S"
    dates: List[datetime] = [
        datetime.strptime(stamp, time_str) for stamp in timestamps
    ]

    total_date = dates[0]
    for date in dates[1:]:
        total_date += timedelta(hours=date.hour,
                                minutes=date.minute,
                                seconds=date.second)

    return str(total_date.time())
