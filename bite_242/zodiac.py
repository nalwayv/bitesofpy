import calendar
from collections import namedtuple
from datetime import datetime
from operator import itemgetter
from typing import List

Sign = namedtuple('Sign', 'name compatibility famous_people sun_dates')


def get_signs(data: list) -> List[Sign]:
    ret = []
    for sign in data:
        name = sign['name']
        compatibility = sign['compatibility']
        famous_people = sign['famous_people']
        sun_dates = sign['sun_dates']
        sign = Sign(name, compatibility, famous_people, sun_dates)
        ret.append(
            sign
        )
    return ret


def get_sign_with_most_famous_people(signs: list):
    """Get the sign with the most famous people associated"""
    famous_people = [
        (s.name, len(s.famous_people)) for s in signs
    ]
    return max(famous_people, key=itemgetter(1))


def signs_are_mutually_compatible(signs: list, sign1: str, sign2: str) -> bool:
    """Given 2 signs return if they are compatible (compatibility field)"""
    ret = False
    for sign in signs:
        if sign.name == sign1:
            ret = sign2 in sign.compatibility
        elif sign.name == sign2:
            ret = sign1 in sign.compatibility
    return ret


def _get_month_int(month):
    month_mapping = dict((v, k) for k, v in
                         enumerate(calendar.month_abbr))
    return int(month_mapping[month[:3]])


def get_sign_by_date(signs: list, date: datetime) -> str:
    """Given a date return the right sign (sun_dates field)"""
    month = date.month
    day = date.day

    for sign in signs:
        start, end = sign.sun_dates
        start_month, start_day = start.split()
        end_month, end_day = end.split()
        if(month == _get_month_int(start_month) and day >= int(start_day)
           or month == _get_month_int(end_month) and day <= int(end_day)):
            return sign.name