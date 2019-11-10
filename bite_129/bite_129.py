"""
Bite 129. Analyze Stock Data
"""
import json
import os
from typing import List, Tuple

FILE_PATH = os.path.join(os.path.dirname(__file__), 'tmp', 'data.json')
ABS_FILE_PATH = os.path.abspath(FILE_PATH)


def open_file() -> List[dict]:
    json_data = None

    try:
        with open(ABS_FILE_PATH) as file:
            data = file.read()
            json_data = json.loads(data)
    except Exception as err:
        print(f"ERROR: {err}")
        return None

    return json_data


def _cap_str_to_mln_float(cap: str) -> float:
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    try:
        if cap[-1:] == "M":
            return float(cap[1:len(cap) - 1])
        elif cap[-1:] == "B":
            if_b = 1000
            return float(cap[1:len(cap) - 1]) * if_b
    except ValueError:
        print("ERROR: converting to float")

    # if n/a
    return 0


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    jdata = [
        data["cap"] for data in open_file() if data["industry"] == industry
    ]
    return round(sum([_cap_str_to_mln_float(cap) for cap in jdata]), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""

    fields = ["symbol", "cap"]
    jdata = [{key: val
              for key, val in data.items() if key in fields}
             for data in open_file()]

    return max(jdata, key=lambda x: _cap_str_to_mln_float(x['cap']))['symbol']


def get_sectors_with_max_and_min_stocks() -> Tuple[str, str]:
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""

    sectors = dict.fromkeys(
        {d["sector"]
         for d in open_file() if d["sector"] != "n/a"}, 0)

    for data in open_file():
        sec = data['sector']
        cap = data['cap']

        if sec != 'n/a':
            sectors[sec] += _cap_str_to_mln_float(cap)

    return (max(sectors, key=sectors.get), min(sectors, key=sectors.get))


print(get_stock_symbol_with_highest_cap())