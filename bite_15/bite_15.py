"""
Bite 15
"""

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    CHAR = 11
    for idx, values in enumerate(zip(names, countries)):
        name, country = values
        print(f"{idx+1}. {name}{' '*(CHAR-len(name))}{country}")
