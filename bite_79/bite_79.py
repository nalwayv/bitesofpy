"""
Bite 79. Parse a csv file and create a bar chart 
"""
import csv
import requests
from collections import defaultdict

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv() -> str:
    """Use requests to download the csv and return the
       decoded content
    """
    with requests.Session() as session:
        download = session.get(CSV_URL)
        return download.content.decode('utf-8')


def create_user_bar_chart(content: str) -> None:
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)
    """
    data = defaultdict(list)
    for row in csv.DictReader(content.splitlines(), delimiter=','):
        tz = row['tz']
        data[tz].append(tz)

    for d in sorted(data.items(), key=lambda x: x[0]):
        name = d[0]
        bar = len(d[1])
        print("{0:<21}| {1}".format(name, '+' * bar))


if __name__ == "__main__":
    content = get_csv()
    create_user_bar_chart(content)