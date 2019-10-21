"""
Bite_22. write a decorator with arguments.
"""
from functools import wraps
from typing import Callable


def make_html(tag: str):
    """make_html - decorator that takes a html tag to surround some text with

    Paramiters
    ----------
    tag: str
        a html tag

    Returns
    -------
    func:
    function decorator that can tage a single paramiter

    Examples
    --------
        @make_html('a')
        def foo(text):
            return text

        >>> foo("hello")
        <a>hello</a>

    """
    def tag_wrapper(func: Callable[..., str]):
        """tag_wrapper

        Returns
        -------
        func:
            function that returns a string that has been
            updated with html element tags.
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            """wrapper

            Paramiters
            ----------
            *args:
                arguments
            **kwargs:
                key word arguments

            Returns
            -------
            str:
                text with html element tag
            """

            text = func(*args, **kwargs)

            return f"<{tag}>{text}</{tag}>"

        return wrapper

    return tag_wrapper


@make_html("p")
@make_html("strong")
def get_text(text: str = "hello world"):
    """get_text
    """
    return text
