import pandas as pd

from standard_values import standardized_values
from dataframes_correction import get_country_columns
from dataframes_correction import get_code_columns_alpha3
from dataframes_correction import correction

pd.options.mode.chained_assignment = None  # default='warn'

def test_get_country_columns1():
    dataframe = pd.read_csv("./files/test1.csv")
    assert get_country_columns(dataframe, standardized_values.get_countries()) == ["name"]

def test_get_country_columns2():
    dataframe = pd.read_json("./files/test3.json")
    assert get_country_columns(dataframe, standardized_values.get_countries()) == ["id"]

def test_get_country_codes1():
    dataframe = pd.read_csv("./files/test1.csv")
    assert get_code_columns_alpha3(dataframe, standardized_values.get_codes_alpha3()) == ["alpha-3"]

def test_get_country_codes2():
    dataframe = pd.read_json("./files/test3.json")
    assert get_code_columns_alpha3(dataframe, standardized_values.get_codes_alpha3()) == ["name"]

def test_correction():
    countries_set = standardized_values.get_countries()
    codes_set_alpha3 = standardized_values.get_codes_alpha3()
    codes_set_alpha2 = standardized_values.get_codes_alpha2()
    country_code_combinations = standardized_values.get_country_code_combinations()

    standard_file = pd.read_csv("./standard_values/iso_countries.csv")
    print(standard_file)
    input_file = pd.read_csv("./files/test1.csv")
    correction([input_file], countries_set, codes_set_alpha3, codes_set_alpha2, country_code_combinations)

    standard_countries, input_countries = set(standard_file["name"]), set(input_file["name"])
    standard_codes_alpha3, input_codes_alpha3 = set(standard_file["alpha-3"]), set(input_file["alpha-3"])
    standard_codes_alpha2, input_codes_alpha2 = set(standard_file["alpha-2"]), set(input_file["alpha-2"])

    assert (standard_countries == input_countries and
        standard_codes_alpha3 == input_codes_alpha3 and
        standard_codes_alpha2 == input_codes_alpha2)
