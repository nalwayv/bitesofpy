"""
 Bite 87. Convert Decimal to Roman Numerals
"""

ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
         (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"),
         (4, "IV"), (1, "I")]


def romanize(decimal_number: int) -> str:
    """romanize

    Takes a decimal number int and converts its Roman Numeral str
    
    Paramiters:
    -----------
        decimal_number (int):

    Returns:
    --------
        str:
            roman number
    """
    if not isinstance(decimal_number, int):
        raise ValueError("not an int")

    if decimal_number <= 0 or decimal_number >= 4000:
        raise ValueError("out of range")

    result = []
    for num, roman in ROMAN:
        # times symbol is used
        count = decimal_number // num

        # update decimal
        decimal_number = decimal_number % num

        result.append(roman * count)

    return "".join(result)


if __name__ == "__main__":
    tests = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'),
             (5, 'V'), (1, 'I'), (177, 'CLXXVII'), (244, 'CCXLIV'),
             (87, 'LXXXVII'), (1033, 'MXXXIII'), (997, 'CMXCVII'),
             (3999, 'MMMCMXCIX'), (13, 'XIII'), (777, 'DCCLXXVII'),
             (1652, 'MDCLII'), (1981, 'MCMLXXXI'), (2018, 'MMXVIII'),
             (3500, 'MMMD')]
             
    for number, sym in tests:
        print(romanize(number))

    for an_error in ['string', -1, 0, 4000, 10000]:
        try:
            print(romanize(an_error))
        except ValueError as err:
            print(err)