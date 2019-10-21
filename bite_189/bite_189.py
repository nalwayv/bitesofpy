""" 
Bite 189:  Filter a list of names
"""

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    t = 0
    result = []
    err = False
    for name in names:
        if name:

            for c in [v for v in name]:
                if c in [str(i) for i in range(1, 10)]:
                    err = True
                    break

            if name[0] == IGNORE_CHAR:
                err = True

            if name[0] == QUIT_CHAR or t == MAX_NAMES:
                return result

            if not err:
                t += 1
                result.append(name)

            err = False

    return result
