""" 
Bite 151. Contemporary Composers
"""
from collections import namedtuple
from datetime import datetime, date
from typing import List, Dict

Composer = namedtuple('Composer', 'name born died')
Opera = namedtuple('Opera', 'author play date')

composers: Dict[str, Composer] = {
    "beethoven":
    Composer("Ludwig van Beethoven", "17 December 1770", "26 March 1827"),
    "wagner":
    Composer("Richard Wagner", "22 May 1813", "13 February 1883"),
    "verdi":
    Composer("Giuseppe Verdi", "9 October 1813", "27 January 1901"),
    "mozart":
    Composer("Wolfgang Amadeus Mozart", "27 January 1756", "5 December 1791"),
}

operas: List[Opera] = [
    Opera("mozart", "Apollo and Hyacinth", "13 May 1767"),
    Opera("mozart", "Marriage of Figaro", "1 May 1786"),
    Opera("mozart", "Don Giovanni", "29 October 1787"),
    Opera("mozart", "Così fan tutte", "6 January 1790"),
    Opera("mozart", "The Clemency of Titus", "6 September 1791"),
    Opera("mozart", "The Magic Flute", "30 September 1791"),
    Opera("wagner", "The Fairies", "29 June 1888"),
    Opera("wagner", "Rienzi", "20 October 1842"),
    Opera("wagner", "The Flying Dutchman", "2 January 1843"),
    Opera("wagner", "Tannhäuser", "19 October 1845"),
    Opera("wagner", "Lohengrin", "28 August 1850"),
    Opera("wagner", "The Rhinegold", "22 September 1869"),
    Opera("wagner", "The Valkyrie", "26 June 1870"),
    Opera("wagner", "Siegfried", "16 August 1876"),
    Opera("wagner", "Twilight of the Gods", "17 August 1876"),
    Opera("wagner", "Tristan and Isolde", "10 June 1865"),
    Opera("wagner", "The Master-Singers of Nuremberg", "21 June 1868"),
    Opera("wagner", "Parsifal", "26 July 1882"),
    Opera("beethoven", "Fidelio", "20 November 1805"),
    Opera("verdi", "Nabucco", "9 March 1842"),
    Opera("verdi", "Ernani", "9 March 1844"),
    Opera("verdi", "Macbeth", "14 March 1847"),
    Opera("verdi", "Il corsaro", "25 October 1848"),
    Opera("verdi", "Rigoletto", "11 March 1851"),
    Opera("verdi", "La traviata", "6 March 1853"),
    Opera("verdi", "Aroldo", "16 August 1857"),
    Opera("verdi", "Macbeth", "21 April 1865"),
    Opera("verdi", "Don Carlos", "11 March 1867"),
    Opera("verdi", "Aida", "24 December 1871"),
    Opera("verdi", "Otello", "5 February 1887"),
    Opera("verdi", "Falstaff", "9 February 1893"),
]


def _get_date(date_str) -> date:
    return datetime.date(datetime.strptime(date_str, "%d %B %Y"))


def operas_both_at_premiere(guest, composer):
    """Retrieves a list of titles of operas, where the guest and the composer
       could have been together at premiere.

       That is the Opera.author matches the composer passed in, and both guest
       and composer are alive at the time of Opera.date.

       If guest and/or composer are not in the composers dict, raise a
       ValueError

       Args:
       guest (str): one of the composers but not the author of an opera
       composer (str): the author of an opera

       Returns a list (or generator) of titles of operas.
    """

    if guest not in composers or composer not in composers:
        raise ValueError('guest or composer not found in composers')

    plays = []
    for opera in [o for o in operas if o.author == composer]:
        play_title = opera.play

        date_of_play = _get_date(opera.date)
        composer_death = _get_date(composers.get(composer).died)
        guess_birth = _get_date(composers.get(guest).born)
        guess_death = _get_date(composers.get(guest).died)

        #  premiere after death
        if date_of_play > composer_death:
            continue

        # guest is dead
        if date_of_play > guess_death:
            continue

        # guest not born yet when play premiere's
        if date_of_play < guess_birth:
            continue

        plays.append(play_title)

    return plays


if __name__ == "__main__":
    tests = [
        ["wagner", "verdi", 10],
        ["verdi", "wagner", 11],
        ["beethoven", "wagner", 0],
        ["wagner", "beethoven", 0],
        ["beethoven", "mozart", 5],
    ]
    for a, b, c in tests:
        result = len(operas_both_at_premiere(a, b)) == c
        print(result)

    try:
        _ = operas_both_at_premiere("dvorak", "verdi")
    except ValueError as err:
        print(err)