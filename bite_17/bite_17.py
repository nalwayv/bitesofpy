""" 
Bite 17 Form teams from a group of friends

Write a function called friends_teams that takes a list of friends, 
a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True), 
the number of teams would be greater.


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante'), True),
    (('Bob', 'Julian'), True),
    (('Bob', 'Martin'), True),
    (('Dante', 'Julian'), True),
    (('Dante', 'Martin'), True),
    (('Julian', 'Martin'), True),
    # order does not matter
    (('Dante', 'Bob'), False),
    (('Julian', 'Bob'), False),
    (('Martin', 'Bob'), False),
    (('Julian', 'Dante'), False),
    (('Martin', 'Dante'), False),
    (('Martin', 'Julian'), False),
    # not with self
    (('Julian', 'Julian'), False),
])
def test_team_of_two_order_does_not_matter(test_input, expected):
    '''First test lists all combos'''
    combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
    assert len(combos) == 6
    if expected:
        assert test_input in combos
    else:
        assert test_input not in combos
"""
from itertools import permutations, combinations

FRIENDS = 'Bob Dante Julian Martin'.split()


def friends_teams(friends, team_size=2, order_does_matter=False):
    """[summary]
    
    Parameters
    ----------
    friends : list[tuple[str,str]]
        [description]
    team_size : int, optional
        [description], by default 2
    order_does_matter : bool, optional
        [description], by default False
    """
    if order_does_matter:
        get_comb = list(permutations(friends, team_size))
        res = []
        for v in get_comb:
            sv = tuple(sorted(v))
            if sv in res:
                res.append(v)
            else:
                res.append(sv)
        return res

    return list(combinations(friends, team_size))
