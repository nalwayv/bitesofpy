""" 
Bite 133: Convert an Amazon URL into an affiliation link 
"""
import re
from typing import Optional

LINKS = [
    'https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art',
    'https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1',
    'https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234',
    'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    'https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/',
    'https://www.amazon.com/fake-book-with-longer-asin/dp/1449340377000/'
]


def generate_affiliation_link(url: str) -> Optional[str]:
    """generate_affiliation_link -

    Parameters
    ----------
    url : str
        amazon url string
    
    Returns
    -------
    Optional[str]
        ever a string or None
    """

    link = 'http://www.amazon.com/{}/?tag=pyb0f-20'

    pattern = r'(dp\/\w*)'
    match = re.findall(pattern, url)
    if match:
        return link.format(match[0])
    return None


if __name__ == "__main__":
    for link in LINKS:
        result = generate_affiliation_link(link)
        if result:
            print(result)