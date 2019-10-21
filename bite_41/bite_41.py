"""
Bite 41
"""
from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def inner_wrap(user: str):

        msg = ""

        if user not in known_users:
            msg = "please create an account"
        else:
            if user in known_users:
                if user not in loggedin_users:
                    msg = "please login"
                else:
                    msg = f"welcome back {user}"

        return func(f"{msg}")

    return inner_wrap


@login_required
def welcome(user: str):
    """Return a welcome message if logged in
    """
    print(user)

