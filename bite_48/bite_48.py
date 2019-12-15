""" 
Bite 48. Make a bar chart of new Safari books  
"""
import os
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '+', '.'


FILE_PATH = os.path.join(os.path.dirname(__file__), 'tmp', DATA)


def open_file(file_path):
    with open(file_path) as file_data:
        return [line.strip() for line in file_data.readlines()]


def create_chart() -> str:

    data = open_file(FILE_PATH)

    n = len(data)
    dd = defaultdict(list)

    for i in range(0, n, 2):
        info = data[i]
        send = data[i + 1]

        if 'sending to slack channel' in send:
            if 'python' in info.lower():
                dd[info[:6]].append(PY_BOOK)
            else:
                dd[info[:6]].append(OTHER_BOOK)

    print('\n    '.join([f"{key}{''.join(vals)}" for key, vals in dd.items()]))


if __name__ == "__main__":

    create_chart()
