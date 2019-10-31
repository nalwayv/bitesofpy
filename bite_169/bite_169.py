""" 
Bite 169: Simple length converter
"""


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """

    if not isinstance(value, (int, float)):
        raise TypeError('wrong type')

    CM = 2.54
    IN = 1 / CM

    if fmt.lower() == 'cm':
        return round(value * CM, 4)
    elif fmt.lower() == 'in':
        return round(value * IN, 4)

    raise ValueError('wrong convert format')


if __name__ == "__main__":
    tests_cm = [(1, 2.54), (10, 25.4), (16, 40.64), (17, 43.18), (18, 45.72),
                (29, 73.66), (30, 76.2), (31, 78.74), (32, 81.28), (33, 83.82),
                (49, 124.46), (61, 154.94), (62, 157.48), (64, 162.56),
                (74, 187.96), (75, 190.5), (81, 205.74), (82, 208.28),
                (83, 210.82), (84, 213.36), (99, 251.46), (100, 254.0)]
    print(all(
        convert(in_put, 'cm') == out_put for in_put, out_put in tests_cm))

    print('-' * 45)

    tests_in = [(1, 0.3937), (2, 0.7874), (3, 1.1811), (4, 1.5748),
                (5, 1.9685), (6, 2.3622), (7, 2.7559), (8, 3.1496),
                (23, 9.0551), (24, 9.4488), (53, 20.8661), (54, 21.2598),
                (55, 21.6535), (70, 27.5591), (75, 29.5276), (79, 31.1024),
                (80, 31.4961), (90, 35.4331), (91, 35.8268), (92, 36.2205),
                (99, 38.9764), (100, 39.3701)]
    print(all(
        convert(in_put, 'in') == out_put for in_put, out_put in tests_in))

    print('-' * 45)

    try:
        convert(10, 'km')
    except ValueError as err:
        print(err)

    print('-' * 45)

    try:
        convert('10', 'in')
    except TypeError as err:
        print(err)