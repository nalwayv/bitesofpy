"""
Bite 64 fix a truncated zip
"""

import itertools

NAMES = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
LOCATIONS = 'DE ES AUS NL BR US'.split()
CONFIRMED = [False, True, True, False, True]


def get_attendees():
    """get_attendees - use of itertools.zip_longest
    """
    for participant in itertools.zip_longest(NAMES,
                                             LOCATIONS,
                                             CONFIRMED,
                                             fillvalue="-"):
        print(participant)


def zip_foo():
    """zip_foo - its a zip_foo
    """
    max_len = -1
    arr_with_lens = [(NAMES, len(NAMES)), 
                     (LOCATIONS, len(LOCATIONS)),
                     (CONFIRMED, len(CONFIRMED))]

    for _, size in arr_with_lens:
        max_len = max(max_len, size)

    result_arr = []
    for arr, size in arr_with_lens:
        if max_len - size >= 0:
            N = max_len - size
            result_arr.append(arr[:] + ["-"] * N)

    for result in zip(result_arr[0], result_arr[1], result_arr[2]):
        print(result)
