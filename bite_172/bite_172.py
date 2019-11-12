from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places
rounder_int =  partial(lambda x: round(x))
rounder_detailed =  partial(lambda x: round(x, 4))
