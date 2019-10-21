"""
Bite 12
"""
from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    def __init__(self):
        super().__init__("user does not exist")

class UserAccessExpired(Exception):
    def __init__(self):
        super().__init__("user aceess has expired")

class UserNoPermission(Exception):
    def __init__(self):
        super().__init__("user has no permission")


def get_secret_token(username: str):
    for user in USERS:
        if user.name == username:

            if not user.expired:
                if user.role == ADMIN:
                    return SECRET
                else:
                    raise UserNoPermission()
            else:
                raise UserAccessExpired()

    raise UserDoesNotExist()

