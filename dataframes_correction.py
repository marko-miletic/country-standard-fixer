import pandas as pd
from random import randrange
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process

from standard_values import standardized_values


SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN = 20
THRESHOLD_FOR_MATCHING_COUNTRY_COLUMN = 12
THRESHOLD_FOR_MATCHING_CODE_COLUMN = 8


def get_country_columns(dataframe: pd.DataFrame, countries_set: set) -> list:
    current_df_columns = dataframe.columns.values.tolist()
    target_columns_countries = []
    for column in current_df_columns:
        ### from every column in given dataframe takes random 20 entries
        ### and for each of those check if they are contained in countries_set
        ### for each entry contained in given sets, counter value increases
        ### if counter value is bigger than 12 (of 20) then
        ### given column is considered to be filled with country values
        test_counter_countries = 0
        column_length = len(dataframe[column])
        for _ in range(SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN):
            if dataframe[column][randrange(column_length)] in countries_set:
                test_counter_countries += 1
        if test_counter_countries > THRESHOLD_FOR_MATCHING_COUNTRY_COLUMN:
            target_columns_countries.append(column)
    print("country columns: ", target_columns_countries)
    return target_columns_countries

def get_code_columns(dataframe: pd.DataFrame, codes_set: set) -> list:
    current_df_columns = dataframe.columns.values.tolist()
    target_columns_codes = []
    for column in current_df_columns:
        ### from every column in given dataframe takes random 20 entries
        ### and for each of those check if they are contained in codes_set
        ### for each entry contained in given sets, counter value increases
        ### if counter value is bigger than 12 (of 20) then
        ### given column is considered to be filled with code values
        test_counter_codes = 0
        column_length = len(dataframe[column])
        for _ in range(SAMPLE_SIZE_FOR_MATCHING_COUNTRY_CODE_COLUMN):
            if dataframe[column][randrange(column_length)] in codes_set:
                test_counter_codes += 1
        if test_counter_codes > THRESHOLD_FOR_MATCHING_CODE_COLUMN:
            target_columns_codes.append(column)
    print("code columns: ", target_columns_codes)
    return target_columns_codes


def correction(dataframes: list, countries_set: set, codes_set: set, combinations: dict) -> None:
    """
        input -> takes dataframes and standardized data
        maps every column that contains country names or country codes to correct value
    """
    for df in dataframes:
        ###iterates trough every dataframe passed
        target_columns_countries = get_country_columns(df, countries_set)
        """ columns that contain country names """
        target_columns_codes = get_code_columns(df, codes_set)
        """ columns that contain country codes """

        print('country columns: ', target_columns_countries)
        print('codes columns: ', target_columns_codes)

        for column in target_columns_countries:
            ### every country value is changed to fit iso3166 standard
            ### and every code value is changed according to country
            for i in range(len(df[column])):
                if df[column][i] not in countries_set:
                    x = process.extractOne(df[column][i], countries_set, scorer=fuzz.token_set_ratio)
                    df[column][i] = x[0]
                for code_column in target_columns_codes:
                    df[code_column][i] = combinations[df[column][i]]


### tests

def test_get_country_columns1():
    dataframe = pd.read_csv("./files/test1.csv")
    assert get_country_columns(dataframe, standardized_values.get_countries()) == ["name"]

def test_get_country_columns2():
    dataframe = pd.read_json("./files/test3.json")
    assert get_country_columns(dataframe, standardized_values.get_countries()) == ["id"]

def test_get_country_codes1():
    dataframe = pd.read_csv("./files/test1.csv")
    assert get_code_columns(dataframe, standardized_values.get_codes()) == ["alpha-3"]

def test_get_country_codes2():
    dataframe = pd.read_json("./files/test3.json")
    assert get_code_columns(dataframe, standardized_values.get_codes()) == ["name"]

def test_correction():
    countries_set = standardized_values.get_countries()
    codes_set = standardized_values.get_codes()
    country_code_combinations = standardized_values.get_country_code_combinations()

    standard_file = pd.read_csv("./standard_values/iso_countries.csv")
    print(standard_file)
    input_file = pd.read_csv("./files/test1.csv")
    correction([input_file], countries_set, codes_set, country_code_combinations)

    standard_countries, input_countries = set(standard_file["name"]), set(input_file["name"])
    standard_codes, input_codes = set(standard_file["alpha-3"]), set(input_file["alpha-3"])

    assert standard_countries == input_countries and standard_codes == input_codes
