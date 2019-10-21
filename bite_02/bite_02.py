"""
Bite 02 re fun
"""
import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')

TWEET2 = ('PyBites My Reading List | 12 Rules for Life - #books '
          'that expand the mind! '
          'http://pbreadinglist.herokuapp.com/books/'
          'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
          ' #psychology #philosophy')

HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    # find times
    pattern = r"([\d]{2}:[\d]{2})"
    check = re.compile(pattern)
    ok = check.findall(course)
    if ok:
        return ok
    return None


# TODO
def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    # find tags or link
    # tuple because of the |
    pattern = r"(http://[\w+?\.\w+]+[a-zA-Z0-9\~\!\@\#\$\%\^\&\*\(\)_\-\=\+\\\/\?\.\:\;\'\,]*)|(#\w+)"
    check = re.compile(pattern)
    ok = check.findall(tweet)
    if ok:
        result = []
        for a, b in ok:
            if len(a):
                result.append(a)
            if len(b):
                result.append(b)
        return result
    return None


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    # text between tags
    pattern = r"(?<=>)((?!\s*<)[\s\S]+?)(?=<)"
    check = re.compile(pattern)
    ok = check.findall(html)
    if ok:
        return ok[0]
    return None

