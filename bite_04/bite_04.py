""" 
Bite 4. Top 10 PyBites tags
"""
import os
import re
from collections import Counter
from typing import List

# import urllib.request

# prep
tempfile = os.path.join(os.path.dirname(__file__), 'tmp', 'feed')
# urllib.request.urlretrieve('http://bit.ly/2zD8d8b', os.path.abspath(tempfile))


def open_file():
    content = None
    with open(tempfile) as f:
        content = f.read().lower()
    return content


def get_all_categorys(data: str) -> List[str]:
    """get_all_categorys
    
    Args:
        data (str): data passed in
    
    Returns:
        list: list of strings
    """
    pattern = r"(?:<category>)([a-zA-Z0-9 ]+)(?:</category>)"
    check = re.compile(pattern)
    find = check.findall(data)
    return find


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable
    """
    data = open_file()
    find = get_all_categorys(data)
    count = Counter(find)
    return count.most_common(n)
