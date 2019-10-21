"""
Bite 159 cal
"""

def simple_calculator(calculation: str):
    """simple_calculator - its a simple calculator
    

    Paramiters
    ----------
    calculation: str
        simple string mathj calculation like 1 + 1

    Examples
    --------
        >>> simple_calculator("2 * 2")
        4
        >>> simple_calculator(2*2)
        ValueError
    """
    try:
        # Phase 1: split
        numbers = [
            float(num.strip()) for num in calculation.split(" ")
            if num not in ["+", "-", "*", "/"]
        ]

        syms = [
            sym.strip() for sym in calculation.split(" ")
            if sym in ["+", "-", "*", "/"]
        ]

        if not numbers or not syms:
            raise ValueError()

        # Phase 2: ?
        start_cal = numbers.pop(0)
        for sym, num in list(zip(syms, numbers)):
            if sym == "+":
                start_cal += num
            if sym == "-":
                start_cal -= num
            if sym == "*":
                start_cal *= num
            if sym == "/":
                round_num = round(start_cal / num, 2)
                start_cal = round_num

        # Phase 3: profit...
        if not float.is_integer(start_cal):
            return start_cal
        return int(start_cal)

    except ValueError:
        raise ValueError()

    except ZeroDivisionError:
        raise ValueError()


# if __name__ == "__main__":
#     output = simple_calculator("1 * 2 * 3")
#     print(output)
