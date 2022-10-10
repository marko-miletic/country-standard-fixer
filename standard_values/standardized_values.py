import pandas as pd

STANDARD_DATA_FRAME = pd.read_csv('./standard_values/iso_countries.csv')

# standardized country code standard

def get_countries() -> set:
    """ return -> set() structure of standard countries """
    return set(STANDARD_DATA_FRAME['name'])

def get_codes() -> set:
    """ return -> set() structure of standard codes """
    return set(STANDARD_DATA_FRAME['alpha-3'])

def get_country_code_combinations() -> dict:
    """ return -> dict(): dict['country'] = 'country code' """
    combinations = dict()
    for i in range(len(STANDARD_DATA_FRAME)):
        combinations[STANDARD_DATA_FRAME['name'][i]] = STANDARD_DATA_FRAME['alpha-3'][i]
    return combinations
    