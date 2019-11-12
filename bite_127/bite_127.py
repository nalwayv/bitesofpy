def get_ordinal_suffix(number) -> str:
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    st = 'st'
    nd = 'nd'
    rd = 'rd'
    th = 'th'

    if number == 0:
        return f"{number}{th}"

    num1 = number % 10
    num2 = number % 100

    if num1 == 1 and num2 != 11:
        return f"{number}{st}"

    if num1 == 2 and num2 != 12:
        return f"{number}{nd}"

    if num1 == 3 and num2 != 13:
        return f"{number}{rd}"

    return f"{number}{th}"


if __name__ == "__main__":
    tests = [(0, '0th'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'),
             (9, '9th'), (10, '10th'), (11, '11th'),
             (12, '12th'), (13, '13th'), (20, '20th'), (21, '21st'),
             (22, '22nd'), (23, '23rd'), (24, '24th'), (25, '25th'),
             (30, '30th'), (50, '50th'), (51, '51st'), (52, '52nd'),
             (53, '53rd'), (54, '54th'), (55, '55th'), (99, '99th'),
             (100, '100th'), (101, '101st'), (102, '102nd'), (103, '103rd'),
             (104, '104th'), (110, '110th'), (111, '111th'), (1001, '1001st'),
             (1003, '1003rd'), (1111, '1111th')]
    print(all(get_ordinal_suffix(i)==j for i,j in tests))

