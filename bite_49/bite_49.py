"""
Bite 49: Scrape Packt's html with BeautifulSoup
"""
from collections import namedtuple

import requests
from bs4 import BeautifulSoup as Soup

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text
BOOK_SOUP = Soup(CONTENT, features="html.parser")

Book = namedtuple('Book', 'title description image link')


def get_book() -> Book:
    """get_book
    
    make a Soup object, parse the relevant html sections, and return a Book namedtuple
    
    Returns:
    -------
        Book (namedtuple) = namedtuple with book information
    """
    book_content = BOOK_SOUP.select_one('div#deal-of-the-day')

    link = book_content.select_one('a')
    img = link.findNext('noscript').select_one('img')
    title = book_content.findNext('h2')
    descr = book_content.select_one('.dotd-title').findNext('div')

    return Book(title=title.text.strip(),
                description=descr.text.strip(),
                image=img.attrs.get('src').strip(),
                link=link.attrs.get('href').strip())
