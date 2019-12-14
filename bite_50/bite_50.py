"""
Bite 50. Make a little PyBites search engine (feedparser)
"""
from collections import namedtuple
from datetime import date, datetime
import feedparser

from typing import List
from pathlib import Path

FILE_PATH = Path('./tmp/mock.xml')

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime) -> date:
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(year=stime.tm_year, month=stime.tm_mon, day=stime.tm_mday)


def get_feed_entries(feed=FEED) -> List[Entry]:
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    entries: List[Entry] = []
    feed_data: "FeedParserDict" = feedparser.parse(feed)

    for data in feed_data.entries:
        entry_date = data['published_parsed']
        entry_title = data['title']
        entry_link = data['link']
        entry_tags = [t.term.lower() for t in data['tags']]

        new_entry = Entry(date=_convert_struct_time_to_dt(entry_date),
                          title=entry_title,
                          link=entry_link,
                          tags=entry_tags)

        entries.append(new_entry)

    return entries


def filter_entries_by_tag(search, entry: Entry) -> bool:
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    lower_search = search.lower()

    if '&' in lower_search:
        res = []
        for v in lower_search.split('&'):
            if v in entry.tags:
                res.append(True)
            else:
                res.append(False)

        return all(res)

    elif '|' in lower_search:
        res = []
        for v in lower_search.split('|'):
            if v in entry.tags:
                res.append(True)
            else:
                res.append(False)

        return any(res)

    else:
        return lower_search in entry.tags

    return False


def get_user_input(msg: str) -> (bool, str):
    user_input = ''
    exit_loop = True

    while True:
        user_input = input(msg).lower()

        if user_input:
            if user_input in ['q', 'Q']:
                return exit_loop, user_input
            else:
                exit_loop = False
                break
        else:
            print('\nPlease provide a search term\n')

    return exit_loop, user_input


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    # TEST WITH MOCK DATA
    # entries = get_feed_entries(FILE_PATH)

    entries = get_feed_entries()

    while True:

        exit_loop, text_result = get_user_input('Search for (q for exit): ')
        if exit_loop:
            break

        res = []
        for e in entries:
            ok = filter_entries_by_tag(text_result, e)
            if ok:
                res.append(e)
        if res:
            for entry in sorted(res, key=lambda e: e.date):
                text_entry_2 = '{title}'
                print(text_entry_2.format(title=entry.title))

            if len(res) == 1:
                print("\n1 entry matched\n")
            else:
                print(f'\n{len(res)} entries matched\n')

        else:
            print('\n0 entries matched\n')

    print('Bye')


if __name__ == '__main__':
    main()