""" 
Bite 13. Convert dict to namedtuple/json
"""
from collections import namedtuple
from datetime import datetime
import json
from typing import NamedTuple

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here


def dict2nt(dict_: dict) -> NamedTuple:
    """dict2nt - convert dict to a named tuple
    
    Args:
        dict_ (dict): dict object
    
    Returns:
        NamedTuple: named tuple with dicts_ keys and values
    """
    named_t = namedtuple("Dict2Nt", " ".join([key for key in dict_.keys()]))
    # unpack dict
    new_tuple = named_t(**dict_)  
    return new_tuple


def nt2json(nt) -> json:
    """nt2json
    
    Args:
        nt (NamedTuple): a named tuple
    
    Returns:
        json: named tuple converted to a json object
    """

    start = nt._asdict()
    result = {}

    for data_a, data_b in start.items():

        # if data is of type datetime convert to iso format
        # to become json serializable
        if isinstance(data_b, datetime):
            result[data_a] = data_b.isoformat()
        else:
            result[data_a] = data_b

    return json.dumps(result)
