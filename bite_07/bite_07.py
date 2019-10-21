"""
Bite 07
"""
import os
import re
from datetime import datetime

FILE_DIR = os.path.join(os.path.abspath(__file__), "..", "tmp", "log.txt")


def open_file():
    """open file
    """
    text = []
    try:
        with open(FILE_DIR, "r") as file:
            text = file.readlines()

    except FileNotFoundError as err:
        print(f"ERROR: {err}")
        return []

    return text


def _get_time_stamp(text: str) -> list:
    pattern_text_init = r"([0-9]{4}-[0-9]{2}-[0-9\w]{5}:[0-9]{2}:[0-9]{2})"
    pattern = re.compile(pattern_text_init)
    matches = pattern.findall(text)
    return matches


def _get_time_events(text: str) -> list:
    pattern_text_init = r"([0-9]{4}-[0-9]{2}-[0-9\w]{5}:[0-9]{2}:[0-9]{2}.+Shutdown.initiated)"
    pattern = re.compile(pattern_text_init)
    matches = pattern.findall(text)
    return matches


def convert_to_datetime(line: str):
    """convert_to_datetime

    convert string date fmt ro datetime obj

    Args:
        line (str): a str date format

    Examples:
        >>> convert_to_datetime("2014-07-03T23:27:51")
        datetime(2014, 07, 03, 23, 27, 51)

    Raises:
        ValueError: if fails to convert line tyo a datetime object

    Returns:
        datetime.datetime: a new datetime obj
    """
    time_stamp = _get_time_stamp(line)[0]

    date_fmt_str = "%Y-%m-%dT%H:%M:%S"
    fmt_date = None

    try:
        fmt_date = datetime.strptime(time_stamp, date_fmt_str)
    except ValueError as err:
        raise ValueError(err)

    return fmt_date


def time_between_shutdowns(loglines: list):
    """time_between_shutdowns

    finds to two shutdown initiated logs and gets the time between them

    Args:
        loglines (list[str]): a list of stings

    Retruns:
        datetime.datetime: a new datetime obj with the time difference
    """
    text = " ".join(loglines)
    matches = _get_time_events(text)
    stamps = [
        convert_to_datetime(_get_time_stamp(stamp)[0]) for stamp in matches
    ]
    return stamps[1] - stamps[0]


# if __name__ == "__main__":
#     # - sep
#     res = convert_to_datetime("ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file")
#     print(res)

#     # - time diff
#     text_lines = open_file()
#     output = time_between_shutdowns(text_lines)
#     print(output)
