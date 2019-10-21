"""
Bite 36: args and kwargs
"""


def get_profile(*args, **kwargs) -> dict:
    """get_profile
    
    Raises:
        TypeError: if no args are passed or only one arg is passed
        ValueError: age value is not an int
        ValueError: to many sports added
    
    Example:
        >>> get_profile('john', 5)
        {
            'name': 'john', 
            'age': 5
        }

        >>> get_profile('john', 5, 'football')
        {
            'name': 'john', 
            'age':5, 
            'sports': ['football']
        }

        >>> get_profile('john', 5, 'football', champ='winning goal')
        {
            'name':'john', 
            'age':5, 
            'sports':['football'], 
            'awards':{
                'champ':'winning goal'
            }
        }

    Returns:
        dict:
    """
    result = {}
    name = None  # str
    age = None  # int
    sports = None  # list
    awards = None  # dict

    check_is_int = lambda x: isinstance(x, int)

    # *Args
    if not args or len(args) == 1:
        raise TypeError("empty")

    if len(args) == 2:
        name, age = args
        ok = check_is_int(age)
        if not ok:
            raise ValueError("age is not an int")

    if len(args) >= 3:
        name, age, *sports = args

        ok = check_is_int(age)
        if not ok:
            raise ValueError("age is not an int")

        if len(sports) > 5:
            raise ValueError("to many sports")

    # **Kwargs
    if kwargs:
        awards = kwargs

    # Results
    if name:
        result['name'] = name
    if age:
        result['age'] = age
    if sports:
        result['sports'] = sorted(sports)
    if awards:
        result['awards'] = awards

    return result
