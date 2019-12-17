""" 
Bite 170. Analyze McDonald's food data
"""
import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object

df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    mc_item = df[['Item', 'Calories']] \
                                    .sort_values(by='Calories', ascending=False)\
                                    .values

    return mc_item[0][0]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""

    check_category = lambda x: x not in [
        'Beverages', 'Coffee & Tea', 'Smoothies & Shakes'
    ]
    calories = lambda x: x > 0

    foods = None

    if excl_drinks:
        foods = df[['Item','Protein', 'Calories']] \
                            .loc[(df['Category'].apply(check_category)) & (df['Calories'].apply(calories))].values
    else:
        foods = df[['Item','Protein', 'Calories']] \
                            .loc[(df['Calories'].apply(calories))].values

    # v[0] = Item
    # v[1] = Protein
    # v[2] = Calories
    return [
        v[0]
        for v in sorted(foods, key=lambda x: x[1] / x[2], reverse=True)[:5]
    ]
