""" 
Bite 247. Mocking a standard library function
"""
from itertools import islice
from unittest.mock import Mock, patch
import pytest
import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def random_sample_mocks(rand):
    return Mock(side_effect=(v for v in rand))


@patch(
    "color.sample",
    random_sample_mocks([
        (255, 255, 255),    # white
        (255, 0, 0),        # red
        (0, 255, 0),        # green
        (0, 0, 255),        # blue
        (0, 0, 0)           # black
    ]))
def test_gen_hex_color(gen):
    values = list(islice(gen, 5))
    expected = ['#FFFFFF', '#FF0000', '#00FF00', '#0000FF', '#000000']
    assert values == expected
