""" 
Bite 180
"""
from collections import defaultdict

data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str) -> defaultdict:
    """group_names_by_country"""
    countries = defaultdict(list)

    values = [
        (a, b, c)
        for (a, b, c) in [v.split(",") for v in data.strip("',/\n").split("\n")]
    ]

    for f_name, l_name, c_name in values[1:]:
        countries[c_name].append(f"{l_name} {f_name}")

    return countries
