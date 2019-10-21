"""
Bite 171. Make a terminal spinner animation
"""
from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds) -> None:
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout.
    Args:
        seconds (float): animation run time
    """
    animation = cycle(''.join(SPINNER_STATES))
    start = time()
    while True:
        sleep(STATE_TRANSITION_TIME)
        sym = next(animation)
        sys.stdout.write(f"\r{sym}")
        sys.stdout.flush()

        end = time()
        if (end - start) >= seconds:
            break
