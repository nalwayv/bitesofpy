"""
Bite 112. Social Media Username Validator 
"""
# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re
from typing import List, Dict, Tuple
social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string() -> Dict[str, Validator]:
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples
    
    Retruns:
    --------
        Dict[str, namedtuple]: 
    """

    lines = [line for line in social_platforms.splitlines() if line]
    
    names = [lines[i] for i in range(0, len(lines), 4)]

    # get all leave blank
    prop = [
        p[1]
        for p in re.findall(r'(Min|Max|Can contain):(.+)', social_platforms)
        if p
    ]

    # split up results into tuples[(name,(min, max, reg)),
    #                              (name,(min, max, reg))]
    split_up: List[Tuple[str, Tuple[str, str, str]]] = list(
        zip(names, [tuple(prop[i:i + 3]) for i in range(0, len(prop), 3)])
    )

    validator = {}
    for plat, values in split_up:
        _min = int(values[0].strip())
        _max = int(values[1].strip())
        _pattern = f"[{''.join([v for v in values[2].strip() if v != ' '])}]+"
        _reg = re.compile(_pattern)
        validator[plat] = Validator(range=range(_min, _max), regex=_reg)

    return validator


def validate_username(platform, username) -> bool:
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    # ...

    if platform not in all_validators:
        raise ValueError('platform not found')

    current_platform: Validator = all_validators[platform]

    if len(username) >= min(current_platform.range) and len(username) < max(
            current_platform.range):
        if all(v == '' for v in current_platform.regex.split(username)):
            return True
    return False


if __name__ == "__main__":
    # 3=pass 3=fail
    for test in ['bob', 'boB123', 'bo__89A', 'bob-123', 'PyBitesbob@', 'bob.']:
        ok = validate_username('Twitter', test)
        print(ok)

    # 3=pass 3=fail
    for test in ['bob_PyBites', '-123ABC', '123-abc__', 'bobb.', 'bob@PyBites','bob$56']:
        ok = validate_username('Reddit', test)
        print(ok)
