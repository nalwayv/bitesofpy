"""
Bite 89.  Playing with lists and dicts
"""
from typing import List, Dict

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

states = [
    'Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon', 'Mississippi',
    'Minnesota', 'Colorado', 'Alabama', 'Massachusetts', 'Arizona',
    'Connecticut', 'Montana', 'West Virginia', 'Nebraska', 'New York',
    'Nevada', 'Idaho', 'New Jersey', 'Missouri', 'South Carolina',
    'Pennsylvania', 'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
    'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky', 'Virginia',
    'Ohio', 'Wisconsin', 'Maryland', 'Florida', 'Utah', 'Maine', 'California',
    'Vermont', 'Arkansas', 'Wyoming', 'Louisiana', 'North Dakota',
    'South Dakota', 'Texas', 'Illinois', 'Iowa', 'Michigan', 'Delaware'
]

NOT_FOUND = 'N/A'


def get_every_nth_state(states: List[str], n=10) -> List[str]:
    """Return a list with every nth item (default argument n=10, so every
       10th item) of the states list above (remember: lists keep order)
    
    Parameters
    ----------
    states : List[str]

    n : int

    Returns
    -------
    List[str]
    """
    return [value for idx, value in enumerate(states) if (idx + 1) % n == 0]


def get_state_abbrev(state_name: str, us_state_abbrev: Dict[str, str]) -> str:
    """Look up a state abbreviation by querying the us_state_abbrev
       dict by full state name, for instance 'Alabama' returns 'AL',
       'Illinois' returns 'IL'.
       If the state is not in the dict, return 'N/A' which we stored
       in the NOT_FOUND constant (takeaway: dicts are great for lookups)

    Parameters
    ----------
    state_name : str   
    
    us_state_abbrev: Dict[str, str]

    Returns
    -------
    str
    """
    if state_name in us_state_abbrev:
        return us_state_abbrev.get(state_name)
    return NOT_FOUND


def get_longest_state(data) -> str:
    """Receives data, which can be the us_state_abbrev dict or the states
       list (see above). It returns the longest state measured by the length
       of the string

    Paramiters
    ----------
    data : List[str]

    Returns
    -------
    str   
    """
    longest = ""
    for state in data:
        if len(state) > len(longest):
            longest = state
    return longest


def combine_state_names_and_abbreviations(us_state_abbrev: Dict[str, str],
                                          states: List[str]) -> List[str]:
    """Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from
       the us_state_abbrev dict, and the last 10 states from the states
       list (see above) and combine them into a new list without losing
       alphabetical order
    
    Paramiters
    ----------
    us_state_abbrev : Dict[str, str]

    states : List[str]
    
    Returns
    -------
    List[str]
    """
    return sorted(list(us_state_abbrev.values())[:10]) + sorted(states)[-10:]


if __name__ == "__main__":
    nth = get_every_nth_state(states, 20)
    print(nth)
    print('-' * 45)
    get_state = get_state_abbrev('Alabama', us_state_abbrev)
    print(get_state)
    print('-' * 45)
    longest = get_longest_state(states)
    print(longest)
    print('-' * 45)
    com = combine_state_names_and_abbreviations(us_state_abbrev, states)
    print(com)
    print('-' * 45)
