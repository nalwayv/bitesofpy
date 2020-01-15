"""
Bite 141. Primitive date format inferrer
"""
from enum import Enum
from datetime import datetime
from collections import Counter
from typing import List, Dict


class DateFormat(Enum):
    DDMMYYYY = 0
    DDMMYY = 1
    YYMMDD = 2
    MMDDYY = 3
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, idx=None):
        d_parse_formats = ["%d.%m.%Y", "%d/%m/%y", "%y/%m/%d", "%m/%d/%y"]
        if idx is None:
            return d_parse_formats
        if 0 <= idx <= len(d_parse_formats):
            return d_parse_formats[idx]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt)  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def str_dates(dates_data: Dict[str, List[DateFormat]], format_type: DateFormat,
              str_format: str) -> List[str]:
    res = []
    for key, val in dates_data.items():
        # is DateFormat within dates_dates array
        if format_type in val:
            new_date = str(datetime.strptime(key, str_format).date())
            res.append(new_date)
        else:
            res.append("Invalid")
    return res


def get_dates(dates: List[str]):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """

    date_data: Dict[str, List[DateFormat]] = dict()
    nums: List[int] = []

    # USE ENUM TO CHECK DATES
    for date in dates:
        res: List[DateFormat] = _maybe_DateFormats(date)
        # print(res)
        for val in res:
            nums.append(val.value)
        date_data[date] = res

    # MOST COMMON
    count_results = Counter(nums).most_common()
    most_common = count_results[0][0]

    # TOO MANY FORMATS
    if all([len(d) == 3 for d in date_data.values()]):
        raise InfDateFmtError

    # FORMAT
    for date_format in DateFormat:
        if date_format == DateFormat.NONPARSABLE:
            raise InfDateFmtError

        if date_format.value == most_common:
            fmt_str = None
            if date_format.name == "DDMMYY":
                fmt_str = "%d/%m/%y"

            elif date_format.name == "MMDDYY":
                fmt_str = "%m/%d/%y"

            elif date_format.name == "YYMMDD":
                fmt_str = "%y/%m/%d"

            elif date_format.name == "DDMMYYYY":
                fmt_str = "%d.%m.%Y"

            return str_dates(date_data, date_format, fmt_str)

    return []


if __name__ == "__main__":

    dates = [
        "12/16/30", "16.03.1954", "97/07/26", "04.04.1931", "01.08.1907",
        "02/02/29", "73/03/08", "06.07.1955", "10.09.1977", "18.03.1943",
        "30/11/24", "08.01.1951"
    ]
    results = [
        "Invalid", "1954-03-16", "Invalid", "1931-04-04", "1907-08-01",
        "Invalid", "Invalid", "1955-07-06", "1977-09-10", "1943-03-18",
        "Invalid", "1951-01-08"
    ]
    try:
        values = get_dates(dates)
        print(values == results)
    except InfDateFmtError:
        print("inf error found")