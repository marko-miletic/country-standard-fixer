import pandas as pd

STANDARD_DATA_FRAME = pd.read_csv('./standard_values/iso_countries.csv')

# standardized country code standard

def get_countries() -> set:
    """ return -> set() structure of standard countries """
    countries_set = set()
    for country in STANDARD_DATA_FRAME['name']:
        countries_set.add(country)
    return countries_set

def get_codes() -> set:
    """ return -> set() structure of standard codes """
    codes_set = set()
    for code in STANDARD_DATA_FRAME['alpha-3']:
        codes_set.add(code)
    return codes_set

def get_country_code_combinations() -> dict:
    """ return -> dict(): dict['country'] = 'country code' """
    combinations = dict()
    for i in range(len(STANDARD_DATA_FRAME)):
        combinations[STANDARD_DATA_FRAME['name'][i]] = STANDARD_DATA_FRAME['alpha-3'][i]
    return combinations
    