"""
Bite 125: Get the most recommended books
"""
from collections import Counter
from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"

# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/tribe-mentors-books.html')


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()

    # code here ...
    soup = BeautifulSoup(content, features='html.parser')

    names=[
        (atag.attrs.get('href'), atag.text) for atag in soup.findAll('a')
        if AMAZON in atag.attrs.get('href')
    ]

    return [title[1] for title,_ in Counter(names).most_common(limit)]


if __name__ == "__main__":
    books = get_top_books(load_page(), 10)
    for book in books:
        print(book)
