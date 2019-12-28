""" 
Bite 242. Zodiacal data parsing
"""
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
from urllib.request import urlretrieve
from typing import List
import pytest

from zodiac import (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")

@pytest.fixture(scope='module')
def signs() -> List["Sign"]:
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH, encoding='utf-8') as f:
        data = json.loads(f.read())
    return get_signs(data)


# write your pytest code here ...


def test_new_signs_are_signs(signs) -> None:
    for sign in signs:
        assert str(type(sign))[-6:-2] == "Sign"


def test_signs_are_mutually_compatible_are_in_compatible(signs) -> None:
    # if true does it actualy have it?
    for sign in signs:
        if signs_are_mutually_compatible(signs, sign.name, 'Leo'):
            assert 'Leo' in [c.strip() for c in sign.compatibility]


def test_most_famous_sign(signs) -> None:
    assert get_sign_with_most_famous_people(signs) == ('Scorpio', 35)
    assert get_sign_with_most_famous_people(signs[:1]) == ('Aries', 32)
    assert get_sign_with_most_famous_people(signs[:3]) == ('Gemini', 33)


def test_signs_are_mutually_compatible(signs) -> None:
    assert signs_are_mutually_compatible(signs, 'Scorpio', ' Gemini') == False
    assert signs_are_mutually_compatible(signs, 'Leo', ' Pisces') == False
    assert signs_are_mutually_compatible(signs, 'Gemini', ' Leo') == True


def test_get_sign_by_date(signs) -> None:
    PYBITES_BORN = datetime(year=2016, month=12, day=19)
    
    assert get_sign_by_date(signs, PYBITES_BORN) == 'Sagittarius'
    assert get_sign_by_date(signs,PYBITES_BORN + timedelta(days=100)) == 'Aries'
    assert get_sign_by_date(signs,PYBITES_BORN - timedelta(days=100)) == 'Virgo'


def test_get_sign_by_date_in_range(signs) -> None:
    sign = 'Scorpio'
    date_a = datetime(year=2016, month=10, day=23)
    date_b = datetime(year=2016, month=11, day=21)

    while date_a <= date_b:
        assert get_sign_by_date(signs, date_a) == sign
        date_a = date_a + timedelta(days=1)
    

