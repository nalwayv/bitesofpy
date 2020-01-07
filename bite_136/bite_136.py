"""
Bite 136. Bloodtypes

Write a function which checks the red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum
from typing import Dict, Tuple


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text: Dict[str, Bloodtype] = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}


def _is_type_str(value: str) -> Bloodtype:
    bloodtype = blood_type_text.get(value)
    if not bloodtype:
        raise ValueError
    return bloodtype


def _is_type_int(value: int) -> Bloodtype:
    try:
        return Bloodtype(value)
    except ValueError as err:
        raise err


# complete :
def check_bt(donor, recipient) -> bool:
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """
    if not isinstance(donor, (int, str, Bloodtype)):
        raise TypeError
    if not isinstance(recipient, (int, str, Bloodtype)):
        raise TypeError

    # NOTE: get Bloodtype enum based on type
    db_type: Bloodtype = None
    if isinstance(donor, str):
        db_type = _is_type_str(donor)
    elif isinstance(donor, int):
        db_type = _is_type_int(donor)
    else:
        db_type = donor

    re_type: Bloodtype = None
    if isinstance(recipient, str):
        re_type = _is_type_str(recipient)
    elif isinstance(recipient, int):
        re_type = _is_type_int(recipient)
    else:
        re_type = recipient

    db_value: int = db_type.value
    re_value: int = re_type.value
    result = _particular_antigen_comp(db_value, re_value)
    
    if all([r >= 0 for r in result]):
        return True

    return False


# hint
def _particular_antigen_comp(donor: int,
                             recipient: int) -> Tuple[int, int, int]:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that 
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )


if __name__ == "__main__":
    print(check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG))
    print(check_bt("0+", "A+"))
    print(check_bt(0, 7))

    try:
        check_bt(3, ["AB", "Rh+"])
    except TypeError:
        print('type error')

    try:
        check_bt("X-", "Y+")
    except ValueError:
        print('value error')
