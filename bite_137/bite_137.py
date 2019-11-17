""" 
Bite 137. Gourmets' Nightmare
"""

from collections import Counter, defaultdict

# import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def score(word1: str, word2: str):
    len_w1 = len(word1)
    len_w2 = len(word2)

    _set = Counter(word1.lower()) & Counter(word2.lower())
    _sum = sum(list(_set.values()))

    return _sum / (1 + (len_w1 - len_w2)**2)


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    wines = None
    if wine_type == 'all':
        wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    elif wine_type == 'white':
        wines = WHITE_WINES
    elif wine_type == 'red':
        wines = RED_WINES
    elif wine_type == 'sparkling':
        wines = SPARKLING_WINES
    else:
        raise ValueError('wine type not found')

    res = []
    for wine in wines:
        for cheese in CHEESES:
            value = score(wine, cheese)
            res.append((wine, cheese, value))

    return sorted(res, key=lambda x: x[2])[-1]


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """

    res = defaultdict(list)

    wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    for wine in wines:
        for cheese in CHEESES:
            value = score(wine, cheese)
            res[wine].append((cheese, value))

    res2 = []
    for key, val in dict(res).items():

        v1 = sorted(val, key=lambda x: (-x[1], x[0]))
        v2 = [name for name, _ in v1][:5]
        v3 = (key, v2)
        res2.append(v3)

    return sorted(res2, key=lambda x: x[0])


if __name__ == "__main__":
    print(best_match_per_wine('white'))
    print(best_match_per_wine('red'))
    print(best_match_per_wine('sparkling'))
    print("-" * 45)
    for v in match_wine_5cheeses()[:3]:
        print(v)
