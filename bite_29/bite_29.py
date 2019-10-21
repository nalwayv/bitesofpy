""" 
Bite 29. Martin's IQ test
"""

def get_index_different_char(chars):
    ABC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    data = {"a": {"tally": 0, "idx": -1}, "b": {"tally": 0, "idx": -1}}

    for idx, val in enumerate([str(v) for v in chars]):
        if val:
            if val in ABC:
                data["a"]["tally"] += 1
                data["a"]["idx"] = idx
            else:
                data["b"]["tally"] += 1
                data["b"]["idx"] = idx

    if data["a"]["tally"] < data["b"]["tally"]:
        return data["a"]["idx"]

    return data["b"]["idx"]


# if __name__ == "__main__":
#     inputs = (
#         ['A', 'f', '.', 'Q', 2],
#         ['.', '{', ' ^', '%', 'a'],
#         [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
#         ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
#         list(range(1, 9)) + ['}'] + list('abcde'),  # noqa E230
#         [2, '.', ',', '!'])

#     for v in inputs:
#         print(get_index_different_char(v))
