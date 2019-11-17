import os
import glob
from tempfile import TemporaryDirectory

ONE_KB = 1024

TMP = os.path.join(os.path.dirname(__file__), 'tmp')


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""

    res = []

    for root, _, files in os.walk(dirname):
        for f in files:
            if os.stat(os.path.join(root, f)).st_size >= ONE_KB * size_in_kb:
                res.append(f)
    return res


if __name__ == "__main__":

    tests = [
        ([800, 1000, 1200], 1, ['1200']),
        ([1024, 1025], 1, ['1024', '1025']),
        ([1024, 1025], 1.026, []),
        ([1000, 1300, 1777, 900], 1.25, ['1300', '1777']),
        ([1024, 2047, 2048, 2500], 2, ['2048', '2500']),
    ]
    for byte_size, size_in_kb, expected in tests:
        with TemporaryDirectory(dir=TMP) as dirname:
            for size in byte_size:
                with open(os.path.join(dirname, str(size)), 'wb') as f:
                    f.write(os.urandom(size))
            res = [
                os.path.basename(fi) for fi in get_files(dirname, size_in_kb)
            ]
            print(res == expected)