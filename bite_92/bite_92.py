""" 
Bite 92. Humanize a datetime
"""
from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()

MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60

TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2 * MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2 * HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2 * DAY, 'yesterday', None),
)


def pretty_date(date: datetime):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS
    """
    if not isinstance(date, datetime):
        raise ValueError("not a datetime")
    if date > NOW:
        raise ValueError("date if bigger then NOW")

    time = NOW - date
    ts = time.total_seconds()

    for time_offset in TIME_OFFSETS:
        offset = (ts / time_offset.offset) * time_offset.offset

        if offset < time_offset.offset:
            if time_offset.divider:
                return time_offset.date_str.format(int(offset / time_offset.divider))
            else:
                return time_offset.date_str.format(int(offset))

    return date.strftime('%m/%d/%y')


if __name__ == "__main__":
    tests = [
        NOW - timedelta(seconds=1), NOW - timedelta(seconds=9),
        NOW - timedelta(seconds=10), NOW - timedelta(seconds=59),
        NOW - timedelta(minutes=1), NOW - timedelta(minutes=1, seconds=40),
        NOW - timedelta(minutes=2), NOW - timedelta(minutes=59),
        NOW - timedelta(hours=1), NOW - timedelta(hours=2),
        NOW - timedelta(hours=23), NOW - timedelta(hours=24),
        NOW - timedelta(hours=47), NOW - timedelta(days=1),
        NOW - timedelta(days=2)
    ]
    for t in tests:
        print(pretty_date(t))
        print("-" * 45)

    try:
        pretty_date(123)
    except ValueError as err:
        print(err.args[0])