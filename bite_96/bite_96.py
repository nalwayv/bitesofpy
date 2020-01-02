"""
Bite 96. BUild Unix' wc program in Python
"""


def wc(file_) -> str:
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)
    """

    with open(file_, 'r') as file_info:
        data = file_info.read()

        lines = len(data.splitlines())
        words = len(data.replace('\n', ' ').split())
        chars = len(data)

        return f'{lines} {words} {chars} {file_}'
    return ''


if __name__ == '__main__':
    import sys
    try:
        print(wc(sys.argv[1]))
    except IndexError:
        print('out of range!')
