"""
Bite 226. Get top titles from news.python.sc 
"""

from collections import namedtuple
from bs4 import BeautifulSoup
import requests
import re

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    # your code

    titles = []
    scores = []
    entrys = []

    for v in soup.findAll('tr', id=True):
        title = v.find('span', attrs={'class': 'title'})
        if title:
            link = soup.findNextSibling('span', attrs={'class': 'smaller'})
            if link:
                titles.append(f"{title.text.strip()} ({link.text.strip()})")
            else:
                titles.append(f"{title.text.strip()}")

    for v in soup.findAll('tr', id=False):
        points = v.select('.controls>span')
        if points:
            text = ' '.join(x for x in points[0].text.split(" ")
                            if x != '').replace("\n", '')

            p_and_c = re.findall(r'\d+\s(?:points)|\d+\s(?:comments)', text)

            if p_and_c and len(p_and_c) == 2:
                en_points = int(p_and_c[0].split(" ")[0].strip())
                en_comment = int(p_and_c[1].split(" ")[0].strip())
                scores.append((en_points, en_comment))

    for name, score in list(zip(titles, scores)):
        entrys.append(Entry(title=name, points=score[0], comments=score[1]))

    return sorted(entrys, key=lambda x: (x.points, x.comments),
                  reverse=True)[:top]


if __name__ == "__main__":
    link_a = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'
    link_b = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html'
    for x in get_top_titles(link_a):
        print(x)
