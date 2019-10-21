"""
Bite 150: csv to jason
"""

import json
import re
from typing import List

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def text_cleanup(text: str) -> List[List[str]]:
    """text_cleanup

    simple regex pattern to clean up csv file.

    Args:
        text (str): csv file in string format
    """
    values = [w.strip() for w in text.rsplit()]
    pattern = "[,;|]+"
    check = re.compile(pattern)

    result = []
    for value in values:
        val = check.split(value)
        result.append(val)

    return result


def convert_to_json(members=members) -> str:
    """convert_to_json

    convert valid csv string data to json string

    Args:
        members (str): string format of a csv file

    Returns (str):
        string that when run though json.loads
        returns an array of json objects
    """
    values = text_cleanup(members)
    row_zero = values[0]
    result = []
    for row in values[1:]:
        dict_it = [f'"{key}": "{value}"' for key, value in zip(row_zero, row)]
        result.append(f"{{{','.join(dict_it)}}}")

    return f"[{','.join(result)}]"


# if __name__ == "__main__":
#     my_json = convert_to_json()
#     test_j = json.loads(my_json)
#     for j in test_j:
#         print(j)
