"""
Bite 135. Sort a list of book object
"""

from collections import namedtuple
from datetime import datetime
from operator import attrgetter
from typing import List

Book = namedtuple('Book', 'title authors pages published')

books = [
    Book(title="Python Interviews",
         authors="Michael Driscoll",
         pages=366,
         published="2018-02-28"),
    Book(title="Python Cookbook",
         authors="David Beazley, Brian K. Jones",
         pages=706,
         published="2013-05-10"),
    Book(title="The Quick Python Book",
         authors="Naomi Ceder",
         pages=362,
         published="2010-01-15"),
    Book(title="Fluent Python",
         authors="Luciano Ramalho",
         pages=792,
         published="2015-07-30"),
    Book(title="Automate the Boring Stuff with Python",
         authors="Al Sweigart",
         pages=504,
         published="2015-04-14"),
]

# all functions return books sorted in ascending order.


def sort_books_by_len_of_title(books=books) -> List[Book]:
    """sort_books_by_len_of_title

    Expected last book in list:
    Automate the Boring Stuff with Python

    Paramiters
    ----------
    books : List[Book]

    Returns
    -------
    List[Book] :
        list of namedtuples called Book
    """
    return sorted(books, key=lambda book: len(book.title))


def sort_books_by_first_authors_last_name(books=books) -> List[Book]:
    """sort_books_by_first_authors_last_name

    Expected last book in list:
    Automate the Boring Stuff with Python

    Paramiters
    ----------
    books : List[Book]

    Returns
    -------
    List[Book] :
        list of namedtuples called Book
    """
    def first_author_last_name(book: Book) -> str:
        # if there are more then one author split via , and get first
        author = book.authors.split(",")[0]
        return author.split(" ")[1]

    return sorted(books, key=first_author_last_name)


def sort_books_by_number_of_page(books=books) -> List[Book]:
    """sort_books_by_number_of_page

    Expected last book in list:
    Fluent Python

    Paramiters
    ----------
    books : list

    Returns
    -------
    List[Book] :
        list of namedtuples called Book
    """
    return sorted(books, key=lambda book: book.pages)


def sort_books_by_published_date(books=books) -> List[Book]:
    """sort_books_by_published_date

    Expected last book in list:
    Python Interviews

    Paramiters
    ----------
    books : List[Book]

    Returns
    -------
    List[Book] :
        list of namedtuples called Book
    """
    def date_it(book: Book) -> datetime:
        try:
            # book.published = '1990-1-1'
            year, month, day = book.published.split("-")
            return datetime(int(year), int(month), int(day))
        except TypeError:
            raise TypeError()

    return sorted(books, key=date_it)


if __name__ == "__main__":
    for book in sort_books_by_published_date(books):
        print(book)