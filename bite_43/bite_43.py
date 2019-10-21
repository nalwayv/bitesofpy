"""
Bite 43: Force keyword arguments.
"""

def get_profile(*, name="julian", profession="programmer"):
    """get_profile - use of * forces the use of key word args.
    """
    return f"{name} is a {profession}"
