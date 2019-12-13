"""
Bite 229. Scrape best programming books
"""
from pathlib import Path
from bs4 import BeautifulSoup

from dataclasses import dataclass
from typing import List

tmp = Path("./tmp")
html_file = tmp / "books.html"


@dataclass
class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    title: str
    author: str
    year: int
    rank: int
    rating: float

    def __str__(self):
        str_rank = str(self.rank)
        n = len(str_rank)
        zeros = '0' * (3 - n)
        return f"[{zeros}{str_rank}] {self.title} ({self.year})\n{' '*6}{self.author} {float(self.rating)}"

    def __getitem__(self, item):
        data = {
            'title': self.title.lower(),
            'rating': -self.rating,
            'year': self.year,
            'author': self.author
        }
        return data.get(item)


def _get_soup(file) -> BeautifulSoup:
    with file.open(encoding='utf8') as html_source:
        return BeautifulSoup(html_source, "html.parser")


def display_books(books: List[Book], limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    if year:
        for res in [b for b in books if b.year >= year][:limit]:
            print(res)
    else:
        for res in books[:limit]:
            print(res)


def name_order(name: str) -> str:
    if name[:3] == 'Dr.':
        new_name = name[3:].strip()
        name = new_name

    values = name.split(" ")

    if len(values) == 2:
        first, last = values
        name = ', '.join([last, first])

    if len(values) == 3:
        first, middle, last = values
        new_last = ' '.join([first, middle])
        name = ', '.join([last, new_last])

    return name


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    books = []

    soup: BeautifulSoup = _get_soup(html_file)

    book_table = soup.findAll('div', attrs={'class': 'book accepted normal'})
    if book_table:
        b: BeautifulSoup = None

        for b in book_table:
            title = b.find('h2', attrs={'class': 'main'})
            author = b.find('h3', attrs={'class': 'authors'}).findNext('a')
            year = b.find('span', attrs={'class': 'date'})
            rank = b.find('div', attrs={'class': 'rank'})
            rating = b.find('span', attrs={'class': 'our-rating'})

            if all([title, author, year, rank, rating]):
                if 'python' in title.text.lower():

                    new_name_order = name_order(author.text)

                    book = Book(title.text, 
                                new_name_order,
                                int(year.text.strip(' | ')), 
                                int(rank.text),
                                float(rating.text))

                    books.append(book)

    sb = sorted(books,
                key=lambda x:
                (x['rating'], x['year'], x['title'], x['author']))

    for idx, b in enumerate(sb):
        b.rank = idx + 1

    return sb


def main():
    """If done correctly, the previous function call should display the
    output below.
    """
    books = load_data()
    display_books(books, limit=40)


if __name__ == "__main__":
    main()
