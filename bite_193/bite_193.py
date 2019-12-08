""" 
Bite 193. Most upvoted StackOverflow Python questions
"""
import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


def get_request_content(url: str) -> BeautifulSoup:
    with requests.Session() as session:
        r = session.get(url).content.decode('utf-8')
        soup = BeautifulSoup(r, features="html.parser")
        return soup


def top_python_questions(url: str = cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    data = []
    content = get_request_content(url)
    questions: BeautifulSoup = content.findAll(
        'div', attrs={'class': 'question-summary'})

    for q in questions:
        title = q.find('h3').text
        vote = q.find('span', attrs={'class': 'vote-count-post'}).text.strip()
        view = q.find('div', attrs={'class': 'views'}).text.strip()

        if 'm' in view:
            data.append((title, int(vote)))

    return sorted(data, key=lambda x: x[1], reverse=True)
