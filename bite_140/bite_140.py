"""
Bite 140. PyBites First Pandas Bite
"""

import pandas as pd
from typing import Dict

data1 = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"
data2 = "https://bites-data.s3.us-east-2.amazonaws.com/summer_2008-2012.csv"


def athletes_most_medals(data: str) -> Dict[str, int]:
    df = pd.read_csv(data)

    men = df[['Athlete', 'Medal']][df.Gender=='Men'] \
                                                    .groupby(['Athlete'])['Medal'] \
                                                    .count() \
                                                    .reset_index(name='Medals') \
                                                    .sort_values(['Medals'],ascending=False) \
                                                    .head(1) \
                                                    .values

    women = df[['Athlete', 'Medal']][df.Gender=='Women'] \
                                                    .groupby(['Athlete'])['Medal'] \
                                                    .count() \
                                                    .reset_index(name='Medals') \
                                                    .sort_values(['Medals'],ascending=False) \
                                                    .head(1) \
                                                    .values
    return {
        men[0][0]: men[0][1],
        women[0][0]: women[0][1],
    }


if __name__ == "__main__":
    ok = athletes_most_medals(data2)
    print(ok)
