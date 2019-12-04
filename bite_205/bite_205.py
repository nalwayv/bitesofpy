"""
Bite 205. Female speakers @ Pycon US
"""
from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

from typing import List

TMP = Path('./tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

# if not PYCON_HTML.exists():
#     urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None) -> List[str]:
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """

    tables = soup.select('table.calendar>tbody')  # select both tables

    first_names = []

    for table in tables:
        for span in table.findAll('span', attrs={'class': 'speaker'}):
            names = span.text.strip()
            if ',' in names:
                for name in names.split(','):
                    first_name = name.strip().split(" ")[0]
                    first_names.append(first_name)
            elif '/' in names:
                for name in names.split('/'):
                    first_name = name.strip().split(" ")[0]
                    first_names.append(first_name)
            else:
                first_name = names.split(" ")[0]
                first_names.append(first_name)

    return first_names


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""

    check_gender = gender.Detector()

    fems = 0
    for name in first_names:
        gen = check_gender.get_gender(name)
        if gen in ['female', 'mostly_female']:
            fems += 1

    return round(fems * 100 / len(first_names), 2)


if __name__ == "__main__":
    print('foo')
    soup = _get_soup()
    first_names = get_pycon_speaker_first_names(soup)
    get_percentage_of_female_speakers(first_names)