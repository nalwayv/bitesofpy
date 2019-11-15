""" 
Bite 47. Write a new password field validator
"""
import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password: str) -> bool:
    """validate_password

    - is between 6 and 12 chars long (both inclusive)
    - has at least 1 digit [0-9]
    - has at least two lowercase chars [a-z]
    - has at least one uppercase char [A-Z]
    - has at least one punctuation char (use: PUNCTUATION_CHARS)
    - Has not been used before (use: used_passwords)
    
    Parameters
    ----------
    password : str

    Returns
    -------
    bool
    """

    pass_len = True if len(password) >= 6 and len(password) <= 12 else False
    digits_1 = len([x for x in password if x.isdigit()]) >= 1
    two_lowercase = len([x for x in password if x.islower()]) >= 2
    one_uppercase = len([x for x in password if x.isupper()]) >= 1
    one_punc = len([x for x in password if x in string.punctuation]) >= 1
    not_used = True if password not in used_passwords else False

    ok = (pass_len and digits_1 and two_lowercase and one_uppercase
          and one_punc and not_used)
    if ok:
        used_passwords.add(password)
        return True
    return False


if __name__ == "__main__":

    print("Wrong Size:")
    print("-", validate_password('short'))
    print("-", validate_password('waytoolongpassword'))

    print("Missing chars:")
    print("-", validate_password('UPPERCASE'))
    print("-", validate_password('lowercase'))
    print("-", validate_password('PW_no_digits'))
    print("-", validate_password('Pw9NoPunc'))
    print("-", validate_password('_password_'))
    print("-", validate_password('@#$$)==1'))

    print("One letter")
    print("-", validate_password('@#$$)==1a'))

    print("Good:", )
    print("-", validate_password('passWord9_'))
    print("-", validate_password('another>4Y'))
    print("-", validate_password('PyBites@1912'))
    print("-", validate_password('We<3Python'))

    print("Not used before:")
    print("-", validate_password('PassWord@1'))
    print("-", validate_password('PyBit$s9'))

    print("Used:")
    num_passwords_use = len(used_passwords)
    print("-", validate_password('go1@PW'))
    print("-", len(used_passwords) == num_passwords_use + 1)
    print("-", validate_password('go1@PW'))
