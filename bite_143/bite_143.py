""" 
Bite 143
"""

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if not isinstance(name, str):
        return NOT_FOUND

    data = {}
    groups = [group1, group2, group3]
    for group in groups:
        data.update(group)

    if name.lower() in data:
        return data[name.lower()]
    return NOT_FOUND


if __name__ == "__main__":
    v = get_person_age(None)
    print(v)
